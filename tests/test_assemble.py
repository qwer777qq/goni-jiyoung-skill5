from pathlib import Path
from fractions import Fraction
import sys,tempfile,unittest,xml.etree.ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'skills/goni-jiyoung-skill5/scripts'))
from assemble import validate,build,clone_title,seconds

class AssemblyTests(unittest.TestCase):
    def plan(self):
        return dict(fps='30000/1001',width=1920,height=1080,source_uri='file:///tmp/local.mp4',source_frames=1000,cuts=[{'in':100,'out':200},{'in':300,'out':400}],captions=[{'in':150,'out':350,'text':'공의 결과 확인','template':'JY'}])
    def test_deleted_gap_and_subtitle_mapping(self):
        fps,cuts,cues,total=validate(self.plan(),False)
        self.assertEqual(total,200);self.assertEqual([(c['start'],c['end']) for c in cues],[(50,100),(100,150)])
        self.assertEqual(fps,Fraction(30000,1001))
    def test_repeated_source_cut_maps_each_occurrence(self):
        p=self.plan();p['cuts']=[{'in':100,'out':200}]*2
        self.assertEqual([x['start'] for x in validate(p,False)[2]],[50,150])
    def test_outside_source_rejected(self):
        p=self.plan();p['cuts'][0]['out']=1001
        with self.assertRaises(ValueError):validate(p,False)
    def test_overlap_rejected(self):
        p=self.plan();p['captions']*=2
        with self.assertRaises(ValueError):validate(p,False)
    def test_fractional_xml_and_no_fake_style(self):
        with tempfile.TemporaryDirectory() as td:
            out=Path(td)/'out';r=build(self.plan(),out,check_file=False)
            root=ET.parse(out/'edit.fcpxml').getroot()
            self.assertEqual(seconds(root.find('.//sequence').get('duration')),Fraction(200*1001,30000))
            self.assertFalse(r['render_verified']);self.assertEqual(r['styled_titles'],0)
            self.assertEqual((out/'captions.srt').read_text(encoding='utf-8').count('-->'),2)
            with self.assertRaises(ValueError):build(self.plan(),out,check_file=False)
    def test_seed_style_and_source_coordinate_preserved(self):
        seed=ET.fromstring('<title name="JY" duration="2s" start="0s" ref="r2"><text><text-style ref="ts1">{{TEXT}}</text-style></text><text-style-def id="ts1"><text-style font="OriginalFont" fontColor="1 1 0 1"/></text-style-def></title>')
        cue={'start':0,'end':30,'text':'결과 확인'}
        got=clone_title(seed,cue,Fraction(30),600,1)
        self.assertEqual(got.get('offset'),'20/1s');self.assertEqual(got.find('.//text-style-def/text-style').get('font'),'OriginalFont')
        self.assertEqual(seed.find('./text/text-style').text,'{{TEXT}}')
        self.assertEqual(got.find('./text/text-style').text,'결과 확인')
    def test_animated_seed_cannot_silently_stretch(self):
        seed=ET.fromstring('<title duration="2s"><text><text-style>{{TEXT}}</text-style></text><param><keyframeAnimation/></param></title>')
        with self.assertRaises(ValueError):clone_title(seed,{'start':0,'end':30,'text':'a'},Fraction(30),0,1)
    def test_missing_token_rejected(self):
        seed=ET.fromstring('<title duration="2s"><text><text-style>원래 글자</text-style></text></title>')
        with self.assertRaises(ValueError):clone_title(seed,{'start':0,'end':30,'text':'a'},Fraction(30),0,1)

if __name__=='__main__':unittest.main()

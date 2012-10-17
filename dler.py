import io
import urllib2 as ul2
import zipimport as zi
import subprocess as sp

for ctr in range(5000,10000):
  try:
    fobj = ul2.urlopen( "http://thenounproject.com/site_media/zipped/svg_"+ str(ctr) +".zip" );
  except:
    continue
  
  fdata = fobj.read();
  
  if len(fdata) > 100:
    print "Got: " + str(ctr);
    fio = io.FileIO("zip/"+ str(ctr) +".zip", "wb");
    fio.write(fdata);
    fio.close();
    
    zobj = zi.zipimporter("zip/"+ str(ctr) +".zip");
    zdata = zobj.get_data("noun_project_"+ str(ctr) +".svg");
    
    fio = io.FileIO("svg/"+ str(ctr) +".svg", "wb");
    fio.write(zdata);
    fio.close();
    
    sp.Popen(["inkscape/inkscape.exe", "-f", "svg/"+ str(ctr) +".svg", "-e", "png/"+ str(ctr) +".png"]);

raw_input("Press Enter to continue...");
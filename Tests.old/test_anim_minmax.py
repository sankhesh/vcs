import cdms2
import vcs
x = vcs.init()
f = cdms2.open(vcs.sample_data + "/clt.nc")
s = f("clt", time=slice(0, 23))
gm = x.createboxfill()
levs = vcs.mkevenlevels(20, 80)
gm.levels = levs
gm.fillareacolors = vcs.getcolors(levs)
d = x.plot(s, gm)
raw_input("Press enter")
x.animate.create(thread_it=False, min=20, max=80)
x.animate.fps(5000)
x.animate.run()
raw_input("Press enter to end")
x.animate.stop()

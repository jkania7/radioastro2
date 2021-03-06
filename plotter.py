import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.interpolate import CubicSpline
from scipy.interpolate import UnivariateSpline
from scipy.optimize import curve_fit
import scipy as s

def line(x,b,c):
    return x*b+c

def power(x,a,b):
    return b*x**a

rc('font',**{'family':'sans-serif','sans-serif':['Computer Modern Roman','Helvetica']})#makes the plots have pretty fonts
rc('text', usetex=True)

fluxes = np.loadtxt('fluxes.txt',skiprows=1)#load fluxes from file
print("fluxes={0}".format(fluxes))

spline = CubicSpline(np.log10(fluxes[:,0]),np.log10(fluxes[:,1]))
uspline = UnivariateSpline(np.log10(fluxes[:,0]),np.log10(fluxes[:,1]))
xspline = np.arange(np.amin(np.log10(fluxes[:,0])), np.max(np.log10(fluxes[:,0])),0.01)
line1 =  np.polyfit( np.log10(fluxes[0:3,0]),np.log10(fluxes[0:3,1]),1)
line2 =  np.polyfit(np.log10(fluxes[2:6,0]),np.log10(fluxes[2:6,1]),1)
x1 =  np.arange(np.amin(np.log10(fluxes[0:3,0])), np.max(np.log10(fluxes[0:3,0])),0.01)
x2 =  np.arange(np.amin(np.log10(fluxes[2:6,0])), np.max(np.log10(fluxes[2:6,0])),0.01)
p1 = np.poly1d(line1)
p2 = np.poly1d(line2)


popt1, pcov1 = curve_fit(line, np.log10(fluxes[0:3,0]),np.log10(fluxes[0:3,1]))
popt2, pcov2 = curve_fit(line, np.log10(fluxes[2:6,0]),np.log10(fluxes[2:6,1]))
perr1 = np.sqrt(np.diag(pcov1))
perr2 = np.sqrt(np.diag(pcov2))
popt1line, pcov1line = curve_fit(line, fluxes[0:3,0],fluxes[0:3,1])
popt2line, pcov2line = curve_fit(line, fluxes[2:6,0],fluxes[2:6,1])
perr1line = np.sqrt(np.diag(pcov1))
perr2line = np.sqrt(np.diag(pcov2))
x1line =  np.arange(np.amin(fluxes[0:3,0]), np.max(fluxes[0:3,0]),0.01)
x2line =  np.arange(np.amin(fluxes[2:6,0]), np.max(fluxes[2:6,0]),0.01)

linefull =  np.arange(np.amin(fluxes[:,0]), np.max(fluxes[:,0]),0.01)
poptpower, pcovpower = curve_fit(power, fluxes[:,0], fluxes[:,1], bounds=([-2,0],[0,1000]))
perrpower = np.sqrt(np.diag(pcovpower))
print("area under the curve = {0} uJy".format(s.integrate.simps(fluxes[:,1],fluxes[:,0])))
#splineFull = CubicSpline(fluxes[:,0],fluxes[:,1])
#xFull =  np.arange(np.amin(fluxes[:,0]), np.max(fluxes[:,0]),0.01)
#fig3 = plt.figure()#plot fluxes
#ax3 = fig3.add_subplot(111)
#ax3.errorbar(fluxes[:,0],fluxes[:,1],fluxes[:,2],fmt='o')
#ax3.errorbar(fluxes[:,0],fluxes[:,1],fluxes[:,2],fmt='o')
#ax3.plot(xFull,splineFull(xFull))
#ax3.set_title(r"Continuum Spectrum")
#ax3.set_xlabel(r"$(\nu$ [GHz])")
#ax3.set_ylabel(r"(Flux Density [$\mu$Jy])")

#print("Area under spline = {0)".format(splineFull.integrate()(22.1)-splineFull.integrate.(1.63)))
fig1 = plt.figure()#plot fluxes
ax1 = fig1.add_subplot(111)

print np.log10(np.add(fluxes[:,1], fluxes[:,2]))
#ax1.errorbar(np.log10(fluxes[:,0]),np.log10(fluxes[:,1]),yerr=np.multiply(np.divide(np.log10(fluxes[:,1]),fluxes[:,1]),fluxes[:,2]),fmt='o')
ax1.errorbar(np.log10(fluxes[:,0]),np.log10(fluxes[:,1]),yerr=[np.subtract(np.log10(np.subtract(fluxes[:,1],fluxes[:,2])),np.log10(fluxes[:,1])),-np.subtract(np.log10(np.add(fluxes[:,1],fluxes[:,2])),np.log10(fluxes[:,1]))],fmt='o')
#print(xspline)
#print(spline(xspline))
ax1.plot(xspline,spline(xspline))
#ax1.plot(xspline,uspline(xspline))
#ax1.plot(x1,p1(x1), x2, p2(x2))
ax1.set_title(r"Continuum Spectrum")
ax1.set_xlabel(r"$\log_{10}(\nu$ [GHz])")
ax1.set_ylabel(r"$\log_{10}$(Flux Density [$\mu$Jy])")
ax1.legend(["Cubic Spline","Measured Flux Density"], loc='best')
ax1.margins(0.05)
fig1.savefig('fluxVsFreq.png', dpi=300, bbox_inches='tight')
#plt.legend()
#plt.show()

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(xspline,spline.derivative(1)(xspline))
#ax2.plot(xspline,uspline.derivative()(xspline))
ax2.set_title(r"Spectral index as a function of frequency")
ax2.set_xlabel(r"$\log_{10}(\nu$ [GHz])")
ax2.set_ylabel(r"$\alpha$")
ax2.legend(["Derivative of Cubic Spline"], loc='best')
ax2.margins(0.05)
fig2.savefig('spectral index.png', dpi=300,  bbox_inches='tight')

fig3 = plt.figure()#plot fluxes
ax3 = fig3.add_subplot(111)
ax3.errorbar(np.log10(fluxes[:,0]),np.log10(fluxes[:,1]),yerr=[np.subtract(np.log10(np.subtract(fluxes[:,1],fluxes[:,2])),np.log10(fluxes[:,1])),-np.subtract(np.log10(np.add(fluxes[:,1],fluxes[:,2])),np.log10(fluxes[:,1]))],fmt='o')
#print(xspline)
#print(spline(xspline))
#ax3.plot(xspline,spline(xspline))
#ax3.plot(xspline,uspline(xspline))
ax3.plot(x1,line(x1,*popt1), x2, line(x2,*popt2))
ax3.set_title(r"Continuum Spectrum")
ax3.set_xlabel(r"$\log_{10}(\nu$ [GHz])")
ax3.set_ylabel(r"$\log_{10}$(Flux Density [$\mu$Jy])")
ax3.legend([r"Best Fit Line ({0:.3f}$\pm${1:.3f})x+{2:.3f}$\pm${3:.3f}".format(popt1[0],perr1[0],popt1[1],perr1[1]),"Best Fit Line ({0:.3f}$\pm${1:.3f})x+{2:.3f}$\pm${3:.3f}".format(popt2[0],perr2[0],popt2[1],perr2[1]),"Measured Flux Density"], loc='best')
ax3.margins(0.05)
fig3.savefig('fluxVsFreqLineFit.png', dpi=300, bbox_inches='tight')

fig4 = plt.figure()#plot fluxes
ax4 = fig4.add_subplot(111)
ax4.errorbar(fluxes[:,0],fluxes[:,1],yerr=fluxes[:,2],fmt='o')
#print(xspline)
#print(spline(xspline))
#ax3.plot(xspline,spline(xspline))
#ax3.plot(xspline,uspline(xspline))
ax4.plot(linefull,power(linefull,*poptpower))
ax4.set_title(r"Continuum Spectrum")
ax4.set_xlabel(r"$\nu$ [GHz])")
ax4.set_ylabel(r"Flux Density [$\mu$Jy]")
ax4.legend([r"Best Fit Power ({2:.4f}$\pm${3:.4f})$\nu$({0:.0f}$\pm${1:.0f})".format(poptpower[1],perrpower[1],poptpower[0],perrpower[0])], loc='best')
ax4.margins(0.05)
fig4.savefig('fluxnolog.png', dpi=300, bbox_inches='tight')


plt.show()

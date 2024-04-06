# 2024S1RSRCommissioning

The usual thing here are some LineCheck observations.

For some the "blanking.sum.txt" spectrum is 0, this must be a bug, except
it happens on unity,and not on peter's laptop.

affects these obsnums:

110898
111032
111033

solution:    increase cthr from 0.01 to 0.015

## Comparing PEAK and FLUX


     nemopars obsnum,src,linecheck1 2024S1RSRCommissioning/??????/lmtoy_??????.rc > linecheck2.log 


- tabcols linecheck2.log 2,7,4  | grep I12112 | tabhist - 2 0 16 bins=32
  flux Mean and dispersion  : 11.0025 1.97459 0.301122  11.4197 1.53337
- tabcols linecheck2.log 2,7,4  | grep I12112 | tabhist - 3 0 40 bins=32 robust=t
  peak Mean and dispersion  : 29.8336 4.95594 0.783603  30.2083 4.40676
- tabcols linecheck2.log 2,7,6  | grep I12112 | tabhist - 3 bins=32 robust=t
  fwhm Mean and dispersion  : 329.939 129.037 19.9108   345.019 17.724
- grep I12112 linecheck2.log | tabcols - 4,6,7 | tabmath - - 1.064*%1*%2/1000,%3 all

peak*fwhm -> 1.064*30.2*345.0/1000 =  11.08 K.km/s
flux      -> 11.00 K.km/s

excellent comparison

xlab="1.064*peak*fwhm"
ylab="line integral flux"
grep I12112 linecheck2.log | tabcols - 4,6,7 | tabmath - - 1.064*%1*%2/1000,%3 all | tabplot - 1 2 0 16 0 16 point=2,0.2 headline=I12112 xlab="$xlab" ylab="$ylab"
grep I10565 linecheck2.log | tabcols - 4,6,7 | tabmath - - 1.064*%1*%2/1000,%3 all | tabplot - 1 2 0 32 0 32 point=2,0.2 headline=I10655
grep I17208 linecheck2.log | tabcols - 4,6,7 | tabmath - - 1.064*%1*%2/1000,%3 all | tabplot - 1 2 0 64 0 64 point=2,0.2 headline=I17208

xlab="1.064*peak*fwhm"
ylab="line integral flux"
grep I12112 linecheck2.log | tabcols - 4,6,7 | tabmath - - %1,%3 all | tabplot - 1 2 0 48 0 16 point=2,0.2 headline=I12112 xlab="Peak(mK)" ylab="Flux(K.km/s)"


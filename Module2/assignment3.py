import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
servo = pd.read_csv('/Users/superpup/Documents/edx python/Module2/Datasets/servo.data',header=None)
servo.columns = ['motor', 'screw', 'pgain', 'vgain', 'class']
# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
s1 = servo[servo.vgain == 5]
print len(s1.index)

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
s2 = servo[(servo['motor']== "E") & (servo['screw'] == "E")]
print len(s2.index)


# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
s3 = servo[servo.pgain == 4]
s3v = s3.loc[:,'vgain']
sum(s3v)/len(s3v)

# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!




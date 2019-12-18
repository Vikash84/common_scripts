#!/usr/bin/python

Usage = """
creates a job file for desired number of commands per job

Usage:

  makeSLURMs.py <number of jobs per PBS file> <commands file>

eg:
  
  makeSLURMs.py 10 bowtie2.cmds

will create bowtie2_N.sub files, where N equals to number of lines in bowtie2.cmds divided by 10

If you have large number of commands that you would like to package (a set number) in a single
PBS script file, you can run this script along with desired number of commands per job.
Note that all commands will run in serially with this script (s suffix). If you want to run all commands at a time,
parallel fashion, then use the p suffix script 

Arun Seetharam
arnstrm@iastate.edu
11/08/2016
"""
import sys
import os
if len(sys.argv)<3:
    print Usage
else:
   cmdargs = str(sys.argv)
   cmds = open(sys.argv[2],'r')
   jobname = str(os.path.splitext(sys.argv[2])[0])
   filecount = 0
   numcmds = int(sys.argv[1])
   line = cmds.readline()
   while line:
        cmd = []
        while len(cmd) != int(sys.argv[1]):
                cmd.append(line)
                line = cmds.readline()
        w = open(jobname+'_'+str(filecount)+'.sub','w')
        w.write("#!/bin/bash\n")
        w.write("#SBATCH -N 1\n")
        w.write("#SBATCH --ntasks-per-node=16\n")
        w.write("#SBATCH -t 96:00:00\n")
        w.write("#SBATCH -J "+jobname+"_"+str(filecount)+"\n")
        w.write("#SBATCH -o "+jobname+"_"+str(filecount)+".o%j\n")
        w.write("#SBATCH -e "+jobname+"_"+str(filecount)+".e%j\n")
        w.write("#SBATCH --mail-user=arnstrm@gmail.com\n")
        w.write("#SBATCH --mail-type=begin\n")
        w.write("#SBATCH --mail-type=end\n")
        w.write("cd $SLURM_SUBMIT_DIR\n")
        w.write("ulimit -s unlimited\n")
<<<<<<< HEAD
        w.write("module use /work/GIF/software/modules\n")
=======
        w.write("module use /opt/rit/spack-modules/lmod/linux-rhel7-x86_64/Core\n")
        w.write("module use /opt/rit/spack-modules/lmod/linux-rhel7-x86_64/gcc/7.3.0\n")
        w.write("#module use /work/GIF/software/modules\n")
>>>>>>> a35fba4736ace90b227e33922c7ea97cf0451901
        w.write("module purge\n")
        w.write("cd ${TMPDIR}\n")
        w.write("RC=1\n")
        w.write("date\n")
        w.write("while [[ $RC -ne 0 ]]; do\n")
<<<<<<< HEAD
        w.write("rsync -rtsLP $SLURM_SUBMIT_DIR/ $TMPDIR/\n")
=======
        w.write("rsync -rts $SLURM_SUBMIT_DIR/ $TMPDIR/\n")
>>>>>>> a35fba4736ace90b227e33922c7ea97cf0451901
        w.write("RC=$?\n")
        w.write("sleep 10\n")
        w.write("done\n")
        w.write("date\n")
<<<<<<< HEAD
        w.write("module purge\n")
=======
>>>>>>> a35fba4736ace90b227e33922c7ea97cf0451901
        w.write("module load parallel\n")
        w.write("parallel -j 1 --joblog "+jobname+"_progress_"+str(filecount)+".log --workdir $PWD <<FIL\n")
        count = 0
        while (count < numcmds):
           w.write(cmd[count])
           count = count + 1
<<<<<<< HEAD
        w.write("FIL\n")
=======
>>>>>>> a35fba4736ace90b227e33922c7ea97cf0451901
        w.write("RC=1\n")
        w.write("date\n")
        w.write("while [[ $RC -ne 0 ]]; do\n")
        w.write("rsync -rts $TMPDIR/ $SLURM_SUBMIT_DIR/\n")
        w.write("RC=$?\n")
        w.write("sleep 10\n")
        w.write("done\n")
        w.write("date\n")
<<<<<<< HEAD
=======
        w.write("FIL\n")
>>>>>>> a35fba4736ace90b227e33922c7ea97cf0451901
        w.write("scontrol show job $SLURM_JOB_ID\n")
        w.close()
        filecount += 1




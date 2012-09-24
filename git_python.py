#!/usr/bin/python

import os, sys, subprocess

def cur_branch():
   # get the current branch
   proc = subprocess.Popen(['git', 'symbolic-ref', '-q', 'HEAD'],
                           stdout=subprocess.PIPE)
   proc.wait()
   current_branch = proc.stdout.read().split('/')[2].strip()
   
   return current_branch


def is_dirty():
   proc = subprocess.Popen(['git', 'diff', '--shortstat'], 
                           stdout=subprocess.PIPE)
   if proc.stdout.read().strip() != "":
      return "dirty"
   else:
      return "clean"

def checkout(branch):
   proc = subprocess.Popen(['git', 'checkout', branch],
                          stderr=subprocess.STDOUT, stdout=subprocess.PIPE) 
   rc = proc.wait()
   if rc != 0:
      print proc.stdout
      print "git checkout : unable to checkout branch " + branch
      return -1
   return 0

def stash():
   proc = subprocess.Popen(['git', 'stash'], 
                          stderr=subprocess.STDOUT, stdout=subprocess.PIPE) 
   rc = proc.wait()
   if rc != 0:
      print proc.stdout
      print "git stash: unable to stash local modifications"
      return -1
   return 0

def stash_pop():
   proc = subprocess.Popen(['git', 'stash', 'pop'], 
                          stderr=subprocess.STDOUT, stdout=subprocess.PIPE) 
   rc = proc.wait()
   if rc != 0:
      print proc.stdout
      print "git stash pop: unable to pop stash"
      return -1
   return 0


def svn_rebase():
   proc = subprocess.Popen(['git', 'svn', 'rebase'], 
                          stderr=subprocess.STDOUT, stdout=subprocess.PIPE) 
   rc = proc.wait()
   if rc != 0:
      print proc.stdout
      print "svn rebase: execute 'git rebase --continue|--abort', then exit shell to continue the svn rebase process"
      subprocess.call(['$SHELL'], shell=True)
   return 0
 
def rebase(base, branch, flags=[]):
   args = ['git', 'rebase']
   args = args + flags
   args.append(base)
   args.append(branch)

   proc = subprocess.Popen(args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE) 
   rc = proc.wait()
   if rc != 0:
      print proc.stdout
      print "git rebase: execute 'git rebase --continue|--abort', then exit shell to continue the git rebase process"
      subprocess.call(['$SHELL'], shell=True)
   return 0





 


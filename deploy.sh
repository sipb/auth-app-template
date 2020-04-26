# To run this script you must have 'aklog' written in ~/.bash_environment
# (or the environment file for whatever shell you use)
# and 'sipb' and 'athena' written in ~/.xlog (both of these files should be in your athena locker).
# Otherwise, you will not have permission to access the wisp locker,
# even if you are on the moira list.

#syntax: ./deploy.sh [kerberos]
yarn build
scp -r backend.py dist/* $1@athena.dialup.mit.edu:/mit/internet/web_scripts/

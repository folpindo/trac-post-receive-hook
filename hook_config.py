"""Project-specific configuration for git hooks"""

TRAC_ENV = '/var/trac/TRAC_ENV/'
GIT_PATH = '/usr/bin/git'

# Verbose mode for post-recieve. The client will see debug messages.
VERBOSE = False

# Set to False to disable re-posting messages from already-seen commits.
REPOST_SEEN = False

# Set to True to enable post-receive comments to trac.
POST_COMMENT = True

# The format of commit messages posted to tickets.
PRETTY_FORMAT = "'''%s'''  ''by %cn'' ([changeset:%H %h])\n\n%b"

# The ticket post-receive will post to if no ticket number can be parsed
# from the refname or commit message.
# It is recommended to set up a ticket for testing purposes,
# so that ticket should be used here.
DEFAULT_POST_RECEIVE_TKT_ID = 511


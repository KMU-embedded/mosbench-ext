# MOSBENCH involves three types of hosts:
# 1. The single primary host runs the benchmark applications.  It
#    should be a large multicore machine.  For the Apache and
#    Memcached benchmarks, it should have a very fast network
#    connection to the load generators.
# 2. A set of client machines act as load generators for the
#    memcached, Apache, and Postgres benchmarks.  This list should
#    *not* include the primary host.
# 3. The driver host runs the driver script, which coordinates the
#    benchmark programs and load generators on the primary and
#    secondary hosts and gather results.  The benchmark was designed
#    so that this can be a different host from the primary host;
#    however, this is NOT a well-tested configuration.  This host must
#    have ssh keys set up for passwordless access to all hosts except
#    the one it is running on.
# Here we configure these hosts.  All of the host names provided here
# must work from all of the hosts.  Don't use "localhost".  The driver
# will detect if it is running on one of these hosts and forgo ssh
# automatically).

__all__ = ["primaryHost"]

from mparts.host import Host
from support import perfLocked
from memcached import MemcachedHost
import support.rsshash as rsshash

# Use "cmdModifier = perfLocked" if you use the "perflock" script to
# prevent conflicting machine access.  You probably don't.
#tom = Host("MOSS", cmdModifier = perfLocked)
tom = Host("MOSS", None)

clientHosts = ["MOSC"]
clients = dict((hostname.split(".",1)[0], Host(hostname))
               for hostname in clientHosts)

# All clients are on the 10GB switch, so they should address tom using
# its 10GB IP.
#for host in clients.values():
#    host.addRoute(tom, "192.168.42.11")

# josmp is multihomed and uses a different IP for its 10GB interface.
#tom.addRoute(josmp, "192.168.42.10")

# tom is our big multicore
primaryHost = tom

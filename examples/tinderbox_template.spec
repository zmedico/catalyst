# generic tinderbox specfile

# The subarch can be any of the supported catalyst subarches (like athlon-xp).
# Refer to "man catalyst" or <https://wiki.gentoo.org/wiki/Catalyst>
# for supported subarches
# example:
# subarch: athlon-xp
subarch:

# The version stamp is an identifier for the build.  It can be anything you wish
# it to be, but it is usually a date.
# example:
# version_stamp: 2006.1
version_stamp:

# The target specifies what target we want catalyst to do.
# example:
# target: tinderbox
target: tinderbox

# The rel_type defines what kind of build we are doing.  This is merely another
# identifier, but it useful for allowing multiple concurrent builds.  Usually,
# default will suffice.
# example:
# rel_type: default
rel_type:

# This is the system profile to be used by catalyst to build this target.  It is
# specified as a relative path from /var/db/repos/gentoo/profiles.
# example:
# profile: default-linux/x86/2006.1
profile:

# This specifies which snapshot to use for building this target.
# example:
# snapshot: 2006.1
snapshot:

# This specifies where the seed stage comes from for this target,  The path is
# relative to $clst_sharedir/builds.  The rel_type is also used as a path prefix
# for the seed.
# example:
# default/stage3-x86-2006.1
source_subpath:

# These are the hosts used as distcc slaves when distcc is enabled in your
# catalyst.conf.  It follows the same syntax as distcc-config --set-hosts and
# is entirely optional.
# example:
# distcc_hosts: 127.0.0.1 192.168.0.1
distcc_hosts:

# This is an optional directory containing portage configuration files.  It
# follows the same syntax as /etc/portage and should be consistent across all
# targets to minimize problems.
# example:
# portage_confdir: /etc/portage
portage_confdir:

# This option specifies the location to a portage overlay that you would like to
# have used when building this target.
# example:
# portage_overlay: /usr/local/portage
portage_overlay:

# This allows the optional directory containing the output packages for
# catalyst.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# pkgcache_path: /tmp/packages
pkgcache_path:

# The tinderbox target can build packages with any USE settings.  However, it
# should be noted that these settings are additive to the settings in the
# chosen profile.  This is extremely useful when testing possible changed to a
# profile or package.
# example:
# tinderbox/use: gtk2 gnome kde qt bonobo cdr esd gtkhtml mozilla mysql perl ruby tcltk cups ldap ssl tcpd -svga
tinderbox/use:

# This is the list of packages that will be built by the tinderbox target.
# Each of these is considered a separate target to test, and catalyst will use
# rsync to reset the build area to the default from the source_subpath before
# each package.  This allows for testing USE changes on individual packages as
# well as for dependency issues.
# exampleL
# tinderbox/packages: dante tsocks sys-apps/eject minicom links acpid apmd parted whois tcpdump cvs zip unzip netcat partimage app-admin/sudo app-cdr/cdrtools gnome emacs dev-lang/ruby enlightenment kde mozilla-firefox mozilla-thunderbird xfce4 openbox fluxbox sylpheed openoffice-bin gimp xemacs xmms abiword gaim xchat pan tetex xcdroast k3b samba nmap gradm ettercap ethereal mplayer
tinderbox/packages:

# Setting the option overrides the location of the kerncache
kerncache_path:


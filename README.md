# Justify Text

A simple Python implementation of how to justify text.

An example is the following text:

	There are two different ways for rsync to contact a remote system: using a  remote-shell program as the transport (such as ssh or rsh) or contacting an rsync daemon directly via TCP.  The remote-shell transport is used whenever the source or destination path contains a single colon (:) separator after a  host  specification.   Contacting  an rsync daemon directly happens when the source or destination path contains a double colon (::) separator after a host specification, OR when an  rsync://  URL  is specified  (see  also  the "USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION" section for an exception to this latter rule).

Which is justified to the following with a 40 character width.

	There  are  two different ways for rsync
	to  contact  a  remote  system:  using a
	remote-shell  program  as  the transport
	(such  as  ssh  or rsh) or contacting an
	rsync   daemon  directly  via  TCP.  The
	remote-shell     transport    is    used
	whenever   the   source  or  destination
	path   contains   a   single  colon  (:)
	separator  after  a  host specification.
	Contacting   an  rsync  daemon  directly
	happens  when  the source or destination
	path   contains   a  double  colon  (::)
	separator  after  a  host specification,
	OR  when  an  rsync://  URL is specified
	(see   also   the   "USING  RSYNC-DAEMON
	FEATURES      VIA     A     REMOTE-SHELL
	CONNECTION"  section  for  an  exception

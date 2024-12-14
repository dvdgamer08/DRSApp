#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@                               ,@@@@@@@@@@@@@@@@@                          ,@@@@@@@@@@@@@@@@@@                                     @@(((((
#@@@@@@@&((@@@@                                    %@@@@@@@@@                                (@@@@@@@@.                                       @@((((((@
#@@@@@@@(((((@@@@                                     @@@@@@@                                  (@@@@                                        @@#(((((@@@
#@@@@@@@((((((&@@@,                                    @@@@@                                    ,@@                                        @@(((((@@@@@
#@@@@@@(((((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           @@@@          @@@@@@@@@@@@@@@@@@%        @@        (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@(((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@          @@@(         @@@@@@@@@@@@@@@@@&*         @@          %%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@
#@@@@@#((((((((((((&@@@@@@@@@@@@@@@@@@@@@@@@@@,         @@@                                     @@@@                                  &@@@@@@@@@@@@@@@@
#@@@@@(((((((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@          @@&                                   %@@@@@@@                                  ,@@@@@@@@@@@@@@
#@@@@%(((((((((((((((((@@@@@@@@@@@@@@@@@@@@@@          &@@                                 &@@@@@@@@@@@@@#                                @@@@@@@@@@@@@
#@@@@(((((((((((((((((((#@@@@@@@@@@@@@@@@@@(          %@@@          @@@@@@@@@@           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        %@@@@@@@@@@@@
#@@@&(((((((((((((((((((((@@@@@@@@@@@@@/             @@@@          @@@@@@@@@@@@,           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@@@@@@
#@@@((((((((((((((((((((((((@@@@                   @@@@@@          @@@@@@@@@@@@@@           @@@@%                                        @@@@@@@@@@@@@@
#@@@(((((((((((((((((((((((((&@@@/              (@@@@@@@          &@@@@@@@@@@@@@@@            @@@@.                                     @@@@@@@@@@@@@@@
#@@((((((((((((((((((((((((((((@@@@        &@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@/           (@@@@                                 @@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# © 2021 Digital Rally Series
# Wrapper module for _socket, providing some additional facilities
# implemented in Python.

_E='_closed'
_D='I/O operation on closed socket.'
_C=False
_B=True
_A=None
import os,sys,io,platform
if platform.architecture()[0]=='64bit':sysdir='stdlib64'
else:sysdir='stdlib'
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'libreria',sysdir))
os.environ['PATH']=os.environ['PATH']+';.'
import _socket
from _socket import*
try:import errno
except ImportError:errno=_A
EBADF=getattr(errno,'EBADF',9)
EAGAIN=getattr(errno,'EAGAIN',11)
EWOULDBLOCK=getattr(errno,'EWOULDBLOCK',11)
__all__=['getfqdn','create_connection']
__all__.extend(os._get_exports_list(_socket))
_realsocket=socket
if sys.platform.lower().startswith('win'):errorTab={};errorTab[10004]='The operation was interrupted.';errorTab[10009]='A bad file handle was passed.';errorTab[10013]='Permission denied.';errorTab[10014]='A fault occurred on the network??';errorTab[10022]='An invalid operation was attempted.';errorTab[10035]='The socket operation would block';errorTab[10036]='A blocking operation is already in progress.';errorTab[10048]='The network address is in use.';errorTab[10054]='The connection has been reset.';errorTab[10058]='The network has been shut down.';errorTab[10060]='The operation timed out.';errorTab[10061]='Connection refused.';errorTab[10063]='The name is too long.';errorTab[10064]='The host is down.';errorTab[10065]='The host is unreachable.';__all__.append('errorTab')
class socket(_socket.socket):
	'A subclass of _socket.socket adding the makefile() method.';__slots__=['__weakref__','_io_refs',_E]
	def __init__(self,family=AF_INET,type=SOCK_STREAM,proto=0,fileno=_A):_socket.socket.__init__(self,family,type,proto,fileno);self._io_refs=0;self._closed=_C
	def __enter__(self):return self
	def __exit__(self,*args):
		if not self._closed:self.close()
	def __repr__(self):
		'Wrap __repr__() to reveal the real class name.';s=_socket.socket.__repr__(self)
		if s.startswith('<socket object'):s='<%s.%s%s%s'%(self.__class__.__module__,self.__class__.__name__,getattr(self,_E,_C)and' [closed] 'or'',s[7:])
		return s
	def __getstate__(self):raise TypeError('Cannot serialize socket object')
	def dup(self):'dup() -> socket object\n\n        Return a new socket object connected to the same system resource.\n        ';fd=dup(self.fileno());sock=self.__class__(self.family,self.type,self.proto,fileno=fd);sock.settimeout(self.gettimeout());return sock
	def accept(self):
		'accept() -> (socket object, address info)\n\n        Wait for an incoming connection.  Return a new socket\n        representing the connection, and the address of the client.\n        For IP sockets, the address info is a pair (hostaddr, port).\n        ';fd,addr=self._accept();sock=socket(self.family,self.type,self.proto,fileno=fd)
		if getdefaulttimeout()is _A and self.gettimeout():sock.setblocking(_B)
		return sock,addr
	def makefile(self,mode='r',buffering=_A,*,encoding=_A,errors=_A,newline=_A):
		"makefile(...) -> an I/O stream connected to the socket\n\n        The arguments are as for io.open() after the filename,\n        except the only mode characters supported are 'r', 'w' and 'b'.\n        The semantics are similar too.  (XXX refactor to share code?)\n        "
		for c in mode:
			if c not in{'r','w','b'}:raise ValueError('invalid mode %r (only r, w, b allowed)')
		writing='w'in mode;reading='r'in mode or not writing;assert reading or writing;binary='b'in mode;rawmode=''
		if reading:rawmode+='r'
		if writing:rawmode+='w'
		raw=SocketIO(self,rawmode);self._io_refs+=1
		if buffering is _A:buffering=-1
		if buffering<0:buffering=io.DEFAULT_BUFFER_SIZE
		if buffering==0:
			if not binary:raise ValueError('unbuffered streams must be binary')
			return raw
		if reading and writing:buffer=io.BufferedRWPair(raw,raw,buffering)
		elif reading:buffer=io.BufferedReader(raw,buffering)
		else:assert writing;buffer=io.BufferedWriter(raw,buffering)
		if binary:return buffer
		text=io.TextIOWrapper(buffer,encoding,errors,newline);text.mode=mode;return text
	def _decref_socketios(self):
		if self._io_refs>0:self._io_refs-=1
		if self._closed:self.close()
	def _real_close(self,_ss=_socket.socket):_ss.close(self)
	def close(self):
		self._closed=_B
		if self._io_refs<=0:self._real_close()
	def detach(self):'detach() -> file descriptor\n\n        Close the socket object without closing the underlying file descriptor.\n        The object cannot be used after this call, but the file descriptor\n        can be reused for other purposes.  The file descriptor is returned.\n        ';self._closed=_B;return super().detach()
def fromfd(fd,family,type,proto=0):' fromfd(fd, family, type[, proto]) -> socket object\n\n    Create a socket object from a duplicate of the given file\n    descriptor.  The remaining arguments are the same as for socket().\n    ';nfd=dup(fd);return socket(family,type,proto,nfd)
if hasattr(_socket.socket,'share'):
	def fromshare(info):' fromshare(info) -> socket object\n\n        Create a socket object from a the bytes object returned by\n        socket.share(pid).\n        ';return socket(0,0,0,info)
if hasattr(_socket,'socketpair'):
	def socketpair(family=_A,type=SOCK_STREAM,proto=0):
		'socketpair([family[, type[, proto]]]) -> (socket object, socket object)\n\n        Create a pair of socket objects from the sockets returned by the platform\n        socketpair() function.\n        The arguments are the same as for socket() except the default family is\n        AF_UNIX if defined on the platform; otherwise, the default is AF_INET.\n        '
		if family is _A:
			try:family=AF_UNIX
			except NameError:family=AF_INET
		a,b=_socket.socketpair(family,type,proto);a=socket(family,type,proto,a.detach());b=socket(family,type,proto,b.detach());return a,b
_blocking_errnos={EAGAIN,EWOULDBLOCK}
class SocketIO(io.RawIOBase):
	'Raw I/O implementation for stream sockets.\n\n    This class supports the makefile() method on sockets.  It provides\n    the raw I/O interface on top of a socket object.\n    '
	def __init__(self,sock,mode):
		if mode not in('r','w','rw','rb','wb','rwb'):raise ValueError('invalid mode: %r'%mode)
		io.RawIOBase.__init__(self);self._sock=sock
		if'b'not in mode:mode+='b'
		self._mode=mode;self._reading='r'in mode;self._writing='w'in mode;self._timeout_occurred=_C
	def readinto(self,b):
		'Read up to len(b) bytes into the writable buffer *b* and return\n        the number of bytes read.  If the socket is non-blocking and no bytes\n        are available, None is returned.\n\n        If *b* is non-empty, a 0 return value indicates that the connection\n        was shutdown at the other end.\n        ';self._checkClosed();self._checkReadable()
		if self._timeout_occurred:raise IOError('cannot read from timed out object')
		while _B:
			try:return self._sock.recv_into(b)
			except timeout:self._timeout_occurred=_B;raise
			except InterruptedError:continue
			except error as e:
				if e.args[0]in _blocking_errnos:return
				raise
	def write(self,b):
		'Write the given bytes or bytearray object *b* to the socket\n        and return the number of bytes written.  This can be less than\n        len(b) if not all data could be written.  If the socket is\n        non-blocking and no bytes could be written None is returned.\n        ';self._checkClosed();self._checkWritable()
		try:return self._sock.send(b)
		except error as e:
			if e.args[0]in _blocking_errnos:return
			raise
	def readable(self):
		'True if the SocketIO is open for reading.\n        '
		if self.closed:raise ValueError(_D)
		return self._reading
	def writable(self):
		'True if the SocketIO is open for writing.\n        '
		if self.closed:raise ValueError(_D)
		return self._writing
	def seekable(self):
		'True if the SocketIO is open for seeking.\n        '
		if self.closed:raise ValueError(_D)
		return super().seekable()
	def fileno(self):'Return the file descriptor of the underlying socket.\n        ';self._checkClosed();return self._sock.fileno()
	@property
	def name(self):
		if not self.closed:return self.fileno()
		else:return-1
	@property
	def mode(self):return self._mode
	def close(self):
		"Close the SocketIO object.  This doesn't close the underlying\n        socket, except if all references to it have disappeared.\n        "
		if self.closed:return
		io.RawIOBase.close(self);self._sock._decref_socketios();self._sock=_A
def getfqdn(name=''):
	'Get fully qualified domain name from name.\n\n    An empty argument is interpreted as meaning the local host.\n\n    First the hostname returned by gethostbyaddr() is checked, then\n    possibly existing aliases. In case no FQDN is available, hostname\n    from gethostname() is returned.\n    ';name=name.strip()
	if not name or name=='0.0.0.0':name=gethostname()
	try:hostname,aliases,ipaddrs=gethostbyaddr(name)
	except error:pass
	else:
		aliases.insert(0,hostname)
		for name in aliases:
			if'.'in name:break
		else:name=hostname
	return name
_GLOBAL_DEFAULT_TIMEOUT=object()
def create_connection(address,timeout=_GLOBAL_DEFAULT_TIMEOUT,source_address=_A):
	"Connect to *address* and return the socket object.\n\n    Convenience function.  Connect to *address* (a 2-tuple ``(host,\n    port)``) and return the socket object.  Passing the optional\n    *timeout* parameter will set the timeout on the socket instance\n    before attempting to connect.  If no *timeout* is supplied, the\n    global default timeout setting returned by :func:`getdefaulttimeout`\n    is used.  If *source_address* is set it must be a tuple of (host, port)\n    for the socket to bind as a source address before making the connection.\n    An host of '' or port 0 tells the OS to use the default.\n    ";host,port=address;err=_A
	for res in getaddrinfo(host,port,0,SOCK_STREAM):
		af,socktype,proto,canonname,sa=res;sock=_A
		try:
			sock=socket(af,socktype,proto)
			if timeout is not _GLOBAL_DEFAULT_TIMEOUT:sock.settimeout(timeout)
			if source_address:sock.bind(source_address)
			sock.connect(sa);return sock
		except error as _:
			err=_
			if sock is not _A:sock.close()
	if err is not _A:raise err
	else:raise error('getaddrinfo returns an empty list')
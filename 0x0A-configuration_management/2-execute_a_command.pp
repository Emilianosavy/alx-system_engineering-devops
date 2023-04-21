# This puppet executes a kill command

exec { 'pkill killmenow':
  path     => '/usr/bin',
  provider => 'shell',
}

# This puppet installs flask version 2.1.0 from pip3

package { 'flask':
  ensure   => '2.1.0',
  name     => 'Flask',
  provider => 'pip3',
}

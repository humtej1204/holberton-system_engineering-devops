#Installing puppet-lint

package { 'puppet-lint':
  ensure   => '2.5.0',
  source   => 'http://rubygems.org',
}

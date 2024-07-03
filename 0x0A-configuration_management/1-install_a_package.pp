# install flask from pip3. Using Puppe

# installs the package puppet-lint
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

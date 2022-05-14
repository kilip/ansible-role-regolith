Ansible Role: Regolith
=========
Installs and Configure Zeus Workstations.

[![CI](https://github.com/kilip/ansible-role-regolith/workflows/CI/badge.svg?event=push)](https://github.com/kilip/ansible-role-zeus/actions?query=workflow%3ACI)

Requirements
------------
None

Role Variables
--------------
```yaml
# vars file for zeus
zeus_user: toni
zeus_group: "{{ zeus_user }}"
zeus_home: "/home/{{ zeus_user }}"

linux_utils:
  - vim
  - curl
  - wget
  - git

configure_composer: true
composer_path: "{{ zeus_home }}/.local/bin/composer"
composer_keep_updated: false
composer_version: ''
# The directory where global packages will be installed.
composer_home_path: '~/.composer'
composer_home_owner: "{{ zeus_user }}"
composer_home_group: "{{ zeus_group }}"
# A list of packages to install globally. See commented examples below for
# usage; the 'release' is optional, and defaults to '@stable'.
composer_global_packages: []
# - { name: phpunit/phpunit, release: "4.7.x" }
# - { name: phpunit/phpunit, release: "@stable" }
composer_add_to_path: true
# Add a project vendor/bin directory to the PATH
composer_add_project_to_path: false
# composer_project_path: /path/to/project/vendor/bin
# GitHub OAuth token (used to help overcome API rate limits).
composer_github_oauth_token: ''

configure_chrome: true
chrome_release_channel: 'stable'
chrome_package_name: 'google-chrome-{{ chrome_release_channel }}'
chrome_disable_gpu: false
chrome_policies_managed: []
chrome_policies_recommended: []
chrome_policies_filename: 'policy.json'
chrome_download_url: 'https://dl.google.com/linux/direct/'
__chrome_package: '{{ chrome_package_name }}_current_amd64.deb'

configure_ohmyzsh: true
ohmyzsh_packages:
  - zsh
  - zsh-autosuggestions
  - zsh-antigen
  - zsh-syntax-highlighting
ohmyzsh_zshrc: "{{ zeus_home }}/.zshrc"
ohmyzsh_path: "{{ zeus_home }}/.oh-my-zsh"
ohmyzsh_temp_dir: '/tmp'
ohmyzsh_installer_url: "https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh"
ohmyzsh_installer: "{{ ohmyzsh_temp_dir }}/install-ohmyzsh.sh"
ohmyzsh_change_shell: true
ohmyzsh_zsh_bin: /usr/bin/zsh
ohmyzsh_plugins: []
ohmyzsh_theme: "agnoster"
ohmyzsh_theme_repo: ""
ohmyzsh_plugins_repo: []

configure_docker: true
# Used only for Debian/Ubuntu. Switch 'stable' to 'edge' if needed.
docker_apt_release_channel: stable
docker_apt_arch: amd64
docker_apt_repository: "deb [arch={{ docker_apt_arch }}] https://download.docker.com/linux/{{ ansible_distribution | lower }} {{ ansible_distribution_release }} {{ docker_apt_release_channel }}"
docker_apt_ignore_key_error: true
docker_apt_gpg_key: https://download.docker.com/linux/{{ ansible_distribution | lower }}/gpg
docker_user: "{{ zeus_user }}"
docker_packages:
  - docker-ce
  - docker-ce-cli
  - containerd.io
  - docker-compose-plugin

configure_gpg: true
gpg_home: "{{ zeus_home }}"
gpg_user: "{{ zeus_user }}"
gpg_group: "{{ zeus_group }}"
gpg_key_id: null
gpg_private_key: null
gpg_temp_dir: "/tmp/gpg"
gpg_import_key: true
```

Dependencies
------------
None

Example Playbook
----------------
Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: workstation
      roles:
         - role: kilip.zeus

License
-------
MIT

Author Information
------------------
This role was created in 2022 by [Anthonius Munthi](https://itstoni.com)

Fedora Drupal 8 Dev RPMs
========================

*** **WARNING: These are just a development RPMs.  Please submit issues at <https://github.com/siwinski/drupal8-rpms/issues> and prefix your issue title with "[%{name}] " -- ex: "[drupal8] ", "[drupal8-devel] ", "[drupal8-token] "** ***

Core TODO
---------
* Dependencies requiring update:
  * [php-doctrine-annotations](https://admin.fedoraproject.org/pkgdb/package/php-doctrine-annotations/)
  * [php-doctrine-common](https://admin.fedoraproject.org/pkgdb/package/php-doctrine-common/)
* Unbundle libraries
  * Composer
    * Guzzle 4 (core/vendor/guzzlehttp)
  * Modules
    * [CKEditor](https://admin.fedoraproject.org/pkgdb/package/ckeditor/) (core/modules/ckeditor)
  * JavaScript/CSS (core/core.libraries.yml; core/assets/vendor/*)
    * backbone
    * classList
    * farbtastic
    * jquery
    * jquery-form
    * jquery-once
    * jquery-ui-touch-punch
    * normalize-css
    * underscore
    * [ckeditor](https://admin.fedoraproject.org/pkgdb/package/ckeditor/)
    * domready
    * html5shiv
    * jquery.cookie
    * jquery-joyride
    * jquery.ui
    * modernizr
    * picturefill

Fedora Drafts
-------------
* [Packaging Guidelines](https://fedoraproject.org/wiki/User:Siwinski/Draft:Packaging:Drupal8)
* [Feature](http://fedoraproject.org/wiki/User:Siwinski/Draft:Features:Drupal8)

Fedora Dev Repos
----------------
* [Fedora Copr](http://copr.fedoraproject.org/coprs/siwinski/drupal8/)
  * [Fedora 19](http://copr.fedoraproject.org/coprs/siwinski/drupal8/repo/fedora-19-i386/)
  * [Fedora 20](http://copr.fedoraproject.org/coprs/siwinski/drupal8/repo/fedora-20-i386/)
  * [Fedora rawhide](http://copr.fedoraproject.org/coprs/siwinski/drupal8/repo/fedora-rawhide-i386/)
  * [EPEL 7](http://copr.fedoraproject.org/coprs/siwinski/drupal8/repo/epel-7-x86_64/)

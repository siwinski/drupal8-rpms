Fedora Drupal 8 Dev RPMs
========================

*** **WARNING: These are just a development RPMs.  Please submit issues at <https://github.com/siwinski/drupal8-rpms/issues> and prefix your issue title with "[%{name}] " -- ex: "[drupal8] ", "[drupal8-devel] ", "[drupal8-token] "** ***

Core TODO
---------
* Dependencies requiring update? (need to check):
  * [php-doctrine-annotations](https://admin.fedoraproject.org/pkgdb/package/php-doctrine-annotations/)
  * [php-doctrine-common](https://admin.fedoraproject.org/pkgdb/package/php-doctrine-common/)
* Unbundle libraries
  * Modules
    * [CKEditor](https://admin.fedoraproject.org/pkgdb/package/ckeditor/) (core/modules/ckeditor)
  * JavaScript/CSS ([core/core.libraries.yml](http://cgit.drupalcode.org/drupal/tree/core/core.libraries.yml?h=8.0.x); [core/assets/vendor/*](http://cgit.drupalcode.org/drupal/tree/core/assets/vendor?h=8.0.x))
    * [backbone](https://github.com/jashkenas/backbone)
    * [ckeditor](https://admin.fedoraproject.org/pkgdb/package/ckeditor/)
    * [classList](https://github.com/eligrey/classList.js)
    * [domready](https://github.com/ded/domready)
    * [html5shiv](https://github.com/aFarkas/html5shiv)
    * [jquery.form](https://github.com/malsup/form)
    * [jquery.once](https://github.com/RobLoach/jquery-once)
    * [jquery.cookie](https://github.com/carhartl/jquery-cookie)
    * [jquery.farbtastic](https://github.com/mattfarina/farbtastic)
    * [jquery.joyride](https://github.com/zurb/joyride)
    * [matchmedia](https://github.com/paulirish/matchMedia.js)
    * [modernizr](https://github.com/Modernizr/Modernizr)
    * [normalize](https://github.com/necolas/normalize.css)
    * [picturefill](https://github.com/scottjehl/picturefill)
    * [underscore](https://github.com/jashkenas/underscore)

Fedora
-------------
* Drafts
    * [Packaging Guidelines](https://fedoraproject.org/wiki/User:Siwinski/Draft:Packaging:Drupal8)
    * [Feature](http://fedoraproject.org/wiki/User:Siwinski/Draft:Features:Drupal8)
* [COPR](http://copr.fedoraproject.org/coprs/siwinski/drupal8/)

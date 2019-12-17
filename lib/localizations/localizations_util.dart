import 'package:flutter/material.dart';
import 'package:flutter_localization_sample/localizations/app_localizations.dart';

class Strings {

  static AppLocalizations of(BuildContext context) {
    return Localizations.of<AppLocalizations>(context, AppLocalizations);
  }

}
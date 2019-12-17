import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_localization_sample/localizations/resources/string_resources.dart';
import 'package:intl/intl.dart';

import 'package:flutter_localization_sample/l10n/dart/messages_all.dart';

class AppLocalizations with StringResources {
  static Future<AppLocalizations> load(Locale locale) {
    final String name =
    locale.countryCode == null ? locale.languageCode : locale.toString();
    final String localeName = Intl.canonicalizedLocale(name);

    return initializeMessages(localeName).then((bool _) {
      Intl.defaultLocale = localeName;
      return new AppLocalizations();
    });
  }

  static AppLocalizations of(BuildContext context) {
    return Localizations.of<AppLocalizations>(context, AppLocalizations);
  }
}
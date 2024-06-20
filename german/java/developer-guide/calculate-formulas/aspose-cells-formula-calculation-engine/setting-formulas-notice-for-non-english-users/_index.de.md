---
title: Formeln einstellen  Hinweis für nicht englischsprachige Benutzer
type: docs
weight: 20
url: /de/java/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt die meisten Formeln/Funktionen, die Teil von Microsoft Excel sind. Entwickler können diese Formeln entweder mit der API oder [Designer-Tabellenkalkulationen](/cells/de/java/was-ist-eine-designer-tabelle/) verwenden. Aspose.Cells unterstützt eine große Auswahl an mathematischen, Zeichen-, Booleschen, Datums-/Zeit-, statistischen, Datenbank-, Such- und Verweisformeln. Die Formeln sollten im Stil Englisch (US) angegeben werden.

Es gibt zwei Tipps, die nicht-englischsprachige Benutzer beim Erstellen von Formeln mit Aspose.Cells beachten müssen:

1. Formeln müssen auf Englisch eingegeben werden.
   Verwenden Sie beispielsweise das englische "=SUM()" und nicht das deutsche "=SUMME()".
1. Verwenden Sie immer ein Komma (,) zur Trennung von Funktionsparametern.
   Bei einigen Sprachoptionen oder Einstellungen wird das Trennzeichen für Funktionsparameter als Semikolon verwendet, aber Aspose.Cells verwendet das englische Komma. Verwenden Sie beispielsweise "=IF (C5=0,0,C3/C4)" und nicht "=IF(C5=0;0;C3/C4)". 

{{% /alert %}}

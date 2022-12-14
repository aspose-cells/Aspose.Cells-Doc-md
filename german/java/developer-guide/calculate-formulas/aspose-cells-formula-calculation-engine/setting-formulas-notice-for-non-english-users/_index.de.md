---
title: Festlegen von Formeln – Hinweis für nicht englische Benutzer
type: docs
weight: 20
url: /de/java/setting-formulas-notice-for-non-english-users/
---
{{% alert color="primary" %}} 

 Aspose.Cells unterstützt die meisten Formeln/Funktionen, die Teil von Microsoft Excel sind. Entwickler können diese Formeln entweder mit API oder verwenden[Designer-Tabellen](/cells/de/java/what-is-a-designer-spreadsheet/). Aspose.Cells unterstützt eine große Menge mathematischer, Zeichenfolgen-, Boolean-, Datums-/Uhrzeit-, Statistik-, Datenbank-, Such- und Referenzformeln. Die Formeln sollten im englischen (US) Stil angegeben werden.

Es gibt zwei Tipps, die nicht-englische Benutzer beim Erstellen von Formeln mit Aspose.Cells befolgen müssen:

1. Formeln müssen in englischer Sprache eingegeben werden.
 Verwenden Sie zum Beispiel das englische „=SUM()“ und nicht das deutsche „=SUMME()“.
1. Verwenden Sie immer ein Komma (,), um Funktionsparameter abzugrenzen.
Bei einigen Sprachoptionen oder -einstellungen ist das Trennzeichen für Funktionsparameter ein Semikolon, aber Aspose.Cells verwendet das englische Komma. Verwenden Sie beispielsweise „=IF (C5=0,0,C3/C4)“ und nicht „=IF(C5=0;0;C3/C4)“.

{{% /alert %}}

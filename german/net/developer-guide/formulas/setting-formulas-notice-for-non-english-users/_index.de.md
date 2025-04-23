---
title: Formeln einstellen  Hinweis für nicht englischsprachige Benutzer
type: docs
weight: 10
url: /de/net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt die meisten Formeln/Funktionen, die Teil von Microsoft Excel sind. Entwickler können diese Formeln entweder mit der API oder [designer spreadsheets](/cells/de/net/what-is-a-designer-spreadsheet/) verwenden. Aspose.Cells unterstützt eine große Menge an mathematischen, string, Boolean, Datum/Uhrzeit, statistischen, Datenbank-, Such- und Verweisformeln. Die Formeln sollten im englischen (US) Stil angegeben werden.

{{% /alert %}} 
## **Hinweis für Nicht-Englisch-Sprachige Benutzer**
Es gibt zwei Tipps, die nicht-englischsprachige Benutzer beim Erstellen von Formeln mit Aspose.Cells beachten müssen:

1. Formeln müssen auf Englisch eingegeben werden. Verwenden Sie z.B. das englische "=SUM()" und nicht das deutsche "=SUMME()".
1. Verwenden Sie immer ein Komma (,) zur Trennung von Funktionsparametern. Für einige Sprachoptionen oder Einstellungen ist das Trennzeichen für Funktionsparameter ein Semikolon, aber Aspose.Cells verwendet das englische Komma. Verwenden Sie z.B. "=IF (C5=0,0,C3/C4)" und nicht "=IF(C5=0;0;C3/C4)"
{{< app/cells/assistant language="csharp" >}}

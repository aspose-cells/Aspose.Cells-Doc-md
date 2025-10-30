---
title: Formeln einstellen  Hinweis für nicht englischsprachige Benutzer
type: docs
weight: 10
url: /de/python-net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells für Python via .NET unterstützt die meisten Formeln/Funktionen, die Teil von Microsoft Excel sind. Entwickler können diese Formeln entweder mit der API oder [Designer-Tabellen](/cells/de/net/was-ist-eine-designer-tabelle/) verwenden. Aspose.Cells für Python via .NET unterstützt eine große Menge an mathematischen, String-, Booleschen, Datum/Uhrzeit-, statistischen, Datenbank-, Nachschlage- und Referenz-Formeln. Die Formeln sollten im US-Englisch-Stil angegeben werden.

{{% /alert %}} 

## **Hinweis für Nicht-Englisch-Sprachige Benutzer**
Es gibt zwei Tipps, die Nicht-Englisch sprechende Nutzer beim Erstellen von Formeln mit Aspose.Cells für Python via .NET befolgen müssen:

1. Formeln müssen auf Englisch eingegeben werden. Verwenden Sie z.B. das englische "=SUM()" und nicht das deutsche "=SUMME()".
1. Verwenden Sie immer ein Komma (,) zur Trennung der Funktionsparameter. Für einige Sprachoptionen oder Einstellungen ist das Trennzeichen für Funktionsparameter ein Semikolon, aber Aspose.Cells für Python via .NET verwendet den englischen Stil-Komma. Zum Beispiel verwenden Sie "=IF (C5=0,0,C3/C4)" anstelle von "=IF(C5=0;0;C3/C4)"

{{< app/cells/assistant language="python-net" >}}

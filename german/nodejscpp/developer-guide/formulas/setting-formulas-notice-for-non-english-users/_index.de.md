---
title: Formeln festlegen  Hinweis für Nicht Englisch Nutzer mit Node.js über C++
linktitle: Formeln einstellen  Hinweis für nicht englischsprachige Benutzer
type: docs
weight: 10
url: /de/nodejs-cpp/setting-formulas-notice-for-non-english-users/
---  

{{% alert color="primary" %}} 

Aspose.Cells unterstützt die meisten Formeln/Funktionen, die Teil von Microsoft Excel sind. Entwickler können diese Formeln entweder mit der API oder [Designer-Tabellen](/cells/de/nodejs-cpp/what-is-a-designer-spreadsheet/) verwenden. Aspose.Cells unterstützt eine große Reihe von mathematischen, String-, Booleschen-, Datum/Uhrzeit-, statistischen, Datenbank-, Lookup- und Referenz-Formeln. Die Formeln sollten im Englisch (US)-Stil angegeben werden.

{{% /alert %}} 

## **Hinweis für Nicht-Englisch-Sprachige Benutzer**
Es gibt zwei Tipps, die nicht-englischsprachige Benutzer beim Erstellen von Formeln mit Aspose.Cells beachten müssen:

1. Formeln müssen auf Englisch eingegeben werden. Verwenden Sie z.B. das englische "=SUM()" und nicht das deutsche "=SUMME()".
1. Verwenden Sie immer ein Komma (,) um Funktionsparameter zu trennen. Für einige Sprachoptionen oder Einstellungen ist das Trennzeichen für Funktionsparameter ein Semikolon, aber Aspose.Cells verwendet den englischen Stil-Komma. Zum Beispiel verwenden Sie "=IF (C5=0,0,C3/C4)" und nicht "=IF(C5=0;0;C3/C4)".  

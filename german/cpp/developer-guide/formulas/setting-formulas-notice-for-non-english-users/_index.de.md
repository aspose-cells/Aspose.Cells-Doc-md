---
title: Festlegen von Formeln  Hinweis für Nicht Englischsprachige Benutzer mit C++
linktitle: Formeln einstellen  Hinweis für nicht englischsprachige Benutzer
type: docs
weight: 10
url: /de/cpp/setting-formulas-notice-for-non-english-users/
description: Erfahren Sie, wie Sie Formeln in Aspose.Cells for C++ mit englischem (US) Stil für nicht englische Benutzer festlegen.
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt die meisten Formeln/Funktionen, die Teil von Microsoft Excel sind. Entwickler können diese Formeln entweder mit der API oder [Designer-Tabellen](/cells/de/cpp/what-is-a-designer-spreadsheet/) verwenden. Aspose.Cells unterstützt eine große Reihe mathematischer, Zeichenketten-, Boolean-, Datum/Uhrzeit-, statistischer, Datenbank-, Lookup- und Bezug-Formeln. Die Formeln sollten im englischen (US) Stil angegeben werden.

{{% /alert %}} 

## **Hinweis für Nicht-Englisch-Sprachige Benutzer**
Es gibt zwei Tipps, die nicht-englischsprachige Benutzer beim Erstellen von Formeln mit Aspose.Cells beachten müssen:

1. Formeln müssen auf Englisch eingegeben werden. Verwenden Sie z.B. das englische "=SUM()" und nicht das deutsche "=SUMME()".
1. Verwenden Sie immer ein Komma (,) um Funktionsparameter zu trennen. Für einige Sprachoptionen oder Einstellungen ist das Trennzeichen für Funktionsparameter ein Semikolon, aber Aspose.Cells verwendet den englischen Stil-Komma. Zum Beispiel verwenden Sie "=IF (C5=0,0,C3/C4)" und nicht "=IF(C5=0;0;C3/C4)".

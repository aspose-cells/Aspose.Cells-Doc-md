---
title: Subtotal oder Gesamtsummenbeschriftungen in anderen Sprachen implementieren
type: docs
weight: 50
url: /de/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---

## **Mögliche Verwendungsszenarien**

Manchmal möchte man Teilergebnis- und Gesamtergebnisbezeichnungen in nicht-englischen Sprachen wie Chinesisch, Japanisch, Arabisch, Hindi usw. anzeigen. Mit Aspose.Cells können Sie dies mit der [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)-Klasse und der [**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings)-Eigenschaft tun. Bitte lesen Sie diesen Artikel, um zu erfahren, wie Sie die [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)-Klasse verwenden können.

- [Verwendung der GlobalizationSettings-Klasse für benutzerdefinierte Teilergebnisbeschriftungen und andere Beschriftungen des Kuchendiagramms](/cells/de/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implementierung von Teilergebnisse oder Gesamtergebnisbezeichnungen in anderen Sprachen**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](5115151.xlsx) und implementiert die Teilergebnis- und Gesamtergebnisbezeichnungen in chinesischer Sprache. Bitte überprüfen Sie die von diesem Code generierte [Ausgabe-Excel-Datei](5115152.xlsx) als Referenz. Zuerst erstellen wir eine Klasse [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) und verwenden sie dann in unserem Code.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

Verwenden Sie die oben erstellte Klasse im Code wie unten gezeigt:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}

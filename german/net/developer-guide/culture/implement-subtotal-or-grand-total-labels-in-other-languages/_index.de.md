---
title: Implementieren Sie Beschriftungen für Zwischensummen oder Gesamtsummen in anderen Sprachen
type: docs
weight: 50
url: /de/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---
## **Mögliche Nutzungsszenarien**

Manchmal möchten Sie Zwischensummen- und Gesamtsummenbeschriftungen in nicht-englischen Sprachen wie Chinesisch, Japanisch, Arabisch, Hindi usw. anzeigen. Aspose.Cells ermöglicht Ihnen dies mit der[**Globalisierungseinstellungen**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)Klasse und[**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) Eigentum. Bitte lesen Sie diesen Artikel zur Verwendung von[**Globalisierungseinstellungen**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)Klasse

- [Verwenden der GlobalizationSettings-Klasse für benutzerdefinierte Zwischensummenbeschriftungen und andere Beschriftungen von Kreisdiagrammen](/cells/de/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implementieren Sie Beschriftungen für Zwischensummen oder Gesamtsummen in anderen Sprachen**

 Der folgende Beispielcode lädt die[Excel-Beispieldatei](5115151.xlsx) und implementiert Zwischensummen- und Gesamtsummennamen in der chinesischen Sprache. Bitte überprüfen Sie die[Excel-Datei ausgeben](5115152.xlsx) generiert von diesem Code für Ihre Referenz. Wir erstellen zuerst eine Klasse von[**Globalisierungseinstellungen**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)und dann in unserem Code verwenden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

Verwenden Sie nun die oben erstellte Klasse im Code wie unten:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}

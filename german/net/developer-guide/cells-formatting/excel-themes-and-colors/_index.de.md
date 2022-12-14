---
title: Excel-Designs und -Farben
type: docs
weight: 100
url: /de/net/excel-themes-and-colors/
---
## **Excel-Designs und -Farben**

Designs bieten ein einheitliches Erscheinungsbild mit benannten Stilen, grafischen Effekten und anderen Objekten, die in einer Arbeitsmappe verwendet werden. Beispielsweise sieht der Accent1-Stil in den Office- und Apex-Designs anders aus. Häufig wenden Sie ein Dokumentdesign an und ändern es dann nach Ihren Wünschen.

Aspose.Cells bietet Funktionen zum Anpassen von Themen und Farben.

### **Themenfarben abrufen und festlegen**

Nachfolgend sind einige Methoden und Eigenschaften aufgeführt, die Designfarben implementieren.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Zum Einstellen der Vordergrundfarbe.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Zum Einstellen der Hintergrundfarbe.
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Zum Einstellen der Schriftfarbe.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Wird verwendet, um eine Designfarbe zu erhalten.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Wird verwendet, um eine Designfarbe festzulegen.

Das folgende Beispiel zeigt, wie Designfarben abgerufen und festgelegt werden.

Das folgende Beispiel verwendet eine XLSX-Vorlagendatei, ruft die Farben für verschiedene Themenfarbtypen ab, ändert die Farben und speichert die Excel-Datei Microsoft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

#### **Passen Sie Themen an**

Das folgende Beispiel zeigt, wie Sie benutzerdefinierte Designs mit Ihren gewünschten Farben anwenden. Wir verwenden eine Beispielvorlagendatei, die manuell in Microsoft Excel 2007 erstellt wurde.

Das folgende Beispiel lädt eine XLSX-Vorlagendatei, definiert Farben für verschiedene Themenfarbtypen, wendet die benutzerdefinierten Farben an und speichert die Excel-Datei.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

#### **Verwenden Sie Themenfarben**

Im folgenden Beispiel werden die Vordergrund- und Schriftfarben einer Zelle basierend auf den Farbtypen des Standarddesigns (der Arbeitsmappe) angewendet. Es speichert auch die Excel-Datei auf der Festplatte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

## **Themen vorantreiben**
- [Extrahieren Sie Themendaten aus einer Excel-Datei](/cells/de/net/extract-theme-data-from-excel-file/)

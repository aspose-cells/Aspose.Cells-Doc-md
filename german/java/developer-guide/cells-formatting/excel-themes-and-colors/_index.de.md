---
title: Excel-Designs und -Farben
type: docs
weight: 130
url: /de/java/excel-2007-themes-and-colors/
---
{{% alert color="primary" %}}

Designs bieten ein einheitliches Erscheinungsbild mit benannten Stilen, grafischen Effekten und anderen Objekten, die in einer Arbeitsmappe verwendet werden. Beispielsweise sieht der Accent1-Stil in den Office- und Apex-Designs anders aus. Häufig wenden Sie ein Dokumentdesign an und ändern es dann gemäß Ihren Anforderungen.

**Anwenden von Designs in Microsoft Excel**

![todo: Bild_alt_Text](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **Themenfarben abrufen und festlegen**

Aspose.Cells APIs bieten Funktionen zum Anpassen von Designs und Farben. Im Folgenden sind einige Methoden und Eigenschaften aufgeführt, die Designfarben implementieren.

- Die Style.ForegroundThemeColor-Eigenschaft kann verwendet werden, um die Vordergrundfarbe festzulegen.
- Die Eigenschaft Style.BackgroundThemeColor kann verwendet werden, um die Hintergrundfarbe festzulegen.
- Font.ThemeColor-Eigenschaft kann verwendet werden, um die Schriftfarbe festzulegen.
- Die Workbook.getThemeColor-Methode kann verwendet werden, um eine Designfarbe zu erhalten.
- Die Workbook.setThemeColor-Methode kann verwendet werden, um eine Designfarbe festzulegen.

Das folgende Beispiel zeigt, wie Designfarben abgerufen und festgelegt werden.

Das folgende Beispiel verwendet eine XLSX-Vorlagendatei, ruft die Farben für verschiedene Themenfarbtypen ab, ändert die Farben und speichert die Microsoft-Excel-Datei.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **Anpassen von Themen**

Das folgende Beispiel zeigt, wie Sie benutzerdefinierte Designs mit Ihren gewünschten Farben anwenden. Das Beispiel verwendet eine Beispielvorlagendatei, die manuell in Microsoft Excel 2007 erstellt wurde.

**Die Vorlagendatei CustomThemeColor.xlsx**

![todo: Bild_alt_Text](excel-2007-themes-and-colors_2.png)

Das folgende Beispiel lädt eine Vorlagendatei XLSX, definiert Farben für verschiedene Themenfarbtypen, wendet die benutzerdefinierten Farben an und speichert die Excel-Datei.

**Die generierte Datei mit benutzerdefinierten Designfarben**

![todo: Bild_alt_Text](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **Themenfarben verwenden**

Im folgenden Beispiel werden die Vordergrund- und Schriftfarben einer Zelle basierend auf den Farbtypen des Standarddesigns (der Arbeitsmappe) angewendet. Es speichert auch die Excel-Datei auf der Festplatte.

Beim Ausführen des Codes wird die folgende Ausgabe generiert.

**Die auf die D3-Zelle des Arbeitsblatts angewendeten Designfarben** 

![todo: Bild_alt_Text](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **Themen vorantreiben**
- [Extrahieren Sie Themendaten aus einer Excel-Datei](/cells/de/java/extract-theme-data-from-excel-file/)

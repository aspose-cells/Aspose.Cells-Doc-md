---
title: Excel Themen und Farben
type: docs
weight: 130
url: /de/java/excel-2007-themes-and-colors/
---

{{% alert color="primary" %}}

Themen bieten einen einheitlichen Look mit benannten Stilen, grafischen Effekten und anderen Objekten, die in einer Arbeitsmappe verwendet werden. Zum Beispiel sieht der Akzent1-Stil in den Office- und den Apex-Themen unterschiedlich aus. Oft wenden Sie ein Dokumententhema an und passen es dann nach Ihren Bedürfnissen an.

** Anwenden von Themen in Microsoft Excel **

![todo:image_alt_text](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **Themenfarben abrufen und festlegen**

Aspose.Cells APIs bieten Funktionen zum Anpassen von Themen und Farben. Im Folgenden sind einige Methoden und Eigenschaften aufgeführt, die Themenfarben implementieren.

- Die Eigenschaft Style.ForegroundThemeColor kann verwendet werden, um die Vordergrundfarbe festzulegen.
- Die Eigenschaft Style.BackgroundThemeColor kann verwendet werden, um die Hintergrundfarbe festzulegen.
- Die Eigenschaft Font.ThemeColor kann verwendet werden, um die Schriftfarbe festzulegen.
- Die Methode Workbook.getThemeColor kann verwendet werden, um eine Themafarbe abzurufen.
- Die Methode Workbook.setThemeColor kann verwendet werden, um eine Themafarbe festzulegen.

Das folgende Beispiel zeigt, wie Designs erhalten und gesetzt werden.

Das folgende Beispiel verwendet eine Vorlagendatei im XLSX-Format, ruft die Farben für verschiedene Designtypen ab, ändert die Farben und speichert die Microsoft Excel-Datei.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **Anpassen von Themen**

Das folgende Beispiel zeigt, wie man benutzerdefinierte Themen mit den gewünschten Farben anwendet. Das Beispiel verwendet eine beispielhafte Vorlagendatei, die manuell in Microsoft Excel 2007 erstellt wurde.

**Die Vorlagendatei CustomThemeColor.xlsx**

![todo:image_alt_text](excel-2007-themes-and-colors_2.png)

Im folgenden Beispiel wird eine Vorlagendatei im XLSX-Format geladen, Farben für verschiedene Designtypen definiert und die benutzerdefinierten Farben angewendet, bevor die Excel-Datei gespeichert wird.

**Die generierte Datei mit angepassten Themafarben**

![todo:image_alt_text](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **Verwendung von Themafarben**

Im folgenden Beispiel werden die Vordergrund- und Schriftfarben einer Zelle basierend auf den Standarddesignfarben (des Arbeitsmappen) angewendet. Die Excel-Datei wird ebenfalls auf der Festplatte gespeichert.

Die folgende Ausgabe wird bei der Ausführung des Codes generiert.

**Die auf Zelle D3 im Arbeitsblatt angewendeten Themafarben** 

![todo:image_alt_text](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **Erweiterte Themen**
- [Extrahieren von Themen-Daten aus Excel-Datei](/cells/de/java/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="java" >}}

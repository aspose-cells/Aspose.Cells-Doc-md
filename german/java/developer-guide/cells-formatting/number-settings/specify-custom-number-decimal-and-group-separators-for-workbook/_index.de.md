---
title: Geben Sie benutzerdefinierte Dezimalzahlen und Gruppentrennzeichen für die Arbeitsmappe an
type: docs
weight: 100
url: /de/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Dieser Artikel zeigt, wie Sie die Dezimalzahl und das Gruppentrennzeichen in MS Excel und mit dem Code Java ändern, indem Sie den Code Aspose.Cells for Java API verwenden.
keywords: specify custom decimal separator excel, specify custom decimal separator excel java, specify custom group separator excel, specify custom group separator excel java, specify custom decimal and group separator excel, specify custom decimal and group separator excel java, change decimal and group separator excel java, change decimal and group separator excel, change decimal separator excel, change decimal separator excel java, change group separator excel, change group separator excel java
---
{{% alert color="primary" %}}

 In Microsoft Excel können Sie die benutzerdefinierten Dezimal- und Tausendertrennzeichen angeben, anstatt Systemtrennzeichen aus dem zu verwenden**Erweiterte Excel-Optionen** wie im Screenshot unten gezeigt.

 Aspose.Cells bietet die[**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) und[WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) Eigenschaften zum Festlegen der benutzerdefinierten Trennzeichen zum Formatieren/Parsen von Zahlen.

{{% /alert %}}

## **Angeben von benutzerdefinierten Trennzeichen mit Microsoft Excel**

1.  Offen**Optionen** in dem**Datei** Tab.
1. Öffne das**Fortschrittlich** Tab.
1.  Ändern Sie die Einstellungen in der**Bearbeitungsoptionen** Sektion.

Der folgende Screenshot zeigt die**Erweiterte Excel-Optionen** und hebt den Abschnitt hervor, um die anzugeben**Benutzerdefinierte Trennzeichen**.

![todo: Bild_alt_Text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Angeben von benutzerdefinierten Trennzeichen mit Aspose.Cells**

 Der folgende Beispielcode veranschaulicht, wie die benutzerdefinierten Trennzeichen mit Aspose.Cells API angegeben werden. Er gibt die benutzerdefinierten Dezimalzahlen und Gruppentrennzeichen als Punkt bzw. Leerzeichen an. Also die Nummer**123,456.789** wird angezeigt als**123 456.789** wie im Screenshot gezeigt, der die vom Code generierte Ausgabe PDF zeigt.

![todo: Bild_alt_Text](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}

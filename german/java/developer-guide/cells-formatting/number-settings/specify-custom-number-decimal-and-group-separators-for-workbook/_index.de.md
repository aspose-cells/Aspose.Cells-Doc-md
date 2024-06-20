---
title: Benutzerdefinierte Dezimal und Gruppentrennzeichen für Arbeitsmappe festlegen
type: docs
weight: 100
url: /de/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Dieser Artikel zeigt, wie Sie im MS Excel und mit Java Code die benutzerdefinierten Dezimal und Gruppentrennzeichen unter Verwendung der Aspose.Cells for Java API ändern können.
keywords: benutzerdefinierten Dezimaltrennzeichen excel angeben, benutzerdefinierten Dezimaltrennzeichen excel java angeben, benutzerdefinierte Gruppentrennzeichen excel angeben, benutzerdefinierte Gruppentrennzeichen excel java angeben, benutzerdefinierten Dezimal und Gruppentrennzeichen excel angeben, benutzerdefinierten Dezimal und Gruppentrennzeichen excel java angeben, Dezimal und Gruppentrennzeichen in Excel mit Java ändern, Dezimal und Gruppentrennzeichen in Excel ändern, Dezimaltrennzeichen in Excel ändern, Dezimaltrennzeichen in Excel java ändern, Gruppentrennzeichen in Excel ändern, Gruppentrennzeichen in Excel java ändern
---

{{% alert color="primary" %}}

In Microsoft Excel können Sie die benutzerdefinierten Dezimal- und Tausendertrennzeichen festlegen, anstatt die Systemtrennzeichen aus den **Erweiterten Excel-Optionen** zu verwenden, wie im untenstehenden Screenshot gezeigt.

Aspose.Cells bietet die Eigenschaften [**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) und [WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) an, um die benutzerdefinierten Trennzeichen für die Formatierung/Analyse von Zahlen festzulegen.

{{% /alert %}}

## **Benutzerdefinierte Trennzeichen mit Microsoft Excel festlegen**

1. Öffnen Sie **Optionen** im **Datei**-Register.
1. Öffnen Sie das **Erweitert**-Register.
1. Ändern Sie die Einstellungen im Abschnitt **Bearbeitungsoptionen**.

Der folgende Screenshot zeigt die **Erweiterten Excel-Optionen** und hebt den Abschnitt hervor, um die **Benutzerdefinierten Trennzeichen** festzulegen.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Benutzerdefinierte Trennzeichen mit Aspose.Cells festlegen**

Der folgende Beispielcode veranschaulicht, wie die benutzerdefinierten Trennzeichen mithilfe der Aspose.Cells API spezifiziert werden. Es spezifiziert die benutzerdefinierten Dezimal- und Gruppentrennzeichen als Punkt und Leerzeichen. Die Zahl **123,456.789** wird also wie im Screenshot gezeigt als **123 456.789** angezeigt, der die von dem Code generierte Ausgabe-PDF zeigt.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}

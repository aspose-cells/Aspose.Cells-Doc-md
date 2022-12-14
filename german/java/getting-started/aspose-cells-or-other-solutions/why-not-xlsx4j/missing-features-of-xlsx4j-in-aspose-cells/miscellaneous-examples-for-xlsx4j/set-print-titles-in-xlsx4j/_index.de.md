---
title: Legen Sie Drucktitel in xlsx4j fest
type: docs
weight: 40
url: /de/java/set-print-titles-in-xlsx4j/
---
## **Aspose.Cells - Drucktitel festlegen**
Aspose.Cells ermöglicht es Ihnen, Zeilen- und Spaltenüberschriften festzulegen, die auf allen Seiten eines gedruckten Arbeitsblatts wiederholt werden sollen. Verwenden Sie dazu die[Seiteneinrichtung](/java/PageSetup)der Eigenschaften setPrintTitleColumns und setPrintTitleRows der Klasse.

Die Zeilen oder Spalten, die wiederholt werden, werden durch die Übergabe ihrer Zeilen- oder Spaltennummern definiert. Beispielsweise werden Zeilen als $1:$2 und Spalten als $A:$B definiert.

**Java**

{{< highlight "java" >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/setprinttitles/AsposeSetPrintTitles.java)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Druckoptionen einstellen](/cells/de/java/page-setup-features/#setting-print-options).

{{% /alert %}}

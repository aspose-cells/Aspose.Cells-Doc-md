---
title: Bildlaufleisten von Arbeitsmappen in xlsx4j anzeigen und ausblenden
type: docs
weight: 30
url: /de/java/display-and-hide-scrollbars-of-workbooks-in-xlsx4j/
---
## **Aspose.Cells – Bildlaufleisten von Arbeitsmappen anzeigen und ausblenden**
 Aspose.Cells bietet eine Klasse,**Arbeitsmappe** die eine Excel-Datei darstellt.**Arbeitsmappe** -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten einer Excel-Datei. Aber um die Sichtbarkeit der Bildlaufleisten in der Excel-Datei zu steuern, können Entwickler verwenden**setVScrollBarVisible** & **setHScrollBarVisible** Methoden der**Arbeitsmappe** Klasse.

**Java**

{{< highlight "java" >}}

 //Instantiating a Excel object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeSrollbarsHide.xls");

// ===============================================================

//Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true);

//Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplaySrollbars.xls");


{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidescrollbars/AsposeDisplayAndHideScrollbars.java)

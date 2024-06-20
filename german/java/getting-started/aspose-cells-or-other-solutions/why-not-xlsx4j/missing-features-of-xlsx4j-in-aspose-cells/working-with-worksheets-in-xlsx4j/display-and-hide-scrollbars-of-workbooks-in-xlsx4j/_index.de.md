---
title: Anzeigen und Ausblenden von Bildlaufleisten von Arbeitsmappen in xlsx4j
type: docs
weight: 30
url: /de/java/display-and-hide-scrollbars-of-workbooks-in-xlsx4j/
---

## **Aspose.Cells - Anzeigen und Ausblenden von Bildlaufleisten von Arbeitsmappen**
Aspose.Cells bietet eine Klasse, **Workbook**, die eine Excel-Datei repräsentiert. Die Klasse **Workbook** bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Excel-Datei. Um jedoch die Sichtbarkeit der Bildlaufleisten in der Excel-Datei zu steuern, können Entwickler die Methoden **setVScrollBarVisible** und **setHScrollBarVisible** der Klasse **Workbook** verwenden.

**Java**

{{< highlight java >}}

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
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidescrollbars/AsposeDisplayAndHideScrollbars.java)

---
title: Neue Zeile in Zellen
type: docs
weight: 30
url: /de/java/new-line-in-cells/
---

## **Aspose.Cells - Neue Zeile in Zellen**
Um sicherzustellen, dass der Text in einer Zelle gelesen werden kann, können explizite Zeilenumbrüche und Textumbrüche angewendet werden. Textumbrüche verwandeln eine Zeile in mehrere in einer Zelle, wobei explizite Zeilenumbrüche genau dort eingefügt werden, wo Sie sie haben möchten.

Um Text in einer Zelle umzubrechen, verwenden Sie die Methode Style.setTextWrapped.

**Java**

{{< highlight java >}}

 // Add Text to the First Cell with Explicit Line Breaks

cell.get(0, 0).setValue("I am using \nthe latest version of \nAspose.Cells \nto test this functionality");

//Get Cell's Style

Style style = cell.get(0, 0).getStyle();

//Set Text Wrap property to true

style.setTextWrapped(true);

//Set Cell's Style

cell.get(0, 0).setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Neue Zeile in Zellen**
CellStyle.setWrapText sollte für umgebrochenen Text true sein.

**Java**

{{< highlight java >}}

 Row row = sheet.createRow(2);

Cell cell = row.createCell(2);

cell.setCellValue("Use \n with word wrap on to create a new line");

//to enable newlines you need set a cell styles with wrap=true

CellStyle cs = wb.createCellStyle();

cs.setWrapText(true);

cell.setCellStyle(cs);

{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/newlineincells)

{{% alert color="primary" %}} 

Weitere Informationen finden Sie unter [Zeilenumbrüche und Textumbrüche](/java/line-breaks-and-text-wrapping).

{{% /alert %}}

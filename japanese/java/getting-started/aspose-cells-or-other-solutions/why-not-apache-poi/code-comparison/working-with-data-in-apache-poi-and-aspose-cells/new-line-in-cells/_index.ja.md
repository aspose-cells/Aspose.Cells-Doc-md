---
title: 改行 in Cells
type: docs
weight: 30
url: /ja/java/new-line-in-cells/
---
## **Aspose.Cells - Cells の改行**
セル内のテキストを確実に読み取れるようにするために、明示的な改行とテキストの折り返しを適用できます。テキストの折り返しにより、セル内の 1 行が複数の行に変わり、明示的な改行によって、必要な場所に正確に改行が挿入されます。

セル内のテキストを折り返すには、Style.setTextWrapped メソッドを使用します。

**Java**

{{< highlight "java" >}}

 // Add Text to the First Cell with Explicit Line Breaks

cell.get(0, 0).setValue("I am using \nthe latest version of \nAspose.Cells \nto test this functionality");

//Get Cell's Style

Style style = cell.get(0, 0).getStyle();

//Set Text Wrap property to true

style.setTextWrapped(true);

//Set Cell's Style

cell.get(0, 0).setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Cells の改行**
CellStyle.setWrapText は、折り返されたテキストに対して true にする必要があります。

**Java**

{{< highlight "java" >}}

 Row row = sheet.createRow(2);

Cell cell = row.createCell(2);

cell.setCellValue("Use \n with word wrap on to create a new line");

//to enable newlines you need set a cell styles with wrap=true

CellStyle cs = wb.createCellStyle();

cs.setWrapText(true);

cell.setCellStyle(cs);

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/newlineincells)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[改行とテキストの折り返し](/java/line-breaks-and-text-wrapping).

{{% /alert %}}

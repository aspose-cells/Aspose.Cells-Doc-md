﻿---
title: 使用 Aspose.Cells 打印工作簿
type: docs
weight: 20
url: /zh/java/printing-workbooks-using-aspose-cells/
---
## **Aspose.Cells - 打印工作簿**
完成电子表格创建后，您可能需要根据需要打印一份工作表的硬拷贝。打印时，MS Excel 假定您要打印整个工作表区域，除非您指定了您的选择。

打印工作表

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook

Workbook book = new Workbook(dataDir + "AsposeDataInput.xls");

//Create an object for ImageOptions

ImageOrPrintOptions  imgOptions = new ImageOrPrintOptions ();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Create a SheetRender object with respect to your desired sheet

SheetRender sr = new SheetRender(sheet, imgOptions);

//Print the worksheet

sr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}

打印工作簿

**Java**

{{< highlight "java" >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **下载运行代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[打印工作簿](/cells/zh/java/printing-workbooks).

{{% /alert %}}
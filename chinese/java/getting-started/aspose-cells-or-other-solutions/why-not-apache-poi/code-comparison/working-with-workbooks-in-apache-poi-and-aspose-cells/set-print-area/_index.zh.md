---
title: 设置打印区域
type: docs
weight: 40
url: /zh/java/set-print-area/
---

## **Aspose.Cells - 设置打印区域**
默认情况下，只有打印区域包括所有包含数据的工作表区域。开发人员可以为工作表设定特定的打印区域。

要选择特定的打印区域，使用 [PageSetup](/java/pagesetup) 类的 setPrintArea 方法。将定义打印区域的单元格范围分配给此属性。

**Java**

{{< highlight java >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Workbook file

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet sheet = worksheets.get(0);

// Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

// Specifying the cells range (from A1 cell to F20 cell) of the print area

pageSetup.setPrintArea("A1:F20");

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 设置打印区域**
Workbook.setPrintArea方法可用于设置打印区域的页面属性

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

Sheet sheet = wb.createSheet("Sheet1");

//sets the print area for the first sheet

wb.setPrintArea(0, "$A$1:$C$2");

//Alternatively:

wb.setPrintArea(

        0, //sheet index

        0, //start column

        1, //end column

        0, //start row

        0  //end row

);

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/setprintarea)

{{% alert color="primary" %}} 

要了解更多详情，请访问[设置打印选项](/cells/zh/java/page-setup-features/#setting-print-options)。

{{% /alert %}}

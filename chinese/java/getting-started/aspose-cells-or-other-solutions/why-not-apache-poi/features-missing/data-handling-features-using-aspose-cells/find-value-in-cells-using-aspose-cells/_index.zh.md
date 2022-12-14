---
title: 使用 Aspose.Cells 在 Cells 中查找值
type: docs
weight: 10
url: /zh/java/find-value-in-cells-using-aspose-cells/
---
## **Aspose.Cells - 在 Cells 中寻找价值**
在 Microsoft Excel 中，用户可以搜索包含特定数据的单元格。例如，点击**编辑**接着**寻找**打开搜索对话框。用户输入一个值并点击**好的**搜索它。 Excel 突出显示匹配字段。

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

//Finding the cell containing the specified formula

Cells cells = worksheet.getCells();

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.setLookAtType(LookAtType.START_WITH);

Cell cell = cells.find("SH",null,findOptions);

//Printing the name of the cell found after searching worksheet

System.out.println("Name of the cell containing String: " + cell.getName());

{{< /highlight >}}
## **下载运行代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/search/AsposeFindCellsWithString.java)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[查找或搜索数据](/cells/zh/java/find-or-search-data).

{{% /alert %}}

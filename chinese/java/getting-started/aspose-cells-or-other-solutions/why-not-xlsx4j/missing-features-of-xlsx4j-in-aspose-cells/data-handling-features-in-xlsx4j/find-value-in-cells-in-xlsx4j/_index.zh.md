---
title: 在xlsx4j中查找单元格中的值
type: docs
weight: 30
url: /zh/java/find-value-in-cells-in-xlsx4j/
---

## **Aspose.Cells - 在单元格中查找数值**
在Microsoft Excel中，用户可以搜索包含特定数据的单元格。例如，点击**编辑**然后**查找**打开搜索对话框。用户输入一个值并点击**确定**来搜索它。Excel会高亮显示匹配字段。

**Java**

{{< highlight java >}}

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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/findvalueincells/AsposeFindValueInCells.java)

{{% alert color="primary" %}} 

更多详情，请访问[查找或搜索数据](/cells/zh/java/find-or-search-data)。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

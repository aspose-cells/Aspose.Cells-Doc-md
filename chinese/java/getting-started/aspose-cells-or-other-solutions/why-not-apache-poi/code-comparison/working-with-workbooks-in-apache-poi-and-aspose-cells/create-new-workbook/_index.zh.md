---
title: 创建新工作簿
type: docs
weight: 20
url: /zh/java/create-new-workbook/
---

## **Aspose.Cells - 创建新工作簿**
Workbook类可用于简单使用

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.save("newWorkBook.xlsx", SaveFormat.XLSX); //Workbooks can be saved in many formats

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 创建新工作簿**
使用Workbook类创建新工作簿，并使用FileOutputStream保存

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

FileOutputStream fileOut;

fileOut = new FileOutputStream("newWorkbook.xls");

wb.write(fileOut);

fileOut.close();

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/createnewworkbook)

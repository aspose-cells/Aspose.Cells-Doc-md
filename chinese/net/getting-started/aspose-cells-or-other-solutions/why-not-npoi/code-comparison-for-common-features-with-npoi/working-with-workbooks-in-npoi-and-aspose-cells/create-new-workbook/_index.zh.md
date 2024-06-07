---
title: 创建新工作簿
type: docs
weight: 20
url: /zh/net/create-new-workbook/
---

## **Aspose.Cells - 创建新工作簿**
Workbook类可供简单使用

**C#**

{{< highlight cs >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /highlight >}}
## **NPOI - HSSF XSSF - 创建新工作簿**
使用Workbook类创建新工作簿，然后使用FileOutputStream保存。

**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

workbook.CreateSheet("Sheet A1");

workbook.CreateSheet("Sheet A2");

workbook.CreateSheet("Sheet A3");

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **下载运行代码**
从以下社交编码网站之一下载**创建新工作簿**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)

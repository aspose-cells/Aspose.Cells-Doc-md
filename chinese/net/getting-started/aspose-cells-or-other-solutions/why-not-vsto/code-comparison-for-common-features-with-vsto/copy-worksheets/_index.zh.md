﻿---
title: 复制工作表
type: docs
weight: 60
url: /zh/net/copy-worksheets/
---
## **迁移提示：**
\1.创建工作簿对象并获取工作表。
\2。在工作表中插入文本。
\3。创建新的工作表并将其复制到之前制作的工作表中。
### **VSTO**
呈现宏“代码”时出错：为参数 lang 指定的值无效
### **Aspose.Cells**
{{< highlight "csharp" >}}

  private static string fileName ="CopyWorksheets.xlsx";

 Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0, 0].PutValue("Some Text");

 Worksheet worksheet2 = newWorkbook.Worksheets.Add("MySheet");

 worksheet2.Copy(worksheet);

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **下载**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)

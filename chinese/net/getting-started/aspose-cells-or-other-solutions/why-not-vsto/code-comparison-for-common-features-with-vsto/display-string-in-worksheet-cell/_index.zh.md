---
title: 在工作表单元格中显示字符串
type: docs
weight: 110
url: /zh/net/display-string-in-worksheet-cell/
---

## **VSTO**
{{< highlight csharp >}}

  Excel.Workbook myWorkbook = this.Application.Workbooks.Open(fileName);

 Excel.Worksheet mySheet = myWorkbook.ActiveSheet;

 Excel.Range cells = mySheet.Cells;

 cells.set_Item(1, 1, "Some Text");

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

  Workbook myWorkbook = new Workbook(fileName);

 Worksheet mySheet = myWorkbook.Worksheets[myWorkbook.Worksheets.ActiveSheetIndex];

 Cells cells = mySheet.Cells;

 cells[0, 0].PutValue("Some Text");

 myWorkbook.Save(fileName);

{{< /highlight >}}
## **下载**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DisplayStringInCell.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}

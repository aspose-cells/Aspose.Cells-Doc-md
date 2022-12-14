---
title: 将样式应用于工作簿中的范围
type: docs
weight: 40
url: /zh/net/apply-styles-to-ranges-in-workbooks/
---
下面是对工作簿的行和列应用样式的代码对比：
## **VSTO**
{{< highlight "csharp" >}}

  Excel.Workbook myWorkbook = this.Application.Workbooks.Open(fileName);

 Excel.Worksheet mySheet = myWorkbook.ActiveSheet;

 Excel.Style style = this.Application.ActiveWorkbook.Styles.Add("NewStyle");

 style.Font.Name = "Verdana";

 style.Font.Size = 12;

 style.Font.Color = System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.Red);

 style.Interior.Color = System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.Gray);

 style.Interior.Pattern = Excel.XlPattern.xlPatternSolid;

 Excel.Range FormatingRange = mySheet.get_Range("A1", "A10");

 FormatingRange.Style = "NewStyle";

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

  Workbook myWorkbook = new Workbook(fileName);

 Worksheet mySheet = myWorkbook.Worksheets[myWorkbook.Worksheets.ActiveSheetIndex];

 Style style = myWorkbook.CreateStyle();

 style.VerticalAlignment = TextAlignmentType.Center;

 //Setting the horizontal alignment of the text in the "A1" cell

 style.HorizontalAlignment = TextAlignmentType.Center;

 //Setting the font color of the text in the "A1" cell

 style.Font.Color = Color.Green;

 //Shrinking the text to fit in the cell

 style.ShrinkToFit = true;

 //Setting the bottom border color of the cell to red

 style.Borders[BorderType.BottomBorder].Color = Color.Red;

 //Creating StyleFlag

 StyleFlag styleFlag = new StyleFlag();

 styleFlag.HorizontalAlignment = true;

 styleFlag.VerticalAlignment = true;

 styleFlag.ShrinkToFit = true;

 styleFlag.Borders = true;

 styleFlag.FontColor = true;

 //Accessing a row from the Rows collection

 Column column = mySheet.Cells.Columns[0];

 //Assigning the Style object to the Style property of the row

 column.ApplyStyle(style, styleFlag);

 myWorkbook.Save(fileName);

{{< /highlight >}}
## **下载**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/ApplyStylesToRanges.Aspose.Cells.zip)

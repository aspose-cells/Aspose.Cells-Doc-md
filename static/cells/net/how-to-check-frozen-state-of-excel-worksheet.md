##How to check Frozen State without Excel.
In this article, you will learn how check frozen state of excel worksheet programmatically using C# Library with .NET API.
## **Introduction**
In this article, we will learn how check frozen state of excel worksheet programmatically. We can simply find whether the worksheet is frozen or splitted in MS Excel. But is there a way to find whether it is frozen or splitted with CSharp. We can simply do it with Aspose.Cells for .Net.
## **Are Window Panes Frozen**
With Aspose.Cells for .Net, we can check whether the window is frozen and how many rows and columns are locked.
Please use the [**Worksheet.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) property to check the state of window panes
and gets locked rows and columns with  [**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/) method.
1. Construct Workbook to open the file.
2. Check whether the worksheet is frozen.
3. Gets the locked row and columns

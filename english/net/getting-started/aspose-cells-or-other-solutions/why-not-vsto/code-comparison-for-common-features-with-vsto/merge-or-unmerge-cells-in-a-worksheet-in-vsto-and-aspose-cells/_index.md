---
title: Merge or UnMerge Cells in a Worksheet in VSTO and Aspose.Cells
type: docs
weight: 170
url: /net/merge-or-unmerge-cells-in-a-worksheet-in-vsto-and-aspose-cells/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Open an existing **Excel** file, **merge** some cells in the first worksheet of the workbook, and save the **Excel** file.

## **Merging Cells**
### **VSTO**
Following are the parallel code snippets for VSTO (C#) and Aspose.Cells for .NET (C#).

{{< highlight csharp >}}

 //Instantiate the Application object.

 Excel.Application excelApp = Application;

//Specify the template **Excel** file path.

 string myPath = "Book1.xls";

//Open the Excel file.

 excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value);

//Get the range of cells i.e., A1:C1.

 Excel.Range rng1 = excelApp.get_Range("A1", "C1");

//Merge the cells.

 rng1.Merge(Missing.Value);

 rng1 = excelApp.get_Range("A1", Missing.Value);

//Save the file.

 excelApp.ActiveWorkbook.Save();

//Quit the Application.

 excelApp.Quit();

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Instantiate a new Workbook.

  Workbook workbook = new Workbook();

//Specify the template **Excel** file path.

 string myPath = "Book1.xls";

//Open the Excel file.

 workbook.Open(myPath);

//Get the range of cells i.e., A1:C1.

 Aspose.Cells.Range rng1 = workbook.Worksheets[0].Cells.CreateRange("A1", "C1");

//Merge the cells.

 rng1.Merge();

//Save the file.

  workbook.Save("Book1.xls");

{{< /highlight >}}
## **UnMerging Cells**
To unmerge the cell(s), use the following lines of code for VSTO (C#) and Aspose.Cells for .NET (C#).
### **VSTO**
{{< highlight csharp >}}

 //Unmerge the cell.

  rng1.UnMerge();

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

   Cells rng = workbook.Worksheets[0].Cells;

//Unmerge the cell.

  rng.UnMerge(0, 0, 1, 3);

{{< /highlight >}}
## **Download Sample Code**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Merge.or.UnMerge.Cells.in.a.Worksheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Merge%20or%20UnMerge%20Cells%20in%20a%20Worksheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Merge%20or%20UnMerge%20Cells%20in%20a%20Worksheet%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}

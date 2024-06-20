---
title: Unisci o Dividi Celle in un Foglio di Lavoro in VSTO e Aspose.Cells
type: docs
weight: 170
url: /it/net/merge-or-unmerge-cells-in-a-worksheet-in-vsto-and-aspose-cells/
---

Aprire un file Excel esistente, unire alcune celle nel primo foglio di lavoro nel workbook e salvare il file di Excel.
## **Unione di celle**
### **VSTO**
Di seguito sono riportati i paralleli frammenti di codice per VSTO (C#) e Aspose.Cells for .NET (C#).

{{< highlight csharp >}}

 //Instantiate the Application object.

 Excel.Application excelApp = Application;

//Specify the template excel file path.

 string myPath = "Book1.xls";

//Open the excel file.

 excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value);

//Get the range of cells i.e.., A1:C1.

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

//Specify the template excel file path.

 string myPath = "Book1.xls";

//Open the excel file.

 workbook.Open(myPath);

//Get the range of cells i.e.., A1:C1.

 Aspose.Cells.Range rng1 = workbook.Worksheets[0].Cells.CreateRange("A1", "C1");

//Merge the cells.

 rng1.Merge();

//Save the file.

  workbook.Save("Book1.xls");

{{< /highlight >}}
## **Dividere le celle**
Per dividere le celle, utilizzare le seguenti righe di codice per VSTO (C#) e Aspose.Cells for .NET (C#).
### **VSTO**
{{< highlight csharp >}}

 //UnMerge the cell.

  rng1.UnMerge();

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

   Cells rng = workbook.Worksheets[0].Cells;

//UnMerge the cell.

  rng.UnMerge(0, 0, 1, 3);

{{< /highlight >}}
## **Scarica il codice di esempio**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Merge.or.UnMerge.Cells.in.a.Worksheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Merge%20or%20UnMerge%20Cells%20in%20a%20Worksheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Merge%20or%20UnMerge%20Cells%20in%20a%20Worksheet%20\(Aspose.Cells\).zip)

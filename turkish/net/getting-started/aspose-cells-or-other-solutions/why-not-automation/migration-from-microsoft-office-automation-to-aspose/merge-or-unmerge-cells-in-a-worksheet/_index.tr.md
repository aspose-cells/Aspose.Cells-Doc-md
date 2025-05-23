---
title: Çalışma Sayfasında Hücreleri Birleştirme veya Ayırma
type: docs
weight: 40
url: /tr/net/merge-or-unmerge-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Çalışma sayfaları ile çalışırken, genellikle çalışma sayfanızın üst kısmını kaplayan tek bir hücrede bir başlık / başlık oluşturmanız gerekebilir. Fatura oluşturuyor olabilirsiniz ve toplam veya özet değerler için daha az sütun isteyebilirsiniz. İki veya daha fazla hücreden bir hücre yapmak istediğinizde hücreleri birleştirirsiniz. Bu görevi VSTO ve Aspose.Cells for .NET kullanarak bağımsız olarak gerçekleştiririz.

{{% /alert %}}

## **Açıklama**

Var olan bir excel dosyasını aç, çalışma kitabındaki ilk sayfadaki bazı hücreleri birleştir ve excel dosyasını kaydet.

## **Hücreleri Birleştirme**

Aşağıdakiler VSTO (C#, VB) ve Aspose.Cells for .NET (C#, VB) için paralel kod parçacıklarıdır.

### **1) VSTO**

**C#**

{{< highlight csharp >}}

 .......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template excel file path.

string myPath=@"d:\test\MyBook.xls";

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

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template excel file path.

string myPath=@"d:\test\MyBook.xls";

//Open the excel file.

workbook.Open(myPath);

//Get the range of cells i.e.., A1:C1.

Aspose.Cells.Range rng1 = workbook.Worksheets[0].Cells.CreateRange("A1", "C1");

//Merge the cells.

rng1.Merge();

//Save the file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **Hücreleri Ayırmak**

Hücre(ler)i ayırmak için VSTO (C#, VB) ve Aspose.Cells for .NET (C#, VB) için aşağıdaki kod satırlarını kullanın.

### **1) VSTO**

**C#**

{{< highlight csharp >}}

 //Get the A1 cell (Merged Cell).

Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);

//UnMerge the cell.

rng1.UnMerge();     



{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 //Get the A1 cell (Merged Cell).

Cells rng1 = workbook.Worksheets[0].Cells;

//UnMerge the cell.

rng1.UnMerge(0, 0, 1, 3); 

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

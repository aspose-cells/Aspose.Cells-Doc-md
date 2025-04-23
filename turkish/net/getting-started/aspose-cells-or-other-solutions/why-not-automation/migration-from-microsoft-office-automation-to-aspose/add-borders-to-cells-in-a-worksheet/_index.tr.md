---
title: Bir Çalışma Sayfasında Hücrelere Kenarlık Eklemek
type: docs
weight: 50
url: /tr/net/add-borders-to-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET, Microsoft Excel'de bir kullanıcının gerçekleştirebileceği neredeyse tüm görevleri uygulamanız aracılığıyla gerçekleştirmenize olanak tanır. Aspose.Cells performanslı ve sağlamdır ve Microsoft Automation'dan bağımsız olarak çalışma avantajına sahiptir. Bu makale, VSTO'ya kıyasla Aspose.Cells for .NET kullanarak bir çalışma sayfasındaki hücrelere kenarlık eklemenin nasıl yapıldığını göstermektedir.

{{% /alert %}}

## **Hücrelere Kenarlık Eklemek**

Bir elektronik tabloya hücrelere kenarlık eklemek için aşağıdaki adımları izleyin:

1. Çalışma sayfasını kurun:
   1. Bir Uygulama nesnesi örnekleyin.
      (Sadece VSTO.)
   1. Bir çalışma kitabı ekleyin.
   1. İlk sayfayı alın.
   1. Sınırlar ekleyeceğiniz hücrelere metin ekleyin.
1. Kenarlık ekle:
   1. Bir aralık tanımlayın.
   1. Arağ stilini aralığa uygulayın.
      Her aralık ve sınır stili için tekrarlayın. Bu örnek, hairlines, thin, medium ve thick çizgiler uygular.
1. Bitir:
   1. Hücrelerin bulunduğu sütunu metne sığacak şekilde otomatik boyutlandırın.
   1. Belgeyi kaydedin.

Bu adımlar aşağıda verilen kod örneğinde gösterilmiştir. İlk kod örnekleri, [VSTO](/cells/tr/net/add-borders-to-cells-in-a-worksheet/) kullanarak bunları C# veya Visual Basic ile nasıl uygulayacağınızı gösterir. VSTO örneklerinden sonra, aynı adımları yapmak için [Aspose.Cells for .NET](/cells/tr/net/add-borders-to-cells-in-a-worksheet/) kullanarak, yine C# veya Visual Basic ile nasıl yapılacağını gösteren örnekler bulunmaktadır. Aspose.Cells kod örnekleri daha kısadır çünkü Aspose.Cells verimli kodlama için optimize edilmiştir.

Kod, birinci sayfadaki farklı kenarlıklı birçok hücreye sahip bir Excel dosyası oluşturur

![todo:image_alt_text](add-borders-to-cells-in-a-worksheet_1.png)

**Sınırlı Hücreler.**

### **VSTO Kullanarak Sınırlar Ekleme**

**C#**

{{< highlight csharp >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[2, 1] = "Hair Lines";

objSheet.Cells[4, 1] = "Thin Lines";

objSheet.Cells[6, 1] = "Medium Lines";

objSheet.Cells[8, 1] = "Thick Lines";

//Define a range object(A2).

Excel.Range _range;

_range = objSheet.get_Range("A2", "A2");

//Get the borders collection.

Excel.Borders borders = _range.Borders;

//Set the hair lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 1d;



//Define a range object(A4).

_range = objSheet.get_Range("A4", "A4");

//Get the borders collection.

borders = _range.Borders;

//Set the thin lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 2d;



//Define a range object(A6).

_range = objSheet.get_Range("A6", "A6");

//Get the borders collection.

borders = _range.Borders;

//Set the medium lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 3d;



//Define a range object(A8).

_range = objSheet.get_Range("A8", "A8");

//Get the borders collection.

borders = _range.Borders;

//Set the thick lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 4d;



//Auto-fit Column A.

objSheet.get_Range("A2", "A2").EntireColumn.AutoFit();



//Save the excel file.

objBook.SaveAs("f:\\test\\ApplyBorders.xls",

Microsoft.Office.Interop.Excel.XlFileFormat.xlExcel8,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Microsoft.Office.Interop.Excel.XlSaveAsAccessMode.xlNoChange,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing);



//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Aspose.Cells for .NET Kullanarak Sınırlar Ekleme**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook objBook = new Workbook();  

//Get the First sheet.

Worksheet objSheet = objBook.Worksheets["Sheet1"];



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[1, 0].PutValue("Hair Lines");

objSheet.Cells[3, 0].PutValue("Thin Lines");

objSheet.Cells[5, 0].PutValue("Medium Lines");

objSheet.Cells[7, 0].PutValue("Thick Lines");

//Define a range object(A2).

Aspose.Cells.Range _range;

_range = objSheet.Cells.CreateRange("A2", "A2");

//Set the borders with hair lines style.

_range.SetOutlineBorders( CellBorderType.Hair, Color.Black);

//Define a range object(A4).

_range = objSheet.Cells.CreateRange("A4", "A4");

//Set the borders with thin lines style.

_range.SetOutlineBorders(CellBorderType.Thin, Color.Black);

//Define a range object(A6).

_range = objSheet.Cells.CreateRange("A6", "A6");

//Set the borders with medium lines style.

_range.SetOutlineBorders(CellBorderType.Medium, Color.Black);

//Define a range object(A8).

_range = objSheet.Cells.CreateRange("A8", "A8");

//Set the borders with thick lines style.

_range.SetOutlineBorders(CellBorderType.Thick, Color.Black);

//Auto-fit Column A.

objSheet.AutoFitColumn(0);

//Save the excel file.

objBook.Save("f:\\test\\ApplyBorders.xls");        



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

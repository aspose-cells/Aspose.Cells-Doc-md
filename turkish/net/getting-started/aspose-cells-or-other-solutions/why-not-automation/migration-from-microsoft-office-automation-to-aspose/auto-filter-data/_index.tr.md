---
title: Verileri Başlangıç Filtrele
type: docs
weight: 120
url: /tr/net/auto-filter-data/
---

{{% alert color="primary" %}}

Bir aralıktaki verilerin ne olduğunu anlamak için, sütunlardaki düzenlenmemiş verilere bakmaktan ziyade verileri sıralamak ve filtrelemek genellikle daha kolaydır. Sıralama, verileri artan veya azalan düzende düzenler ve belirli değerleri bulmayı kolaylaştırır. Verileri filtrelemek, yalnızca belirli değerleri göstermenize olanak tanır. Örneğin, satış kayıtlarında belirli öğelere odaklanmanıza yardımcı olur.

Microsoft Excel kullanıcıları sütunlara otomatik filtreleme uygulayabilirler. Otomatik filtreleme, sütun verilerine sıralama veya filtre uygulamanızı sağlayan bir menü ekler. Bu özellik, Excel elektronik tablolarıyla çalışan geliştiricilere de [VSTO](/hücreler/tr/net/verileri-başlangıç-filtrele/) veya [Aspose.Cells for .NET](/hücreler/tr/net/verileri-başlangıç-filtrele/) ile erişilebilir.

{{% /alert %}}

## **Verileri Otomatik Filtreleme**

Bir sütuna otomatik filtre uygulamak için:

1. Bir çalışma kitabı oluşturma.
1. Bir çalışsayfayı alın.
1. Örnek veri ekleyin.
1. Otomatik filtre uygulayın.
1. Görüntüyü çekici hale getirmek için sütunları otomatik uygun hale getirin.
1. Elektronik tabloyu kaydedin.

Bu makaledeki kod örnekleri, bu adımları [VSTO](/hücreler/tr/net/verileri-başlangıç-filtrele/) ile C# veya Visual Basic veya [Apose.Cells](/hücreler/tr/net/verileri-başlangıç-filtrele/), tekrar C# veya Visual Basic kullanarak nasıl gerçekleştireceğinizi gösterir.

### **VSTO ile Verileri Otomatik Filtreleme**

**C#**

{{< highlight csharp >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;.........//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();



//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);



//Get the First sheet.

Excel.Worksheet sheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Add data into A1 and B1 Cells as headers.

sheet.Cells[1, 1] = "Product ID";

sheet.Cells[1, 2] = "Product Name";

//Add data into details cells.

sheet.Cells[2, 1] = 1;

sheet.Cells[3, 1] = 2;

sheet.Cells[4, 1] = 3;

sheet.Cells[5, 1] = 4;

sheet.Cells[2, 2] = "Apples";

sheet.Cells[3, 2] = "Bananas";

sheet.Cells[4, 2] = "Grapes";

sheet.Cells[5, 2] = "Oranges";

//Enable Auto-filter.           

sheet.EnableAutoFilter = true;



//Create the range.

Excel.Range range = sheet.get_Range("A1", "B5");



//Auto-filter the range.

range.AutoFilter("1", "<>", Microsoft.Office.Interop.Excel.XlAutoFilterOperator.xlOr, "", true);

//Auto-fit the second column.

sheet.get_Range("B1", "B5").EntireColumn.AutoFit();



//Save the copy of workbook as .xlsx file.

objBook.SaveCopyAs("e:\\test2\\vsto_autofilter.xlsx");



{{< /highlight >}}

**VSTO ile uygulanan otomatik filtreleme** 

![todo:image_alt_text](auto-filter-data_1.png)

### **Aspose.Cells for .NET ile Verileri Otomatik Filtreleme**

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook.

Workbook objBook = new Workbook();



//Get the First sheet.

Worksheet sheet = objBook.Worksheets["Sheet1"];

//Add data into A1 and B1 Cells as headers.

sheet.Cells[0, 0].PutValue("Product ID");

sheet.Cells[0, 1].PutValue("Product Name");

//Add data into details cells.

sheet.Cells[1, 0].PutValue(1);

sheet.Cells[2, 0].PutValue(2);

sheet.Cells[3, 0].PutValue(3);

sheet.Cells[4, 0].PutValue(4);

sheet.Cells[1, 1].PutValue("Apples");

sheet.Cells[2, 1].PutValue("Bananas");

sheet.Cells[3, 1].PutValue("Grapes");

sheet.Cells[4, 1].PutValue("Oranges");

//Auto-filter the range.

sheet.AutoFilter.Range = "A1:B5";

//Auto-fit the second column.

sheet.AutoFitColumn(1,0,4);

//Save the copy of workbook as .xlsx file.

objBook.Save("e:\\test2\\aspose-cells_autofilter.xlsx");



{{< /highlight >}}

**Aspose.Cells for .NET ile otomatik filtreleme uygulandı** 

![todo:image_alt_text](auto-filter-data_2.png)
{{< app/cells/assistant language="csharp" >}}

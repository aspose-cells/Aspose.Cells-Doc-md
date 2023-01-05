---
title: Verileri Otomatik Filtrele
type: docs
weight: 120
url: /tr/net/auto-filter-data/
---
{{% alert color="primary" %}}

Hangi verilerin bir aralıkta olduğunu anlamak için, genellikle sıralanmamış veri sütunlarına bakmaktansa verileri sıralamak ve filtrelemek daha kolaydır. Sıralama, verileri artan veya azalan düzende düzenleyerek belirli değerleri bulmayı kolaylaştırır. Verileri filtrelemek, yalnızca belirli değerleri göstermenizi sağlar. Örneğin, satış kayıtlarındaki belirli kalemlere odaklanmaya yardımcı olur.

Microsoft Excel kullanıcıları sütunlara otomatik filtreleme uygulayabilir. Otomatik filtreleme, sütunun üstüne, sütun verilerini filtreleyebileceğiniz bir menü ekler. Bu özellik, VSTO veya Aspose.Cells for .NET aracılığıyla Excel elektronik tablolarıyla çalışan geliştiriciler tarafından da kullanılabilir.

{{% /alert %}}

## **Verileri Otomatik Filtreleme**

Bir sütuna otomatik filtreleme uygulamak için:

1. Bir çalışma kitabı oluşturun.
1. Bir çalışma sayfası alın.
1. Örnek verileri ekleyin.
1. Otomatik filtre uygulayın.
1. Görüntüyü çekici hale getirmek için sütunları otomatik sığdırın.
1. Elektronik tabloyu kaydedin.

 Bu makaledeki kod örnekleri, kullanarak bu adımların nasıl gerçekleştirileceğini gösterir.[VSTO](/cells/tr/net/auto-filter-data/) C# veya Visual Basic ile veya kullanarak[Apose.Cells](/cells/tr/net/auto-filter-data/), yine C# veya Visual Basic ile.

### **VSTO ile Verileri Otomatik Filtreleme**

**C#**

{{< highlight "csharp" >}}

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

sheet.Cells[1, 1]= "Product ID";

sheet.Cells[1, 2]= "Product Name";

//Add data into details cells.

sheet.Cells[2, 1]= 1;

sheet.Cells[3, 1]= 2;

sheet.Cells[4, 1]= 3;

sheet.Cells[5, 1]= 4;

sheet.Cells[2, 2]= "Apples";

sheet.Cells[3, 2]= "Bananas";

sheet.Cells[4, 2]= "Grapes";

sheet.Cells[5, 2]= "Oranges";

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

**VSTO ile uygulanan otomatik filtre** 

![yapılacaklar:resim_alternatif_metin](auto-filter-data_1.png)

### **Aspose.Cells for .NET ile Verileri Otomatik Filtreleme**

**C#**

{{< highlight "csharp" >}}

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

**Aspose.Cells for .NET ile uygulanan otomatik filtre** 

![yapılacaklar:resim_alternatif_metin](auto-filter-data_2.png)

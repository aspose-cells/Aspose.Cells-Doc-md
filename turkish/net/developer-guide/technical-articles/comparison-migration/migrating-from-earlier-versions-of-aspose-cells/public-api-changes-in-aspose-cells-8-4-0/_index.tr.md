---
title: Genel API Aspose.Cells 8.4.0'daki değişiklikler
type: docs
weight: 130
url: /tr/net/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürüm 8.3.2'den 8.4.0'a modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-4-0/) ve[kaldırılan sınıflar vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-4-0/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **Elektronik Tablolardaki VBA/Makro Kodunu Değiştirme Mekanizması**
 özelliğini sağlamak için[VBA/Makro Kod Manipülasyonu](/cells/tr/net/modifying-vba-or-macro-code-using-aspose-cells/)Aspose.Cells for .NET 8.4.0, Aspose.Cells.Vba ad alanında bir dizi yeni sınıf ve özellik ortaya çıkardı. Bu yeni sınıfların önemli detaylarından birkaçı aşağıdaki gibidir.

- VbaProject sınıfı, belirli bir elektronik tablodan VBA projesini getirmek için kullanılabilir.
- VbaModuleCollection sınıfı, belirli bir VbaProject'in parçası olan VBA modüllerinin koleksiyonunu temsil eder.
- VbaModule sınıfı, VbaModuleCollection'dan tek bir modülü temsil eder.

Aşağıdaki kod parçacığı, VBA kod bölümlerinin dinamik olarak nasıl değiştirileceğini gösterir.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

foreach (VbaModule module in workbook.VbaProject.Modules)

{

    string code = module.Codes;

    //Replace the original message with the modified message

    if (code.Contains("This is test message."))

    {

        code = code.Replace("This is test message.", "This is Aspose.Cells message.");

        module.Codes = code;

    }

}

//Save the output Excel file

workbook.Save("output.xlsm");

{{< /highlight >}}


### **Pivot Tabloyu Kaldırma Yeteneği**
Aspose.Cells for .NET 8.4.0, PivotTableCollection'ın belirli bir e-tablodan Pivot Tablo kaldırma özelliği sağlaması için iki yöntem ortaya çıkardı. Bahsi geçen yöntemlerin detayları aşağıdaki gibidir.

- PivotTableCollection.Remove yöntemi, PivotTable'ın bir nesnesini kabul eder ve onu koleksiyondan kaldırır.
- PivotTableCollection.RemoveAt yöntemi, sıfır dizin tabanlı bir tamsayı değeri kabul eder ve belirli PivotTable'ı koleksiyondan kaldırır.

Aşağıdaki kod parçacığı, PivotTable'ın yukarıda belirtilen her iki yöntemi de kullanarak nasıl kaldırılacağını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first pivot table object

PivotTable pivotTable = worksheet.PivotTables[0];

//Remove pivot table using pivot table object

worksheet.PivotTables.Remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.PivotTables.RemoveAt(0);

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Farklı Pivot Tablo Düzenleri için Destek**
Aspose.Cells for .NET 8.4.0, Pivot Tablolar için önceden tanımlanmış farklı düzenler için destek sağlar. Bu özelliği sağlamak için Aspose.Cells API'leri, PivotTable sınıfı için aşağıda ayrıntılı olarak açıklanan üç yöntemi kullanıma sunmuştur.

- PivotTable.ShowInCompactForm yöntemi, Pivot Tabloyu Kompakt mizanpajda işler.
- PivotTable.ShowInOutlineForm yöntemi, Pivot Tabloyu Anahat düzeninde işler.
- PivotTable.ShowInTabularForm yöntemi, Pivot Tabloyu Tablo düzeninde işler.

{{% alert color="primary" %}} 

Yukarıda belirtilen düzenlerden herhangi birini ayarladıktan sonra PivotTable.RefreshData & PivotTable.CalculateData'yı çağırmak önemlidir.

{{% /alert %}} 

Aşağıdaki örnek kod, Pivot Tablo için farklı düzenler ayarlar ve sonucu diskte depolar.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table

PivotTable pivotTable = worksheet.PivotTables[0];

//Render the pivot table in compact form

pivotTable.ShowInCompactForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("CompactForm.xlsx");

//Render the pivot table in outline form

pivotTable.ShowInOutlineForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("OutlineForm.xlsx");

//Render the pivot table in tabular form

pivotTable.ShowInTabularForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("TabularForm.xlsx");

{{< /highlight >}}


### **Sınıf TxtLoadStyleStrategy ve Özellik TxtLoadOptions.LoadStyleStrategy Eklendi**
Aspose.Cells for .NET 8.4.0, dize değerini sayıya veya tarih saatine dönüştürürken ayrıştırılan değerleri biçimlendirme stratejisini belirtmek için TxtLoadStyleStrategy sınıfını ve TxtLoadOptions.LoadStyleStrategy özelliğini kullanıma sundu.
### **Yöntem DataBar.ToImage Eklendi**
v8.4.0'ın piyasaya sürülmesiyle, Aspose.Cells API, koşullu olarak biçimlendirilmiş DataBar'ları görüntü biçiminde kaydetmek için DataBar.ToImage yöntemini sağladı. {DataBar.ToImage}} yöntemi, aşağıda ayrıntıları verilen iki parametreyi kabul eder.

- İlk parametre, koşullu biçimlendirmenin uygulandığı Aspose.Cells.Cell türündedir.
- Elde edilen görüntünün farklı parametrelerini ayarlamak için ikinci parametre Aspose.Cells.Rendering.ImageOrPrintOptions türündedir.

Aşağıdaki örnek kod, DataBar'ı görüntü biçiminde işlemek için DataBar.ToImage yönteminin kullanımını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.Cells["C1"];

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.GetFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc[0].DataBar;

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.ImageFormat = ImageFormat.Png;

//Get the image bytes of the databar

byte[]imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Özellik Border.ThemeColor Eklendi**
Aspose.Cells API'ler, elektronik tablolardan temayla ilgili biçimlendirme verilerinin çıkarılmasına izin verir. Aspose.Cells for .NET 8.4.0 sürümüyle birlikte API, Cell kenarlıklarının tema rengi özniteliklerini almak için kullanılabilecek Border.ThemeColor özelliğini kullanıma sundu.
### **Özellik DrawObject.ImageBytes Eklendi**
Aspose.Cells for .NET 8.4.0, Grafik veya Şekil'den resim verilerini almak için DrawObject.ImageBytes özelliğini kullanıma sundu.
### **Özellik HtmlSaveOptions.ExportBogusRowData Eklendi**
Aspose.Cells for .NET 8.4.0, {HtmlSaveOptions.ExportBogusRowData}} özelliğini sağladı. Boole tipi özelliği, elektronik tabloyu HTML biçimine dışa aktarırken API'in sahte alt sıra verileri enjekte edip etmeyeceğini belirler.

{{% alert color="primary" %}} 

Varsayılan değer doğrudur.

{{% /alert %}} 

Aşağıdaki örnek kod, yukarıda bahsedilen özelliğin kullanımını göstermektedir.

**C#**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Özellik HtmlSaveOptions.CellCssPrefix Eklendi**
Yeni eklenen özellik HtmlSaveOptions.CellCssPrefix, e-tabloları HTML biçiminde dışa aktarırken CSS dosyaları için önek ayarlamanıza olanak tanır.

{{% alert color="primary" %}} 

Varsayılan değer boş bir dizedir).

{{% /alert %}}
## **Eski API'ler**
### **Yöntemler Cells.GetCellByIndex & Row.GetCellByIndex Kullanımdan Kaldırıldı**
Bunun yerine tüm hücreleri yinelemek için GetEnumerator yöntemini kullanın.
### **DrawObject.Image Özelliği Kullanımdan Kaldırıldı**
Bunun yerine resim verilerini almak için DrawObject.ImageBytes özelliğini kullanın.

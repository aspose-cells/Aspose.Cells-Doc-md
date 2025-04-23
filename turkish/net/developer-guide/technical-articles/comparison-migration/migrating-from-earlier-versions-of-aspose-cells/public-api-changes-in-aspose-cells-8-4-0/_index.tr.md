---
title: Aspose.Cells 8.4.0 taki Genel API Değişiklikleri
type: docs
weight: 130
url: /tr/net/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'deki 8.3.2'den 8.4.0'a kadar olan değişiklikleri, modül/uygulama geliştiricilerin ilgisini çekebilecek olanları açıklamaktadır. Bu, sadece yeni ve güncellenmiş genel yöntemleri içermekle kalmaz, aynı zamanda Aspose.Cells'in arka planında olan herhangi bir değişikliğin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Elektronik Tablolardaki VBA/Makro Kodunu Değiştirme Mekanizması**
Aspose.Cells for .NET 8.4.0'da Aspose.Cells.Vba ad alanında yeni sınıflar ve özellikler serilerini sunmak için VBA/Makro Kodu Manipülasyonu özelliğini sağlamak amacıyla bir dizi yeni sınıf ve özelliği açığa çıkardı. Bu yeni sınıfların bazı önemli detayları şu şekildedir.

- VbaProject sınıfı, verilen elektronik tablodan VBA projesini almak için kullanılabilir.
- VbaModuleCollection sınıfı, verilen VbaProject'ın bir parçası olan VBA modüllerinin koleksiyonunu temsil eder.
- VbaModule sınıfı, VbaModuleCollection'dan tek bir modülü temsil eder.

Aşağıdaki kod parçası, VBA kod segmentlerini dinamik olarak nasıl değiştireceğinizi gösterir.

**C#**

{{< highlight csharp >}}

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


### **Pivot Tablosu Kaldırma Yeteneği**
Aspose.Cells for .NET 8.4.0, PivotTableCollection için bir elek tablodan Pivot Tablosu kaldırma özelliğini sağlamak amacıyla iki yöntem açığa çıkardı. Yukarıda bahsedilen yöntemlerin detayları şu şekildedir.

- PivotTableCollection.Remove yöntemi bir PivotTable nesnesi alır ve onu koleksiyondan kaldırır.
- PivotTableCollection.RemoveAt yöntemi sıfır indeks tabanlı bir tamsayı değeri alır ve belirli bir PivotTable'ı koleksiyondan kaldırır.

Aşağıdaki kod parçası, yukarıda bahsedilen her iki yöntemi kullanarak PivotTablosu'nu nasıl kaldıracağınızı gösterir.

**C#**

{{< highlight csharp >}}

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


### **Farklı Pivot Tablosu Düzenleri Desteği**
Aspose.Cells for .NET 8.4.0, Pivot Tables için farklı önceden tanımlanmış düzenlere destek sağlar. Bu özelliği sağlamak için Aspose.Cells API'ları PivotTable sınıfı için aşağıda detayları verilen üç yöntemi açığa çıkarmıştır.

- PivotTable.ShowInCompactForm yöntemi Pivot Tablosunu Kompakt düzeninde render eder.
- PivotTable.ShowInOutlineForm yöntemi Pivot Tablosunu Anahat düzeninde render eder.
- PivotTable.ShowInTabularForm yöntemi Pivot Tablosunu Tablo düzeninde render eder.

{{% alert color="primary" %}} 

Yukarıda bahsedilen düzenlerden herhangi birini ayarladıktan sonra PivotTable.RefreshData ve PivotTable.CalculateData yöntemlerini çağırmak önemlidir.

{{% /alert %}} 

Aşağıdaki örnek kod, bir Pivot Tablosu için farklı düzenler belirler ve sonucu diske kaydeder.

**C#**

{{< highlight csharp >}}

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


### **Class TxtLoadStyleStrategy & Property TxtLoadOptions.LoadStyleStrategy Eklendi**
Aspose.Cells for .NET 8.4.0, TxtLoadStyleStrategy sınıfını ve TxtLoadOptions.LoadStyleStrategy özelliğini metin değerini sayıya veya tarih saatine dönüştürürken ayrı biçimlenmiş değerleri belirtmek için açığa çıkarmıştır.
### **DataBar.ToImage Metodu Eklendi**
V8.4.0 sürümü ile Aspose.Cells API, koşullu biçimlendirilmiş DataBar'ları resim formatında kaydetmek için DataBar.ToImage yöntemini sağlamıştır. DataBar.ToImage yöntemi aşağıda detayları verilen iki parametreyi kabul eder.

- İlk parametre, koşullu biçimlendirmenin uygulandığı Aspose.Cells.Cell türündedir.
- İkinci parametre, farklı görüntü parametrelerini ayarlamak için Aspose.Cells.Rendering.ImageOrPrintOptions türündedir.

Aşağıdaki örnek kod, DataBar.ToImage yönteminin kullanımını resim formatında DataBar'ı render etmek için gösterir.

**C#**

{{< highlight csharp >}}

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

byte[] imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Border.ThemeColor Özelliği Eklendi**
Aspose.Cells API'ları, elektronik tablolardan temaya ilişkin biçimlendirme verilerini çıkarmaya olanak sağlar. Aspose.Cells for .NET 8.4.0 sürümü ile API, Hücre sınırları tema rengi özelliklerini almak için kullanılabilen Border.ThemeColor özelliğini açığa çıkarmıştır.
### **DrawObject.ImageBytes Özelliği Eklendi**
Aspose.Cells for .NET 8.4.0 sürümü ile DrawObject.ImageBytes özelliği, Grafik veya Şekilden resim verileri almak için açığa çıkarılmıştır.
### **HtmlSaveOptions.ExportBogusRowData Özelliği Eklendi**
Aspose.Cells for .NET 8.4.0, HtmlSaveOptions.ExportBogusRowData özelliğini sağlamıştır. Boolean türünde özellik, elektronik tabloyu HTML formatına dönüştürürken API'nin yanlış alt satır verisi ekleyip eklemediğini belirler.

{{% alert color="primary" %}} 

Varsayılan değer true'dur.

{{% /alert %}} 

Aşağıdaki örnek kod, yukarıdaki özellik kullanımını göstermektedir.

**C#**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **HtmlSaveOptions.CellCssPrefix Özelliği Eklendi**
Yeni eklenen HtmlSaveOptions.CellCssPrefix özelliği, elektronik tabloları HTML formatına dönüştürürken CSS dosyaları için önek belirlemeye olanak tanır.

{{% alert color="primary" %}} 

Varsayılan değer "" (boş dize) dir.

{{% /alert %}}
## **Eski API'ler**
### **Kullanım dışı hale getirilen Cells.GetCellByIndex & Row.GetCellByIndex Yöntemleri**
Hücreleri tümünü yinelemek için GetEnumerator yöntemini kullanın.
### **Eski DrawObject.Image Özelliği**
Resim verilerini almak için DrawObject.ImageBytes özelliğini kullanın.
{{< app/cells/assistant language="csharp" >}}

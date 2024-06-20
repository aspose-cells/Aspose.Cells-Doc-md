---
title: Aspose.Cells 8.4.0 taki Genel API Değişiklikleri
type: docs
weight: 140
url: /tr/java/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sındaki 8.3.2'den 8.4.0'a kadar olan değişiklikleri, modül / uygulama geliştiricilerin ilgisini çekebilecek şekilde açıklar. Sadece yeni ve güncellenmiş genel yöntemleri, [eklenen sınıflar vb.](/cells/tr/java/public-api-changes-in-aspose-cells-8-4-0/) ve [kaldırılan sınıflar vb.](/cells/tr/java/public-api-changes-in-aspose-cells-8-4-0/) içermez, aynı zamanda Aspose.Cells'in arka plandaki davranışındaki değişikliklerin bir açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Elektronik Tablolardaki VBA/Makro Kodunu Değiştirme Mekanizması**
[VBA/Makro Kodu Manipülasyonu](/cells/tr/java/modifying-vba-or-macro-code-using-aspose-cells/) özelliğini sağlamak için, Aspose.Cells for Java 8.4.0, com.aspose.cells.Vba paketinde bir dizi yeni sınıf ve özellikleri açığa çıkarmıştır. Bu yeni sınıfların bazı önemli ayrıntıları aşağıdaki gibidir.

- VbaProject sınıfı, verilen elektronik tablodan VBA projesini almak için kullanılabilir.
- VbaModuleCollection sınıfı, verilen VbaProject'ın bir parçası olan VBA modüllerinin koleksiyonunu temsil eder.
- VbaModule sınıfı, VbaModuleCollection'dan tek bir modülü temsil eder.

Aşağıdaki kod parçası, VBA kod segmentlerini dinamik olarak nasıl değiştireceğinizi gösterir.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

VbaModuleCollection modules = workbook.getVbaProject().getModules();

for(int i=0; i < modules.getCount(); i++)

{

	VbaModule module = modules.get(i);

    String code = module.getCodes();

    //Replace the original message with the modified message

    if (code.contains("This is test message."))

    {

        code = code.replace("This is test message.", "This is Aspose.Cells message.");

        module.setCodes(code);

    }

}

//Save the output Excel file

workbook.save("output.xlsm");

{{< /highlight >}}
### **Pivot Tablosu Kaldırma Yeteneği**
Aspose.Cells for Java 8.4.0, belirli bir elektronik tablodan Pivot Tablosu kaldırma özelliğini sağlamak için PivotTableCollection için iki yöntem sağlamıştır. Yukarıdaki yöntemlerin ayrıntıları aşağıdaki gibidir.

- PivotTableCollection.remove yöntemi, bir PivotTable nesnesini kabul eder ve onu koleksiyondan kaldırır.
- PivotTabloKoleksiyonu.removeAt yöntemi, sıfır tabanlı bir tamsayı değeri kabul eder ve belirli PivotTable'ı koleksiyondan kaldırır.

Aşağıdaki kod parçası, yukarıda bahsedilen her iki yöntemi kullanarak PivotTablosu'nu nasıl kaldıracağınızı gösterir.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first pivot table object

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Remove pivot table using pivot table object

worksheet.getPivotTables().remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.getPivotTables().removeAt(0);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Farklı Pivot Tablosu Düzenleri Desteği**
Aspose.Cells for Java 8.4.0, Pivot Tabloları için farklı önceden tanımlanmış düzenleri desteklemektedir. Bu özelliği sağlamak için Aspose.Cells API'leri PivotTable sınıfı için aşağıdaki üç yöntemi sağlamıştır.

- PivotTable.showInCompactForm yöntemi, Pivot Tablosunu Kompakt düzeninde renderlar.
- PivotTable.showInOutlineForm yöntemi, Pivot Tablosunu Anahat düzeninde renderlar.
- PivotTable.showInTabularForm yöntemi, Pivot Tablosunu Tablo düzeninde renderlar.

{{% alert color="primary" %}} 

Yukarıdaki düzenlerden herhangi birini ayarladıktan sonra PivotTable.refreshData ve PivotTable.calculateData metodlarını çağırmak önemlidir. 

{{% /alert %}} 

Aşağıdaki örnek kod, bir Pivot Tablosu için farklı düzenler belirler ve sonucu diske kaydeder.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//1 - Show the pivot table in compact form

pivotTable.showInCompactForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("CompactForm.xlsx");

//2 - Show the pivot table in outline form

pivotTable.showInOutlineForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("OutlineForm.xlsx");

//3 - Show the pivot table in tabular form

pivotTable.showInTabularForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("TabularForm.xlsx");

{{< /highlight >}}
### **Class TxtLoadStyleStrategy & Property TxtLoadOptions.LoadStyleStrategy Eklendi**
Aspose.Cells for Java 8.4.0, dize değerini sayıya veya tarih saatine dönüştürürken ayrıntılı değerleri biçimlendirmek için TxtLoadStyleStrategy sınıfını ve TxtLoadOptions.LoadStyleStrategy özelliğini sağlamıştır.
### **DataBar.ToImage Metodu Eklendi**
V8.4.0'ın yayınlanmasıyla, Aspose.Cells API'si, koşullu olarak biçimlendirilmiş DataBar'ı resim formatında kaydetmek için DataBar.toImage yöntemini sağlamıştır. {DataBar.toImage}} yöntemi aşağıdaki şekilde iki parametreyi kabul eder.

- İlk parametre, üzerinde koşullu biçimlendirme uygulanan com.aspose.cells.Cell türünden bir hücredir.
- İkinci parametre, sonuç resminin farklı parametrelerini ayarlamak için com.aspose.cells.rendering.ImageOrPrintOptions türündendir.

Aşağıdaki örnek kod, DataBar.toImage yönteminin kullanımını resim formatında DataBar'ı renderlamak için gösterir.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.getCells().get("C1");

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.getFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc.get(0).getDataBar();

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setImageFormat(ImageFormat.getPng());

//Get the image bytes of the databar

byte[] imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **Border.ThemeColor Özelliği Eklendi**
Aspose.Cells API'leri, elektronik tablolardan temaya ilişkin verilerin çıkarılmasına olanak tanır. Aspose.Cells for Java 8.4.0'ın yayınlanmasıyla, API, Hücre sınırlarının tema rengi özniteliğini almak için Border.ThemeColor özelliğini sağlamıştır.
### **DrawObject.ImageBytes Özelliği Eklendi**
Aspose.Cells for Java 8.4.0, Grafik veya Şekilden resim verilerini almak için DrawObject.ImageBytes özelliğini sağlamıştır.
### **HtmlSaveOptions.ExportBogusRowData Özelliği Eklendi**
Aspose.Cells for Java 8.4.0, {HtmlSaveOptions.ExportBogusRowData}} özelliğini sağlamıştır. Boolean türünde bir özellik olan bu property, elektronik tabloyu HTML formatına dönüştürürken sahte alt satır verileri ekleyip eklemeyeceğini belirler. 

{{% alert color="primary" %}} 

Varsayılan değer true'dur.

{{% /alert %}} 

Aşağıdaki örnek kod, yukarıdaki özellik kullanımını göstermektedir.

**Java**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **HtmlSaveOptions.CellCssPrefix Özelliği Eklendi**
Yeni eklenen HtmlSaveOptions.CellCssPrefix özelliği, elektronik tabloları HTML formatına dönüştürürken CSS dosyaları için önek belirlemeye olanak tanır.

{{% alert color="primary" %}} 

Varsayılan değer "" (boş dize) dir.

{{% /alert %}}
## **Eski API'ler**
### **Obsoleted Cells.getCellByIndex & Row.getCellByIndex Yöntemleri**
Tüm hücreleri yinelemek için getEnumerator yöntemini kullanın.
### **Eski DrawObject.Image Özelliği**
Resim verilerini almak için DrawObject.ImageBytes özelliğini kullanın.

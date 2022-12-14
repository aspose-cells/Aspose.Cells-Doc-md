---
title: Genel API Aspose.Cells 8.4.0'daki değişiklikler
type: docs
weight: 140
url: /tr/java/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürüm 8.3.2'den 8.4.0'a modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/java/public-api-changes-in-aspose-cells-8-4-0/) ve[kaldırılan sınıflar vb.](/cells/tr/java/public-api-changes-in-aspose-cells-8-4-0/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **Elektronik Tablolardaki VBA/Makro Kodunu Değiştirme Mekanizması**
 özelliğini sağlamak için[VBA/Makro Kod Manipülasyonu](/cells/tr/java/modifying-vba-or-macro-code-using-aspose-cells/)Aspose.Cells for Java 8.4.0, com.aspose.cells.Vba paketinde bir dizi yeni sınıf ve özellik ortaya çıkardı. Bu yeni sınıfların önemli detaylarından birkaçı aşağıdaki gibidir.

- VbaProject sınıfı, belirli bir elektronik tablodan VBA projesini getirmek için kullanılabilir.
- VbaModuleCollection sınıfı, belirli bir VbaProject'in parçası olan VBA modüllerinin koleksiyonunu temsil eder.
- VbaModule sınıfı, VbaModuleCollection'dan tek bir modülü temsil eder.

Aşağıdaki kod parçacığı, VBA kod bölümlerinin dinamik olarak nasıl değiştirileceğini gösterir.

**Java**

{{< highlight "csharp" >}}

 Çalışma kitabı çalışma kitabı = yeni Çalışma Kitabı("source.xlsm");

//VBA Modül Kodunu Değiştirin

VbaModuleCollection modülleri = workbook.getVbaProject().getModules();

 for(int i=0; ben< modules.getCount(); i++)

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
### **Pivot Tabloyu Kaldırma Yeteneği**
Aspose.Cells for Java 8.4.0, PivotTableCollection'ın belirli bir e-tablodan Pivot Tablo kaldırma özelliği sağlaması için iki yöntem ortaya çıkardı. Bahsi geçen yöntemlerin detayları aşağıdaki gibidir.

- PivotTableCollection.remove yöntemi, PivotTable'ın bir nesnesini kabul eder ve onu koleksiyondan kaldırır.
- PivotTableCollection.removeAt yöntemi, sıfır dizin tabanlı bir tamsayı değeri kabul eder ve belirli PivotTable'ı koleksiyondan kaldırır.

Aşağıdaki kod parçacığı, PivotTable'ın yukarıda belirtilen her iki yöntemi de kullanarak nasıl kaldırılacağını gösterir.

**Java**

{{< highlight "csharp" >}}

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
### **Farklı Pivot Tablo Düzenleri için Destek**
Aspose.Cells for Java 8.4.0, Pivot Tablolar için önceden tanımlanmış farklı düzenler için destek sağlar. Bu özelliği sağlamak için Aspose.Cells API'leri, PivotTable sınıfı için aşağıda ayrıntılı olarak açıklanan üç yöntemi kullanıma sunmuştur.

- PivotTable.showInCompactForm yöntemi, Pivot Tabloyu Kompakt mizanpajda işler.
- PivotTable.showInOutlineForm yöntemi, Pivot Tabloyu Anahat düzeninde işler.
- PivotTable.showInTabularForm yöntemi, Pivot Tabloyu Tablo düzeninde işler.

{{% alert color="primary" %}} 

 Yukarıda belirtilen düzenlerden herhangi birini ayarladıktan sonra PivotTable.refreshData & PivotTable.calculateData'yı çağırmak önemlidir.

{{% /alert %}} 

Aşağıdaki örnek kod, Pivot Tablo için farklı düzenler ayarlar ve sonucu diskte depolar.

**Java**

{{< highlight "csharp" >}}

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
### **Sınıf TxtLoadStyleStrategy ve Özellik TxtLoadOptions.LoadStyleStrategy Eklendi**
Aspose.Cells for Java 8.4.0, dize değerini sayıya veya tarih saatine dönüştürürken ayrıştırılan değerleri biçimlendirme stratejisini belirtmek için TxtLoadStyleStrategy sınıfını ve TxtLoadOptions.LoadStyleStrategy özelliğini kullanıma sundu.
### **Yöntem DataBar.ToImage Eklendi**
v8.4.0'ın piyasaya sürülmesiyle, Aspose.Cells API, koşullu olarak biçimlendirilmiş DataBar'ı görüntü biçiminde kaydetmek için DataBar.toImage yöntemini sağladı. {DataBar.toImage}} yöntemi, aşağıda ayrıntıları verilen iki parametreyi kabul eder.

- İlk parametre, koşullu biçimlendirmenin uygulandığı com.aspose.cells.Cell türündedir.
- Elde edilen görüntünün farklı parametrelerini ayarlamak için ikinci parametre com.aspose.cells.rendering.ImageOrPrintOptions türündedir.

Aşağıdaki örnek kod, DataBar'ı görüntü biçiminde işlemek için DataBar.toImage yönteminin kullanımını gösterir.

**Java**

{{< highlight "csharp" >}}

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

byte[]imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **Özellik Border.ThemeColor Eklendi**
Aspose.Cells API'ler, elektronik tablolardan temayla ilgili verilerin çıkarılmasına izin verir. Aspose.Cells for Java 8.4.0 sürümüyle birlikte API, Cell kenarlıklarının tema rengi özniteliklerini almak için kullanılabilecek Border.ThemeColor özelliğini kullanıma sundu.
### **Özellik DrawObject.ImageBytes Eklendi**
Aspose.Cells for Java 8.4.0, Grafik veya Şekil'den resim verilerini almak için DrawObject.ImageBytes özelliğini kullanıma sundu.
### **Özellik HtmlSaveOptions.ExportBogusRowData Eklendi**
 Aspose.Cells for Java 8.4.0, {HtmlSaveOptions.ExportBogusRowData}} özelliğini sağladı. Boole tipi özelliği, e-tabloyu HTML biçimine dışa aktarırken API'in sahte alt satır verileri enjekte edip etmeyeceğini belirler.

{{% alert color="primary" %}} 

Varsayılan değer doğrudur.

{{% /alert %}} 

Aşağıdaki örnek kod, yukarıda bahsedilen özelliğin kullanımını göstermektedir.

**Java**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Özellik HtmlSaveOptions.CellCssPrefix Eklendi**
Yeni eklenen özellik HtmlSaveOptions.CellCssPrefix, elektronik tabloları HTML biçimine dışa aktarırken CSS dosyaları için önek ayarlamanıza olanak tanır.

{{% alert color="primary" %}} 

Varsayılan değer boş bir dizedir).

{{% /alert %}}
## **Eski API'ler**
### **Yöntemler Cells.getCellByIndex & Row.getCellByIndex Kullanımdan Kaldırıldı**
Bunun yerine tüm hücreleri yinelemek için getEnumerator yöntemini kullanın.
### **DrawObject.Image Özelliği Kullanımdan Kaldırıldı**
Bunun yerine resim verilerini almak için DrawObject.ImageBytes özelliğini kullanın.

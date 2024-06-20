---
title: Aspose.Cells 8.6.3 te Kamu API Değişiklikleri
type: docs
weight: 220
url: /tr/net/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sinde 8.6.2'den 8.6.3'e yapılan değişiklikleri modül/uygulama geliştiricileri için ilginç olabilecek değişiklikleri açıklar. Yeni ve güncellenmiş kamu metodları, eklenen sınıfların yanı sıra Aspose.Cells'in arka planda olan herhangi bir değişikliği de içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Veri İçeri Aktarılırken HTML Ayrışma Desteği**
Aspose.Cells for .NET API'nin bu sürümü, ImportTableOptions.IsHtmlString özelliğini açığa çıkardı. Bu özellik, API'nin Veri Tablo üzerine veri aktarırken HTML etiketlerini ayrıştırmak ve ayrıştırılmış sonucu hücre değeri olarak ayarlamak için yönlendirmektedir. Lütfen dikkat edin, Aspose.Cells API'lerinin zaten tek bir hücre için bu görevi gerçekleştirmek için Cell.HtmlString'i sağladığını, ancak DataTable gibi toplu veri aktarılırken, ImportTableOptions.IsHtmlString özelliğinin (true olarak ayarlandığında) tüm desteklenen HTML etiketlerini ayrıştırmaya çalıştığını ve ayrıştırılmış sonuçları karşılık gelen hücrelere ayarladığını belirtmek gerekir.

İşte en basit kullanım senaryosu.

**C#**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Workbook.CreateBuiltinStyle Yöntemi Eklendi**
Aspose.Cells for .NET 8.6.3, Excel uygulaması tarafından sunulan [yerleşik stiller kullanılarak](/cells/tr/net/built-in-styles-kullanimi/) Style sınıfına karşılık gelen bir nesne oluşturmak için kullanılabilecek Workbook.CreateBuiltinStyle yöntemini açığa çıkardı. Workbook.CreateBuiltinStyle yöntemi, BuiltinStyleType numaralandırmasından sabit bir değer kabul etmektedir. Lütfen dikkat edin, önceki Aspose.Cells API sürümleriyle aynı görev, StyleCollection.CreateBuiltinStyle yöntemi aracılığıyla gerçekleştirilebiliyordu ancak Aspose.Cells API'lerinin son sürümleri, StyleCollection sınıfını kaldırdığından dolayı, yeni başlatılan Workbook.CreateBuiltinStyle yöntemi, aynı işi gerçekleştirmenin alternatif bir yaklaşımı olarak düşünülebilir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Cells.ImportGridView Yöntemi Eklendi**
Aspose.Cells for .NET 8.6.3, ImportTableOptions örneğini kabul edebilecek şekilde yeniden yüklenmiş bir Cells.ImportGridView versiyonunu açığa çıkardı ve veri aktarım süreci üzerinde daha fazla kontrol sağlamaktadır.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions & set its various properties

var importOptions = new ImportTableOptions();

importOptions.IsHtmlString = true;

importOptions.IsFieldNameShown = true;

//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **ImportTableOptions.ConvertGridStyle Özelliği Eklendi**
Yukarıdaki geliştirmelerle ilgili olarak, Aspose.Cells for .NET API'nin en son sürümü ayrıca ImportTableOptions.ConvertGridStyle özelliğini açığa çıkardı. Bu Boolean tip özellik, geliştiricilere, içeri aktarılan verinin görünümünü kontrol etme imkanı verir. ImportTableOptions.ConvertGridStyle özelliğini true olarak ayarlamak, API'nin, veri içeri aktarılan hücrelere GridView'in stilini uygulayacağı anlamına gelir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set ConvertGridStyle property to true

importOptions.ConvertGridStyle = true;



//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **LoadDataOption.OnlyVisibleWorksheet Özelliği Eklendi**
Aspose.Cells for .NET 8.6.3, LoadDataOption.OnlyVisibleWorksheet özelliğini açığa çıkardı. Bu özellik true olarak ayarlandığında, API'nin yükleme mekanizmasını etkileyerek, verilen bir elektronik tablodan yalnızca görünür çalışma sayfaları yüklenecektir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of LoadDataOption

var loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.OnlyVisibleWorksheet = true;

//Create an instance of LoadOptions

var loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.LoadDataOptions = loadDataOptions;



//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

var book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **Eskimiş API'lar**
### **Worksheet.CopyConditionalFormatting Yöntemi Eskiler**
Worksheet.CopyConditionalFormatting yönteminin yerine, Cells.CopyRows veya Range.Copy yöntemlerinden herhangi birini kullanmanız önerilir.
### **Eskiye Çıkarılan Cells.End Özelliği**
Cells.End özelliğinin yerine lütfen Cells.LastCell özelliğini kullanın.

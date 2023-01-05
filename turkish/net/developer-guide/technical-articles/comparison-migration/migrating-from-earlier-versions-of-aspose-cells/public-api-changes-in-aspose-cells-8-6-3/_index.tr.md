---
title: Genel API Aspose.Cells'deki değişiklikler 8.6.3
type: docs
weight: 220
url: /tr/net/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.6.2'den 8.6.3'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen sınıfları değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Verileri İçe Aktarırken HTML Ayrıştırma Desteği**
Aspose.Cells for .NET API'in bu sürümü, API'i Çalışma Sayfasına veri aktarırken HTML etiketlerini ayrıştırmaya ve ayrıştırılan sonucu hücre değeri olarak ayarlamaya yönlendiren ImportTableOptions.IsHtmlString özelliğini ortaya çıkardı. Lütfen Aspose.Cells API'lerinin bu görevi tek bir hücre için gerçekleştirmek üzere Cell.HtmlString'i zaten sağladığını unutmayın, ancak verileri bir DataTable'dan toplu olarak içe aktarırken, ImportTableOptions.IsHtmlString özelliği (true olarak ayarlandığında) desteklenen tüm verileri ayrıştırmaya çalışır. HTML, ayrıştırılan sonuçları ilgili hücrelere etiketler ve ayarlar.

İşte en basit kullanım senaryosu.

**C#**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Yöntem Workbook.CreateBuiltinStyle Eklendi**
 Aspose.Cells for .NET 8.6.3, Workbook.CreateBuiltinStyle öğelerinden birine karşılık gelen Style sınıfından bir nesne oluşturmak için kullanılabilecek yöntemi ortaya çıkardı.[Excel uygulaması tarafından sunulan yerleşik stiller](/cells/tr/net/using-built-in-styles/)Workbook.CreateBuiltinStyle yöntemi, DahiliStyleType numaralandırmasından bir sabit kabul eder. Aspose.Cells API'lerinin önceki sürümleriyle aynı görevin StyleCollection.CreateBuiltinStyle yöntemiyle gerçekleştirilebileceğini ancak Aspose.Cells API'lerinin son sürümleri StyleCollection sınıfını kaldırdığından, yeni kullanıma sunulan Workbook.CreateBuiltinStyle yönteminin alternatif bir yaklaşım olarak değerlendirilebileceğini unutmayın. aynısını elde etmek.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Yöntem Cells.ImportGridView Eklendi**
Aspose.Cells for .NET 8.6.3, Cells.ImportGridView'ün artık içe aktarma işlemi üzerinde daha fazla kontrol sağlamak için bir ImportTableOptions örneğini kabul edebilen aşırı yüklenmiş bir sürümünü kullanıma sundu.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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


### **Özellik ImportTableOptions.ConvertGridStyle Eklendi**
Yukarıda belirtilen geliştirmelere referans olarak, Aspose.Cells for .NET API'in en son sürümü de ImportTableOptions.ConvertGridStyle özelliğini kullanıma sunmuştur. Bu Boole türü özelliği, geliştiricilerin içe aktarılan verilerin görünümünü kontrol etmelerine olanak tanır; burada ImportTableOptions.ConvertGridStyle özelliğinin true olarak ayarlanması, API'in verilerin içe aktarıldığı hücrelere GridView stilini uygulayacağını belirtir.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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


### **Özellik LoadDataOption.OnlyVisibleWorksheet Eklendi**
 Aspose.Cells for .NET 8.6.3, true olarak ayarlandığında Aspose.Cells for .NET API'in yükleme mekanizmasını etkileyecek olan LoadDataOption.OnlyVisibleWorksheet özelliğini ortaya çıkardı, sonuç olarak belirli bir elektronik tablodan yalnızca görünür çalışma sayfaları yüklenecek. lütfen kontrol ediniz[ayrıntılı makale](/cells/tr/net/different-ways-to-open-files/) bu konuda.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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
## **Eski API'ler**
### **Yöntem Worksheet.CopyConditionalFormatting Kullanılmayan**
Worksheet.CopyConditionalFormatting yöntemine alternatif olarak Cells.CopyRows veya Range.Copy yöntemlerinden herhangi birinin kullanılması önerilir.
### **Özellik Cells.End Eskidi**
Lütfen Cells.End özelliğine alternatif olarak Cells.LastCell özelliğini kullanın.

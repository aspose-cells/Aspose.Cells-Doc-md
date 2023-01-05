---
title: Genel API Aspose.Cells'deki değişiklikler 8.6.3
type: docs
weight: 230
url: /tr/java/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.6.2'den 8.6.3'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen sınıfları değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Verileri İçe Aktarırken HTML Ayrıştırma Desteği**
Aspose.Cells for Java API'in bu sürümü, API'i Çalışma Sayfasına veri aktarırken HTML etiketlerini ayrıştırmaya ve ayrıştırılan sonucu hücre değeri olarak ayarlamaya yönlendiren ImportTableOptions.setHtmlString özniteliğini ortaya çıkardı. Lütfen unutmayın, Aspose.Cells API'leri, bu görevi tek bir hücre için gerçekleştirmek üzere Cell.setHtmlString özniteliğini zaten sağlar, ancak verileri toplu olarak içe aktarırken, ImportTableOptions.setHtmlString özniteliği (true olarak ayarlandığında) desteklenen tüm HTML etiketlerini ve kümelerini ayrıştırmaya çalışır. ayrıştırılan sonuçlar karşılık gelen hücrelere gönderilir.

İşte en basit kullanım senaryosu.

**Java**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Yöntem Workbook.createBuiltinStyle Eklendi**
 Aspose.Cells for Java 8.6.3, Workbook.createBuiltinStyle öğelerinden birine karşılık gelen Style sınıfından bir nesne oluşturmak için kullanılabilecek yöntemi ortaya çıkardı.[Excel uygulaması tarafından sunulan yerleşik stiller](/cells/tr/java/using-built-in-styles/)Workbook.createBuiltinStyle yöntemi, DahiliStyleType numaralandırmasından bir sabit kabul eder. Lütfen unutmayın, Aspose.Cells API'lerinin önceki sürümleriyle aynı görev StyleCollection.createBuiltinStyle yöntemiyle gerçekleştirilebilirdi ancak Aspose.Cells API'lerinin son sürümleri StyleCollection sınıfını kaldırdığından, yeni kullanıma sunulan Workbook.createBuiltinStyle yöntemi alternatif bir yaklaşım olarak kabul edilebilir. aynısını elde etmek.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Özellik LoadDataOption.OnlyVisibleWorksheet Eklendi**
Aspose.Cells for Java 8.6.3, true olarak ayarlandığında Aspose.Cells for Java API'in yükleme mekanizmasını etkileyecek olan LoadDataOption.OnlyVisibleWorksheet özelliğini ortaya çıkardı, sonuç olarak belirli bir elektronik tablodan yalnızca görünür çalışma sayfaları yüklenecek.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadDataOption

LoadDataOption loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.setOnlyVisibleWorksheet(true);

//Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.setLoadDataOptions(loadDataOptions);

//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

Workbook book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **Eski API'ler**
### **Yöntem Worksheet.copyConditionalFormatting Kullanılmayan**
Worksheet.copyConditionalFormatting yöntemine alternatif olarak Cells.copyRows veya Range.copy yöntemlerinden herhangi birinin kullanılması önerilir.
### **Özellik Cells.End Eskidi**
Lütfen Cells.End özelliğine alternatif olarak Cells.LastCell özelliğini kullanın.

---
title: Aspose.Cells 8.6.3 te Kamu API Değişiklikleri
type: docs
weight: 230
url: /tr/java/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sinde 8.6.2'den 8.6.3'e yapılan değişiklikleri modül/uygulama geliştiricileri için ilginç olabilecek değişiklikleri açıklar. Yeni ve güncellenmiş kamu metodları, eklenen sınıfların yanı sıra Aspose.Cells'in arka planda olan herhangi bir değişikliği de içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Veri İçeri Aktarılırken HTML Ayrışma Desteği**
Bu sürümde, Aspose.Cells for Java API, ImportTableOptions.setHtmlString özelliğini ortaya çıkardı, bu özellik, API'nin HTML etiketlerini ayrıştırmasını sağlar ve ayrıştırılmış sonucu hücre değeri olarak ayarlar. Lütfen not edin, Aspose.Cells API'ları zaten tek bir hücre için bu görevi yerine getirmek için Cell.setHtmlString özelliğini sağlar, ancak toplu veri alırken ImportTableOptions.setHtmlString özelliği (true olarak ayarlandığında) tüm desteklenen HTML etiketlerini ayrıştırmaya çalışır ve ayrıştırılmış sonuçları ilgili hücrelere ayarlar.

İşte en basit kullanım senaryosu.

**Java**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Eklendi Workbook.createBuiltinStyle Yöntemi**
Aspose.Cells for Java 8.6.3, Excel uygulaması tarafından sağlanan [dahili stillerden birine karşılık gelen Stil sınıfının bir nesnesini oluşturmak için kullanılabilen Workbook.createBuiltinStyle yöntemini açığa çıkardı](/cells/tr/java/using-built-in-styles/). Workbook.createBuiltinStyle yöntemi, BuiltinStyleType numaralandırmasından sabit bir değer alır. Lütfen not edin, Aspose.Cells API'nın önceki sürümleriyle aynı görev, StyleCollection.createBuiltinStyle yöntemi aracılığıyla gerçekleştirilebiliyordu ancak Aspose.Cells API'lerinin son sürümleri StyleCollection sınıfını kaldırdığından, yeni açığa çıkarılan Workbook.createBuiltinStyle yöntemi aynı şeyi başarmak için alternatif bir yaklaşım olarak değerlendirilebilir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Eklendi LoadDataOption.OnlyVisibleWorksheet Özelliği**
Aspose.Cells for Java 8.6.3, LoadDataOption.OnlyVisibleWorksheet özelliğini açığa çıkardı. bu özelliğin true olarak ayarlanması, Aspose.Cells for Java API'nin yükleme mekanizmasını etkileyecek, sonuç olarak verilen bir elektronik tablodan yalnızca görünen çalışma sayfaları yüklenecektir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

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
## **Eskimiş API'lar**
### **Eskiye Çıkarılan Worksheet.copyConditionalFormatting Yöntemi**
Worksheet.copyConditionalFormatting yönteminin yerine, Cells.copyRows veya Range.copy yöntemlerinden herhangi birini kullanmanız tavsiye edilir.
### **Eskiye Çıkarılan Cells.End Özelliği**
Cells.End özelliğinin yerine lütfen Cells.LastCell özelliğini kullanın.
{{< app/cells/assistant language="java" >}}

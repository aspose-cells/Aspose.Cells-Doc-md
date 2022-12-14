---
title: Genel API Aspose.Cells 16.12.0'daki değişiklikler
type: docs
weight: 370
url: /tr/java/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 16.11.0 sürümünden 16.12.0 sürümüne Aspose.Cells API değişikliklerini açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Yükleme Süresinde Nesneleri Filtrele**
Aspose.Cells 16.12.0, bir şablon dosyasından bir Çalışma Kitabı örneğini başlatırken yüklenecek veri türünü birlikte kontrol edebilen LoadFilter sınıfını ve LoadOptions.LoadFilter özelliğini kullanıma sundu.

Bir şablon dosyasından yalnızca belge özelliklerini yüklemek için basit bir kullanım senaryosu.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.DOCUMENT_PROPERTIES);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

Aşağıdaki snippet, grafikler dışında mevcut bir e-tablodaki her şeyi yükler.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

Aşağıdaki kod, yalnızca hücre verilerini (formüllerle birlikte) ve mevcut bir elektronik tablodan biçimlendirmeyi yükler.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.CELL_DATA);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}
### **FileFormatType.OTS Numaralandırması Eklendi**
Aspose.Cells 16.12.0, OTS dosyalarının biçimini algılamak için FileFormatType numaralandırmasına OTS girişi ekledi.

Aşağıdaki kod parçası, FileFormatType.OTS'den yararlanır.

**Java**

{{< highlight "csharp" >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **BuiltInDocumentPropertyCollection.ScaleCrop Özelliği eklendi**
Aspose.Cells 16.12.0, ScaleCrop özelliğini BuiltInDocumentPropertyCollection sınıfına ekledi. ScaleCrop, belge küçük resminin görüntüleme modunu belirtir. Bu öğenin true olarak ayarlanması, belge küçük resminin ekrana göre ölçeklenmesini sağlarken, false olarak ayarlanması, ekrana uyan bölümü göstermek için belge küçük resminin kırpılmasını sağlar.
### **BuiltInDocumentPropertyCollection.LinksUpToDate Özelliği eklendi**
 Aspose.Cells 16.12.0 ayrıca, BuiltInDocumentPropertyCollection sınıfı için LinksUpToDate özelliğini kullanıma sunmuştur. LinksUpToDate özelliği, bir belgedeki köprülerin güncel olup olmadığını gösterir.
### **Workbook.exportXml Yöntemi Eklendi**
Aspose.Cells 16.12.0, XML eşleme verilerinin belirtilen dosya yolunda depolanmasına izin veren Workbook.exportXml yöntemini kullanıma sundu. Workbook.exportXml yöntemi 2 parametre kabul eder; burada string türündeki ilk parametre XML eşleme adı olmalıdır ve ikinci parametre, XML verilerini depolamak için dosya yolu konumu olmalıdır.
### **WorksheetCollection.createRange Yöntemi Eklendi**
Aspose.Cells 16.12.0, bir adrese (hücre alanı referansı) ve Çalışma Sayfası dizinine dayalı aralık oluşturmaya izin veren WorksheetCollection.createRange yöntemini ekledi.

Aşağıdaki kod parçacığı, ilk (varsayılan) çalışma sayfasında A1'den A2'ye kadar uzanan bir hücre aralığı oluşturmak için WorksheetCollection.createRange yöntemini kullanır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

{{< /highlight >}}
## **Eski API'ler**
### **Eski LoadOptions.LoadDataOptions Özelliği**
Lütfen alternatif olarak LoadOptions.LoadFilter özelliğini kullanın.
### **Eski LoadOptions.LoadDataFilterOptions Özelliği**
Lütfen bunun yerine LoadOptions.LoadFilter özelliğini kullanın.
### **Eski LoadOptions.OnlyLoadDocumentProperties Özelliği**
Lütfen alternatif olarak LoadOptions.LoadFilter özelliğini kullanın.
### **Eski LoadOptions.LoadDataAndFormatting Özellik**
Lütfen bunun yerine LoadOptions.LoadFilter özelliğini kullanın.

{{% alert color="primary" %}} 

Tüm eskimiş API'ler için kod parçacıkları yukarıda paylaşılmıştır.

{{% /alert %}}
## **Silinmiş API'ler**
### **Silinmiş DataLabels.Rotation Özelliği**
Lütfen bunun yerine DataLabels.RotationAngle özelliğini kullanın.
### **Title.Rotation Özelliği Silindi**
Lütfen alternatif olarak Title.RotationAngle özelliğini kullanın.
### **Silinmiş DataLabels.Background Özelliği**
Bunun yerine DataLabels.BackgroundMode özelliğinin kullanılması önerilir.
### **DisplayUnitLabel.Rotation Özelliği Silindi**
Lütfen aynı hedefe ulaşmak için DisplayUnitLabel.RotationAngle özelliğini kullanmayı düşünün.
### **Title.getCharacters Yöntemi Silindi**
Lütfen bunun yerine Title.characters yöntemini kullanın.

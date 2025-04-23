---
title: Aspose.Cells 16.12.0 daki Genel API Değişiklikleri
type: docs
weight: 370
url: /tr/java/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Bu belge, 16.11.0'dan 16.12.0'a Aspose.Cells API'sindeki değişiklikleri modül/uygulama geliştiricilerinin ilgisini çekebilecek değişiklikleri açıklar. Sadece yeni ve güncellenmiş genel yöntemleri, eklendikçe ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'in arka planda olan değişikliklerini de açıklar.

{{% /alert %}} 
## **Eklenen API'lar**
### **Yükleme Zamanında Filtre Nesneleri**
Aspose.Cells 16.12.0, bir şablon dosyasından bir Workbook örneğini başlatırken yüklenmesini kontrol edebilen LoadFilter sınıfını ve LoadOptions.LoadFilter özelliğini açığa çıkarmıştır.

Şablon dosyasından sadece belge özelliklerini yüklemek için basit bir kullanım senaryosu burada.

**Java**

{{< highlight csharp >}}

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

Aşağıdaki kesit, grafikler hariç mevcut bir elektronik tablodan her şeyi yükler.

**Java**

{{< highlight csharp >}}

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

Aşağıdaki kod, yalnızca mevcut bir elektronik tablodan hücre verilerini (formüllerle birlikte) ve biçimlendirmeyi yükler.

**Java**

{{< highlight csharp >}}

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
### **Eklendi FileFormatType.OTS Numaralandırması**
Aspose.Cells 16.12.0, OTS dosyalarının biçimini algılamak için FileFormatType numaralandırmasına OTS girişi eklemiştir.

Aşağıdaki kesit, FileFormatType.OTS'yi kullanır.

**Java**

{{< highlight csharp >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **Eklendi BuiltInDocumentPropertyCollection.ScaleCrop Özelliği**
Aspose.Cells 16.12.0, BuiltInDocumentPropertyCollection sınıfına ScaleCrop özelliğini eklemiştir. ScaleCrop, belge küçük resminin görüntü modunu gösterir. Bu öğeyi true olarak ayarlamak, belge küçük resminin görüntüye göre ölçeklenmesini sağlarken, false olarak ayarlamak, belge küçük resminin gösterilen bölümünü kırpılmasını sağlar.
### **Eklendi BuiltInDocumentPropertyCollection.LinksUpToDate Özelliği**
Aspose.Cells 16.12.0, BuiltInDocumentPropertyCollection sınıfı için LinksUpToDate özelliğini de açıklamıştır. LinksUpToDate özelliği, bir belgedeki bağlantıların güncel olup olmadığını gösterir. 
### **Eklendi Workbook.exportXml Yöntemi**
Aspose.Cells 16.12.0, XML harita verilerini belirtilen dosya yoluna depolamak için Workbook.exportXml yöntemini açığa çıkarmıştır. Workbook.exportXml yöntemi, string türünde ilk parametre olarak XML harita adı ve ikinci parametre olarak depolanacak XML verilerinin dosya yolu konumunu kabul eder.
### **Eklendi WorksheetCollection.createRange Yöntemi**
Aspose.Cells 16.12.0, bir adres (hücre alanı referansı) ve Worksheet dizini üzerinde aralık oluşturmak için WorksheetCollection.createRange yöntemini eklemiştir.

Aşağıdaki kesit, WorksheetCollection.createRange yöntemini kullanarak varsayılan olarak ilk çalışma sayfasında A1'den A2'ye uzanan bir hücre aralığı oluşturur.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

{{< /highlight >}}
## **Eskimiş API'lar**
### **Yönetimsiz LoadOptions.LoadDataOptions Özelliği**
Lütfen alternatif olarak LoadOptions.LoadFilter özelliğini kullanın.
### **Yönetimsiz LoadOptions.LoadDataFilterOptions Özelliği**
Lütfen alternatif olarak LoadOptions.LoadFilter özelliğini kullanın.
### **Yönetimsiz LoadOptions.OnlyLoadDocumentProperties Özelliği**
Lütfen alternatif olarak LoadOptions.LoadFilter özelliğini kullanın.
### **Yönetimsiz LoadOptions.LoadDataAndFormatting Özelliği**
Lütfen alternatif olarak LoadOptions.LoadFilter özelliğini kullanın.

{{% alert color="primary" %}} 

Tüm yönetimsiz API'ler için kod parçacıkları yukarıda paylaşılmıştır.

{{% /alert %}}
## **Silinmiş API'lar**
### **Silinmiş DataLabels.Rotation Özelliği**
Lütfen alternatif olarak DataLabels.RotationAngle özelliğini kullanın.
### **Silinmiş Title.Rotation Özelliği**
Lütfen alternatif olarak Title.RotationAngle özelliğini kullanın.
### **Silinmiş DataLabels.Background Özelliği**
Bunun yerine DataLabels.BackgroundMode özelliğini kullanmanız önerilir.
### **Silinmiş DisplayUnitLabel.Rotation Özelliği**
Aynı hedefe ulaşmak için lütfen DisplayUnitLabel.RotationAngle özelliğini kullanmayı düşünün.
### **Silinmiş Title.getCharacters Yöntemi**
Lütfen Title.characters yöntemini kullanın.
{{< app/cells/assistant language="java" >}}

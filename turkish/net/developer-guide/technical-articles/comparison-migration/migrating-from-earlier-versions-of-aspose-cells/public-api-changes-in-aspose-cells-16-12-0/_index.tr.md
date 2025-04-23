---
title: Aspose.Cells 16.12.0 daki Genel API Değişiklikleri
type: docs
weight: 360
url: /tr/net/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Bu belge, 16.11.0'dan 16.12.0'a Aspose.Cells API'sindeki değişiklikleri modül/uygulama geliştiricilerinin ilgisini çekebilecek değişiklikleri açıklar. Sadece yeni ve güncellenmiş genel yöntemleri, eklendikçe ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'in arka planda olan değişikliklerini de açıklar.

{{% /alert %}} 
## **Eklenen API'lar**
### **Yükleme Zamanında Filtre Nesneleri**
Aspose.Cells 16.12.0, bir şablon dosyasından bir Workbook örneğini başlatırken yüklenmesini kontrol edebilen LoadFilter sınıfını ve LoadOptions.LoadFilter özelliğini açığa çıkarmıştır.

Şablon dosyasından sadece belge özelliklerini yüklemek için basit bir kullanım senaryosu burada.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Aşağıdaki kesit, grafikler hariç mevcut bir elektronik tablodan her şeyi yükler.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Aşağıdaki kod, yalnızca mevcut bir elektronik tablodan hücre verilerini (formüllerle birlikte) ve biçimlendirmeyi yükler.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



YükFilter sınıfı aynı zamanda Yapısayfaların özelliklerine göre yükleme sürecini özelleştirmenize olanak tanır. Yükleme sürecini yapıl sayfa olarak özelleştirmek için, aşağıda gösterildiği gibi LoadFilter.StartSheet yöntemini geçersiz kılmak gerekir.

**C#**

{{< highlight csharp >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}



Yukarıda tanımlanan CustomFilter sınıfının kullanımı aşağıdaki örnekte gösterilmiştir.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **Eklendi FileFormatType.OTS Numaralandırması**
Aspose.Cells 16.12.0, OTS dosyalarının biçimini algılamak için FileFormatType numaralandırmasına OTS girişi eklemiştir.

Aşağıdaki kesit, FileFormatType.OTS'yi kullanır.

**C#**

{{< highlight csharp >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **EKLENEN FontConfigs.PreferSystemFontSubstitutes Özelliği**
Aspose.Cells 16.12.0, FontConfigs sınıfı için PreferSystemFontSubstitutes özelliğini ortaya çıkarmıştır. FontConfigs.PreferSystemFontSubstitutes özelliği, belirli bir yazı tipinin belirtilmiş bir biçimlendirme olmaksızın mevcut olmaması durumunda, API'nin ilk olarak sistem yazı tipi değişim mekanizmasını kullanıp kullanmayacağını gösteren Boolean türündedir. FontConfigs.PreferSystemFontSubstitutes özelliğinin varsayılan değeri false'tur.
### **Eklendi BuiltInDocumentPropertyCollection.ScaleCrop Özelliği**
Aspose.Cells 16.12.0, BuiltInDocumentPropertyCollection sınıfına ScaleCrop özelliğini eklemiştir. ScaleCrop, belge küçük resminin görüntü modunu gösterir. Bu öğeyi true olarak ayarlamak, belge küçük resminin görüntüye göre ölçeklenmesini sağlarken, false olarak ayarlamak, belge küçük resminin gösterilen bölümünü kırpılmasını sağlar.
### **Eklendi BuiltInDocumentPropertyCollection.LinksUpToDate Özelliği**
Aspose.Cells 16.12.0, BuiltInDocumentPropertyCollection sınıfı için LinksUpToDate özelliğini de açıklamıştır. LinksUpToDate özelliği, bir belgedeki bağlantıların güncel olup olmadığını gösterir.
### **EKLENEN Workbook.ExportXml Yöntemi**
Aspose.Cells 16.12.0, XML haritası verilerini belirtilen dosya yoluna saklamayı sağlayan Workbook.ExportXml yöntemini ortaya çıkarmıştır. Workbook.ExportXml yöntemi, ilk parametresi string türünde olan XML haritası adını ve ikinci parametresi saklanacak XML verilerinin dosya yolunu belirtmelidir.
### **EKLENEN WorksheetCollection.CreateRange Yöntemi**
Aspose.Cells 16.12.0, WorksheetCollection.CreateRange yöntemini, bir adres (hücre alanı referansı) ve Çalışsayfa dizine dayalı olarak bir aralık oluşturmanıza olanak tanır.

Aşağıdaki kesitte, ilk (varsayılan) çalışsayfa içinde A1'den A2'ye uzanan hücrelerin bir aralığını oluşturmak için WorksheetCollection.CreateRange yöntemi kullanılmaktadır.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

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
{{< app/cells/assistant language="csharp" >}}

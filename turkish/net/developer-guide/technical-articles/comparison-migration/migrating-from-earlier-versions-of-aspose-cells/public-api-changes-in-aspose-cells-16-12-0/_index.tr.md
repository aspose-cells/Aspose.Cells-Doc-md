---
title: Genel API Aspose.Cells 16.12.0'daki değişiklikler
type: docs
weight: 360
url: /tr/net/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 16.11.0 sürümünden 16.12.0 sürümüne Aspose.Cells API değişikliklerini açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Yükleme Süresinde Nesneleri Filtrele**
Aspose.Cells 16.12.0, bir şablon dosyasından bir Çalışma Kitabı örneğini başlatırken yüklenecek veri türünü birlikte kontrol edebilen LoadFilter sınıfını ve LoadOptions.LoadFilter özelliğini kullanıma sundu.

Bir şablon dosyasından yalnızca belge özelliklerini yüklemek için basit bir kullanım senaryosu.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Aşağıdaki snippet, grafikler dışında mevcut bir e-tablodaki her şeyi yükler.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Aşağıdaki kod, yalnızca hücre verilerini (formüllerle birlikte) ve mevcut bir elektronik tablodan biçimlendirmeyi yükler.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



LoadFilter sınıfı, yükleme işleminin Çalışma Sayfasının özelliklerine göre özelleştirilmesine de izin verir. Yükleme işlemini çalışma sayfasına göre özelleştirmek için, aşağıda gösterildiği gibi LoadFilter.StartSheet yöntemini geçersiz kılmak gerekir.

**C#**

{{< highlight "csharp" >}}

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



Aşağıdaki kod parçacığı, yukarıda tanımlanan CustomFilter sınıfını kullanır.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **FileFormatType.OTS Numaralandırması Eklendi**
Aspose.Cells 16.12.0, OTS dosyalarının biçimini algılamak için FileFormatType numaralandırmasına OTS girişi ekledi.

Aşağıdaki kod parçası, FileFormatType.OTS'den yararlanır.

**C#**

{{< highlight "csharp" >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **FontConfigs.PreferSystemFontSubstitutes Özelliği Eklendi**
Aspose.Cells 16.12.0, FontConfigs sınıfı için PreferSystemFontSubstitutes özelliğini kullanıma sundu. FontConfigs.PreferSystemFontSubstitutes özelliği Boolean türündedir ve gerekli bir yazı tipinin olmaması ve belirli bir yazı tipi için herhangi bir ikamenin tanımlanmaması durumunda API'in önce sistemin yazı tipi değiştirme mekanizmasını kullanıp kullanmayacağını belirtir. FontConfigs.PreferSystemFontSubstitutes özelliğinin varsayılan değeri yanlıştır.
### **BuiltInDocumentPropertyCollection.ScaleCrop Özelliği eklendi**
Aspose.Cells 16.12.0, ScaleCrop özelliğini BuiltInDocumentPropertyCollection sınıfına ekledi. ScaleCrop, belge küçük resminin görüntüleme modunu belirtir. Bu öğenin true olarak ayarlanması, belge küçük resminin ekrana göre ölçeklenmesini sağlarken, false olarak ayarlanması, ekrana uyan bölümü göstermek için belge küçük resminin kırpılmasını sağlar.
### **BuiltInDocumentPropertyCollection.LinksUpToDate Özelliği eklendi**
Aspose.Cells 16.12.0 ayrıca, BuiltInDocumentPropertyCollection sınıfı için LinksUpToDate özelliğini kullanıma sunmuştur. LinksUpToDate özelliği, bir belgedeki köprülerin güncel olup olmadığını gösterir.
### **Workbook.ExportXml Yöntemi Eklendi**
Aspose.Cells 16.12.0, XML eşleme verilerini belirtilen dosya yolunda depolamaya izin veren Workbook.ExportXml yöntemini kullanıma sundu. Workbook.ExportXml yöntemi 2 parametre kabul eder; burada string türündeki ilk parametre XML eşleme adı olmalıdır ve ikinci parametre, XML verilerini depolamak için dosya yolu konumu olmalıdır.
### **WorksheetCollection.CreateRange Yöntemi Eklendi**
Aspose.Cells 16.12.0, bir adrese (hücre alanı referansı) ve Çalışma Sayfası dizinine dayalı aralık oluşturmaya izin veren WorksheetCollection.CreateRange yöntemini ekledi.

Aşağıdaki kod parçacığı, ilk (varsayılan) çalışma sayfasında A1'den A2'ye kadar uzanan bir hücre aralığı oluşturmak için WorksheetCollection.CreateRange yöntemini kullanır.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

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

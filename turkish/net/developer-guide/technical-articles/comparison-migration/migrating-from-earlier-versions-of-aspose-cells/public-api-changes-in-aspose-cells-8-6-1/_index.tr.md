---
title: Genel API Aspose.Cells 8.6.1'deki değişiklikler
type: docs
weight: 200
url: /tr/net/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.6.0'dan 8.6.1'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen sınıfları değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **HTML Bağlantı Hedefi Türü Desteği**
 Aspose.Cells for .NET API'in bu sürümü, birlikte izin veren yeni bir özellik olan HtmlSaveOptions.LinkTargetType ile birlikte HtmlLinkTargetType adında bir numaralandırma ortaya çıkardı.[HTML formatına dönüştürürken e-tablodaki bağlantılar için hedef tipini ayarlayın](/cells/tr/net/change-the-html-link-target-type/). Varsayılan değerin Self olduğu HtmlLinkTargetType numaralandırmasının olası değerleri aşağıdaki gibidir.

1. HtmlLinkTargetType.Blank: Bağlantılı belgeyi/sayfayı yeni bir pencerede veya sekmede açar.
1. HtmlLinkTargetType.Parent: Bağlı belgeyi/sayfayı ana çerçevede açar.
1. HtmlLinkTargetType.Self: Bağlantı verilen belgeyi/sayfayı, bağlantının tıklandığı çerçevede açar.
1. HtmlLinkTargetType.Top: Bağlantılı belgeyi/sayfayı pencerenin tüm gövdesinde açar.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **Yöntem VbaModuleCollection.Remove Eklendi**
Aspose.Cells for .NET 8.6.1, belirtilen Çalışma Sayfası ile ilişkili tüm VBA modüllerini kaldırmak için artık bir Çalışma Sayfası örneğini kabul edebilen VbaModuleCollection.Remove yönteminin başka bir aşırı yüklemesini ortaya çıkardı.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **Yöntem RangeCollection.Add Eklendi**
Aspose.Cells for .NET 8.6.1, belirli bir Çalışma Sayfası için aralık koleksiyonuna Range nesneleri eklemek için kullanılabilecek RangeCollection.Add yöntemini kullanıma sundu.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **Yöntem Cell.SetCharacters Eklendi**
 Cell.SetCharacters yöntemi şu amaçlarla kullanılabilir:[zengin metnin bölümlerini güncelleme](/cells/tr/net/access-and-update-the-portions-of-rich-text-of-cell/) belirli bir Cell nesnesinin. Cell.GetCharacters yöntemi ile metnin bölümlerine ulaşmak için kullanılır ve daha sonra Cell.SetCharacters yöntemi kullanılarak düzeltmeler yapılabilir.**Elde etmek** yöntemi, yazı tipi adı, yazı tipi rengi, kalınlık vb. çeşitli özellikleri ayarlamak için kullanılabilecek bir FontSetting nesneleri dizisi döndürür ve**Ayarlamak** Yöntem, değişiklikleri uygulamak için kullanılabilir.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **Özellik VbaProject.IsSigned Eklendi**
 Aspose.Cells for .NET 8.6.1, kullanılabilecek VbaProject.IsSigned özelliğini kullanıma sundu.[Çalışma Kitabındaki bir VbaProject'in imzalanıp imzalanmadığını test edin](/cells/tr/net/check-if-vba-project-in-a-workbook-is-signed/)Boole tipi özelliği, proje imzalanmışsa true değerini döndürür.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.VbaProject;

//Test if VbaProject is signed

if (project.IsSigned)

{

    Console.WriteLine("VBA Project is Signed");

}

else

{

    Console.WriteLine("VBA Project is not Signed");

}

{{< /highlight >}}
## **Değiştirilmiş API'ler**
### **Yöntem Cell.GetFormatConditions Değiştirildi**
v8.6.1 sürümüyle, Aspose.Cells for .NET API, artık FormatConditionCollection türünde bir dizi döndüren Cell.GetFormatConditions yönteminin dönüş türünü değiştirdi.
## **Eski API'ler**
### **Yöntem Workbook.CheckWriteProtectedPassword Eskimiş**
v8.6.1 sürümüyle Workbook.CheckWriteProtectedPassword yöntemi amortismana tabi tutuldu olarak işaretlendi. Bir dize değerini parametre olarak kabul edebilen ve parola elektronik tablonun önceden ayarlanmış parolasıyla eşleşirse Boolean döndüren WorkbookSettings.WriteProtection.ValidatePassword yönteminin kullanılması önerilir.

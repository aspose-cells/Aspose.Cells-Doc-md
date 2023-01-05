---
title: Genel API Aspose.Cells 8.6.1'deki değişiklikler
type: docs
weight: 210
url: /tr/java/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.6.0'dan 8.6.1'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen sınıfları değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **HTML Bağlantı Hedefi Türü Desteği**
 Aspose.Cells for Java API'in bu sürümü, birlikte izin veren yeni bir özellik olan HtmlSaveOptions.LinkTargetType ile birlikte HtmlLinkTargetType adında bir numaralandırma ortaya çıkardı.[HTML formatına dönüştürürken e-tablodaki bağlantılar için hedef tipini ayarlayın](/cells/tr/java/change-the-html-link-target-type/). Varsayılan değerin SELF olduğu HtmlLinkTargetType numaralandırmasının olası değerleri aşağıdaki gibidir.

1. HtmlLinkTargetType.BLANK: Bağlantı verilen belgeyi/sayfayı yeni bir pencerede veya sekmede açar.
1. HtmlLinkTargetType.PARENT: Bağlı belgeyi/sayfayı ana çerçevede açar.
1. HtmlLinkTargetType.SELF: Bağlantı verilen belgeyi/sayfayı, bağlantının tıklandığı çerçevede açar.
1. HtmlLinkTargetType.TOP: Bağlantılı belgeyi/sayfayı pencerenin tam gövdesinde açar.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **Yöntem VbaModuleCollection.remove Eklendi**
Aspose.Cells for Java 8.6.1, VbaModuleCollection.remove yönteminin başka bir aşırı yüklemesini ortaya çıkardı ve artık belirtilen Çalışma Sayfası ile ilişkili tüm VBA modüllerini kaldırmak için bir Çalışma Sayfası örneğini kabul edebilir.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **Yöntem RangeCollection.add Eklendi**
Aspose.Cells for Java 8.6.1, belirli bir Çalışma Sayfası için aralık koleksiyonuna Range nesneleri eklemek için kullanılabilecek RangeCollection.Add yöntemini kullanıma sundu.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **Yöntem Cell.setCharacters Eklendi**
 Cell.setCharacters yöntemi şu amaçlarla kullanılabilir:[zengin metnin bölümlerini güncelleme](/cells/tr/java/access-and-update-the-portions-of-rich-text-of-cell/) belirli bir Cell nesnesinin. Cell.getCharacters metodu ile metnin bölümlerine ulaşılır ve sonrasında Cell.setCharacters metodu ile değişiklikler yapılabilir.**elde etmek** yöntemi, yazı tipi adı, yazı tipi rengi, kalınlık vb. çeşitli özellikleri ayarlamak için kullanılabilecek bir FontSetting nesneleri dizisi döndürür ve**ayarlamak** Yöntem, değişiklikleri uygulamak için kullanılabilir.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **Özellik VbaProject.isSigned Eklendi**
 Aspose.Cells for Java 8.6.1, şu amaçlarla kullanılabilecek VbaProject.isSigned özelliğini kullanıma sundu:[Çalışma Kitabındaki bir VbaProject'in imzalanıp imzalanmadığını test edin](/cells/tr/java/check-if-vba-project-in-a-workbook-is-signed/)Boole tipi özelliği, proje imzalanmışsa true değerini döndürür.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.getVbaProject();

//Test if VbaProject is signed

if (project.isSigned())

{

    System.out.println("VBA Project is Signed");

}

else

{

	System.out.println("VBA Project is not Signed");

}

{{< /highlight >}}
## **Değiştirilmiş API'ler**
### **Yöntem Cell.getFormatConditions Değiştirildi**
v8.6.1 sürümüyle, Aspose.Cells for Java API, artık FormatConditionCollection türünde bir dizi döndüren Cell.getFormatConditions yönteminin dönüş türünü değiştirdi.
## **Eski API'ler**
### **Yöntem Workbook.checkWriteProtectedPassword Eskimiş**
v8.6.1 sürümüyle birlikte, Workbook.checkWriteProtectedPassword yöntemi amortismana tabi tutuldu olarak işaretlendi. Bir String değerini parametre olarak kabul edebilen ve parola elektronik tablonun önceden ayarlanmış parolasıyla eşleşirse Boolean döndüren WorkbookSettings.WriteProtection.validatePassword yönteminin kullanılması önerilir.

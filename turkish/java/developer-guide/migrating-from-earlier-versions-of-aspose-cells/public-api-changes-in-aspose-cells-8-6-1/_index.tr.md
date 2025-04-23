---
title: Aspose.Cells 8.6.1 de Genel API Değişiklikleri
type: docs
weight: 210
url: /tr/java/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek Aspose.Cells API'sındaki değişiklikleri, sürüm 8.6.0'dan 8.6.1'e, yeni ve güncellenmiş genel yöntemler, eklenecek sınıflar ve ayrıca Aspose.Cells arka plandaki davranışındaki herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **HTML Bağlantı Hedef Türü Desteği**
Bu Aspose.Cells for Java API sürümü, HTML biçimine dönüştürülürken elektronik tablolardaki bağlantılar için HTMLLinkTargetType adlı bir numaralandırmayı ortaya çıkardı ve HtmlSaveOptions.LinkTargetType adlı yeni bir özelliği hem de bağlantıların hedef türünü ayarlamayı sağlar. HTMLLinkTargetType numaralandırmasının mümkün değerleri şunlardır ve varsayılan değer SELF'tir.

1. HtmlLinkTargetType.BLANC: Bağlantıdaki belge/sayfayı yeni bir pencerede veya sekmede açar.
1. HtmlLinkTargetType.PARENT: Bağlantıdaki belge/sayfayı üst çerçevede açar.
1. HtmlLinkTargetType.SELF: Bağlantıdaki belge/sayfayı, bağlantının tıklandığı çerçevede açar.
1. HtmlLinkTargetType.TOP: Bağlantıdaki belge/sayfayı pencerenin tam gövdesinde açar.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **VbaModuleCollection.remove Yöntemi Eklendi**
Aspose.Cells for Java 8.6.1, VbaModuleCollection.remove yönteminin başka bir aşırı yüklemesini ortaya çıkardı; bu yöntem, belirtilen Çalışsayfa ile ilişkili tüm VBA modüllerini kaldırmak için bir Worksheet örneğini kabul edebilir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **RangeCollection.add Yöntemi Eklendi**
Aspose.Cells for Java 8.6.1, RangeCollection.Add yöntemini ortaya çıkardı; bu yöntem, belirli bir Çalışsayfa için bir aralık nesneleri koleksiyonuna aralık nesneleri eklemek için kullanılabilir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **Cell.setCharacters Yöntemi Eklendi**
Cell.setCharacters yöntemi, bir verilen Cell öğesinin zengin metnin kısımlarını güncellemek için kullanılabilir. Cell.getCharacters yöntemi, metnin kısımlarına erişmek için kullanılır ve ardından değişiklikler Cell.setCharacters yöntemiyle yapılabilirken **get** yöntemi, farklı özellikler font adı, font rengi, kalınlık vb. ayarlamak için manipüle edilebilecek bir FontSetting nesneleri dizisi döndürür ve **set** yöntemi, değişiklikleri uygulamak için kullanılabilir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **VbaProject.isSigned Özelliği Eklendi**
Aspose.Cells for Java 8.6.1, VbaProject.isSigned özelliğini ortaya çıkardı; bu özellik, bir Workbook içindeki bir VbaProject'in imzalı olup olmadığını test etmek için kullanılabilir. Boolean tipinde özellik, proje imzalanmışsa true döndürür.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

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
## **Değiştirilmiş API'lar**
### **Modified Cell.getFormatConditions Metodu**
V8.6.1 sürümüyle birlikte, Aspose.Cells for Java API, Cell.getFormatConditions metodunun dönüş türünü değiştirmiştir ve artık FormatConditionCollection türünde bir dizi döndürmektedir.
## **Eskimiş API'lar**
### **Eski Workbook.checkWriteProtectedPassword Metodu**
V8.6.1 sürümüyle birlikte, Workbook.checkWriteProtectedPassword metodu iptal edilmiştir. İt is advised to use the WorkbookSettings.WriteProtection.validatePassword method that can accept a String value as parameter and returns Boolean if password matches the preset password of the spreadsheet.
{{< app/cells/assistant language="java" >}}

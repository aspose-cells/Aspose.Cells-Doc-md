---
title: Aspose.Cells 8.6.1 de Genel API Değişiklikleri
type: docs
weight: 200
url: /tr/net/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek Aspose.Cells API'sındaki değişiklikleri, sürüm 8.6.0'dan 8.6.1'e, yeni ve güncellenmiş genel yöntemler, eklenecek sınıflar ve ayrıca Aspose.Cells arka plandaki davranışındaki herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **HTML Bağlantı Hedef Türü Desteği**
Bu sürümde Aspose.Cells for .NET API, HtmlLinkTargetType adlı bir numaralandırmayı ve birlikte, elektronik tabloyu HTML biçimine dönüştürürken bağlantıların hedef türünü [ayarlamaya izin veren HtmlSaveOptions.LinkTargetType adlı yeni bir özelliği ortaya çıkarmıştır](/cells/tr/net/change-the-html-link-target-type/). HtmlLinkTargetType numaralandırmasının olası değerleri aşağıdaki gibidir, varsayılan değeri Self'tir.

1. HtmlLinkTargetType.Blank: Bağlantılı belge/sayfa yeni bir pencerede veya sekmede açılır.
1. HtmlLinkTargetType.Parent: Bağlantılı belge/sayfa üst çerçevede açılır.
1. HtmlLinkTargetType.Self: Bağlantılı belge/sayfa, bağlantının tıklandığı yerdeki çerçevede açılır.
1. HtmlLinkTargetType.Top: Bağlantılı belge/sayfa, pencerenin tam gövdesinde açılır.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **Eklenen VbaModuleCollection.Remove Yöntemi**
Aspose.Cells for .NET 8.6.1, VbaModuleCollection.Remove yönteminin, belirli Worksheet ile ilişkili tüm VBA modüllerini kaldırmak için bir Worksheet örneğini kabul edebilen bir overload'unu ortaya çıkarmıştır.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **Eklenen RangeCollection.Add Yöntemi**
Aspose.Cells for .NET 8.6.1, bir Worksheet için belirli bir Collection of ranges'e Range nesneleri eklemek için kullanılan RangeCollection.Add yöntemini ortaya çıkarmıştır.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **Cell.SetCharacters Methodu Eklendi**
Cell.SetCharacters yöntemi, verilen bir Hücre nesnesinin zengin metninin bölümlerini güncellemek için kullanılabilir. Cell.GetCharacters yöntemi metnin bölümlerine erişmek için kullanılır ve ardından değişiklikler, **Get** yöntemi bir FontSetting nesnesi dizisi döndürür ve font adı, font rengi, kalınlık vb. gibi çeşitli özelliklerini ayarlamak için manipüle edilebilir ve **Set** yöntemi değişiklikleri uygulamak için kullanılabilir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **VbaProject.IsSigned Özelliği Eklendi**
Aspose.Cells for .NET 8.6.1, VbaProject.IsSigned özelliğini açığa çıkardı. Bu özellik, bir Workbook içindeki VbaProject'in imzalı olup olmadığını kontrol etmek için kullanılabilir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

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
## **Değiştirilmiş API'lar**
### **Cell.GetFormatConditions Methodu Değiştirildi**
v8.6.1'in piyasaya sürülmesiyle, Aspose.Cells for .NET API'sı Cell.GetFormatConditions yönteminin dönüş türünü değiştirmiştir ve artık FormatConditionCollection türünde bir dizi döndürmektedir.
## **Eskimiş API'lar**
### **Workbook.CheckWriteProtectedPassword Yöntemi Kullanımdan Kaldırıldı**
V8.6.1'in piyasaya sürülmesiyle, Workbook.CheckWriteProtectedPassword yöntemi kullanımdan kaldırılmıştır. Önerilen, belirli bir şifre ile eşleşip eşleşmediğini kontrol eden ve True döndüren WorkbookSettings.WriteProtection.ValidatePassword yöntemini kullanmaktır.

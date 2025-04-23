---
title: Aspose.Cells 8.7.0 da Genel API Değişiklikleri
type: docs
weight: 230
url: /tr/net/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

Bu belge, modül/uçbirim geliştiricilerin ilgisini çekebilecek Aspose.Cells API'sindeki değişiklikleri, 8.6.3 sürümünden 8.7.0 sürümüne kadar açıklar. Yeni ve güncellenmiş genel yöntemler, eklenen ve kaldırılan sınıflar vb. yanı sıra Aspose.Cells'in arka plandaki davranışında herhangi bir değişikliği de içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **VBA Projesi Dijital İmzalama, Algılama ve Çıkarma Desteği**
Bu sürümde, Aspose.Cells for .NET, VBA projesini dijital imzalama, bir VBA projesinin imzalı ve geçerli olup olmadığını algılama gibi görevlerde kullanıcılarına yardımcı olmak için bazı yeni özellikleri ve yöntemleri açığa çıkardı. Ayrıca, yeni API, dijital imzalı VBA projesinden sertifikayı ham veri olarak çıkarmaya olanak tanımaktadır.
###### **VBA Projesini Dijital İmzala**
Aspose.Cells for .NET 8.7.0, VbaProject.Sign yöntemi açığa çıkardı, bu [Bir Worbook'taki VBA projesini dijital olarak imzalamak](/cells/tr/net/digitally-sign-a-vba-code-project-with-certificate/) için kullanılabilir. Söz konusu yöntem, Aspose.Cells.DigitalSignatures ad alanında bulunan DigitalSignature sınıfının bir örneğini kabul eder.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **Dijital İmzalı VBA Projesinin Algılanması**
Yeni açığa çıkarılan VbaProject.IsSigned özelliği, bir Workbook'taki VBA projesinin [dijital olarak imzalanıp imzalanmadığını tespit etmek](/cells/tr/net/check-if-vba-code-is-signed/) için kullanılabilir. VbaProject.IsSigned özelliği, Boolean türünde olup, VBA projesi dijital olarak imzalanmışsa true değerini döndürür, aksi halde söz konusu özellik null olacaktır.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    Console.WriteLine("VbaProject is digitally signed");

}

else

{

    Console.WriteLine("VbaProject is not digitally signed");

}

{{< /highlight >}}


###### **VBA Projesinden Dijital İmza Çıkarılması**
Bu API'nin bu revizyonunda ayrıca VbaProject.CertRawData özelliği açığa çıkarılmıştır. Bu özellik, bir Woorkbook'tan [dijital sertifikanın ham verilerini çıkarmak](/cells/tr/net/export-vba-certificate-to-file-or-stream/) için kullanılabilir. VbaProject.CertRawData özelliği, eğer VBA projesi dijital olarak imzalanmışsa, raw sertifika verilerini içeren bayt dizisi türündedir, aksi halde söz konusu özellik null olacaktır.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **VBA Projesinin Dijital İmzasının Doğrulanması**
Genel API'ye eklenen diğer bir özellik VbaProject.IsValidSigned özelliğidir, bu özellik VBA projesinin [dijital imzasının doğrulanmasında](/cells/tr/net/check-if-digital-signature-of-vba-code-is-valid/) kullanışlı olabilir. Söz konusu özellik, dijital imzanın geçerli ise true değerini, aksi halde geçersiz ise false değerini geri döndürür.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    //Check if signature is valid

    if (vbaProject.IsValidSigned)

    {

        Console.WriteLine("VbaProject is digitally signed & signature is valid");

    }

}

{{< /highlight >}}


### **Protection.VerifyPassword Yöntemi Eklendi**
Aspose.Cells for .NET 8.7.0, Koruma.VerifyPassword yöntemini açığa çıkardı, bu [Çalışsayı Korumak İçin Kullanılan Şifrenin Doğrulanması](/cells/tr/net/verify-password-used-to-protect-the-worksheet/) için kullanılabilir. Bu yöntem, bir dize örneğini parametre olarak kabul eder ve belirtilen şifrenin çalışsayı korumak için kullanılan şifre ile eşleşmesi durumunda true değerini döndürür.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Verify the password for Worksheet

if (protection.VerifyPassword(password))

{

    Console.WriteLine("Password has matched");

}

else

{

    Console.WriteLine("Password did not match");

}

{{< /highlight >}}


### **Protection.IsProtectedWithPassword Özelliği Eklendi**
Bu Aspose.Cells for .NET'nın bu sürümü ayrıca Protection.IsProtectedWithPassword özelliğini açığa çıkardı, Bu özellik, bir Worlsheet'in [şifre ile korunup korunmadığını tespit etmek](/cells/tr/net/detect-if-worksheet-is-password-protected/) için kullanışlı olabilir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Check if Worksheet is password protected

if (protection.IsProtectedWithPassword)

{

    Console.WriteLine("Worksheet is password protected");

}

else

{

    Console.WriteLine("Worksheet is not password protected");

}

{{< /highlight >}}


### **Eklendi ColorScale.Is3ColorScale Özelliği**
Aspose.Cells for .NET 8.7.0, ColorScale.Is3ColorScale özelliğini açığa çıkardı, bu özellik [2 Renkli Ölçekli koşullu biçimlendirme oluşturmak](/cells/tr/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/) için kullanılabilir. Söz konusu özellik, varsayılan değeri true olan Boolean türündedir, bunun anlamı, koşullu biçimlendirme varsayılan olarak 3 Renkli Ölçekli olacaktır. Bununla birlikte, ColorScale.Is3ColorScale özelliğini false olarak değiştirme, 2 Renkli Ölçekli bir koşullu biçimlendirme [oluşturacaktır](/cells/tr/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

var sheet = book.Worksheets[0];

//Add FormatConditions to the collection

int index = sheet.ConditionalFormattings.Add();

//Access newly added formatConditionCollection via its index

var formatConditionCollection = sheet.ConditionalFormattings[index];

//Create a CellArea on which conditional formatting rule will be applied

var cellArea = CellArea.CreateCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.AddArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.AddCondition(FormatConditionType.ColorScale);

//Access newly added format condition via its index

var formatCondition = formatConditionCollection[index];

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.ColorScale.Is3ColorScale = false;

//Set other necessary properties

{{< /highlight >}}


### **Added TxtLoadOptions.HasFormula Property**
Aspose.Cells for .NET 8.7.0, CSV/TXT dosyalarını yüklerken [formülleri tanımlamaya ve ayrılmış düz veriye formülleri ayrıştırmaya](/cells/tr/net/load-or-import-csv-file-with-formulas/) olanak tanıdı. Yeni başlayan TxtLoadOptions.HasFormula özelliği, true olarak ayarlandığında, API'yi girdi ayrılmış dosyadan formülleri ayrıştırmak ve bunları ilgili hücrelere eklemek için yönlendirirken herhangi ek işlem gerektirmez.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of TxtLoadOptions

var options = new TxtLoadOptions();

//Set HasFormula property to true

options.HasFormula = true;

//Set the Separator property as desired

options.Separator = ',';

//Load the CSV/TXT file using the instance of TxtLoadOptions

var book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.CalculateFormula();

//Write result in any of the supported formats

book.Save(outFilePath);

{{< /highlight >}}


### **DataLabels.IsResizeShapeToFitText Özelliği Eklendi**
Aspose.Cells for .NET 8.7.0'nin açığa çıkardığı bir diğer kullanışlı özellik, DataLabels.IsResizeShapeToFitText özelliğidir, bu özellik, Excel uygulaması için [Grafik veri etiketlerinin şeklini metne sığdırma](/cells/tr/net/resize-chart-s-data-label-shape-to-fit-text/) özelliğini etkinleştirebilir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook containing the Chart

var book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

var sheet = book.Worksheets[0];

//Access the desired Chart via its index or name

var chart = sheet.Charts[0];

//Access the DataLabels of desired NSeries

var labels = chart.NSeries[0].DataLabels;

//Set ResizeShapeToFitText property to true

labels.IsResizeShapeToFitText = true;

//Calculate Chart

chart.Calculate();

{{< /highlight >}}


### **PdfSaveOptions.OptimizationType Özelliği Eklendi**
Aspose.Cells for .NET 8.7.0, PdfSaveOptions.OptimizationType özelliğini ve PdfOptimizationType numaralandırmasını kullanıcıların, [çalışsayfalarını PDF biçimine dönüştürürken istedikleri optimizasyon algoritmasını seçmelerini](/cells/tr/net/save-excel-into-pdf-with-standard-or-minimum-size/) kolaylaştırmak üzere açığa çıkardı. PdfSaveOptions.OptimizationType özelliğinin 2 mümkün değeri aşağıda ayrıntılı olarak belirtilmiştir.

1. PdfOptimizationType.MinimumSize: Sonuç dosya boyutu için kalite feda edilmektedir.
2. PdfOptimizationType.Standard: Kalite feda edilmez bu nedenle sonuç dosya boyutu büyük olacaktır.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of PdfSaveOptions

var pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.OptimizationType = PdfOptimizationType.MinimumSize;

//Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.Save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
## **Removed APIs**
### **Property Workbook.SaveOptions Kaldırıldı**
Workbook.SaveOptions özelliği bir süre önce işaretlenmişti. Bu sürümle birlikte, bu özellik tamamen genel API'den kaldırıldı, bu nedenle alternatif olarak Workbook.Save(Stream, SaveOptions) veya Workbook.Save(string, SaveOptions) yöntemini kullanmanız önerilir.
{{< app/cells/assistant language="csharp" >}}

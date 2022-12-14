---
title: Genel API Aspose.Cells 8.7.0'daki değişiklikler
type: docs
weight: 230
url: /tr/net/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 8.6.3 sürümünden 8.7.0 sürümüne Aspose.Cells API üzerindeki değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **VBA Projesi Dijital İmzalama, Algılama ve Çıkarma Desteği**
Aspose.Cells for .NET numaralı bu sürüm, kullanıcılara bir VBA projesini dijital olarak imzalama, bir VBA projesinin imzalanıp imzalanmadığını ve geçerli olup olmadığını belirleme gibi görevlerde yardımcı olacak bazı yeni özellikler ve yöntemler ortaya çıkardı. Ayrıca yeni API, sertifikanın Workbook'ta dijital olarak imzalanmış VBA projesinden ham veri olarak çıkarılmasına izin verir.
###### **VBA Projesini Dijital Olarak İmzalayın**
 Aspose.Cells for .NET 8.7.0, kullanılabilecek VbaProject.Sign yöntemini kullanıma sundu.[VBA projesini bir Çalışma Kitabında dijital olarak imzalayın](/cells/tr/net/digitally-sign-a-vba-code-project-with-certificate/). Bahsedilen yöntem, Aspose.Cells.DigitalSignatures ad alanında bulunan DigitalSignature sınıfının bir örneğini kabul eder.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **Dijital Olarak İmzalanmış VBA Projesinin Tespiti**
 Yeni ortaya çıkan VbaProject.IsSigned özelliği,[Çalışma Kitabındaki VBA projesinin dijital olarak imzalanıp imzalanmadığını tespit edin](/cells/tr/net/check-if-vba-code-is-signed/). VbaProject.IsSigned özelliği Boolean türündedir ve VBA projesi dijital olarak imzalanmışsa veya tersi geçerliyse doğru değerini döndürür.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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


###### **VBA Projesinden Dijital İmza Çıkarma**
API'in bu revizyonu, aşağıdakilere izin veren VbaProject.CertRawData özelliğini de ortaya çıkardı.[dijital sertifikanın ham verilerini VBA projesinden çıkarın](/cells/tr/net/export-vba-certificate-to-file-or-stream/). VbaProject.CertRawData özelliği, VBA projesi dijital olarak imzalanmışsa ham sertifika verilerini içerecek bayt dizisi türündedir, aksi takdirde söz konusu özellik boş olacaktır.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **VBA Projesinin Dijital İmzasını Doğrulayın**
 Genel API'e bir başka ekleme de yararlı olabilecek VbaProject.IsValidSigned özelliğidir.[VBA projesinin dijital imzasının doğrulanması](/cells/tr/net/check-if-digital-signature-of-vba-code-is-valid/). Söz konusu özellik, dijital imza geçerliyse true, geçersizse false döndürür.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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


### **Yöntem Protection.VerifyPassword Eklendi**
 Aspose.Cells for .NET 8.7.0, şu işlemler için kullanılabilecek Protection.VerifyPassword yöntemini kullanıma sundu[Çalışma Sayfasını korumak için kullanılan parolayı doğrulayın](/cells/tr/net/verify-password-used-to-protect-the-worksheet/)Bu yöntem, bir dize örneğini parametre olarak kabul eder ve belirtilen parola, Çalışma Sayfasını korumak için kullanılan parolayla eşleşirse true değerini döndürür.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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


### **Property Protection.IsProtectedWithPassword Eklendi**
 Aspose.Cells for .NET API'in bu sürümü, şu alanlarda yararlı olabilecek Protection.IsProtectedWithPassword özelliğini de kullanıma sunmuştur.[bir Çalışma Sayfasının parola korumalı olup olmadığını tespit etme](/cells/tr/net/detect-if-worksheet-is-password-protected/).

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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


### **Özellik ColorScale.Is3ColorScale Eklendi**
 Aspose.Cells for .NET 8.7.0, 2-Renk Ölçeği koşullu biçimi oluşturmak için kullanılabilecek ColorScale.Is3ColorScale özelliğini ortaya çıkardı. Bahsedilen özellik, varsayılan değeri true olan Boolean türündedir; bu, koşullu formatın varsayılan olarak 3-Renk Ölçeği olacağı anlamına gelir. Ancak, ColorScale.Is3ColorScale özelliğinin yanlış olarak değiştirilmesi,[2 Renkli Ölçekli bir koşullu format oluşturun](/cells/tr/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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


### **Özellik TxtLoadOptions.HasFormula Eklendi**
 Aspose.Cells for .NET 8.7.0 desteği sağladı[Sınırlandırılmış düz verilere sahip CSV/TXT dosyalarını yüklerken formülleri tanımlayın ve ayrıştırın](/cells/tr/net/load-or-import-csv-file-with-formulas/). Yeni kullanıma sunulan TxtLoadOptions.HasFormula özelliği true olarak ayarlandığında, API'i formülleri girişle ayrılmış dosyadan ayrıştırmaya ve herhangi bir ek işlem gerektirmeden ilgili hücrelere ayarlamaya yönlendirir.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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


### **Özellik DataLabels.IsResizeShapeToFitText Eklendi**
 Aspose.Cells for .NET 8.7.0'ın kullanıma sunduğu bir başka kullanışlı özellik de şu özelliği etkinleştirebilen DataLabels.IsResizeShapeToFitText özelliğidir.[Metni sığdırmak için şekli yeniden boyutlandırma](/cells/tr/net/resize-chart-s-data-label-shape-to-fit-text/) grafiğin veri etiketleri için Excel uygulamasının özelliği.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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


### **Özellik PdfSaveOptions.OptimizationType Eklendi**
Aspose.Cells for .NET 8.7.0, kullanıcıların şunları yapmasını kolaylaştırmak için PdfSaveOptions.OptimizationType özelliğini ve PdfOptimizationType numaralandırmasını kullanıma sundu.[elektronik tabloları PDF formatına dışa aktarırken istenen optimizasyon algoritmasını seçin](/cells/tr/net/save-excel-into-pdf-with-standard-or-minimum-size/). PdfSaveOptions.OptimizationType özelliği için aşağıda ayrıntıları verilen 2 olası değer vardır.

1. PdfOptimizationType.MinimumSize: Ortaya çıkan dosya boyutu için kaliteden ödün verilir.
1. PdfOptimizationType.Standard: Kaliteden ödün verilmez, bu nedenle ortaya çıkan dosya boyutu büyük olur.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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
## **Kaldırılan API'ler**
### **Workbook.SaveOptions Özelliği Kaldırıldı**
Workbook.SaveOptions özelliği bir süre önce geçersiz olarak işaretlendi. Bu sürümle birlikte, genel kullanımdan tamamen kaldırıldı API bu nedenle alternatif olarak Workbook.Save(Stream, SaveOptions) veya Workbook.Save(string, SaveOptions) yönteminin kullanılması tavsiye edilir.

---
title: Genel API Aspose.Cells 8.7.0'daki değişiklikler
type: docs
weight: 240
url: /tr/java/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 8.6.3 sürümünden 8.7.0 sürümüne Aspose.Cells API üzerindeki değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **PDF Optimizasyon Desteği**
 Aspose.Cells API'leri zaten e-tabloları PDF'e dönüştürme özelliğini sağlıyor. API'in bu sürümüyle, kullanıcılar artık[ortaya çıkan PDF boyutunu optimize edin](/cells/tr/java/save-excel-into-pdf-with-standard-or-minimum-size/)ilave olarak. Aspose.Cells for Java 8.7.0, elektronik tabloları PDF biçimine dışa aktarırken kullanıcıların istenen optimizasyon algoritmasını seçmesini kolaylaştırmak için PdfSaveOptions.OptimizationType özelliğinin yanı sıra PdfOptimizationType numaralandırmasını kullanıma sundu. PdfSaveOptions.OptimizationType özelliği için aşağıda ayrıntıları verilen 2 olası değer vardır.

1. PdfOptimizationType.MINIMUM_SIZE: Ortaya çıkan dosya boyutu için kaliteden ödün verilir.
1. PdfOptimizationType.STANDARD: Kaliteden ödün verilmez, bu nedenle ortaya çıkan dosya boyutu büyük olur.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of PdfSaveOptions

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.setOptimizationType(PdfOptimizationType.MINIMUM_SIZE);

//Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
### **Dijital Olarak İmzalanmış VBA Projesinin Tespiti**
 Yeni ortaya çıkan VbaProject.isSigned özelliği,[Çalışma Kitabındaki VBA projesinin dijital olarak imzalanıp imzalanmadığını tespit edin](/cells/tr/java/check-if-vba-code-is-signed/). VbaProject.isSigned özelliği Boolean türündedir ve VBA projesi dijital olarak imzalanmışsa veya tersi geçerliyse doğru değerini döndürür.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

VbaProject vbaProject = book.getVbaProject();

//Check if VbaProject is digitally signed

if (vbaProject.isSigned())

{

	System.out.println("VbaProject is digitally signed");

}

else

{

	System.out.println("VbaProject is not digitally signed");

}

{{< /highlight >}}
### **Yöntem Protection.verifyPassword Eklendi**
Aspose.Cells API'ler, bir parolanın String örneği olarak belirtilmesine izin veren correctPassword yöntemini sunarak Koruma sınıfını geliştirdi ve[Çalışma Sayfasını korumak için aynı parolanın kullanılıp kullanılmadığını doğrular](/cells/tr/java/verify-password-used-to-protect-the-worksheet/). Protection.verifyPassword yöntemi, belirtilen parola verilen çalışma sayfasını korumak için kullanılan parolayla eşleşirse true, belirtilen parola eşleşmezse false değerini döndürür. Aşağıdaki kod parçası, parola korumasını algılamak için Protection.isProtectedWithPassword alanıyla birlikte Protection.verifyPassword yöntemini kullanır ve parolayı doğrular.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load a spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the protected Worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Check if Worksheet is password protected

if (sheet.getProtection().isProtectedWithPassword())

{

  //Verify the password used to protect the Worksheet

  if (sheet.getProtection().verifyPassword("password"))

  {

	  System.out.println("Specified password has matched");

  }

  else

  {

	  System.out.println("Specified password has not matched");

  }

}

{{< /highlight >}}
### **Özellik Koruması.isProtectedWithPassword Eklendi**
 Aspose.Cells for Java'in bu sürümü ayrıca şu alanlarda yararlı olabilecek Protection.isProtectedWithPassword alanını kullanıma sunmuştur.[bir Çalışma Sayfasının parola korumalı olup olmadığını tespit etme](/cells/tr/java/detect-if-worksheet-is-password-protected/).

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

Worksheet sheet = book.getWorksheets().get(0);

//Access Protection module of desired Worksheet

Protection protection = sheet.getProtection();

//Check if Worksheet is password protected

if (protection.isProtectedWithPassword())

{

	System.out.println("Worksheet is password protected");

}

else

{

	System.out.println("Worksheet is not password protected");

}

{{< /highlight >}}
### **Özellik ColorScale.Is3ColorScale Eklendi**
 Aspose.Cells for Java 8.7.0, kullanılabilecek ColorScale.Is3ColorScale özelliğini ortaya çıkardı[Renkli Ölçekli koşullu format oluştur](/cells/tr/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/). Bahsedilen özellik, varsayılan değeri true olan Boolean türündedir; bu, koşullu formatın varsayılan olarak 3-Renk Ölçeği olacağı anlamına gelir. Ancak, ColorScale.Is3ColorScale özelliğinin false olarak değiştirilmesi, 2-Renk Ölçeği koşullu biçimini oluşturur.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

Worksheet sheet = book.getWorksheets().get(0);

//Add FormatConditions to the collection

int index = sheet.getConditionalFormattings().add();

//Access newly added formatConditionCollection via its index

FormatConditionCollection formatConditionCollection = sheet.getConditionalFormattings().get(index);

//Create a CellArea on which conditional formatting rule will be applied

CellArea cellArea = CellArea.createCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.addArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.addCondition(FormatConditionType.COLOR_SCALE);

//Access newly added format condition via its index

FormatCondition formatCondition = formatConditionCollection.get(index);

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.getColorScale().setIs3ColorScale(false);

//Set other necessary properties

{{< /highlight >}}
### **Özellik TxtLoadOptions.HasFormula Eklendi**
 Aspose.Cells for Java 8.7.0 desteği sağladı[sınırlandırılmış düz verilere sahip CSV/TXT dosyaları yüklenirken formülleri tanımlayın ve ayrıştırın](/cells/tr/java/load-or-import-csv-file-with-formulas/). Yeni kullanıma sunulan TxtLoadOptions.HasFormula özelliği true olarak ayarlandığında, API'i formülleri girişle ayrılmış dosyadan ayrıştırmaya ve herhangi bir ek işlem gerektirmeden ilgili hücrelere ayarlamaya yönlendirir.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of TxtLoadOptions

TxtLoadOptions options = new TxtLoadOptions();

//Set HasFormula property to true

options.setHasFormula(true);

//Set the Separator property as desired

options.setSeparator(',');

//Load the CSV/TXT file using the instance of TxtLoadOptions

Workbook book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.calculateFormula();

//Write result in any of the supported formats

book.save(outFilePath);

{{< /highlight >}}
### **Özellik DataLabels.ResizeShapeToFitText Eklendi**
 Aspose.Cells for Java 8.7.0'ın kullanıma sunduğu diğer bir kullanışlı özellik,[metni sığdırmak için şekli yeniden boyutlandırma](/cells/tr/java/resize-chart-s-data-label-shape-to-fit-text/)grafiğin veri etiketleri için Excel uygulamasının özelliği.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook containing the Chart

Workbook book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

Worksheet sheet = book.getWorksheets().get(0);

//Access the desired Chart via its index or name

Chart chart = sheet.getCharts().get(0);

//Access the DataLabels of desired NSeries

DataLabels labels = chart.getNSeries().get(0).getDataLabels();

//Set ResizeShapeToFitText property to true

labels.setResizeShapeToFitText(true);

//Calculate Chart

chart.calculate();

{{< /highlight >}}
## **Kaldırılan API'ler**
### **Workbook.SaveOptions Özelliği Kaldırıldı**
Workbook.SaveOptions özelliği bir süre önce geçersiz olarak işaretlendi. Bu sürümle birlikte, genel kullanımdan tamamen kaldırıldı API bu nedenle, alternatif olarak Workbook.save(Stream, SaveOptions) veya Workbook.save(string, SaveOptions) yönteminin kullanılması tavsiye edilir.

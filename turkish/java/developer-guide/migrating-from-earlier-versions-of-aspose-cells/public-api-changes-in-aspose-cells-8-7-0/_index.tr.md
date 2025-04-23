---
title: Aspose.Cells 8.7.0 da Genel API Değişiklikleri
type: docs
weight: 240
url: /tr/java/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

Bu belge, modül/uçbirim geliştiricilerin ilgisini çekebilecek Aspose.Cells API'sindeki değişiklikleri, 8.6.3 sürümünden 8.7.0 sürümüne kadar açıklar. Yeni ve güncellenmiş genel yöntemler, eklenen ve kaldırılan sınıflar vb. yanı sıra Aspose.Cells'in arka plandaki davranışında herhangi bir değişikliği de içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **PDF Optimizasyon Desteği**
Aspose.Cells API'leri zaten elektronik tabloları PDF'ye dönüştürme özelliğini sağlar. Bu API'nin bu sürümü ile, kullanıcılar artık [üretilen PDF boyutunu optimize edebilir](/cells/tr/java/save-excel-into-pdf-with-standard-or-minimum-size/). Aspose.Cells for Java 8.7.0, kullanıcıların elektronik tabloları PDF biçimine dışa aktarırken istenen optimizasyon algoritmasını seçmelerini kolaylaştırmak için PdfSaveOptions.OptimizationType özelliğini ve PdfOptimizationType numaralandırmasını açığa çıkardı. PdfSaveOptions.OptimizationType özelliğinin 2 olası değeri bulunmaktadır, aşağıda detayları verilmiştir. 

1. PdfOptimizationType.MINIMUM_SIZE: Kalite, sonuç dosya boyutu için riske atılır.
1. PdfOptimizationType.STANDARD: Kalite riske atılmaz, bu nedenle sonuç dosya boyutu büyük olacaktır.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

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
### **Dijital İmzalı VBA Projesinin Algılanması**
Yeni açığa çıkarılan VbaProject.isSigned özelliği, bir Workbook'daki VBA projesinin [dijital olarak imzalanıp imzalanmadığını algılamak için kullanılabilir](/cells/tr/java/check-if-vba-code-is-signed/). VbaProject.isSigned özelliği, Boolean türünde olup, VBA projesinin dijital olarak imzalandıysa true değerini döndürür ve aksi takdirde false değerini döndürür.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

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
### **Eklendi Protection.verifyPassword Yöntemi**
Aspose.Cells API'leri, koruma sınıfını verifyPassword yöntemini kullanarak geliştirdi ve bu yöntemle bir String örneği olarak belirtilen şifreyi belirli bir çalışma sayfasını korumak için kullanılıp kullanılmadığını [onaylar](/cells/tr/java/verify-password-used-to-protect-the-worksheet/). Protection.verifyPassword yöntemi, belirtilen şifrenin verilen çalışma sayfasını korumak için kullanılan şifreyle eşleşmesi durumunda true değerini döndürür ve belirtilen şifre eşleşmiyorsa false değerini döndürür.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

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
### **Eklendi Protection.isProtectedWithPassword Özelliği**
Aspose.Cells for Java'nin bu sürümü ayrıca, [bir Çalışma Sayfasının şifre korunup korunmadığını algılamak için kullanılabilecek olan Protection.isProtectedWithPassword alanını açıkladı](/cells/tr/java/detect-if-worksheet-is-password-protected/).

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

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
### **Eklendi ColorScale.Is3ColorScale Özelliği**
Aspose.Cells for Java 8.7.0, ColorScale.Is3ColorScale özelliğini açığa çıkardı, bu [2-Renkli Ölçek koşullu formatını oluşturmak](/cells/tr/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/) için kullanılabilir. Söz konusu özellik, varsayılan değeri true olan Boolean türündedir, bu da koşullu formatın varsayılan olarak 3-Renkli Ölçek olacağı anlamına gelir. Bununla birlikte, ColorScale.Is3ColorScale özelliğini false olarak değiştirmek, 2-Renkli Ölçek koşullu format oluşturacaktır.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

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
### **Added TxtLoadOptions.HasFormula Property**
Aspose.Cells for Java 8.7.0, [Deli̇mi̇teli̇ düz veri içeren CSV/TXT dosyalarını yüklerken formülleri tanımlamak ve ayrıştırmak](/cells/tr/java/load-or-import-csv-file-with-formulas/) için destek sağladı. Yeni açığa çıkarılan TxtLoadOptions.HasFormula özelliği true olarak ayarlandığında API'nin giriş belirtilen dosyadaki formülleri ayrıştırmasına ve ilgili hücrelere ek işlem gerektirmeksizin ayarlamasına yönlendirmesini sağlar.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

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
### **Added DataLabels.ResizeShapeToFitText Property**
Aspose.Cells for Java 8.7.0 tarafından açığa çıkarılan başka bir faydalı özellik, Excel uygulamasının grafik veri etiketlerinin [metni sığdırmak için şekli yeniden boyutlandırmasını](/cells/tr/java/resize-chart-s-data-label-shape-to-fit-text/) sağlayan DataLabels.ResizeShapeToFitText özelliğidir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

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
## **Removed APIs**
### **Kaldırılan Workbook.SaveOptions Özelliği**
Workbook.SaveOptions özelliği bir süre önce işaretlenmiş olarak eskimiştir. Bu sürümle birlikte, bu özellik API'den tamamen kaldırıldığı için, alternatif olarak Workbook.save(Stream, SaveOptions) veya Workbook.save(string, SaveOptions) yöntemlerini kullanmanız önerilir.
{{< app/cells/assistant language="java" >}}

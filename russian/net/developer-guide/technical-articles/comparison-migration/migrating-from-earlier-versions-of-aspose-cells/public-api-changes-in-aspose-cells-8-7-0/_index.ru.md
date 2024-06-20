---
title: Изменения в публичном API в Aspose.Cells 8.7.0
type: docs
weight: 230
url: /ru/net/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.6.3 до 8.7.0, которые могут быть интересны разработчикам модулей/приложений. Он включает в себя не только новые и обновленные публичные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка цифровой подписи, обнаружение и извлечение проекта VBA**
В данной версии Aspose.Cells for .NET добавлены новые свойства и методы, которые помогают пользователям в таких задачах, как цифровая подпись проекта VBA, обнаружение подписан ли проект VBA и является ли он действительным. Кроме того, новое API позволяет извлечь сертификат в виде сырых данных из цифрово подписанного проекта VBA в книге.
###### **Цифровая подпись проекта VBA**
Aspose.Cells for .NET 8.7.0 добавил метод VbaProject.Sign, который можно использовать для [цифровой подписи проекта VBA в книге](/cells/ru/net/digitally-sign-a-vba-code-project-with-certificate/). Данный метод принимает экземпляр класса DigitalSignature, который находится в пространстве имен Aspose.Cells.DigitalSignatures.

Вот простой сценарий использования.

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


###### **Обнаружение цифровой подписи в проекте VBA**
Новое свойство VbaProject.IsSigned можно использовать для [определения, цифрово подписан ли проект VBA в книге](/cells/ru/net/check-if-vba-code-is-signed/). Свойство VbaProject.IsSigned имеет тип Boolean, которое возвращает true, если проект VBA цифрово подписан, и false в противном случае.

Вот простой сценарий использования.

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


###### **Извлечение цифровой подписи из проекта VBA**
В данном обновлении API также добавлено свойство VbaProject.CertRawData, которое позволяет [извлечь сырые данные цифрового сертификата из проекта VBA](/cells/ru/net/export-vba-certificate-to-file-or-stream/). Свойство VbaProject.CertRawData имеет тип массива байтов, который содержит сырые данные сертификата, если проект VBA цифрово подписан, в противном случае данное свойство будет равно null.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **Проверка цифровой подписи проекта VBA**
Еще одно дополнение к публичному API - свойство VbaProject.IsValidSigned, которое может быть полезным для [проверки цифровой подписи проекта VBA](/cells/ru/net/check-if-digital-signature-of-vba-code-is-valid/). Данное свойство возвращает true, если цифровая подпись действительна, и false, если подпись недействительна.

Вот простой сценарий использования.

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


### **Метод Added Protection.VerifyPassword**
Aspose.Cells for .NET 8.7.0 выявил метод Protection.VerifyPassword, который может использоваться для [проверки пароля, используемого для защиты Листа](/cells/ru/net/verify-password-used-to-protect-the-worksheet/). Этот метод принимает экземпляр строки в качестве параметра и возвращает true, если указанный пароль совпадает с паролем, используемым для защиты Листа.

Вот простой сценарий использования.

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


### **Добавлено свойство Added Protection.IsProtectedWithPassword**
Этот релиз Aspose.Cells for .NET API также выявил свойство Protection.IsProtectedWithPassword, которое может быть полезным для [определения, защищен ли Лист паролем или нет](/cells/ru/net/detect-if-worksheet-is-password-protected/).

Вот простой сценарий использования.

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


### **Добавлено свойство ColorScale.Is3ColorScale**
Aspose.Cells for .NET 8.7.0 выявил свойство ColorScale.Is3ColorScale, которое может использоваться для создания условного форматирования 2-цветной шкалы. Указанное свойство имеет тип Boolean со значением по умолчанию true, что означает, что условное форматирование по умолчанию будет 3-цветной шкалой. Однако переключение свойства ColorScale.Is3ColorScale на false приведет к [созданию условного форматирования 2-цветной шкалы](/cells/ru/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

Вот простой сценарий использования.

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


### **Добавлено свойство TxtLoadOptions.HasFormula**
Aspose.Cells for .NET 8.7.0 предоставил поддержку для [определения и разбора формул при загрузке файлов CSV/TXT с разделенными данными](/cells/ru/net/load-or-import-csv-file-with-formulas/). Вновь выявленное свойство TxtLoadOptions.HasFormula, когда установлено значение true, направляет API на разбор формул из входного файла с разделенными данными и устанавливает их для соответствующих ячеек без необходимости дополнительной обработки.

Вот простой сценарий использования.

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


### **Добавлено свойство Added DataLabels.IsResizeShapeToFitText**
Еще одна полезная функция, которую Aspose.Cells for .NET 8.7.0 выявил, - это свойство DataLabels.IsResizeShapeToFitText, которое может включить функцию [Изменить размер формы по размеру текста](/cells/ru/net/resize-chart-s-data-label-shape-to-fit-text/) в приложении Excel для подписей данных диаграммы.

Вот простой сценарий использования.

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


### **Добавлено свойство Added PdfSaveOptions.OptimizationType**
Aspose.Cells for .NET 8.7.0 выявил свойство PdfSaveOptions.OptimizationType вместе с перечислением PdfOptimizationType для облегчения возможности [выбора желаемого алгоритма оптимизации при экспорте таблиц в формат PDF](/cells/ru/net/save-excel-into-pdf-with-standard-or-minimum-size/). Для свойства PdfSaveOptions.OptimizationType есть 2 возможных значения, подробно описанных ниже.

1. PdfOptimizationType.MinimumSize: Качество жертвуется ради размера результирующего файла.
2. PdfOptimizationType.Standard: Качество не жертвуется, поэтому размер результирующего файла будет большим.

Вот простой сценарий использования.

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
## **Удалены API**
### **Свойство Workbook.SaveOptions удалено**
Свойство Workbook.SaveOptions было объявлено устаревшим некоторое время назад. В этом релизе оно было полностью удалено из общего API, поэтому рекомендуется использовать методы Workbook.Save(Stream, SaveOptions) или Workbook.Save(string, SaveOptions) в качестве альтернативы.

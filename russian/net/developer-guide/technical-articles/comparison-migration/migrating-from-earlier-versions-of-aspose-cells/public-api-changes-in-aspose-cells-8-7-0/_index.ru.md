---
title: Общедоступный API Изменения в Aspose.Cells 8.7.0
type: docs
weight: 230
url: /ru/net/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.6.3 до 8.7.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка цифровой подписи, обнаружения и извлечения проектов VBA**
В этом выпуске Aspose.Cells for .NET представлены некоторые новые свойства и методы, помогающие пользователям выполнять такие задачи, как цифровая подпись проекта VBA, определение того, подписан и действителен ли проект VBA. Более того, новый API позволяет извлекать сертификат в виде необработанных данных из проекта VBA с цифровой подписью в Workbook.
###### **Цифровая подпись проекта VBA**
 Aspose.Cells for .NET 8.7.0 предоставил метод VbaProject.Sign, который можно использовать для[цифровая подпись проекта VBA в рабочей книге](/cells/ru/net/digitally-sign-a-vba-code-project-with-certificate/). Указанный метод принимает экземпляр класса DigitalSignature, который находится в пространстве имен Aspose.Cells.DigitalSignatures.

Ниже приведен простой сценарий использования.

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


###### **Обнаружение проекта VBA с цифровой подписью**
 Новое открытое свойство VbaProject.IsSigned можно использовать для[определить, имеет ли проект VBA в рабочей книге цифровую подпись](/cells/ru/net/check-if-vba-code-is-signed/). Свойство VbaProject.IsSigned имеет логический тип и возвращает значение true, если проект VBA имеет цифровую подпись, и наоборот.

Ниже приведен простой сценарий использования.

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


###### **Извлечение цифровой подписи из проекта VBA**
Эта версия API также предоставляет свойство VbaProject.CertRawData, которое позволяет[извлечь необработанные данные цифрового сертификата из проекта VBA](/cells/ru/net/export-vba-certificate-to-file-or-stream/). Свойство VbaProject.CertRawData имеет тип массива байтов, который будет содержать необработанные данные сертификата, если проект VBA имеет цифровую подпись, в противном случае указанное свойство будет иметь значение null.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **Проверка цифровой подписи проекта VBA**
 Другим дополнением к общедоступному API является свойство VbaProject.IsValidSigned, которое может быть полезно в[проверка цифровой подписи проекта VBA](/cells/ru/net/check-if-digital-signature-of-vba-code-is-valid/). Указанное свойство возвращает true, если цифровая подпись действительна, и false, если подпись недействительна.

Ниже приведен простой сценарий использования.

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


### **Добавлен метод Protection.VerifyPassword**
 Aspose.Cells for .NET 8.7.0 предоставил метод Protection.VerifyPassword, который можно использовать для[проверьте пароль, используемый для защиты рабочего листа](/cells/ru/net/verify-password-used-to-protect-the-worksheet/)Этот метод принимает экземпляр строки в качестве параметра и возвращает true, если указанный пароль совпадает с паролем, используемым для защиты рабочего листа.

Ниже приведен простой сценарий использования.

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


### **Добавлено свойство Protection.IsProtectedWithPassword.**
 В этом выпуске Aspose.Cells for .NET API также раскрыто свойство Protection.IsProtectedWithPassword, которое может быть полезно в[определение, защищен ли рабочий лист паролем или нет](/cells/ru/net/detect-if-worksheet-is-password-protected/).

Ниже приведен простой сценарий использования.

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


### **Добавлено свойство ColorScale.Is3ColorScale**
 Aspose.Cells for .NET 8.7.0 предоставило свойство ColorScale.Is3ColorScale, которое можно использовать для создания условного формата 2-Color Scale. Упомянутое свойство имеет тип Boolean со значением по умолчанию true, что означает, что условный формат по умолчанию будет иметь 3-цветную шкалу. Однако при изменении свойства ColorScale.Is3ColorScale на false[создать условный формат 2-цветной шкалы](/cells/ru/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

Ниже приведен простой сценарий использования.

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


### **Добавлено свойство TxtLoadOptions.HasFormula**
 Aspose.Cells for .NET 8.7.0 предоставил поддержку[идентифицировать и анализировать формулы при загрузке файлов CSV/TXT, содержащих простые данные с разделителями](/cells/ru/net/load-or-import-csv-file-with-formulas/). Недавно открытое свойство TxtLoadOptions.HasFormula, если для него задано значение true, указывает API анализировать формулы из входного файла с разделителями и устанавливать их в соответствующие ячейки без дополнительной обработки.

Ниже приведен простой сценарий использования.

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


### **Добавлено свойство DataLabels.IsResizeShapeToFitText**
 Еще одна полезная функция, представленная в версии Aspose.Cells for .NET 8.7.0, — это свойство DataLabels.IsResizeShapeToFitText, которое позволяет[Изменение размера фигуры в соответствии с текстом](/cells/ru/net/resize-chart-s-data-label-shape-to-fit-text/)функция приложения Excel для меток данных диаграммы.

Ниже приведен простой сценарий использования.

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


### **Добавлено свойство PdfSaveOptions.OptimizationType.**
Aspose.Cells for .NET 8.7.0 предоставило свойство PdfSaveOptions.OptimizationType вместе с перечислением PdfOptimizationType, чтобы облегчить пользователям[выбрать нужный алгоритм оптимизации при экспорте таблиц в формат PDF](/cells/ru/net/save-excel-into-pdf-with-standard-or-minimum-size/). Существует 2 возможных значения свойства PdfSaveOptions.OptimizationType, как описано ниже.

1. PdfOptimizationType.MinimumSize: Качество скомпрометировано из-за результирующего размера файла.
1. PdfOptimizationType.Standard: качество не страдает, поэтому результирующий размер файла будет большим.

Ниже приведен простой сценарий использования.

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
## **Удаленные API**
### **Свойство Workbook.SaveOptions удалено**
Некоторое время назад свойство Workbook.SaveOptions было помечено как устаревшее. В этом выпуске он был полностью удален из общедоступного API, поэтому в качестве альтернативы рекомендуется использовать метод Workbook.Save(Stream, SaveOptions) или Workbook.Save(string, SaveOptions).

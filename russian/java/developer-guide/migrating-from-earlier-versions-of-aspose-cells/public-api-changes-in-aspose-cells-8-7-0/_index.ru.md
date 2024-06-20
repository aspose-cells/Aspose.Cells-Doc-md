---
title: Изменения в публичном API в Aspose.Cells 8.7.0
type: docs
weight: 240
url: /ru/java/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.6.3 до 8.7.0, которые могут быть интересны разработчикам модулей/приложений. Он включает в себя не только новые и обновленные публичные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка оптимизации PDF**
API Aspose.Cells уже предоставляет возможность преобразования электронных таблиц в PDF. С этим выпуском API пользователи теперь могут [оптимизировать размер результирующего PDF](/cells/ru/java/save-excel-into-pdf-with-standard-or-minimum-size/) также. Aspose.Cells for Java 8.7.0 предоставил свойство PdfSaveOptions.OptimizationType вместе с перечислением PdfOptimizationType, чтобы облегчить выбор пользователей желаемого алгоритма оптимизации при экспорте электронных таблиц в формат PDF. Есть 2 возможных значения для свойства PdfSaveOptions.OptimizationType, как описано ниже. 

1. PdfOptimizationType.MINIMUM_SIZE: Качество компрометируется ради размера файла.
1. PdfOptimizationType.STANDARD: Качество не моменты, поэтому размер файла будет большим.

Вот простой сценарий использования.

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
### **Обнаружение цифровой подписи в проекте VBA**
Новое свойство VbaProject.isSigned теперь можно использовать для [определения, является ли проект VBA в книге электронных таблиц цифрово подписанным](/cells/ru/java/check-if-vba-code-is-signed/). Свойство VbaProject.isSigned имеет тип Boolean, которое возвращает true, если проект VBA цифрово подписан, и vice versa.

Вот простой сценарий использования.

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
### **Добавлен метод Protection.verifyPassword**
API Aspose.Cells улучшило класс Protection, введя метод verifyPassword, который позволяет указать пароль в виде строки и [проверяет, использовался ли такой же пароль для защиты Листа](/cells/ru/java/verify-password-used-to-protect-the-worksheet/). Метод Protection.verifyPassword возвращает true, если указанный пароль совпадает с паролем, используемым для защиты заданного листа, и false, если указанный пароль не совпадает. Ниже приведен фрагмент кода, использующий метод Protection.verifyPassword совместно с полем Protection.isProtectedWithPassword для обнаружения защиты паролем и проверки пароля.

Вот простой сценарий использования.

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
### **Добавлено свойство Protection.isProtectedWithPassword**
В этом выпуске Aspose.Cells for Java также было представлено поле Protection.isProtectedWithPassword, которое может быть полезно при [определении, защищен ли Лист паролем или нет](/cells/ru/java/detect-if-worksheet-is-password-protected/).

Вот простой сценарий использования.

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
### **Добавлено свойство ColorScale.Is3ColorScale**
Aspose.Cells for Java 8.7.0 предоставил свойство ColorScale.Is3ColorScale, которое можно использовать для [создания условного форматирования с масштабом 2 цвета](/cells/ru/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/). Указанное свойство имеет тип Boolean со значением по умолчанию true, что означает, что условное форматирование будет представлено как 3-цветное масштабирование по умолчанию. Однако переключение свойства ColorScale.Is3ColorScale на false сгенерирует условное форматирование с масштабом 2 цвета.

Вот простой сценарий использования.

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
### **Добавлено свойство TxtLoadOptions.HasFormula**
Aspose.Cells for Java 8.7.0 добавил поддержку [идентификации и анализа формул при загрузке CSV/TXT файлов с данными в виде разделенных данных](/cells/ru/java/load-or-import-csv-file-with-formulas/). Новое свойство TxtLoadOptions.HasFormula теперь позволяет API анализировать формулы из входного файла с данными и устанавливать их для соответствующих ячеек без дополнительной обработки.

Вот простой сценарий использования.

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
### **Добавлено свойство DataLabels.ResizeShapeToFitText**
Еще одна полезная функция, представленная в Aspose.Cells for Java 8.7.0, - это свойство DataLabels.ResizeShapeToFitText, которое позволяет включить функцию [изменения размера формы под текст](/cells/ru/java/resize-chart-s-data-label-shape-to-fit-text/) для меток данных диаграммы Excel.

Вот простой сценарий использования.

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
## **Удалены API**
### **Удалено свойство Workbook.SaveOptions**
Свойство Workbook.SaveOptions было объявлено устаревшим некоторое время назад. В этом релизе оно было полностью удалено из общедоступного API, поэтому рекомендуется использовать метод Workbook.save(Stream, SaveOptions) или Workbook.save(string, SaveOptions) в качестве альтернативы.

---
title: Общедоступный API Изменения в Aspose.Cells 8.7.0
type: docs
weight: 240
url: /ru/java/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.6.3 до 8.7.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка оптимизации PDF**
 Aspose.Cells API уже предоставляют функцию преобразования электронных таблиц в PDF. В этом выпуске API пользователи теперь могут[оптимизировать результирующий размер PDF](/cells/ru/java/save-excel-into-pdf-with-standard-or-minimum-size/)также. Aspose.Cells for Java 8.7.0 предоставило свойство PdfSaveOptions.OptimizationType вместе с перечислением PdfOptimizationType, чтобы облегчить пользователям выбор желаемого алгоритма оптимизации при экспорте электронных таблиц в формат PDF. Существует 2 возможных значения свойства PdfSaveOptions.OptimizationType, как описано ниже.

1. PdfOptimizationType.MINIMUM_SIZE: Качество скомпрометировано из-за результирующего размера файла.
1. PdfOptimizationType.STANDARD: качество не страдает, поэтому результирующий размер файла будет большим.

Ниже приведен простой сценарий использования.

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
### **Обнаружение проекта VBA с цифровой подписью**
 Новое открытое свойство VbaProject.isSigned можно использовать для[определить, имеет ли проект VBA в рабочей книге цифровую подпись](/cells/ru/java/check-if-vba-code-is-signed/). Свойство VbaProject.isSigned имеет логический тип и возвращает значение true, если проект VBA имеет цифровую подпись, и наоборот.

Ниже приведен простой сценарий использования.

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
### **Добавлен метод Protection.verifyPassword**
Aspose.Cells API-интерфейсы улучшили класс Protection, предоставив метод verifyPassword, который позволяет указать пароль как экземпляр String и[проверяет, использовался ли тот же пароль для защиты рабочего листа](/cells/ru/java/verify-password-used-to-protect-the-worksheet/). Метод Protection.verifyPassword возвращает значение true, если указанный пароль совпадает с паролем, используемым для защиты данного рабочего листа, и значение false, если указанный пароль не совпадает. Следующий фрагмент кода использует метод Protection.verifyPassword в сочетании с полем Protection.isProtectedWithPassword для обнаружения защиты паролем и проверки пароля.

Ниже приведен простой сценарий использования.

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
### **Добавлено свойство Protection.isProtectedWithPassword**
 В этом выпуске Aspose.Cells for Java также представлено поле Protection.isProtectedWithPassword, которое может быть полезно в[определение, защищен ли рабочий лист паролем или нет](/cells/ru/java/detect-if-worksheet-is-password-protected/).

Ниже приведен простой сценарий использования.

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
### **Добавлено свойство ColorScale.Is3ColorScale**
 Aspose.Cells for Java 8.7.0 предоставило свойство ColorScale.Is3ColorScale, которое можно использовать для[создать условный формат двухцветной шкалы](/cells/ru/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/). Упомянутое свойство имеет тип Boolean со значением по умолчанию true, что означает, что условный формат по умолчанию будет иметь 3-цветную шкалу. Однако при переключении свойства ColorScale.Is3ColorScale на false будет создан условный формат двухцветной шкалы.

Ниже приведен простой сценарий использования.

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
### **Добавлено свойство TxtLoadOptions.HasFormula**
 Aspose.Cells for Java 8.7.0 предоставил поддержку[определять и анализировать формулы при загрузке файлов CSV/TXT, содержащих простые данные с разделителями](/cells/ru/java/load-or-import-csv-file-with-formulas/). Недавно открытое свойство TxtLoadOptions.HasFormula, если для него задано значение true, указывает API анализировать формулы из входного файла с разделителями и устанавливать их в соответствующие ячейки без дополнительной обработки.

Ниже приведен простой сценарий использования.

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
### **Добавлено свойство DataLabels.ResizeShapeToFitText.**
 Еще одна полезная функция, представленная в версии Aspose.Cells for Java 8.7.0, — это свойство DataLabels.ResizeShapeToFitText, которое позволяет[изменить размер фигуры, чтобы она соответствовала тексту](/cells/ru/java/resize-chart-s-data-label-shape-to-fit-text/) функция приложения Excel для меток данных диаграммы.

Ниже приведен простой сценарий использования.

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
## **Удаленные API**
### **Свойство Workbook.SaveOptions удалено**
Некоторое время назад свойство Workbook.SaveOptions было помечено как устаревшее. В этом выпуске он был полностью удален из общедоступного API, поэтому в качестве альтернативы рекомендуется использовать метод Workbook.save(Stream, SaveOptions) или Workbook.save(string, SaveOptions).

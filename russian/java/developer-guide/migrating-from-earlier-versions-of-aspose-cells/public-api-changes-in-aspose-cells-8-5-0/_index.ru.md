---
title: Изменения общего API в Aspose.Cells 8.5.0
type: docs
weight: 170
url: /ru/java/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.4.2 до 8.5.0, которые могут быть интересны разработчикам модулей/приложений. В нем содержатся не только новые и обновленные общедоступные методы, [добавленные классы и т.д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-5-0/), но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Изменены параметры метода CalculateCustomFunction интерфейса ICustomFunction**
Если один параметр для пользовательской функции является ссылкой на ячейку, в старых версиях API Aspose.Cells использовался для преобразования ссылки на ячейку в одно значение ячейки или массив объектов всех значений ячеек в указанной области. Однако для многих функций и пользователей массив значений ячеек для всех ячеек в указанной области не требуется, им нужна только одна ячейка, соответствующая позиции формулы, или просто сама ссылка вместо значения ячейки или массива значений. В некоторых случаях получение всех значений ячеек даже увеличивало риск возникновения ошибки циклической ссылки.

Для поддержки такого вида требований Aspose.Cells for Java 8.5.0 изменил значение параметра на "paramsList" для указанной области. С версии v8.5.0 API просто помещает объект ReferredArea в "paramsList", когда соответствующий параметр является ссылкой или его рассчитанный результат является ссылкой. Если вам нужна сама ссылка, то вы можете использовать ReferredArea напрямую. Если вам нужно получить одно значение ячейки из ссылки, соответствующее положению формулы, то вы можете использовать метод ReferredArea.getValue(rowOffset, int colOffset). Если вам нужен массив значений ячеек для всей области, то вы можете использовать метод ReferredArea.getValues.

Теперь после Aspose.Cells for Java 8.5.0, когда параметр "paramsList" предоставляет ReferredArea, ReferredAreaCollection в "contextObjects" больше не понадобится (в старых версиях он не всегда мог обеспечивать однозначное отображение на параметры пользовательской функции), поэтому в данном выпуске он также удален из "contextObjects".

Это изменение требует небольших изменений в коде реализации ICustomFunction, когда вам нужно значение/значения ссылочного параметра.

**Старая реализация**

{{< highlight csharp >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}

**Новая реализация**

{{< highlight csharp >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}
### **Добавлен класс CalculationOptions**
Aspose.Cells for Java 8.5.0 предоставил класс CalculationOptions для добавления большей гибкости и расширяемости для движка расчета формул. Новый добавленный класс имеет следующие свойства. 

1. CalculationOptions.CalcStackSize: Указывает размер стека для рекурсивного вычисления ячеек. -1 указывает, что вычисление будет использовать WorkbookSettings.CalcStackSize соответствующей книги.
1. CalculationOptions.CustomFunction: Расширяет движок расчета формул с помощью пользовательских функций.
1. CalculationOptions.IgnoreError: Значение типа Boolean указывает, следует ли скрывать ошибки при вычислении формул, где ошибки могут быть вызваны неподдерживаемой функцией, внешней ссылкой или другими причинами.
1. CalculationOptions.PrecisionStrategy: Значение типа CalculationPrecisionStrategy, которое указывает стратегию обработки точности расчета.
### **Перечисление CalculationPrecisionStrategy добавлено**
Aspose.Cells for Java 8.5.0 предоставил перечисление CalculationPrecisionStrategy для добавления большей гибкости к движку расчета формул для получения желаемых результатов. Это перечисление стратегий обработки точности расчета. Из-за вопросов точности арифметики с плавающей запятой IEEE 754, некоторые, казалось бы, простые формулы могут не давать ожидаемых результатов, поэтому последняя сборка API предоставила следующие поля для получения желаемых результатов в соответствии с выбором.

1. CalculationPrecisionStrategy.DECIMAL: Использует десятичные разряды там, где это возможно, и является наименее эффективной с точки зрения производительности.
1. CalculationPrecisionStrategy.ROUND: Округляет результаты вычислений в соответствии с значащей цифрой.
1. CalculationPrecisionStrategy.NONE: Никакая стратегия не применяется, поэтому во время расчета движок использует исходное значение double в качестве операнда и возвращает результат напрямую. Этот вариант наиболее эффективен и применим для большинства случаев.
### **Добавлены методы для использования CalculationOptions**
С выпуском v8.5.0 Aspose.Cells API добавил версии перегрузки метода calculateFormula, перечисленные ниже.

- Workbook.calculateFormula(CalculationOptions)
- Worksheet.calculateFormula(CalculationOptions options, bool recursive)
- Cell.calculate(CalculationOptions)
### **Добавлено перечисление Field PasteType.ROW_HEIGHTS**
API Aspose.Cells предоставляет перечисление PasteType.ROW_HEIGHTS для копирования высот строк при копировании диапазонов. При установке свойства PasteOptions.PasteType в ((PasteType.ROW_HEIGHTS}} высоты всех строк внутри исходного диапазона будут скопированы в целевой диапазон.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.getWorksheets().get(0);

//Add destination worksheet

Worksheet dstSheet = workbook.getWorksheets().add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.getCells().setRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.getCells().createRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.getCells().createRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.setPasteType(PasteType.ROW_HEIGHTS);

//Copy source range to destination range with paste options

dstRange.copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.save("output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Добавлено свойство SheetRender.PageScale**
Когда вы устанавливаете масштабирование настройки страницы, используя опцию **Fit to n page(s) wide by m tall**, Microsoft Excel вычисляет коэффициент масштабирования настройки страницы. То же самое можно достичь, используя свойство SheetRender.PageScale, предоставленное Aspose.Cells for Java 8.5.0. Это свойство возвращает значение типа double, которое можно преобразовать в процентное значение. Например, если оно возвращает 0,507968245, то это означает, что коэффициент масштабирования составляет 51%.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some data in these cells

worksheet.getCells().get("A4").putValue("Test");

worksheet.getCells().get("S4").putValue("Test");

//Set paper size

worksheet.getPageSetup().setPaperSize(PaperSizeType.PAPER_A_4);

//Set fit to pages wide as 1

worksheet.getPageSetup().setFitToPagesWide(1);

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Write the page scale value

System.out.println(sr.getPageScale());

{{< /highlight >}}
### **Добавлено перечисление CellValueFormatStrategy**
Aspose.Cells for Java 8.5.0 добавил новую перечисление CellValueFormatStrategy для обработки ситуаций, когда значения ячеек должны быть извлечены с применением форматирования или без него. Перечисление CellValueFormatStrategy имеет следующие поля. 

1. CellValueFormatStrategy.CELL_STYLE: Только с форматированием с оригинальным форматом ячейки.
1. CellValueFormatStrategy.DISPLAY_STYLE: С форматированием отображаемого стиля ячейки.
1. CellValueFormatStrategy.NONE: Без форматирования.
### **Добавлен метод Cell.getStringValue**
Для использования перечисления CellValueFormatStrategy v8.5.0 раскрыл метод Cell.getStringValue, который может принимать параметр типа CellValueFormatStrategy и возвращать значение в зависимости от указанной опции.

Далее приведен фрагмент кода, показывающий, как использовать новый метод Cells.getStringValue.

**Java**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell A1

Cell cell = worksheet.getCells().get("A1");

//Put value inside the cell

cell.putValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.getStyle();

style.setNumber(2);

cell.setStyle(style);

//Get string value as Cell Style

String value = cell.getStringValue(CellValueFormatStrategy.CELL_STYLE);

System.out.println(value);

//Get string value without any formatting

value = cell.getStringValue(CellValueFormatStrategy.NONE);

System.out.println(value);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

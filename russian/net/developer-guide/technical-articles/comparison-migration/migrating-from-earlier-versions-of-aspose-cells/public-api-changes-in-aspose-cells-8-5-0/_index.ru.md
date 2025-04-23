---
title: Изменения общего API в Aspose.Cells 8.5.0
type: docs
weight: 160
url: /ru/net/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

В этом документе описаны изменения в API Aspose.Cells с версии 8.4.2 по 8.5.0, которые могут быть интересны для разработчиков модулей/приложений. Он включает не только новые и обновленные общедоступные методы, [добавленные классы и т. д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-5-0/), но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Изменены параметры метода CalculateCustomFunction интерфейса ICustomFunction**
Если один параметр для пользовательской функции является ссылкой на ячейку, в старых версиях API Aspose.Cells использовался для преобразования ссылки на ячейку в одно значение ячейки или массив объектов всех значений ячеек в указанной области. Однако для многих функций и пользователей массив значений ячеек для всех ячеек в указанной области не требуется, им нужна только одна ячейка, соответствующая позиции формулы, или просто сама ссылка вместо значения ячейки или массива значений. В некоторых случаях получение всех значений ячеек даже увеличивало риск возникновения ошибки циклической ссылки.

Для поддержки такого рода требований Aspose.Cells for .NET 8.5.0 изменил значение параметра на "paramsList" для указанной области. С версии v8.5.0 API просто помещает объект ReferredArea в "paramsList", когда соответствующий параметр является ссылкой или его вычисленный результат является ссылкой. Если вам нужна сама ссылка, то вы можете использовать ReferredArea напрямую. Если вам нужно получить одно значение ячейки из ссылки, соответствующей позиции формулы, вы можете использовать метод ReferredArea.GetValue(rowOffset, colOffset). Если вам нужен массив значений ячеек для всей области, то вы можете использовать метод ReferredArea.GetValues.

Теперь, поскольку Aspose.Cells for .NET 8.5.0 предоставляет ReferredArea в "paramsList", ReferredAreaCollection в "contextObjects" больше не понадобится (в старых версиях он не всегда мог дать однозначное соответствие параметрам пользовательской функции), поэтому в этом выпуске он также был удален из "contextObjects".

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

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

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
Aspose.Cells for .NET 8.5.0 добавил класс CalculationOptions для обеспечения более гибкой и расширяемой работы с движком расчета формул. Вновь добавленный класс имеет следующие свойства.

1. CalculationOptions.CalcStackSize: Указывает размер стека для рекурсивного вычисления ячеек. -1 указывает, что вычисление будет использовать WorkbookSettings.CalcStackSize соответствующей книги.
1. CalculationOptions.CustomFunction: Расширяет движок расчета формул с помощью пользовательских функций.
1. CalculationOptions.IgnoreError: Значение типа Boolean указывает, следует ли скрывать ошибки при вычислении формул, где ошибки могут быть вызваны неподдерживаемой функцией, внешней ссылкой или другими причинами.
1. CalculationOptions.PrecisionStrategy: Значение типа CalculationPrecisionStrategy, которое указывает стратегию обработки точности расчета.
### **Перечисление CalculationPrecisionStrategy добавлено**
Aspose.Cells for .NET 8.5.0 добавил перечисление CalculationPrecisionStrategy для более гибкого управления движком расчета формул для получения желаемых результатов. Это перечисление стратегий обработки точности расчета. Из-за проблем точности в арифметике с плавающей запятой IEEE 754 некоторые кажущиеся простыми формулы могут не давать ожидаемых результатов, поэтому в новой версии API были добавлены следующие поля для получения желаемых результатов в соответствии с выбором.

1. CalculationPrecisionStrategy.Decimal: Использует десятичное точное число в тех случаях, когда это возможно, и является наиболее неэффективным с точки зрения производительности.
1. CalculationPrecisionStrategy.Round: Округляет результаты расчета в соответствии с значащей цифрой.
1. CalculationPrecisionStrategy.None: Никакая стратегия не применяется, поэтому в процессе расчета движок использует исходное значение с плавающей запятой и возвращает результат непосредственно. Этот вариант наиболее эффективен и применим к большинству случаев.
### **Добавлены методы для использования CalculationOptions**
С релизом v8.5.0 API Aspose.Cells добавил перегруженные версии метода CalculateFormula, перечисленные ниже.

- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula(CalculationOptions options, bool recursive)
- Cell.Calculate(CalculationOptions)
### **Добавлено перечисление PasteType.RowHeights**
API Aspose.Cells предоставляет перечисление PasteType.RowHeights для копирования высот строк при копировании диапазонов. При установке свойства PasteOptions.PasteType в PasteType.RowHeights высоты всех строк внутри исходного диапазона будут скопированы в целевой диапазон.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.Worksheets[0];

//Add destination worksheet

Worksheet dstSheet = workbook.Worksheets.Add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.Cells.SetRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.Cells.CreateRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.Cells.CreateRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.PasteType = PasteType.RowHeights;

//Copy source range to destination range with paste options

dstRange.Copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.Cells["D4"].PutValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.Save("output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **Добавлено свойство SheetRender.PageScale**
При установке масштабирования настройки страницы с использованием опции **По количеству страниц по ширине и высоте n** Microsoft Excel вычисляет коэффициент масштабирования настройки страниц. То же самое можно сделать с помощью свойства SheetRender.PageScale, предоставленного Aspose.Cells for .NET 8.5.0. Это свойство возвращает значение double, которое можно преобразовать в процентное значение. Например, если оно возвращает 0.507968245, это означает, что коэффициент масштабирования составляет 51%.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some data in these cells

worksheet.Cells["A4"].PutValue("Test");

worksheet.Cells["S4"].PutValue("Test");

//Set paper size

worksheet.PageSetup.PaperSize = PaperSizeType.PaperA4;

//Set fit to pages wide as 1

worksheet.PageSetup.FitToPagesWide = 1;

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Convert page scale double value to percentage

string strPageScale = sr.PageScale.ToString("0%");

//Write the page scale value

Console.WriteLine(strPageScale);

{{< /highlight >}}


### **Добавлено перечисление CellValueFormatStrategy**
В Aspose.Cells for .NET 8.5.0 добавлено новое перечисление CellValueFormatStrategy для обработки ситуаций, когда значения ячеек должны быть извлечены с использованием форматирования или без него. Перечисление CellValueFormatStrategy имеет следующие поля.

Добавлен метод Cell.GetStingValue
Чтобы использовать перечисление CellValueFormatStrategy, v8.5.0 предоставил метод Cell.GetStingValue, который может принимать параметр типа CellValueFormatStrategy и возвращать значение в зависимости от указанной опции.
Приведен фрагмент кода, показывающий, как использовать вновь предоставленный метод Cells.GetStingValue.
### **Добавлен метод Cell.GetStingValue**
Для использования перечисления CellValueFormatStrategy v8.5.0 предоставил метод Cell.GetStingValue, который может принимать параметр типа CellValueFormatStrategy и возвращать значение в зависимости от указанной опции.

Добавлено свойство ExportTableOptions.FormatStrategy

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Get string value as Cell Style

string value = cell.GetStingValue(CellValueFormatStrategy.CellStyle);

Console.WriteLine(value);

//Get string value without any formatting

value = cell.GetStingValue(CellValueFormatStrategy.None);

Console.WriteLine(value);

{{< /highlight >}}


### **Aspose.Cells for .NET 8.5.0 предоставил свойство ExportTableOptions.FormatStrategy для пользователей, которые хотят экспортировать данные в DataTable с форматированием или без него. Это свойство использует перечисление CellValueFormatStrategy и экспортирует данные в соответствии с указанной опцией.**
Aspose.Cells for .NET 8.5.0 предоставил свойство ExportTableOptions.FormatStrategy для пользователей, которые хотят экспортировать данные в DataTable с форматированием или без. Это свойство использует перечисление CellValueFormatStrategy и экспортирует данные в соответствии с указанной опцией.

Приведен код, поясняющий использование свойства ExportTableOptions.FormatStrategy.

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Print the cell values as it displays in excel

Console.WriteLine("Cell String Value: " + cell.StringValue);

//Print the cell value without any format

Console.WriteLine("Cell String Value without Format: " + cell.StringValueWithoutFormat);

//Export Data Table Options with FormatStrategy as CellStyle

ExportTableOptions opts = new ExportTableOptions();

opts.ExportAsString = true;

opts.FormatStrategy = CellValueFormatStrategy.CellStyle;

//Export Data Table

DataTable dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as Cell Style: " + dt.Rows[0][0].ToString());

//Export Data Table Options with FormatStrategy as None

opts.FormatStrategy = CellValueFormatStrategy.None;

dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as None: " + dt.Rows[0][0].ToString());

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

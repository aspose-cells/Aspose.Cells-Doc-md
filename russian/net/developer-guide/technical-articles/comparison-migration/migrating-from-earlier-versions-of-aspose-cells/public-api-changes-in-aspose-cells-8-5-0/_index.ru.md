---
title: Общедоступный API Изменения в Aspose.Cells 8.5.0
type: docs
weight: 160
url: /ru/net/public-api-changes-in-aspose-cells-8-5-0/
---
{{% alert color="primary" %}} 

 В этом документе описаны изменения в Aspose.Cells API с версии 8.4.2 до 8.5.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы,[добавлены классы и т.д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-5-0/), но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Изменены параметры ICustomFunction.CalculateCustomFunction.**
Если одним параметром пользовательской функции является ссылка на ячейку, в старой версии Aspose.Cells API-интерфейсы использовались для преобразования ссылки на ячейку в одно значение ячейки или массив объектов всех значений ячеек в указанной области. Однако для многих функций и пользователей массив значений ячеек для всех ячеек в указанной области не требуется, им просто нужна одна отдельная ячейка, соответствующая положению формулы, или просто нужна сама ссылка вместо значения ячейки или массива значений. . В некоторых ситуациях извлечение всех значений ячеек даже увеличивало риск ошибки циклической ссылки.

Для поддержки такого рода требований Aspose.Cells for .NET 8.5.0 изменил значение параметра на «paramsList» для указанной области. Начиная с версии 8.5.0, API просто помещает объект ReferredArea в «paramsList», когда соответствующий параметр является ссылкой или его вычисленный результат является ссылкой. Если вам нужна сама ссылка, вы можете напрямую использовать ReferredArea. Если вам нужно получить одно значение ячейки из ссылки, соответствующей позиции формулы, вы можете использовать метод ReferredArea.GetValue(rowOffset, int colOffset). Если вам нужен массив значений ячеек для всей области, вы можете использовать метод ReferredArea.GetValues.

Теперь, когда Aspose.Cells for .NET 8.5.0 дает ReferredArea в «paramsList», ReferredAreaCollection в «contextObjects» больше не понадобится (в старых версиях он не мог всегда давать однозначное сопоставление с параметрами пользовательской функции), так что этот выпуск также удалил его из "contextObjects".

Это изменение требует немного изменений в коде реализации для ICustomFunction, когда вам нужно значение/значения ссылочного параметра.

**Старая реализация**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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


### **Добавлены параметры расчета класса**
Aspose.Cells for .NET 8.5.0 предоставил класс CalculationOptions, чтобы добавить больше гибкости и расширяемости для механизма расчета формул. Недавно добавленный класс имеет следующие свойства.

1. CalculationOptions.CalcStackSize: указан размер стека для рекурсивного вычисления ячеек. -1 указывает, что при вычислении будет использоваться WorkbookSettings.CalcStackSize соответствующей книги.
1. CalculationOptions.CustomFunction: расширяет механизм расчета формул с помощью пользовательской формулы.
1. CalculationOptions.IgnoreError: значение логического типа указывает, следует ли скрывать ошибки при расчете формул, где ошибки могут быть связаны с неподдерживаемой функцией, внешней ссылкой или чем-то еще.
1. CalculationOptions.PrecisionStrategy: значение типа CalculationPrecisionStrategy, указывающее стратегию обработки точности вычислений.
### **Добавлено перечисление CalculationPrecisionStrategy**
Aspose.Cells for .NET 8.5.0 предоставило перечисление CalculationPrecisionStrategy, чтобы добавить больше гибкости механизму вычисления формулы для получения желаемых результатов. Это перечисление определяет стратегию обработки точности вычислений. Из-за проблемы с точностью арифметики с плавающей запятой IEEE 754 некоторые, казалось бы, простые формулы не могут быть рассчитаны для получения ожидаемых результатов, поэтому в последней сборке API были представлены следующие поля для получения желаемых результатов в соответствии с выбором.

1. CalculationPrecisionStrategy.Decimal: по возможности использует десятичный операнд, что наиболее неэффективно с точки зрения производительности.
1. CalculationPrecisionStrategy.Round: результаты вычислений округляются в соответствии со значащей цифрой.
1. CalculationPrecisionStrategy.None: стратегия не применяется, поэтому во время вычисления механизм использует исходное двойное значение в качестве операнда и возвращает результат напрямую. Этот вариант наиболее эффективен и применим в большинстве случаев.
### **Добавлены методы для использования CalculationOptions**
С выпуском версии 8.5.0 в Aspose.Cells API добавлены перегруженные версии метода CalculateFormula, как указано ниже.

- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula (параметры CalculationOptions, логический рекурсивный)
- Cell.Рассчитать(Параметры расчета)
### **Добавлено поле перечисления PasteType.RowHeights**
Aspose.Cells API-интерфейсы предоставили поле перечисления PasteType.RowHeights для копирования высоты строк при копировании диапазонов. При установке для свойства PasteOptions.PasteType значения ((PasteType.RowHeights}} высота всех строк внутри исходного диапазона будет скопирована в целевой диапазон.

**C#**

{{< highlight "csharp" >}}

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
Когда вы устанавливаете Масштабирование параметров страницы с помощью**Вместить до n страниц в ширину и m в высоту** option, Microsoft Excel вычисляет коэффициент масштабирования параметров страницы. То же самое может быть достигнуто с помощью свойства SheetRender.PageScale, предоставленного Aspose.Cells for .NET 8.5.0. Это свойство возвращает двойное значение, которое можно преобразовать в процентное значение. Например, если он возвращает 0,507968245, это означает, что коэффициент масштабирования равен 51%.

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells for .NET 8.5.0 добавлено новое перечисление CellValueFormatStrategy для обработки ситуаций, когда значения ячеек должны быть извлечены с применением форматирования или без него. Перечисление CellValueFormatStrategy имеет следующие поля.

1. CellValueFormatStrategy.CellStyle: форматируется только в исходном формате ячейки.
1. CellValueFormatStrategy.DisplayStyle: форматируется в соответствии со стилем отображения ячейки.
1. CellValueFormatStrategy.None: не форматируется.
### **Метод Cell.GetStingValue добавлен**
Чтобы использовать перечисление CellValueFormatStrategy, версия 8.5.0 предоставила метод Cell.GetStingValue, который может принимать параметр типа CellValueFormatStrategy и возвращает значение, зависящее от указанной опции.

В следующем фрагменте кода показано, как использовать недавно открытый метод Cells.GetStingValue.

**C#**

{{< highlight "csharp" >}}

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


### **Добавлено свойство ExportTableOptions.FormatStrategy.**
Aspose.Cells for .NET 8.5.0 предоставляет свойство ExportTableOptions.FormatStrategy для пользователей, которые хотят экспортировать данные в DataTable с форматированием или без него. Это свойство использует перечисление CellValueFormatStrategy и экспортирует данные в соответствии с указанным параметром.

Следующий код объясняет использование свойства ExportTableOptions.FormatStrategy.

**C#**

{{< highlight "csharp" >}}

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

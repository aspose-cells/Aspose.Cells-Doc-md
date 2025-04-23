---
title: Изменения в общедоступном API в Aspose.Cells 8.9.1
type: docs
weight: 310
url: /ru/net/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.9.0 по 8.9.1, которые могут быть интересны для разработчиков модулей/приложений. Он включает не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Настройка источников шрифтов**
Aspose.Cells for .NET добавил несколько классов для поддержки настраиваемых источников шрифтов для отображения электронных таблиц. Вот список классов, которые были добавлены с Aspose.Cells for .NET 8.9.1.

1. Класс FontConfigs определяет настройки шрифтов.
1. Класс FontSourceBase является абстрактным базовым классом для классов, позволяющих пользователю указывать различные источники шрифтов.
1. Класс FileFontSource представляет собой одиночный файл шрифта TrueType, хранящийся в файловой системе.
1. Класс FolderFontSource представляет собой папку, содержащую файлы шрифтов TrueType.
1. Класс MemoryFontSource представляет собой одиночный файл шрифта TrueType, хранящийся в памяти.
1. Перечисление FontSourceType определяет тип источника шрифта.

С учетом вышеперечисленных изменений Aspose.Cells for .NET позволяет установить шрифты как описано ниже.

1. Установите одну пользовательскую папку шрифтов при использовании метода FontConfigs.SetFontFolder.
1. Установите несколько пользовательских папок шрифтов при использовании метода FontConfigs.SetFontFolders.
1. Установите источники шрифтов из пользовательской папки шрифтов, одного файла шрифта или данных шрифта из массива байтов при использовании метода FontConfigs.SetFontSources.

Вот пример простого сценария использования указанных выше методов.

**C#**

{{< highlight csharp >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[] { fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Both FontConfigs.SetFontFolder и FontConfigs.SetFontFolders методы принимают второй параметр типа Boolean. Передача true в качестве второго параметра направит API Aspose.Cells на поиск подпапок для файлов шрифтов.

{{% /alert %}} 

Aspose.Cells for .NET также позволяет настроить замену шрифтов. Этот механизм полезен, когда необходимый шрифт недоступен на машине, где должно происходить преобразование. Пользователи могут предоставить список названий шрифтов в качестве альтернативы оригинально необходимому шрифту. Для этого API Aspose.Cells предоставляют метод FontConfigs.SetFontSubstitutes, который принимает два параметра. Первый параметр имеет тип string и должен быть именем шрифта, который нужно заменить. Второй параметр - массив типа string. Пользователи могут предоставить список названий шрифтов в качестве замены оригинальному названию шрифта (указанному в первом параметре).

Вот пример простого сценария использования метода FontConfigs.SetFontSubstitutes.

**C#**

{{< highlight csharp >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[] { "Times New Roman", "Calibri" });

{{< /highlight >}}



Aspose.Cells for .NET также предоставляет средства для сбора информации о том, какие источники и замены были установлены.

1. Метод FontConfigs.GetFontSources возвращает массив типа FontSourceBase, содержащий список заданных источников шрифтов. В случае, если источники не были установлены, метод FontConfigs.GetFontSources вернет пустой массив.
1. Метод FontConfigs.GetFontSubstitutes принимает параметр типа string, позволяющий указать название шрифта, для которого установлена замена. В случае, если для указанного названия шрифта не установлена замена, метод FontConfigs.GetFontSubstitutes вернет null.

{{% alert color="primary" %}} 

Для получения дополнительной информации о FontConfigs, ознакомьтесь со статьей [Настройка шрифтов для рендеринга электронных таблиц](/cells/ru/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Добавлен интерфейс IFilePathProvider и свойство HtmlSaveOptions.FilePathProvider**
Aspose.Cells for .NET 8.9.1 позволяет получить/установить интерфейс IFilePathProvider для экспорта листов в отдельные файлы HTML. Эти новые API полезны в сценариях, где ссылки на листе указывают на местоположение на другом листе, а требование приложения - рендерить каждый лист в отдельный файл HTML. Реализация IFilePathProvider позволяет сохранять упомянутые ссылки целыми, независимо от того, указывают ли они на местоположение в отдельном файле HTML или нет.

Вот простой сценарий использования свойства HtmlSaveOptions.FilePathProvider.

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save each Worksheet to separate HTML file

for (int i = 0; i < book.Worksheets.Count; i++)

{

    book.Worksheets.ActiveSheetIndex = i;

    // Create an instance of HtmlSaveOptions & set FilePathProvider property

    var options = new HtmlSaveOptions

    {

        ExportActiveWorksheetOnly = true,

        FilePathProvider = new FilePathProvider()

    };

    // Write HTML file to disc

    book.Save(dir + string.Format(@"sheet{0}.html", i), options);

}

{{< /highlight >}}



Вот как реализовать интерфейс IFilePathProvider.

**C#**

{{< highlight csharp >}}

 public class FilePathProvider : IFilePathProvider

{

    public FilePathProvider()

    {

    }

    /// <summary>

    /// Gets the full path of the file by Worksheet name when exporting Worksheet to html separately.

    /// So the references among the Worksheets can be exported correctly.

    /// </summary>

    /// <param name="sheetName">Worksheet name</param>

    /// <returns>the full path of the file</returns>

    public string GetFullName(string sheetName)

    {

        if ("Sheet2".Equals(sheetName))

        {

            return "sheet1.html";

        }

        else if ("Sheet3".Equals(sheetName))

        {

            return "sheet2.html";

        }

        return "";

    }

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Для получения дополнительной информации об этом улучшении ознакомьтесь со статьей [Реализация интерфейса IFilePathProvider](/cells/ru/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Добавлено свойство CopyOptions.ReferToDestinationSheet и перегрузка для метода Cells.CopyRows.**
Aspose.Cells for .NET API предоставил свойство типа Boolean CopyOptions.ReferToDestinationSheet вместе с перегрузкой метода Cells.CopyRows, чтобы облегчить операцию копирования строк, когда строки для копирования также содержат диаграмму и ее источник данных. Разработчики могут использовать эти новые API для указания источника данных диаграммы для исходного или целевого листа.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet containing the chart & its data source

var source = book.Worksheets[0];

// Add a new worksheet to the collection

var destination = book.Worksheets[book.Worksheets.Add()];

// Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.ReferToDestinationSheet = true;

// Copy the rows

destination.Cells.CopyRows(source.Cells, 0, 0, source.Cells.MaxDisplayRange.RowCount, options);

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции, ознакомьтесь со статьей [Управление источником данных диаграммы при копировании строк](/cells/ru/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Добавлено свойство CalculationOptions.Recursive**
Aspose.Cells for .NET 8.9.1 предоставил свойство типа Boolean CalculationOptions.Recursive. Установка свойства CalculationOptions.Recursive в true и передача объекта в метод Workbook.CalculateFormula направляет API Aspose.Cells на рекурсивный расчет зависимых ячеек при вычислении ячеек, которые зависят от других ячеек.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции ознакомьтесь со статьей [Оптимизация времени расчета](/cells/ru/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Устаревшие API**
### **Свойство CellsHelper.FontDir устарело**
Рекомендуется использовать метод FontConfigs.SetFontFolder(string, bool) с рекурсивным параметром, установленным на false, вместо.
### **Свойство CellsHelper.FontDirs устарело**
Используйте метод FontConfigs.SetFontFolders(string[], bool) с рекурсивным параметром, установленным на false, вместо.
### **Свойство CellsHelper.FontFiles устарело**
Используйте метод FontConfigs.SetFontSources(FontSourceBase[]) вместо.
{{< app/cells/assistant language="csharp" >}}

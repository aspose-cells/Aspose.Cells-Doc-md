---
title: Общедоступный API Изменения в Aspose.Cells 8.9.1
type: docs
weight: 310
url: /ru/net/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.9.0 до 8.9.1, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Настраиваемые источники шрифтов**
Aspose.Cells for .NET предоставляет ряд классов для обеспечения поддержки настраиваемых источников шрифтов для рендеринга электронных таблиц. Вот список классов, которые были добавлены с Aspose.Cells for .NET 8.9.1.

1. Класс FontConfigs определяет параметры шрифта.
1. Класс FontSourceBase — это абстрактный базовый класс для классов, которые позволяют пользователю указывать различные источники шрифтов.
1. Класс FileFontSource представляет единственный файл шрифта TrueType, хранящийся в файловой системе.
1. Класс FolderFontSource представляет папку, содержащую файлы шрифтов TrueType.
1. Класс MemoryFontSource представляет один файл шрифта TrueType, хранящийся в памяти.
1. Перечисление FontSourceType указывает тип источника шрифта.

С учетом вышеупомянутых изменений Aspose.Cells for .NET позволяет устанавливать шрифты, как описано ниже.

1. Установите одну пользовательскую папку шрифтов при использовании метода FontConfigs.SetFontFolder.
1. Установите несколько пользовательских папок шрифтов при использовании метода FontConfigs.SetFontFolders.
1. Установите источники шрифтов из пользовательской папки шрифтов, одного файла шрифта или данных шрифта из массива байтов при использовании метода FontConfigs.SetFontSources.

Вот простой сценарий использования вышеупомянутых методов.

**C#**

{{< highlight "csharp" >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[]{ fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Оба метода FontConfigs.SetFontFolder и FontConfigs.SetFontFolders принимают второй параметр логического типа. Передача true в качестве второго параметра направит API Aspose.Cells на поиск файлов шрифтов во вложенных папках.

{{% /alert %}} 

Aspose.Cells for .NET также позволяет настроить замену шрифта. Этот механизм удобен, когда требуемый шрифт недоступен на машине, на которой должно выполняться преобразование. Пользователи могут предоставить список имен шрифтов в качестве альтернативы первоначально требуемому шрифту. Для этого API-интерфейсы Aspose.Cells предоставили метод FontConfigs.SetFontSubstitutes, который принимает 2 параметра. Первый параметр имеет тип string, который должен быть именем шрифта, который необходимо заменить. Второй параметр представляет собой массив строкового типа. Пользователи могут предоставить список имен шрифтов в качестве замены исходного имени шрифта (указывается в первом параметре).

Вот простой сценарий использования метода FontConfigs.SetFontSubstitutes.

**C#**

{{< highlight "csharp" >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}



Aspose.Cells for .NET также предоставил средства для сбора информации о том, какие источники и замены были установлены.

1. Метод FontConfigs.GetFontSources возвращает массив типа FontSourceBase, содержащий список указанных источников шрифтов. Если источники не заданы, метод FontConfigs.GetFontSources вернет пустой массив.
1. Метод FontConfigs.GetFontSubstitutes принимает параметр типа string, позволяющий указать имя шрифта, для которого установлена подстановка. Если для указанного имени шрифта не задана замена, метод FontConfigs.GetFontSubstitutes вернет значение null.

{{% alert color="primary" %}} 

 Для получения более подробной информации о FontConfigs, пожалуйста, ознакомьтесь со статьей на[Настройка шрифтов для визуализации электронных таблиц](/cells/ru/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Добавлен интерфейс IFilePathProvider и свойство HtmlSaveOptions.FilePathProvider.**
Aspose.Cells for .NET 8.9.1 позволяет получить/установить IFilePathProvider для экспорта листов в отдельные файлы HTML. Эти новые API-интерфейсы полезны в сценариях, где гиперссылки на одном рабочем листе указывают на местоположение на другом рабочем листе, где требованием приложения является преобразование каждого рабочего листа в отдельный файл HTML. Реализация IFilePathProvider позволяет сохранить вышеупомянутые гиперссылки нетронутыми независимо от того, что они указывают на место в отдельном результирующем файле HTML.

Ниже приведен простой сценарий использования свойства HtmlSaveOptions.FilePathProvider.

**C#**

{{< highlight "csharp" >}}

 // Загружаем электронную таблицу в экземпляр Workbook

var book = новая рабочая книга (dir + "sample.xlsx");

// Сохраняем каждый рабочий лист в отдельный файл HTML

 для (целое я = 0; я< book.Worksheets.Count; i++)

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

{{< highlight "csharp" >}}

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

 Дополнительные сведения об этом усовершенствовании см. в статье[Реализация интерфейса IFilePathProvider](/cells/ru/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Добавлено свойство CopyOptions.ReferToDestinationSheet и перегрузка для метода Cells.CopyRows.**
Aspose.Cells for .NET API предоставил свойство CopyOptions.ReferToDestinationSheet логического типа вместе с перегрузкой метода Cells.CopyRows, чтобы упростить операцию копирования строк, когда строки, которые нужно скопировать, также содержат диаграмму и ее источник данных. Разработчики могут использовать эти новые API-интерфейсы, чтобы указать источник данных диаграммы на исходный или целевой рабочий лист.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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

 Подробнее об этой функции читайте в статье[Управление источником данных диаграммы при копировании строк](/cells/ru/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Добавлено свойство CalculationOptions.Recursive.**
Aspose.Cells for .NET 8.9.1 предоставил свойство CalculationOptions.Recursive логического типа. Если задать для свойства CalculationOptions.Recursive значение true и передать объект методу Workbook.CalculateFormula, API-интерфейсы Aspose.Cells будут рекурсивно вычислять зависимые ячейки при вычислении ячеек, которые зависят от других ячеек.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 Подробнее об этой функции читайте в статье[Оптимизация времени расчета](/cells/ru/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Устаревшие API**
### **Устаревшее свойство CellsHelper.FontDir**
Вместо этого рекомендуется использовать метод FontConfigs.SetFontFolder(string, bool) с папкой, рекурсивной к false.
### **Устаревшее свойство CellsHelper.FontDirs**
Вместо этого используйте метод FontConfigs.SetFontFolders(string[], bool) с папкой, рекурсивной к false.
### **Устаревшее свойство CellsHelper.FontFiles**
Вместо этого используйте метод FontConfigs.SetFontSources(FontSourceBase[]).

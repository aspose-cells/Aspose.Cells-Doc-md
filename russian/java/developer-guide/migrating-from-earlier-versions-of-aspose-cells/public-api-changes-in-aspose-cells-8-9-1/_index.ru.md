---
title: Общедоступный API Изменения в Aspose.Cells 8.9.1
type: docs
weight: 320
url: /ru/java/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.9.0 до 8.9.1, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Настраиваемые источники шрифтов**
Aspose.Cells for Java предоставляет ряд классов для обеспечения поддержки настраиваемых источников шрифтов для рендеринга электронных таблиц. Вот список классов, которые были добавлены с Aspose.Cells for Java 8.9.1.

1. Класс FontConfigs определяет параметры шрифта.
1. Класс FontSourceBase — это абстрактный базовый класс для классов, которые позволяют пользователю указывать различные источники шрифтов.
1. Класс FileFontSource представляет единственный файл шрифта TrueType, хранящийся в файловой системе.
1. Класс FolderFontSource представляет папку, содержащую файлы шрифтов TrueType.
1. Класс MemoryFontSource представляет один файл шрифта TrueType, хранящийся в памяти.
1. Перечисление FontSourceType указывает тип источника шрифта.

С учетом вышеупомянутых изменений Aspose.Cells for Java позволяет устанавливать шрифты, как описано ниже.

1. Установите одну папку пользовательского шрифта при использовании метода FontConfigs.setFontFolder.
1. Установите несколько пользовательских папок шрифтов при использовании метода FontConfigs.setFontFolders.
1. Установите источники шрифтов из пользовательской папки шрифтов, одного файла шрифта или данных шрифта из массива байтов при использовании метода FontConfigs.setFontSources.

Вот простой сценарий использования вышеупомянутых методов.

**Java**

{{< highlight "csharp" >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[]{ fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[]bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

 Оба метода FontConfigs.setFontFolder и FontConfigs.setFontFolders принимают второй параметр логического типа. Передача true в качестве второго параметра направит API Aspose.Cells на поиск файлов шрифтов во вложенных папках.

{{% /alert %}} 

Aspose.Cells for Java также позволяет настроить замену шрифта. Этот механизм удобен, когда требуемый шрифт недоступен на машине, на которой должно выполняться преобразование. Пользователи могут предоставить список имен шрифтов в качестве альтернативы первоначально требуемому шрифту. Для этого API-интерфейсы Aspose.Cells предоставили метод FontConfigs.setFontSubstitutes, который принимает 2 параметра. Первый параметр имеет тип string, который должен быть именем шрифта, который необходимо заменить. Второй параметр представляет собой массив строкового типа. Пользователи могут предоставить список имен шрифтов в качестве замены исходного имени шрифта (указывается в первом параметре).

Вот простой сценарий использования метода FontConfigs.SetFontSubstitutes.

**Java**

{{< highlight "csharp" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

Aspose.Cells for Java также предоставил средства для сбора информации о том, какие источники и замены были установлены.

1. Метод FontConfigs.getFontSources возвращает массив типа FontSourceBase, содержащий список указанных источников шрифтов. Если источники не заданы, метод FontConfigs.getFontSources вернет пустой массив.
1. Метод FontConfigs.getFontSubstitutes принимает параметр типа string, позволяющий указать имя шрифта, для которого установлена подстановка. Если для указанного имени шрифта не задана замена, метод FontConfigs.getFontSubstitutes вернет значение null.

{{% alert color="primary" %}} 

 Для получения более подробной информации о FontConfigs, пожалуйста, ознакомьтесь со статьей на[Настройка шрифтов для визуализации электронных таблиц](/cells/ru/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Добавлен интерфейс IFilePathProvider и свойство HtmlSaveOptions.FilePathProvider.**
Aspose.Cells for Java 8.9.1 позволяет получить/установить IFilePathProvider для экспорта листов в отдельные файлы HTML. Эти новые API-интерфейсы полезны в сценариях, где гиперссылки на одном рабочем листе указывают на местоположение на другом рабочем листе, где требованием приложения является преобразование каждого рабочего листа в отдельный файл HTML. Реализация IFilePathProvider позволяет сохранить вышеупомянутые гиперссылки нетронутыми независимо от того, что они указывают на место в отдельном результирующем файле HTML.

Ниже приведен простой сценарий использования свойства HtmlSaveOptions.FilePathProvider.

**Java**

{{< highlight "csharp" >}}

 //Загружаем электронную таблицу в экземпляр Workbook

Книга рабочей книги = новая рабочая книга (каталог + "sample.xlsx");

// Сохраняем каждый рабочий лист в отдельный файл HTML

 для (целое я = 0; я< book.getWorksheets().getCount(); i++)

{

	book.getWorksheets().setActiveSheetIndex(i);

	//Create an instance of HtmlSaveOptions & set FilePathProvider property

	HtmlSaveOptions options = new HtmlSaveOptions();

	options.setExportActiveWorksheetOnly(true);

	options.setFilePathProvider(new IFilePathProvider() 

	{ 

		public String getFullName(String sheetName)

		{

		    if ("Sheet2".equals(sheetName))

		    {

		        return "sheet1.html";

		    }

		    else if ("Sheet3".equals(sheetName))

		    {

		        return "sheet2.html";

		    }



		    return "";

		}

	});



	 //Write HTML file to disc

	 book.save(dir + "sheet"+ i +".html", options);

}

{{< /highlight >}}

{{% alert color="primary" %}} 

 Дополнительные сведения об этом усовершенствовании см. в статье[Реализация интерфейса IFilePathProvider](/cells/ru/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Добавлено свойство CopyOptions.ReferToDestinationSheet и перегрузка для метода Cells.copyRows.**
Aspose.Cells for Java API предоставил свойство CopyOptions.ReferToDestinationSheet логического типа вместе с перегрузкой метода Cells.copyRows, чтобы упростить операцию копирования строк, когда копируемые строки также содержат диаграмму и ее источник данных. Разработчики могут использовать эти новые API-интерфейсы, чтобы указать источник данных диаграммы на исходный или целевой рабочий лист.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet containing the chart & its data source

Worksheet source = book.getWorksheets().get(0);

//Add a new worksheet to the collection

Worksheet destination = book.getWorksheets().get(book.getWorksheets().add());

//Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.setReferToDestinationSheet(true);

//Copy the rows

destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Подробнее об этой функции читайте в статье[Управление источником данных диаграммы при копировании строк](/cells/ru/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Добавлено свойство CalculationOptions.Recursive.**
Aspose.Cells for Java 8.9.1 предоставил свойство CalculationOptions.Recursive логического типа. Установка для свойства CalculationOptions.Recursive значения true и передача объекта в метод Workbook.calculateFormula указывает API Aspose.Cells на рекурсивное вычисление зависимых ячеек при вычислении ячеек, которые зависят от других ячеек.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 Подробнее об этой функции читайте в статье[Оптимизация времени расчета](/cells/ru/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Устаревшие API**
### **Устаревшее свойство CellsHelper.FontDir**
Вместо этого рекомендуется использовать метод FontConfigs.setFontFolder(String, boolean) с папкой, рекурсивной к false.
### **Устаревшее свойство CellsHelper.FontDirs**
Вместо этого используйте метод FontConfigs.setFontFolders(String[], boolean) с папкой, рекурсивной к false.
### **Устаревшее свойство CellsHelper.FontFiles**
Вместо этого используйте метод FontConfigs.setFontSources(FontSourceBase[]).

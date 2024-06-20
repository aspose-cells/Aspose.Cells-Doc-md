---
title: Изменения в общедоступном API в Aspose.Cells 8.9.1
type: docs
weight: 320
url: /ru/java/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.9.0 по 8.9.1, которые могут быть интересны для разработчиков модулей/приложений. Он включает не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Настройка источников шрифтов**
Aspose.Cells for Java предоставляет набор классов для настройки источников шрифтов при визуализации электронных таблиц. Вот список добавленных классов с версией Aspose.Cells for Java 8.9.1.

1. Класс FontConfigs определяет настройки шрифтов.
1. Класс FontSourceBase является абстрактным базовым классом для классов, позволяющих пользователю указывать различные источники шрифтов.
1. Класс FileFontSource представляет собой одиночный файл шрифта TrueType, хранящийся в файловой системе.
1. Класс FolderFontSource представляет собой папку, содержащую файлы шрифтов TrueType.
1. Класс MemoryFontSource представляет собой одиночный файл шрифта TrueType, хранящийся в памяти.
1. Перечисление FontSourceType определяет тип источника шрифта.

С упомянутыми выше изменениями в Aspose.Cells for Java можно устанавливать шрифты, подробности указаны ниже.

1. Установить одну пользовательскую папку шрифтов с помощью метода FontConfigs.setFontFolder.
1. Установить несколько пользовательских папок шрифтов с помощью метода FontConfigs.setFontFolders.
1. Установить источники шрифтов из пользовательской папки шрифтов, одиночного файла шрифта или данных шрифта из массива байтов с помощью метода FontConfigs.setFontSources.

Вот пример простого сценария использования указанных выше методов.

**Java**

{{< highlight csharp >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[] { fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[] bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Оба метода FontConfigs.setFontFolder и FontConfigs.setFontFolders принимают второй параметр логического типа. Передача true в качестве второго параметра направит API Aspose.Cells на поиск подпапок для файлов шрифтов. 

{{% /alert %}} 

Aspose.Cells for Java также позволяет конфигурировать подстановку шрифтов. Этот механизм полезен, когда требуемый шрифт недоступен на машине, где должно произойти преобразование. Пользователи могут предоставить список имен шрифтов в качестве альтернативы изначально требуемому шрифту. Для этого API Aspose.Cells предоставляет метод FontConfigs.setFontSubstitutes, который принимает 2 параметра. Первый параметр имеет тип string, которое должно быть именем шрифта, который требуется заменить. Второй параметр - массив типа string. Пользователи могут предоставить список имен шрифтов в качестве замены для изначального имени шрифта (указанного в первом параметре).

Вот пример простого сценария использования метода FontConfigs.SetFontSubstitutes.

**Java**

{{< highlight csharp >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

Aspose.Cells for Java также предоставляет средства для получения информации о заданных источниках и замене шрифтов.

1. Метод FontConfigs.getFontSources возвращает массив типа FontSourceBase, содержащий список указанных источников шрифтов. Если источники не были установлены, метод FontConfigs.getFontSources вернет пустой массив.
1. Метод FontConfigs.getFontSubstitutes принимает параметр типа string, позволяя указать имя шрифта, для которого задана замена. Если замена не была установлена для указанного имени шрифта, то метод FontConfigs.getFontSubstitutes вернет null.

{{% alert color="primary" %}} 

Для получения дополнительной информации о FontConfigs, ознакомьтесь со статьей по ссылке [Настройка шрифтов для визуализации электронных таблиц](/cells/ru/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Добавлен интерфейс IFilePathProvider и свойство HtmlSaveOptions.FilePathProvider**
Aspose.Cells for Java 8.9.1 позволяет получать/устанавливать IFilePathProvider для экспорта листов книги в отдельные файлы HTML. Эти новые API полезны в ситуациях, когда гиперссылки на одном листе указывают на местонахождение на другом листе, и требуется рендерить каждый лист в отдельный файл HTML. Реализация IFilePathProvider позволяет сохранить указанные гиперссылки независимо от того, указывают ли они на местоположение в отдельном файле HTML.

Вот простой сценарий использования свойства HtmlSaveOptions.FilePathProvider.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save each Worksheet to separate  HTML file

for (int i = 0; i < book.getWorksheets().getCount(); i++)

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

Дополнительные сведения об этом улучшении можно найти в статье [Реализация интерфейса IFilePathProvider](/cells/ru/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Добавлены свойство CopyOptions.ReferToDestinationSheet и перегрузка метода Cells.copyRows**
API Aspose.Cells for Java добавил свойство типа Boolean CopyOptions.ReferToDestinationSheet вместе с перегрузкой метода Cells.copyRows для облегчения операции копирования строк, когда строки для копирования также содержат диаграмму и ее исходные данные. Разработчики могут использовать эти новые API, чтобы связать источник данных диаграммы со стартовым или конечным листом.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

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

Дополнительные сведения об этой функции можно найти в статье [Управление источником данных диаграммы при копировании строк](/cells/ru/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Добавлено свойство CalculationOptions.Recursive**
Aspose.Cells for Java 8.9.1 добавил свойство типа Boolean CalculationOptions.Recursive. Установка свойства CalculationOptions.Recursive в true и передача объекта в метод Workbook.calculateFormula указывает API Aspose.Cells на рекурсивное вычисление зависимых ячеек при вычислении ячеек, зависящих от других ячеек.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

Дополнительные сведения о этой функции можно найти в статье [Оптимизация времени вычислений](/cells/ru/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Устаревшие API**
### **Свойство CellsHelper.FontDir устарело**
Рекомендуется использовать метод FontConfigs.setFontFolder(String, boolean) с рекурсивным параметром false вместо.
### **Свойство CellsHelper.FontDirs устарело**
Рекомендуется использовать метод FontConfigs.setFontFolders(String[], boolean) с рекурсивным параметром false вместо.
### **Свойство CellsHelper.FontFiles устарело**
Рекомендуется использовать метод FontConfigs.setFontSources(FontSourceBase[]) вместо.

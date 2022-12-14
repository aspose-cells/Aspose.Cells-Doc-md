---
title: Общедоступный API Изменения в Aspose.Cells 16.12.0
type: docs
weight: 360
url: /ru/net/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 16.11.0 до 16.12.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Фильтровать объекты во время загрузки**
Aspose.Cells 16.12.0 предоставляет класс LoadFilter вместе со свойством LoadOptions.LoadFilter, которые вместе могут управлять типом загружаемых данных при инициализации экземпляра Workbook из файла шаблона.

Вот простой сценарий использования для загрузки только свойств документа из файла шаблона.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Следующий фрагмент загружает все из существующей электронной таблицы, кроме диаграмм.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Следующий код загружает только данные ячейки (вместе с формулами) и форматирование из существующей электронной таблицы.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Класс LoadFilter также позволяет настроить процесс загрузки в соответствии со свойствами рабочего листа. Чтобы настроить процесс загрузки в соответствии с рабочим листом, необходимо переопределить метод LoadFilter.StartSheet, как показано ниже.

**C#**

{{< highlight "csharp" >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}



В следующем фрагменте используется класс CustomFilter, определенный выше.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **Добавлено перечисление FileFormatType.OTS**
Aspose.Cells 16.12.0 добавил запись OTS в перечисление FileFormatType для определения формата файлов OTS.

В следующем фрагменте используется FileFormatType.OTS.

**C#**

{{< highlight "csharp" >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **Добавлено свойство FontConfigs.PreferSystemFontSubstitutes.**
Aspose.Cells 16.12.0 предоставил свойство PreferSystemFontSubstitutes для класса FontConfigs. Свойство FontConfigs.PreferSystemFontSubstitutes имеет тип Boolean, указывающий, должен ли API сначала использовать системный механизм замены шрифта, если требуемый шрифт отсутствует и замена для конкретного шрифта не определена. Значение свойства FontConfigs.PreferSystemFontSubstitutes по умолчанию — false.
### **Добавлено свойство BuiltInDocumentPropertyCollection.ScaleCrop.**
Aspose.Cells 16.12.0 добавило свойство ScaleCrop в класс BuiltInDocumentPropertyCollection. ScaleCrop указывает режим отображения миниатюры документа. Установка этого элемента в значение true позволяет масштабировать миниатюру документа в соответствии с отображением, тогда как установка значения false позволяет обрезать миниатюру документа, чтобы показать раздел, который соответствует отображению.
### **Добавлено свойство BuiltInDocumentPropertyCollection.LinksUpToDate.**
Aspose.Cells 16.12.0 также предоставляет свойство LinksUpToDate для класса BuiltInDocumentPropertyCollection. Свойство LinksUpToDate указывает, являются ли гиперссылки в документе актуальными.
### **Добавлен метод Workbook.ExportXml**
Aspose.Cells 16.12.0 предоставил метод Workbook.ExportXml, который позволяет сохранять данные сопоставления XML с указанным путем к файлу. Метод Workbook.ExportXml принимает 2 параметра, где первый параметр типа string должен быть именем карты XML, а второй параметр должен быть путем к файлу для хранения данных XML.
### **Добавлен метод WorksheetCollection.CreateRange.**
Aspose.Cells В версии 16.12.0 добавлен метод WorksheetCollection.CreateRange, который позволяет создавать диапазон на основе адреса (ссылки на область ячейки) и индекса рабочего листа.

В следующем фрагменте используется метод WorksheetCollection.CreateRange для создания диапазона ячеек от A1 до A2 на первом листе (по умолчанию).

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

{{< /highlight >}}
## **Устаревшие API**
### **Устаревшее свойство LoadOptions.LoadDataOptions**
В качестве альтернативы используйте свойство LoadOptions.LoadFilter.
### **Устаревшее свойство LoadOptions.LoadDataFilterOptions**
Вместо этого используйте свойство LoadOptions.LoadFilter.
### **Устаревшее свойство LoadOptions.OnlyLoadDocumentProperties**
В качестве альтернативы используйте свойство LoadOptions.LoadFilter.
### **Устаревшее свойство LoadOptions.LoadDataAndFormatting**
Вместо этого используйте свойство LoadOptions.LoadFilter.

{{% alert color="primary" %}} 

Фрагменты кода для всех устаревших API были опубликованы выше.

{{% /alert %}}
## **Удаленные API**
### **Удалено свойство DataLabels.Rotation**
Вместо этого используйте свойство DataLabels.RotationAngle.
### **Удалено свойство Title.Rotation**
В качестве альтернативы используйте свойство Title.RotationAngle.
### **Удаленное свойство DataLabels.Background**
Вместо этого рекомендуется использовать свойство DataLabels.BackgroundMode.
### **Удалено свойство DisplayUnitLabel.Rotation**
Рассмотрите возможность использования свойства DisplayUnitLabel.RotationAngle для достижения той же цели.

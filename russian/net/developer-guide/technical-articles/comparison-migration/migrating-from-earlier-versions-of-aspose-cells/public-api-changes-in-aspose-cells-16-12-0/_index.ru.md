---
title: Изменения в общедоступном API в Aspose.Cells 16.12.0
type: docs
weight: 360
url: /ru/net/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells от версии 16.11.0 до 16.12.0, которые могут быть интересны разработчикам модулей/приложений. В нем представлены не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Фильтровать объекты во время загрузки**
Aspose.Cells 16.12.0 представил класс LoadFilter вместе с свойством LoadOptions.LoadFilter, которые вместе могут контролировать тип данных, которые будут загружены при инициализации экземпляра Workbook из файла шаблона.

Вот простой сценарий использования для загрузки только свойств документа из файла шаблона.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Следующий фрагмент загружает все, кроме диаграмм из существующей электронной таблицы.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Следующий код загружает только данные ячеек (вместе с формулами) и форматирование из существующей электронной таблицы.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Класс LoadFilter также позволяет настраивать процесс загрузки в соответствии с свойствами листа. Чтобы настроить процесс загрузки в соответствии с листом, необходимо переопределить метод LoadFilter.StartSheet, как показано ниже.

**C#**

{{< highlight csharp >}}

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



Следующий фрагмент использует определенный выше класс CustomFilter.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **Добавлено перечисление FileFormatType.OTS**
Aspose.Cells 16.12.0 добавил OTS в перечисление FileFormatType для определения формата файлов OTS.

Следующий фрагмент использует FileFormatType.OTS.

**C#**

{{< highlight csharp >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **Добавлено свойство FontConfigs.PreferSystemFontSubstitutes**
Aspose.Cells 16.12.0 добавил свойство PreferSystemFontSubstitutes для класса FontConfigs. Свойство FontConfigs.PreferSystemFontSubstitutes имеет тип Boolean и указывает, следует ли API сначала использовать механизм замены шрифтов системы, в случае отсутствия необходимого шрифта и отсутствия замены для конкретного шрифта. Значение по умолчанию свойства FontConfigs.PreferSystemFontSubstitutes - false.
### **Добавлено свойство BuiltInDocumentPropertyCollection.ScaleCrop**
Aspose.Cells 16.12.0 добавил свойство ScaleCrop в класс BuiltInDocumentPropertyCollection. ScaleCrop указывает режим отображения миниатюры документа. Установка этого элемента в true позволяет масштабировать миниатюру документа в соответствии с дисплеем, в то время как установка его в false позволяет обрезать миниатюру документа, чтобы показать секцию, которая соответствует дисплею.
### **Добавлено свойство BuiltInDocumentPropertyCollection.LinksUpToDate**
Aspose.Cells 16.12.0 также предоставил свойство LinksUpToDate для класса BuiltInDocumentPropertyCollection. Свойство LinksUpToDate указывает, актуальны ли гиперссылки в документе.
### **Добавлен метод Workbook.ExportXml.**
Aspose.Cells 16.12.0 добавил метод Workbook.ExportXml, который позволяет сохранить данные XML-карты по указанному пути файла. Метод Workbook.ExportXml принимает 2 параметра, где первый параметр типа string должен быть именем XML-карты, а второй параметр должен быть путем к файлу для сохранения XML-данных.
### **Добавлен метод CreateRange для WorksheetCollection.**
Aspose.Cells 16.12.0 добавил метод CreateRange для класса WorksheetCollection, который позволяет создавать диапазон на основе адреса (ссылки на область ячеек) и индекса листа.

Приведенный ниже фрагмент кода использует метод CreateRange для создания диапазона ячеек от A1 до A2 на первом (по умолчанию) листе.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

{{< /highlight >}}
## **Устаревшие API**
### **Свойство Obsoleted LoadOptions.LoadDataOptions**
Пожалуйста, используйте свойство LoadOptions.LoadFilter в качестве альтернативы.
### **Свойство Obsoleted LoadOptions.LoadDataFilterOptions**
Пожалуйста, используйте свойство LoadOptions.LoadFilter вместо.
### **Свойство Obsoleted LoadOptions.OnlyLoadDocumentProperties**
Пожалуйста, используйте свойство LoadOptions.LoadFilter в качестве альтернативы.
### **Свойство Obsoleted LoadOptions.LoadDataAndFormatting**
Пожалуйста, используйте свойство LoadOptions.LoadFilter вместо.

{{% alert color="primary" %}} 

Кодовые фрагменты для всех устаревших API были предоставлены выше.

{{% /alert %}}
## **Удаленные API**
### **Свойство Deleted DataLabels.Rotation**
Пожалуйста, используйте свойство DataLabels.RotationAngle вместо.
### **Свойство Deleted Title.Rotation**
Пожалуйста, используйте свойство Title.RotationAngle в качестве альтернативы.
### **Свойство Deleted DataLabels.Background**
Рекомендуется использовать свойство DataLabels.BackgroundMode вместо.
### **Свойство Deleted DisplayUnitLabel.Rotation**
Пожалуйста, рассмотрите использование свойства DisplayUnitLabel.RotationAngle для достижения того же результата.
{{< app/cells/assistant language="csharp" >}}

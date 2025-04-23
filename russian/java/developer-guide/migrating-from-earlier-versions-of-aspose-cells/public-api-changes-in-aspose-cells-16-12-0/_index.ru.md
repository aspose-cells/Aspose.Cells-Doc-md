---
title: Изменения в общедоступном API в Aspose.Cells 16.12.0
type: docs
weight: 370
url: /ru/java/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells от версии 16.11.0 до 16.12.0, которые могут быть интересны разработчикам модулей/приложений. В нем представлены не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Фильтровать объекты во время загрузки**
Aspose.Cells 16.12.0 представил класс LoadFilter вместе с свойством LoadOptions.LoadFilter, которые вместе могут контролировать тип данных, которые будут загружены при инициализации экземпляра Workbook из файла шаблона.

Вот простой сценарий использования для загрузки только свойств документа из файла шаблона.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.DOCUMENT_PROPERTIES);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

Следующий фрагмент загружает все, кроме диаграмм из существующей электронной таблицы.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

Следующий код загружает только данные ячеек (вместе с формулами) и форматирование из существующей электронной таблицы.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.CELL_DATA);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}
### **Добавлено перечисление FileFormatType.OTS**
Aspose.Cells 16.12.0 добавил OTS в перечисление FileFormatType для определения формата файлов OTS.

Следующий фрагмент использует FileFormatType.OTS.

**Java**

{{< highlight csharp >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **Добавлено свойство BuiltInDocumentPropertyCollection.ScaleCrop**
Aspose.Cells 16.12.0 добавил свойство ScaleCrop в класс BuiltInDocumentPropertyCollection. ScaleCrop указывает режим отображения миниатюры документа. Установка этого элемента в true позволяет масштабировать миниатюру документа в соответствии с дисплеем, в то время как установка его в false позволяет обрезать миниатюру документа, чтобы показать секцию, которая соответствует дисплею.
### **Добавлено свойство BuiltInDocumentPropertyCollection.LinksUpToDate**
Aspose.Cells 16.12.0 также предоставил свойство LinksUpToDate для класса BuiltInDocumentPropertyCollection. Свойство LinksUpToDate указывает, актуальны ли гиперссылки в документе. 
### **Добавлен метод Workbook.exportXml**
Aspose.Cells 16.12.0 предоставил метод Workbook.exportXml, позволяющий сохранить данные XML-карты в указанный файл. Метод Workbook.exportXml принимает 2 параметра, где первый параметр типа string должен быть именем XML-карты, а второй параметр должен быть расположением файла для сохранения XML-данных.
### **Добавлен метод WorksheetCollection.createRange**
Aspose.Cells 16.12.0 добавил метод WorksheetCollection.createRange, позволяющий создавать диапазон на основе адреса (ссылки на область ячеек) и индекса листа.

Следующий фрагмент использует метод WorksheetCollection.createRange для создания диапазона ячеек, охватывающего A1 до A2 в первом (по умолчанию) листе.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

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
### **Метод Deleted Title.getCharacters**
Пожалуйста, используйте метод Title.characters вместо.
{{< app/cells/assistant language="java" >}}

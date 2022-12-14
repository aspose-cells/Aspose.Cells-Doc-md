---
title: Общедоступный API Изменения в Aspose.Cells 16.12.0
type: docs
weight: 370
url: /ru/java/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 16.11.0 до 16.12.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Фильтровать объекты во время загрузки**
Aspose.Cells 16.12.0 предоставляет класс LoadFilter вместе со свойством LoadOptions.LoadFilter, которые вместе могут управлять типом загружаемых данных при инициализации экземпляра Workbook из файла шаблона.

Вот простой сценарий использования для загрузки только свойств документа из файла шаблона.

**Java**

{{< highlight "csharp" >}}

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

Следующий фрагмент загружает все из существующей электронной таблицы, кроме диаграмм.

**Java**

{{< highlight "csharp" >}}

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

Следующий код загружает только данные ячейки (вместе с формулами) и форматирование из существующей электронной таблицы.

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells 16.12.0 добавил запись OTS в перечисление FileFormatType для определения формата файлов OTS.

В следующем фрагменте используется FileFormatType.OTS.

**Java**

{{< highlight "csharp" >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **Добавлено свойство BuiltInDocumentPropertyCollection.ScaleCrop.**
Aspose.Cells 16.12.0 добавило свойство ScaleCrop в класс BuiltInDocumentPropertyCollection. ScaleCrop указывает режим отображения миниатюры документа. Установка этого элемента в значение true позволяет масштабировать миниатюру документа в соответствии с отображением, тогда как установка значения false позволяет обрезать миниатюру документа, чтобы показать раздел, который соответствует отображению.
### **Добавлено свойство BuiltInDocumentPropertyCollection.LinksUpToDate.**
 Aspose.Cells 16.12.0 также предоставляет свойство LinksUpToDate для класса BuiltInDocumentPropertyCollection. Свойство LinksUpToDate указывает, являются ли гиперссылки в документе актуальными.
### **Добавлен метод Workbook.exportXml**
Aspose.Cells 16.12.0 предоставил метод Workbook.exportXml, который позволяет сохранять данные сопоставления XML с указанным путем к файлу. Метод Workbook.exportXml принимает 2 параметра, где первый параметр типа string должен быть именем карты XML, а второй параметр должен быть путем к файлу для хранения данных XML.
### **Добавлен метод WorksheetCollection.createRange.**
Aspose.Cells В версии 16.12.0 добавлен метод WorksheetCollection.createRange, который позволяет создавать диапазон на основе адреса (ссылки на область ячейки) и индекса рабочего листа.

В следующем фрагменте используется метод WorksheetCollection.createRange для создания диапазона ячеек от A1 до A2 на первом листе (по умолчанию).

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

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
### **Удален метод Title.getCharacters**
Вместо этого используйте метод Title.characters.

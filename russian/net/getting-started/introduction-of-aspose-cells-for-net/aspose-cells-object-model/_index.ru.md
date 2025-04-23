---
title: Модель объектов Aspose.Cells
type: docs
weight: 20
url: /ru/net/aspose-cells-object-model/
---

{{% alert color="primary" %}} 

Модель объектов Aspose.Cells предоставляет информацию о структурных отношениях между объектами библиотеки классов Aspose.Cells. 

{{% /alert %}} 

Верхнеуровневая структура модели объектов Aspose.Cells показана ниже иерархическим образом.

|**Верхнеуровневая структура модели объектов Aspose.Cells**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_1.png)|
Как видно из приведенной выше схемы, корнем модели объектов является объект Workbook. Ниже приведено краткое описание некоторых объектов для вводных целей.
## **WorksheetCollection/Worksheet**
Объект Workbook содержит WorksheetCollection, которая представляет собой коллекцию всех объектов Worksheet в электронной таблице, как показано ниже:

|**Листы и объекты листов Worksheet**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_2.png)|
## **Cells/Cell**
Каждый объект Worksheet содержит объект Cells, который представляет собой коллекцию всех объектов Cell в листе, как показано ниже:

|**Ячейки и объекты ячеек Cell**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_3.png)|
Вы можете использовать объект Cell для получения и установки значения, стиля, формулы и других свойств отдельной ячейки.
## **ChartCollection/Chart**
Объект Charts представляет собой коллекцию всех объектов Chart в Worksheet. Каждый объект Chart состоит из нескольких других объектов, которые взаимодействуют между собой для создания и управления диаграммами. Структура диаграмм в Aspose.Cells показана на диаграмме ниже:

|**Объектная модель диаграммы**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_4.png)|
## **CommentCollection/Comment**
Каждый объект Worksheet также содержит объект Comments, представляющий собой коллекцию всех объектов Comment на листе, как показано ниже:

|**Комментарии и объекты комментариев**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_5.png)|
Объект Comment используется для добавления комментария в любую указанную ячейку на листе.
## **HorizontalPageBreakCollection/HorizontalPageBreak**
Каждый объект Worksheet содержит HorizontalPageBreakCollection, представляющий собой коллекцию всех объектов HorizontalPageBreak на листе, как показано ниже:

|**HPageBreaks & объекты HPageBreak**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_6.png)|
Объект HorizontalPageBreak используется для создания горизонтального разрыва страницы на листе.
## **HyperlinkCollection/Hyperlink**
Объект Worksheet также содержит HyperlinkCollection, представляющий собой коллекцию всех объектов Hyperlink на листе, как показано ниже:

|**Гиперссылки и объекты гиперссылок**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_7.png)|
Объект Hyperlink представляет собой гиперссылку на листе. Разработчики могут установить адрес гиперссылки и другие связанные свойства, используя объект Hyperlink.
## **PictureCollection/Picture**
Каждый объект Worksheet содержит объект PictureCollection, представляющий собой коллекцию всех объектов Picture на листе, как показано ниже:

|**Изображения и объекты изображений**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_8.png)|
Объект Picture представляет изображение на листе. Используя объект Picture, разработчики могут не только добавлять изображения на свои листы, но и размещать эти изображения в любом месте. Также можно установить границы или другие свойства изображений.

## **VerticalPageBreakCollection/VerticalPageBreak**
Каждый объект Worksheet содержит объект VerticalPageBreakCollection, представляющий собой коллекцию всех объектов VerticalPageBreak на листе, как показано ниже:

|**VPageBreaks & объекты VPageBreak**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_9.png)|
Объект VerticalPageBreak используется для создания вертикального разрыва страницы в рабочем листе.


## **PivotTableCollection/PivotTable**
Каждый объект Worksheet содержит объект PivotTableCollection, который представляет собой коллекцию всех объектов PivotTable на рабочем листе, как показано ниже:

| **PivotTables и объекты PivotTable** |
| :- |
|![todo:image_alt_text](aspose-cells-object-model_10.png)|
Объект PivotTable представляет собой сводную таблицу на рабочем листе. Разработчики могут установить стиль сводной таблицы и другие связанные свойства, используя объект PivotTable.

## **TimelineCollection/Timeline**
Каждый объект Worksheet содержит объект TimelineCollection, который представляет собой коллекцию всех объектов Timeline на рабочем листе, как показано ниже:

| **Временные шкалы и объекты временных шкал** |
| :- |
|![todo:image_alt_text](aspose-cells-object-model_11.png)|
Объект Timeline представляет собой временную шкалу на рабочем листе. Разработчики могут установить стиль временной шкалы и другие связанные свойства, используя объект Timeline.

## **SlicerCollection/Slicer**
Каждый объект Worksheet содержит объект SlicerCollection, который представляет собой коллекцию всех объектов Slicer на рабочем листе, как показано ниже:

| **Нарезчики и объекты нарезчика** |
| :- |
|![todo:image_alt_text](aspose-cells-object-model_12.png)|
Объект Slicer представляет собой нарезчик на рабочем листе. Разработчики могут установить стиль нарезчика и другие связанные свойства, используя объект Slicer.

## **ListObjectCollection/ListObject**
Каждый объект Worksheet содержит объект ListObjectCollection, который представляет собой коллекцию всех объектов ListObject на рабочем листе, как показано ниже:

| **Таблицы и объекты таблиц** |
| :- |
|![todo:image_alt_text](aspose-cells-object-model_13.png)|
Объект ListObject представляет собой таблицу на рабочем листе. Разработчики могут установить стиль таблицы и другие связанные свойства, используя объект ListObject.

## **ShapeCollection/Shape**
Каждый объект Worksheet содержит объект ShapeCollection, который представляет собой коллекцию всех объектов Shape на рабочем листе, как показано ниже:

| **Формы и объекты формы** |
| :- |
|![todo:image_alt_text](aspose-cells-object-model_14.png)|
Объект Shape представляет фигуру на листе. Разработчики могут задавать стиль фигуры и другие связанные свойства, используя объект Shape.

## **SparklineGroupCollection/SparklineGroup**
Каждый объект Worksheet содержит объект SparklineGroupCollection, представляющий коллекцию всех объектов SparklineGroup на листе, как показано ниже:

|**Объекты SparklineGroups и SparklineGroup**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_15.png)|
Объект SparklineGroup представляет группу мини-диаграмм на листе. Разработчики могут задавать стиль группы мини-диаграмм и другие связанные свойства с использованием объекта SparklineGroup.
{{< app/cells/assistant language="csharp" >}}

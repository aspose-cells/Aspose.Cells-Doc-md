﻿---
title: Aspose.Cells Объектная модель
type: docs
weight: 20
url: /ru/python-net/aspose-cells-object-model/
---
{{% alert color="primary" %}}

Aspose.Cells Объектная модель предоставляет информацию о структурных отношениях между объектами библиотеки классов Aspose.Cells.

{{% /alert %}}

Структура верхнего уровня объектной модели Aspose.Cells показана ниже в иерархическом порядке.

|**Структура верхнего уровня объектной модели Aspose.Cells**|
|:- |
|![дело:изображение_альтернативный_текст](aspose-cells-object-model_1.png)|
Как видно из рисунка выше, корнем объектной модели является объект Workbook. Краткое описание некоторых объектов приведено ниже для ознакомления.

## **Рабочий листКоллекция/Рабочий лист**

Объект Workbook содержит коллекцию WorksheetCollection, которая представляет коллекцию всех объектов Worksheet в электронной таблице, как показано ниже:

|**Рабочие листы и объекты рабочего листа**|
|:- |
|![дело:изображение_альтернативный_текст](aspose-cells-object-model_2.png)|

## **Cells/Cell**

Каждый объект Worksheet содержит объект Cells, который представляет собой набор всех объектов Cell на листе, как показано ниже:

|**Cells и Cell объекты**|
|:- |
|![дело:изображение_альтернативный_текст](aspose-cells-object-model_3.png)|
Вы можете использовать объект Cell для получения и установки значения, стиля, формулы и других свойств отдельной ячейки.

## **ChartCollection/Chart**

Объект Charts представляет собой набор всех объектов Chart на рабочем листе. Каждый объект Chart состоит из нескольких других объектов, которые работают вместе для создания диаграмм и управления ими. Структура диаграммы в Aspose.Cells показана на диаграмме ниже:

|**Объектная модель диаграммы**|
|:- |
|![дело:изображение_альтернативный_текст](aspose-cells-object-model_4.png)|

## **КомментарийКоллекция/Комментарий**

Каждый объект Worksheet также содержит объект Comment, представляющий коллекцию всех объектов Comment на листе, как показано ниже:

|**Комментарии и объекты комментариев**|
|:- |
|![дело:изображение_альтернативный_текст](aspose-cells-object-model_5.png)|
Объект Comment используется для добавления комментария к любой указанной ячейке на листе.

## **HorizontalPageBreakCollection/HorizontalPageBreak**

Каждый объект Worksheet содержит HorizontalPageBreakCollection, представляющий коллекцию всех объектов HorizontalPageBreak на листе, как показано ниже:

|**HPageBreaks и объекты HPageBreak**|
|:- |
|![дело:изображение_альтернативный_текст](aspose-cells-object-model_6.png)|
Объект HorizontalPageBreak используется для создания горизонтального разрыва страницы на листе.

## **Коллекция гиперссылок/гиперссылка**

Объект Worksheet также содержит HyperlinkCollection, представляющий коллекцию всех объектов Hyperlink на листе, как показано ниже:

|**Гиперссылки и объекты гиперссылок**|
|:- |
|![дело:изображение_альтернативный_текст](aspose-cells-object-model_7.png)|
Объект Hyperlink представляет собой гиперссылку на листе. Разработчики могут установить адрес гиперссылки и другие связанные свойства, используя объект Hyperlink.

## **PictureКоллекция/Изображение**

Каждый объект Worksheet содержит объект PictureCollection, представляющий коллекцию всех объектов Picture на листе, как показано ниже:

|**Изображения и объекты изображений**|
|:- |
|![дело:изображение_альтернативный_текст](aspose-cells-object-model_8.png)|
Объект Picture представляет изображение на рабочем листе. Используя объект Picture, разработчики могут не только добавлять изображения на свои рабочие листы, но и размещать эти изображения в любом месте. Также можно установить границы или другие свойства изображений.

## **ВертикальнаяPageBreakCollection/VerticalPageBreak**

Каждый объект Worksheet содержит объект VerticalPageBreakCollection, представляющий коллекцию всех объектов VerticalPageBreak на листе, как показано ниже:

|**VPageBreaks и объекты VPageBreak**|
|:- |
|![дело:изображение_альтернативный_текст](aspose-cells-object-model_9.png)|
Объект VerticalPageBreak используется для создания вертикального разрыва страницы на листе.

---
title: Управление объектами OLE
type: docs
weight: 30
url: /ru/java/managing-ole-objects/
---

## **Введение**

OLE (Object Linking and Embedding) - это технология составного документа, разработанная Microsoft. Коротко говоря, составной документ представляет собой что-то вроде дисплейного рабочего стола, который может содержать визуальные и информационные объекты всех видов: текст, календари, анимации, звук, видео, 3D, постоянно обновляемые новости, элементы управления и т. д. Каждый объект рабочего стола является независимой программной сущностью, которая может взаимодействовать с пользователем и общаться с другими объектами на рабочем столе.

OLE (Object Linking and Embedding) поддерживается многими программами и используется для того, чтобы сделать контент, созданный в одной программе, доступным в другой. Например, вы можете вставить документ Microsoft Word в Microsoft Excel. Чтобы увидеть, какие типы содержимого можно вставить, щелкните ** Объект ** на меню ** Вставить **. В списке ** Тип объекта ** появляются только программы, установленные на компьютере и поддерживающие объекты OLE.

## **Вставка объектов OLE в лист**

Aspose.Cells поддерживает добавление, извлечение и манипулирование объектами OLE в листах. По этой причине в Aspose.Cells существует класс [**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection), используемый для добавления нового объекта OLE в список коллекций. Другой класс, [**OleObject**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject), представляет объект OLE. Он имеет несколько важных членов:

- [**ImageData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData) указывает изображение (иконку) в виде массива байтов. Изображение будет отображаться, чтобы показать объект OLE на листе.
- [**ObjectData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData) указывает данные объекта в виде массива байтов. Эти данные будут показаны в связанной программе при двойном щелчке по иконке объекта OLE.

В следующем примере показано, как добавить объект OLE в лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **Извлечение объектов OLE в книге**

В следующем примере показано, как извлекать объекты OLE в книге. Пример получает различные объекты OLE из существующего файла XLS и сохраняет различные файлы (DOC, XLS, PPT, PDF и т. д.) на основе типа формата файла объекта OLE.

Вот скриншот шаблона файла XLS, в котором встроены различные объекты OLE на первом рабочем листе.

**Шаблонный файл содержит четыре объекта OLE** 

![todo:image_alt_text](managing-ole-objects_1.png)

После выполнения кода мы можем сохранить различные файлы на основе типов форматов их соответствующих объектов OLE. Ниже представлены скриншоты некоторых созданных файлов.

**Извлеченный файл XLS** 

![todo:image_alt_text](managing-ole-objects_2.png)

**Извлеченный файл PPT** 

![todo:image_alt_text](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **Извлечение встроенного файла MOL**

Aspose.Cells поддерживает извлечение объектов необычных типов, таких как MOL (молекулярный файл данных, содержащий информацию об атомах и связях). В следующем фрагменте кода демонстрируется извлечение встроенного файла MOL и его сохранение на диск с использованием этого [образца файла Excel](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **Продвинутые темы**
- [Доступ и изменение отображаемой метки связанного объекта OLE](/cells/ru/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Автоматическое обновление объекта OLE через Microsoft Excel с помощью Aspose.Cells](/cells/ru/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Извлечение объектов OLE из книги](/cells/ru/java/extract-ole-objects-from-workbook/)
- [Получение или установка идентификатора класса встроенного объекта OLE](/cells/ru/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
{{< app/cells/assistant language="java" >}}

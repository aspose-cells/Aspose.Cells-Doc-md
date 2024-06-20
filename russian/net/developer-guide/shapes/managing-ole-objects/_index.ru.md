---
title: Управление объектами OLE
type: docs
weight: 50
url: /ru/net/managing-ole-objects/
---

## **Введение**

OLE (Object Linking and Embedding) - это технология составного документа, разработанная Microsoft. Коротко говоря, составной документ представляет собой что-то вроде дисплейного рабочего стола, который может содержать визуальные и информационные объекты всех видов: текст, календари, анимации, звук, видео, 3D, постоянно обновляемые новости, элементы управления и т. д. Каждый объект рабочего стола является независимой программной сущностью, которая может взаимодействовать с пользователем и общаться с другими объектами на рабочем столе.

OLE (Object Linking and Embedding) поддерживается многими программами и используется для того, чтобы сделать контент, созданный в одной программе, доступным в другой. Например, вы можете вставить документ Microsoft Word в Microsoft Excel. Чтобы увидеть, какие типы содержимого можно вставить, щелкните ** Объект ** на меню ** Вставить **. В списке ** Тип объекта ** появляются только программы, установленные на компьютере и поддерживающие объекты OLE.

### **Вставка объектов OLE в лист**

Aspose.Cells поддерживает добавление, извлечение и манипулирование объектами OLE в листах Excel. По этой причине Aspose.Cells имеет класс [**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection), используемый для добавления нового объекта OLE в список коллекции. Еще один класс, [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), представляет объект OLE. У него есть несколько важных членов:

- Свойство [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata) определяет изображение (иконку) в виде массива байтов. Изображение будет отображаться для показа объекта OLE в листе Excel.
- Свойство [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata) определяет объектные данные в виде массива байтов. Эти данные будут показаны в связанной программе при двойном щелчке по иконке объекта OLE.

Нижеприведенный пример показывает, как добавить объект(ы) OLE в лист Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **Извлечение объектов OLE в книге**

В следующем примере показано, как извлекать объекты OLE в книге. Пример получает различные объекты OLE из существующего файла XLS и сохраняет различные файлы (DOC, XLS, PPT, PDF и т. д.) на основе типа формата файла объекта OLE.

После выполнения кода мы можем сохранить разные файлы на основе их соответствующих типов формата объектов OLE.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **Извлечение встроенного файла MOL**

Aspose.Cells поддерживает извлечение объектов нестандартных типов, таких как MOL (файл молекулярных данных, содержащий информацию об атомах и связях). Следующий фрагмент кода демонстрирует извлечение встроенного файла MOL и его сохранение на диск с использованием этого [образца Excel-файла](94896196.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **Продвинутые темы**
- [Доступ и изменение отображаемой метки связанного объекта OLE](/cells/ru/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Автоматическое обновление объекта OLE через Microsoft Excel с помощью Aspose.Cells](/cells/ru/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Извлечение объектов OLE из книги](/cells/ru/net/extract-ole-objects-from-workbook/)
- [Получение или установка идентификатора класса встроенного объекта OLE](/cells/ru/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Вставка файла WAV в качестве объекта OLE](/cells/ru/net/inserting-a-wav-file-as-an-ole-object/)


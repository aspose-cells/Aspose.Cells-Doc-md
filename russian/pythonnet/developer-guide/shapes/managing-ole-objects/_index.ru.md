---
title: Управление объектами OLE
type: docs
weight: 50
url: /ru/python-net/managing-ole-objects/
---

## **Введение**

OLE (Object Linking and Embedding) - это технология составного документа, разработанная Microsoft. Коротко говоря, составной документ представляет собой что-то вроде дисплейного рабочего стола, который может содержать визуальные и информационные объекты всех видов: текст, календари, анимации, звук, видео, 3D, постоянно обновляемые новости, элементы управления и т. д. Каждый объект рабочего стола является независимой программной сущностью, которая может взаимодействовать с пользователем и общаться с другими объектами на рабочем столе.

OLE (Object Linking and Embedding) поддерживается многими программами и используется для того, чтобы сделать контент, созданный в одной программе, доступным в другой. Например, вы можете вставить документ Microsoft Word в Microsoft Excel. Чтобы увидеть, какие типы содержимого можно вставить, щелкните ** Объект ** на меню ** Вставить **. В списке ** Тип объекта ** появляются только программы, установленные на компьютере и поддерживающие объекты OLE.

### **Вставка объектов OLE в лист**

Aspose.Cells для Python via .NET поддерживает добавление, извлечение и управление объектами OLE в листах. Для этого Aspose.Cells для Python via .NET предоставляет класс [**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection), который используется для добавления нового объекта OLE в список коллекции. Другой класс, [**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject), представляет объект OLE. Он имеет некоторые важные члены:

- Свойство [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data) определяет изображение (иконку) в виде массива байтов. Изображение будет отображаться для показа объекта OLE в листе Excel.
- Свойство [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data) определяет объектные данные в виде массива байтов. Эти данные будут показаны в связанной программе при двойном щелчке по иконке объекта OLE.

Нижеприведенный пример показывает, как добавить объект(ы) OLE в лист Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-InsertingOLEObjects-1.py" >}}

### **Извлечение объектов OLE в книге**

В следующем примере показано, как извлекать объекты OLE в книге. Пример получает различные объекты OLE из существующего файла XLS и сохраняет различные файлы (DOC, XLS, PPT, PDF и т. д.) на основе типа формата файла объекта OLE.

После выполнения кода мы можем сохранить разные файлы на основе их соответствующих типов формата объектов OLE.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-ExtractingOLEObjects-1.py" >}}

### **Извлечение встроенного файла MOL**

Aspose.Cells для Python via .NET поддерживает извлечение объектов редких типов, таких как MOL (молекулярный файл данных, содержащий информацию об атомах и связях). Следующий пример кода демонстрирует извлечение встроенного файла MOL и его сохранение на диск с помощью этого [примера файла Excel](94896196.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractEmbeddedMolFile-1.py" >}}

## **Продвинутые темы**
- [Доступ и изменение отображаемой метки связанного объекта OLE](/cells/ru/python-net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Автоматическое обновление объекта OLE](/cells/ru/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Извлечение объектов OLE из книги](/cells/ru/python-net/extract-ole-objects-from-workbook/)
- [Получение или установка идентификатора класса встроенного объекта OLE](/cells/ru/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Вставка файла WAV в качестве объекта OLE](/cells/ru/python-net/inserting-a-wav-file-as-an-ole-object/)

{{< app/cells/assistant language="python-net" >}}

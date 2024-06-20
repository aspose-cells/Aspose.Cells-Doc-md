---
title: Вставка изображений и формы файлов Excel.
linktitle: Фигуры
type: docs
weight: 140
url: /ru/net/insert-shapes/
description: Управляйте изображениями, объектами OLE, формами в файлы Excel.
---

{{% alert color="primary" %}}

Иногда вам нужно вставить необходимые формы в Лист книги Excel. Возможно, вам понадобится вставить ту же форму в разные позиции на листе. Или вам нужно пакетно вставить формы на Лист книги Excel.

Не волнуйтесь! [Aspose.Cells](https://products.aspose.com/cells/) поддерживает все эти операции.

{{% /alert %}}

Фигуры в Excel в основном разделяются на следующие типы:
- **Изображения**
- **OLE-объекты**
- **Линии**
- **Прямоугольники**
- **Базовые формы**
- **Блочные стрелки**
- **Уравнения**
- **Блок-схемы**
- **Звезды и баннеры**
- **Выноски**

В этом руководстве будет выбрано одна или две формы из каждого типа для создания образцов. Через эти примеры вы узнаете, как использовать [Aspose.Cells](https://products.aspose.com/cells/) для вставки указанной формы в таблицу.

## **Добавление изображений в лист Excel в C#**

Добавление изображений в электронную таблицу очень просто. Нужно лишь несколько строк кода:
Просто вызовите метод [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) коллекции [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) (инкапсулированной в объекте [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). Метод [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) принимает следующие параметры:

- **Индекс верхнего левого ряда**, индекс верхнего левого ряда.
- **Индекс верхнего левого столбца**, индекс верхнего левого столбца.
- **Имя файла изображения**, имя файла изображения с полным путем.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **Вставка объектов OLE в лист Excel в C#**

Aspose.Cells поддерживает добавление, извлечение и манипулирование объектами OLE в листах Excel. По этой причине Aspose.Cells имеет класс [**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection), используемый для добавления нового объекта OLE в список коллекции. Еще один класс, [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), представляет объект OLE. У него есть несколько важных членов:

- Свойство [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata) определяет изображение (иконку) в виде массива байтов. Изображение будет отображаться для показа объекта OLE в листе Excel.
- Свойство [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata) определяет объектные данные в виде массива байтов. Эти данные будут показаны в связанной программе при двойном щелчке по иконке объекта OLE.

Нижеприведенный пример показывает, как добавить объект(ы) OLE в лист Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **Вставка линии на лист Excel в C#**

Форма линии относится к категории **линии**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, куда хотите вставить линию
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите линию из 'Недавно использованные формы' или 'Линии'

![](line.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки линии в таблицу.

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

Метод возвращает объект [LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape).

{{% /alert %}}

В следующем примере показано, как вставить линию на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](line2.png)



## **Вставка стрелки линии в рабочий лист Excel в C#**

Форма стрелочной линии относится к категории **Линии**. Это особый случай линии.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, в которую хотите вставить стрелку.
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите стрелку из 'Недавно используемых форм' или 'Линий'.

![](line_arrow1.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки стрелки на лист.

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn,	int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

Метод возвращает объект [LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape).

{{% /alert %}}

В следующем примере показано, как вставить стрелку на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](line_arrow2.png)



## **Вставка прямоугольника в рабочий лист Excel в C#**

Форма прямоугольника относится к категории **Прямоугольники**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, в которую хотите вставить прямоугольник.
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите прямоугольник из 'Недавно используемых фигур' или 'Прямоугольники'.

![](rectangle.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки прямоугольника на листе.

{{% alert color="primary" %}}

[**public RectangleShape AddRectangle(int upperLeftRow,	int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

Метод возвращает объект [RectangleShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape).

{{% /alert %}}

В следующем примере показано, как вставить прямоугольник на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](rectangle2.png)



## **Вставка куба на лист Excel в C#**

Форма куба относится к категории **Базовые фигуры**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, в которую хотите вставить куб
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите Куб из **Базовые фигуры**

![](cube.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки куба на листе.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

Пример ниже показывает, как вставить куб в лист Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](cube2.png)



## **Вставка стрелочной подписи на лист Excel в C#**

Форма стрелки квадратного выноса относится к категории **Блочные стрелки**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, в которую хотите вставить стрелку квадратного выноса
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите стрелку квадратного выноса из категории **Блочные стрелки**

![](callout_quad_arrow.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки стрелки квадратного выноса на лист Excel.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

Приведенный ниже пример показывает, как вставить стрелку квадратного выноса в лист Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](callout_quad_arrow2.png)



## **Вставка знака умножения в рабочий лист Excel в C#**

Форма знака умножения относится к категории **Формулы**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, в которую хотите вставить знак умножения
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите знак умножения из **Фигуры уравнения**

![](multiplication_sign.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки знака умножения в листе Excel.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

В следующем примере показано, как вставить знак умножения в лист Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](multiplication_sign2.png)



## **Вставка мультидокумента на лист Excel в C#**

Форма мультидокумента принадлежит к категории **Блок-схемы**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, куда вы хотите вставить мультидокумент
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите мультидокумент из **Блок-схемы**

![](multidocument.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки мультидокумента в листе Excel.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

В следующем примере показано, как вставить мультидокумент в лист Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](multidocument2.png)



## **Вставка пятиконечной звезды на лист Excel в C#**

Форма пятиконечной звезды относится к категории **Звезды и транспаранты**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, в которую хотите вставить пятиконечную звезду
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите пятиконечную звезду из **Звезды и транспаранты**

![](star_5_points.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки пятиконечной звезды в лист.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

Следующий пример показывает, как вставить пятиконечную звезду на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](star_5_points2.png)



## **Вставка облачка мыслей в лист Excel с помощью C#**

Форма размышляющего облачка относится к категории **Выноски**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, в которую хотите вставить размышляющее облачко
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите размышляющее облачко из **Выноски**

![](thought_bubble_cloud.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки облака с мыслями на листе.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

В следующем примере показано, как вставить облако с мыслями на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](thought_bubble_cloud2.png)

## **Продвинутые темы**
- [Изменение значений коррекции формы](/cells/ru/net/change-adjustment-values-of-the-shape/)
- [Копировать формы между рабочими листами](/cells/ru/net/copy-shapes-between-worksheets/)
- [Данные в не-примитивной форме](/cells/ru/net/data-in-non-primitive-shape/)
- [Поиск абсолютной позиции формы внутри рабочего листа](/cells/ru/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Получить точки соединения от формы](/cells/ru/net/get-connection-points-from-shape/)
- [Управление элементами управлениями](/cells/ru/net/managing-controls/)
- [Добавление значков на рабочий лист](/cells/ru/net/insert-svg-to-excel/)
- [Управление объектами OLE](/cells/ru/net/managing-ole-objects/)
- [Управление изображениями](/cells/ru/net/managing-pictures/)
- [Управление умным искусством](/cells/ru/net/managing-smartart/)
- [Управление текстовыми полями](/cells/ru/net/managing-textbox-of-excel/)
- [Добавление водяного знака WordArt на лист](/cells/ru/net/add-wordart-watermark-to-worksheet/)
- [Обновить значения связанных форм](/cells/ru/net/refresh-values-of-linked-shapes/)
- [Отправить форму вперед или назад внутри листа](/cells/ru/net/send-shape-front-or-back-inside-the-worksheet/)
- [Управление параметрами формы](/cells/ru/net/managing-shape-options/)
- [Управление параметрами текста формы](/cells/ru/net/managing-shape-text-options/)
- [Веб-расширения - дополнения для Office](/cells/ru/net/web-extensions-office-add-ins/)


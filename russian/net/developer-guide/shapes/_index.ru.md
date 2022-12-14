---
title: Вставка изображений и форм файлов Excel.
linktitle: Формы
type: docs
weight: 140
url: /ru/net/insert-shapes/
description: Управляйте изображениями, объектами, формами в файлы Excel.
---
{{% alert color="primary" %}}

Иногда вам нужно вставить некоторые необходимые фигуры на рабочий лист. Вам может понадобиться вставить одну и ту же фигуру в разные места на рабочем листе. Или вам нужно вставить фигуры в лист в пакетном режиме.

 Не волнуйтесь![Aspose.Cells](https://products.aspose.com/cells/) поддерживает все эти операции.

{{% /alert %}}

Формы в Excel в основном делятся на следующие типы:
- **Картинки**
- **ОлеОбъекты**
- **Линии**
- **прямоугольники**
- **Основные формы**
- **Блок-стрелки**
- **Формы уравнения**
- **Блок-схемы**
- **Звезды и баннеры**
- **Выноски**

В этом руководящем документе будут выбраны одна или две формы каждого типа для создания образцов. С помощью этих примеров вы узнаете, как использовать[Aspose.Cells](https://products.aspose.com/cells/) чтобы вставить указанную фигуру на лист.

## **Добавление изображений на лист Excel в C#**

Добавлять изображения в электронную таблицу очень просто. Требуется всего несколько строк кода:
 Просто позвоните в[**Добавлять**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) метод[**Картинки**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) коллекция (инкапсулированная в[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) объект).[**Добавлять**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)метод принимает следующие параметры:

- **Индекс верхней левой строки**, индекс верхней левой строки.
- **Индекс верхнего левого столбца**, индекс верхнего левого столбца.
- **Имя файла изображения**, имя файла изображения вместе с путем.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **Вставка объектов OLE в рабочий лист Excel по номеру C#**

Aspose.Cells поддерживает добавление, извлечение и управление объектами OLE на листах. По этой причине Aspose.Cells имеет[**Олеобжектколлекшн**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) класс, используемый для добавления нового объекта OLE в список коллекций. Другой класс,[**ОлеОбъект**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), представляет объект OLE. В него входят несколько важных членов:

- [**Данные изображения**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)Свойство указывает данные изображения (значка) типа байтового массива. Изображение будет отображаться, чтобы показать объект OLE на листе.
- [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)свойство указывает данные объекта в виде массива байтов. Эти данные будут показаны в соответствующей программе при двойном щелчке по значку объекта OLE.

В следующем примере показано, как добавить объект(ы) OLE на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **Вставка строки в рабочий лист Excel в C#**

 Форма линии принадлежит**линии** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить строку
- Откройте меню «Вставка» и выберите «Фигуры».
- Затем выберите строку из «Недавно использованных фигур» или «Линий».

![](line.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить строку на лист.

{{% alert color="primary" %}}

[публичный LineShape AddLine(
 верхний левый ряд,
 инт топ,
 интервал верхний левый столбец,
 слева,
 внутренняя высота,
 ширина
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 Метод возвращает[Линейная форма](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) объект.

{{% /alert %}}

В следующем примере показано, как вставить строку на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](line2.png)



## **Вставка стрелки линии в рабочий лист Excel в C#**

 Форма линейной стрелки принадлежит**Линии**категория. Это частный случай линии.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить стрелку линии
- Откройте меню «Вставка» и выберите «Фигуры».
- Затем выберите стрелку линии из «Недавно использованных фигур» или «Линий».

![](line_arrow1.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить стрелку линии на листе.

{{% alert color="primary" %}}

[публичный LineShape AddLine(
 верхний левый ряд,
 инт топ,
 интервал верхний левый столбец,
 слева,
 внутренняя высота,
 ширина
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 Метод возвращает[Линейная форма](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) объект.

{{% /alert %}}

В следующем примере показано, как вставить стрелку линии на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](line_arrow2.png)



## **Вставка прямоугольника в рабочий лист Excel в C#**

 Форма прямоугольника относится к**прямоугольники** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить прямоугольник
- Откройте меню «Вставка» и выберите «Фигуры».
- Затем выберите прямоугольник из «Недавно использованных фигур» или «Прямоугольников».

![](rectangle.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить прямоугольник на лист.

{{% alert color="primary" %}}

[общедоступный RectangleShape AddRectangle (
 верхний левый ряд,
 инт топ,
 интервал верхний левый столбец,
 слева,
 внутренняя высота,
 ширина
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

 Метод возвращает[ПрямоугольникФорма](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) объект.

{{% /alert %}}

В следующем примере показано, как вставить прямоугольник на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](rectangle2.png)



## **Вставка куба в рабочий лист Excel в C#**

 Форма куба относится к**Основные формы** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, куда вы хотите вставить куб
- Откройте меню «Вставка» и выберите «Фигуры».
-  Затем выберите куб из**Основные формы**

![](cube.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить куб на лист.

{{% alert color="primary" %}}

[общедоступная форма AddAutoShape (
 тип автофигуры,
 верхний левый ряд,
 инт топ,
 интервал верхний левый столбец,
 слева,
 внутренняя высота,
 ширина
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Метод возвращает[Форма](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить куб на рабочий лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](cube2.png)



## **Вставка четырехугольной стрелки выноски в рабочий лист Excel в C#**

 Форма четырехугольной стрелки выноски принадлежит**Блок-стрелки** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить четырехугольную стрелку выноски.
- Откройте меню «Вставка» и выберите «Фигуры».
-  Затем выберите четырехугольную стрелку выноски из**Блок-стрелки**

![](callout_quad_arrow.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить четырехугольную стрелку выноски на лист.

{{% alert color="primary" %}}

[общедоступная форма AddAutoShape (
 тип автофигуры,
 верхний левый ряд,
 инт топ,
 интервал верхний левый столбец,
 слева,
 внутренняя высота,
 ширина
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Метод возвращает[Форма](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить четырехугольную стрелку выноски на рабочий лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](callout_quad_arrow2.png)



## **Вставка знака умножения в рабочий лист Excel в C#**

 Форма знака умножения принадлежит**Формы уравнения** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить знак умножения
- Откройте меню «Вставка» и выберите «Фигуры».
-  Затем выберите знак умножения из**Формы уравнения**

![](multiplication_sign.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить знак умножения на листе.

{{% alert color="primary" %}}

[общедоступная форма AddAutoShape (
 тип автофигуры,
 верхний левый ряд,
 инт топ,
 интервал верхний левый столбец,
 слева,
 внутренняя высота,
 ширина
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Метод возвращает[Форма](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить знак умножения на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](multiplication_sign2.png)



## **Вставка мультидокумента в рабочий лист Excel в C#**

Форма мультидокумента относится к**Блок-схемы** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить мультидокумент
- Откройте меню «Вставка» и выберите «Фигуры».
-  Затем выберите мультидокумент из**Блок-схемы**

![](multidocument.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод для вставки мультидокумента на лист.

{{% alert color="primary" %}}

[общедоступная форма AddAutoShape (
 тип автофигуры,
 верхний левый ряд,
 инт топ,
 интервал верхний левый столбец,
 слева,
 внутренняя высота,
 ширина
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Метод возвращает[Форма](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить несколько документов на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](multidocument2.png)



## **Вставка пятиконечной звезды в рабочий лист Excel в C#**

 Форма пятиконечной звезды принадлежит**Звезды и баннеры** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить пятиконечную звезду.
- Откройте меню «Вставка» и выберите «Фигуры».
-  Затем выберите пятиконечную звезду из**Звезды и баннеры**

![](star_5_points.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить пятиконечную звезду на лист.

{{% alert color="primary" %}}

[общедоступная форма AddAutoShape (
 тип автофигуры,
 верхний левый ряд,
 инт топ,
 интервал верхний левый столбец,
 слева,
 внутренняя высота,
 ширина
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Метод возвращает[Форма](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить пятиконечную звезду на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](star_5_points2.png)



## **Вставка облака мысленных пузырей в рабочий лист Excel в C#**

 Форма облака мысленных пузырей принадлежит**Выноски** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить облако мысленных пузырей.
- Откройте меню «Вставка» и выберите «Фигуры».
-  Затем выберите облако мысленных пузырей из**Выноски**

![](thought_bubble_cloud.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить облако мысленных пузырей на лист.

{{% alert color="primary" %}}

[общедоступная форма AddAutoShape (
 тип автофигуры,
 верхний левый ряд,
 инт топ,
 интервал верхний левый столбец,
 слева,
 внутренняя высота,
 ширина
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Метод возвращает[Форма](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить облако мысленных пузырей на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](thought_bubble_cloud2.png)

## **Предварительные темы**
- [Изменить значения настройки формы](/cells/ru/net/change-adjustment-values-of-the-shape/)
- [Копировать фигуры между рабочими листами](/cells/ru/net/copy-shapes-between-worksheets/)
- [Данные в непримитивной форме](/cells/ru/net/data-in-non-primitive-shape/)
- [Нахождение абсолютного положения формы внутри рабочего листа](/cells/ru/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Получить точки соединения из формы](/cells/ru/net/get-connection-points-from-shape/)
- [Управление элементами управления](/cells/ru/net/managing-controls/)
- [Добавить значки на рабочий лист](/cells/ru/net/insert-svg-to-excel/)
- [Управление OLE-объектами](/cells/ru/net/managing-ole-objects/)
- [Управление изображениями](/cells/ru/net/managing-pictures/)
- [Управление смарт-артом](/cells/ru/net/managing-smartart/)
- [Управление текстовым полем](/cells/ru/net/managing-textbox-of-excel/)
- [Добавить водяной знак WordArt на рабочий лист](/cells/ru/net/add-wordart-watermark-to-worksheet/)
- [Обновить значения связанных фигур](/cells/ru/net/refresh-values-of-linked-shapes/)
- [Отправить фигуру спереди или сзади внутри рабочего листа](/cells/ru/net/send-shape-front-or-back-inside-the-worksheet/)
- [Управление параметрами формы](/cells/ru/net/managing-shape-options/)
- [Управление параметрами текста фигуры](/cells/ru/net/managing-shape-text-options/)
- [Веб-расширения — надстройки Office](/cells/ru/net/web-extensions-office-add-ins/)


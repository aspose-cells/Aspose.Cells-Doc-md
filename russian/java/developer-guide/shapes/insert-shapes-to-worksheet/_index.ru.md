---
title: Вставить фигуры в рабочий лист Aspose.Cells
type: docs
weight: 5
url: /ru/java/insert-shapes-to-worksheet-in-aspose-cells/
---
{{% alert color="primary" %}}

Иногда вам нужно вставить некоторые необходимые фигуры на рабочий лист. Вам может понадобиться вставить одну и ту же фигуру в разные места на рабочем листе. Или вам нужно вставить фигуры в лист в пакетном режиме.

 Не волнуйтесь![Aspose.Cells](https://products.aspose.com/cells/)поддерживает все эти операции.

{{% /alert %}}

Формы в Excel в основном делятся на следующие типы:
- **Линии**
- **прямоугольники**
- **Основные формы**
- **Блок-стрелки**
- **Формы уравнения**
- **Блок-схемы**
- **Звезды и баннеры**
- **Выноски**

 В этом руководящем документе будут выбраны одна или две формы каждого типа для создания образцов. С помощью этих примеров вы узнаете, как использовать[Aspose.Cells](https://products.aspose.com/cells/) чтобы вставить указанную фигуру на лист.



## **Вставка строки в рабочий лист**

 Форма линии принадлежит**линии** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить строку
- Откройте меню «Вставка» и выберите «Фигуры».
- Затем выберите строку из «Недавно использованных фигур» или «Линий».

![](line.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить строку на лист.

{{% alert color="primary" %}}

[общедоступная форма addShape (тип int, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Метод возвращает[Форма](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить строку на лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](line2.png)



## **Вставка стрелки на рабочий лист**

 Форма линейной стрелки принадлежит**Линии** категория. Это частный случай линии.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить стрелку линии
- Откройте меню «Вставка» и выберите «Фигуры».
- Затем выберите стрелку линии из «Недавно использованных фигур» или «Линий».

![](line_arrow1.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить стрелку линии на листе.

{{% alert color="primary" %}}

[общедоступная форма addShape (тип int, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Метод возвращает[Форма](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить стрелку линии на лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](line_arrow2.png)



## **Вставка прямоугольника на рабочий лист**

 Форма прямоугольника относится к**прямоугольники** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить прямоугольник
- Откройте меню «Вставка» и выберите «Фигуры».
- Затем выберите прямоугольник из «Недавно использованных фигур» или «Прямоугольников».

![](rectangle.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить прямоугольник на лист.

{{% alert color="primary" %}}

[общедоступная форма addShape (тип int, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Метод возвращает[Форма](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить прямоугольник на лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](rectangle2.png)



## **Вставка куба в рабочий лист**

Форма куба относится к**Основные формы** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, куда вы хотите вставить куб
- Откройте меню «Вставка» и выберите «Фигуры».
-  Затем выберите куб из**Основные формы**

![](cube.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить куб на лист.

{{% alert color="primary" %}}

[общедоступная форма addAutoShape (тип int, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Метод возвращает[Форма](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить куб на рабочий лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](cube2.png)



## **Вставка четырехугольной стрелки выноски на рабочий лист**

 Форма четырехугольной стрелки выноски принадлежит**Блок-стрелки** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить четырехугольную стрелку выноски.
- Откройте меню «Вставка» и выберите «Фигуры».
-  Затем выберите четырехугольную стрелку выноски из**Блок-стрелки**

![](callout_quad_arrow.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить четырехугольную стрелку выноски на лист.

{{% alert color="primary" %}}

[общедоступная форма addAutoShape (тип int, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Метод возвращает[Форма](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить четырехугольную стрелку выноски на рабочий лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](callout_quad_arrow2.png)



## **Вставка знака умножения в рабочий лист**

 Форма знака умножения принадлежит**Формы уравнения** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить знак умножения
- Откройте меню «Вставка» и выберите «Фигуры».
-  Затем выберите знак умножения из**Формы уравнения**

![](multiplication_sign.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить знак умножения на листе.

{{% alert color="primary" %}}

[общедоступная форма addAutoShape (тип int, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Метод возвращает[Форма](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить знак умножения на лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](multiplication_sign2.png)



## **Вставка мультидокумента в рабочий лист**

 Форма мультидокумента относится к**Блок-схемы** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить мультидокумент
- Откройте меню «Вставка» и выберите «Фигуры».
-  Затем выберите мультидокумент из**Блок-схемы**

![](multidocument.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод для вставки мультидокумента на лист.

{{% alert color="primary" %}}

[общедоступная форма addAutoShape (тип int, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Метод возвращает[Форма](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить несколько документов на лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](multidocument2.png)



## **Вставка пятиконечной звезды на рабочий лист**

 Форма пятиконечной звезды принадлежит**Звезды и баннеры** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить пятиконечную звезду.
- Откройте меню «Вставка» и выберите «Фигуры».
-  Затем выберите пятиконечную звезду из**Звезды и баннеры**

![](star_5_points.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить пятиконечную звезду на лист.

{{% alert color="primary" %}}

[общедоступная форма addAutoShape (тип int, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Метод возвращает[Форма](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить пятиконечную звезду на лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](star_5_points2.png)



## **Вставка облака мысленных пузырей в рабочий лист**

 Форма облака мысленных пузырей принадлежит**Выноски** категория.

***В Microsoft Excel (например, 2007):***

- Выберите ячейку, в которую вы хотите вставить облако мысленных пузырей.
- Откройте меню «Вставка» и выберите «Фигуры».
-  Затем выберите облако мысленных пузырей из**Выноски**

![](thought_bubble_cloud.png)

***Использование Aspose.Cells***

Вы можете использовать следующий метод, чтобы вставить облако мысленных пузырей на лист.

{{% alert color="primary" %}}

[общедоступная форма addAutoShape (тип int, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Метод возвращает[Форма](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) объект.

{{% /alert %}}

В следующем примере показано, как вставить облако мысленных пузырей на лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

Выполните приведенный выше код, вы получите следующие результаты:

![](thought_bubble_cloud2.png)

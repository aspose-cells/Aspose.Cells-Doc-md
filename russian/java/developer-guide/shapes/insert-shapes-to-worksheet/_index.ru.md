---
title: Вставить формы в Лист книги Excel с помощью Aspose.Cells
type: docs
weight: 5
url: /ru/java/insert-shapes-to-worksheet-in-aspose-cells/
---


{{% alert color="primary" %}}

Иногда вам нужно вставить необходимые формы в Лист книги Excel. Возможно, вам понадобится вставить ту же форму в разные позиции на листе. Или вам нужно пакетно вставить формы на Лист книги Excel.

Не волнуйтесь! [Aspose.Cells](https://products.aspose.com/cells/) поддерживает все эти операции.

{{% /alert %}}

Фигуры в Excel в основном разделяются на следующие типы:
- **Линии**
- **Прямоугольники**
- **Базовые формы**
- **Блочные стрелки**
- **Уравнения**
- **Блок-схемы**
- **Звезды и баннеры**
- **Выноски**

В этом руководстве будет выбрано одна или две формы из каждого типа для создания образцов. Через эти примеры вы узнаете, как использовать [Aspose.Cells](https://products.aspose.com/cells/) для вставки указанной формы в таблицу.



## **Вставка линии на листе**

Форма линии относится к категории **линии**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, куда хотите вставить линию
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите линию из 'Недавно использованные формы' или 'Линии'

![](line.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки линии в таблицу.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

В следующем примере показано, как вставить линию на лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](line2.png)



## **Вставка стрелки на листе**

Форма стрелочной линии относится к категории **Линии**. Это особый случай линии.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, в которую хотите вставить стрелку.
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите стрелку из 'Недавно используемых форм' или 'Линий'.

![](line_arrow1.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки стрелки на лист.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

В следующем примере показано, как вставить стрелку на лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](line_arrow2.png)



## **Вставка прямоугольника на листе**

Форма прямоугольника относится к категории **Прямоугольники**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, в которую хотите вставить прямоугольник.
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите прямоугольник из 'Недавно используемых фигур' или 'Прямоугольники'.

![](rectangle.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки прямоугольника на листе.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

В следующем примере показано, как вставить прямоугольник на лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](rectangle2.png)



## **Вставка куба на лист**

Форма куба относится к категории **Базовые фигуры**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, в которую хотите вставить куб
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите Куб из **Базовые фигуры**

![](cube.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки куба на листе.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

Пример ниже показывает, как вставить куб в лист Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](cube2.png)



## **Добавление стрелки с подписью на листе расчета**

Форма стрелки квадратного выноса относится к категории **Блочные стрелки**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, в которую хотите вставить стрелку квадратного выноса
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите стрелку квадратного выноса из категории **Блочные стрелки**

![](callout_quad_arrow.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки стрелки квадратного выноса на лист Excel.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

Приведенный ниже пример показывает, как вставить стрелку квадратного выноса в лист Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](callout_quad_arrow2.png)



## **Добавление знака умножения на лист расчета**

Форма знака умножения относится к категории **Формулы**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, в которую хотите вставить знак умножения
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите знак умножения из **Фигуры уравнения**

![](multiplication_sign.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки знака умножения в листе Excel.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

В следующем примере показано, как вставить знак умножения в лист Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](multiplication_sign2.png)



## **Добавление множественного документа на лист расчета**

Форма мультидокумента принадлежит к категории **Блок-схемы**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, куда вы хотите вставить мультидокумент
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите мультидокумент из **Блок-схемы**

![](multidocument.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки мультидокумента в листе Excel.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

В следующем примере показано, как вставить мультидокумент в лист Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](multidocument2.png)



## **Добавление пятиконечной звезды на лист расчета**

Форма пятиконечной звезды относится к категории **Звезды и транспаранты**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, в которую хотите вставить пятиконечную звезду
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите пятиконечную звезду из **Звезды и транспаранты**

![](star_5_points.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки пятиконечной звезды в лист.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

Следующий пример показывает, как вставить пятиконечную звезду на лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](star_5_points2.png)



## **Добавление облачного облака с мыслью на лист расчета**

Форма размышляющего облачка относится к категории **Выноски**.

***В Microsoft Excel (например, 2007 год):***

- Выберите ячейку, в которую хотите вставить размышляющее облачко
- Нажмите меню Вставка и выберите Фигуры.
- Затем выберите размышляющее облачко из **Выноски**

![](thought_bubble_cloud.png)

***Используя Aspose.Cells***

Вы можете использовать следующий метод для вставки облака с мыслями на листе.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Метод возвращает объект [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

В следующем примере показано, как вставить облако с мыслями на лист.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

Выполните приведенный выше код, и вы получите следующие результаты:

![](thought_bubble_cloud2.png)
{{< app/cells/assistant language="java" >}}

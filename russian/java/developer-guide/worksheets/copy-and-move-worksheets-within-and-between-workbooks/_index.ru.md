---
title: Копировать и перемещать рабочие листы внутри и между рабочими книгами
type: docs
weight: 20
url: /ru/java/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

Иногда вам нужно несколько рабочих листов с общим форматированием и вводом данных. Например, если вы работаете с квартальными бюджетами, вы можете создать рабочую книгу с листами, содержащими одинаковые заголовки столбцов, заголовки строк и формулы. Есть способ сделать это: создать один лист, а затем скопировать его три раза.

Aspose.Cells поддерживает копирование или перемещение рабочих листов внутри или между книгами. Рабочие листы, включая данные, форматирование, таблицы, матрицы, диаграммы, изображения и другие объекты, копируются с высочайшей степенью точности.

{{% /alert %}}

## **Копирование и перемещение рабочих листов**

В этой статье объясняется, как использовать Aspose.Cells для:

- [Скопируйте рабочий лист в рабочей книге](/cells/ru/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [Перемещение рабочего листа в рабочей книге](/cells/ru/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [Копировать рабочий лист между рабочими книгами](/cells/ru/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [Перемещение рабочего листа между рабочими книгами](/cells/ru/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **Копирование рабочего листа в рабочую книгу**

Начальные шаги одинаковы для всех примеров.

1. Создайте две книги с некоторыми данными в Microsoft Excel. Для целей этого примера мы создали две новые рабочие книги в Microsoft Excel и ввели некоторые данные в рабочие листы.

- FirstWorkbook.xls (3 рабочих листа)
- SecondWorkbook.xls (1 рабочий лист).

  **FirstWorkbook.xls**

![дело:изображение_альтернативный_текст](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![дело:изображение_альтернативный_текст](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Загрузите и установите Aspose.Cells:
   1. [Скачать Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. Разархивируйте его на своем компьютере для разработки.
 Все[Aspose](http://www.aspose.com/) компоненты при установке работают в ознакомительном режиме. Режим оценки не имеет ограничения по времени и только вставляет водяные знаки в создаваемые документы.
1. Создайте проект:
 1. Создайте проект с помощью редактора Java, такого как Eclipse, или создайте простую программу с помощью текстового редактора.
1. Добавьте путь к классу:
1. Извлеките файлы Aspose.Cells.jar и dom4j_1.6.1.jar из Aspose.Cells.zip.
 1. Установите путь к классам проекта в Eclipse:
 1. Выберите свой проект в Eclipse и щелкните меню.**Проект** , тогда**Характеристики**.
 1. Выберите**Java Путь сборки** в левой части диалогового окна, затем выберите вкладку «Библиотеки»,
 1. Нажмите**Добавить JAR-файлы** или же**Добавить внешние JAR-файлы** чтобы выбрать Aspose.Cells.jar и dom4j_1.6.1.jar и добавить их в пути сборки.

{{% alert color="primary" %}}

Или вы можете установить путь к классам во время выполнения в приглашении DOS на Windows.
Например:

{{< highlight "java" >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. Скопируйте рабочий лист в рабочую книгу:
Ниже приведен код, используемый для выполнения задачи. Он копирует копию рабочего листа в FirstWorkbook.xls.

Выполнение кода перемещает рабочий лист с именем Copy в файле FirstWorkbook.xls с новым именем Last Sheet.

**Выходной файл**

![дело:изображение_альтернативный_текст](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **Перемещение рабочего листа в рабочей книге**

Ниже приведен код, используемый для выполнения задачи.

Выполнение кода перемещает рабочий лист Move из индекса 1 в индекс 2 в FirstWorkbook.xls.

**Выходной файл**

![дело:изображение_альтернативный_текст](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **Копирование рабочего листа между рабочими книгами**

Выполнение кода копирует рабочий лист Copy в SecondWorkbook.xls с новым именем Sheet2.

**Выходной файл**

![дело:изображение_альтернативный_текст](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **Перемещение рабочего листа между рабочими книгами**

Выполнение кода перемещает рабочий лист перемещения из FirstWorkbook.xls в SecondWorkbook.xls с новым именем Sheet3.

**Вывод FirstWorkbook.xls**

![дело:изображение_альтернативный_текст](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**Вывод SecondWorkbook.xls**

![дело:изображение_альтернативный_текст](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **Заключение**

{{% alert color="primary" %}}

В этой статье объясняется, как копировать и перемещать рабочие листы внутри и между книгами с помощью Aspose.Cells.

 Aspose.Cells — результат многолетних исследований, проектирования и тщательной настройки. Будем рады вашим вопросам, комментариям и предложениям на[Aspose.Cells Форум](https://forum.aspose.com/c/cells/9). Мы гарантируем быстрый ответ.

{{% /alert %}}

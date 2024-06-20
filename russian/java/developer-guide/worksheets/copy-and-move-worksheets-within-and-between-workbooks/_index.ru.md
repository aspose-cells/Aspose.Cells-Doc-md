---
title: Копирование и перемещение листов внутри и между книгами
type: docs
weight: 20
url: /ru/java/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

Иногда вам требуется несколько листов с общим форматированием и вводом данных. Например, если вы работаете с квартальными бюджетами, вам может понадобиться создать книгу с листами, содержащими одни и те же заголовки столбцов, заголовки строк и формулы. Есть способ сделать это: создав один лист, а затем скопировав его три раза.

Aspose.Cells поддерживает копирование или перемещение листов внутри или между книгами. Листы включают данные, форматирование, таблицы, матрицы, диаграммы, изображения и другие объекты с наивысшей степенью точности.

{{% /alert %}}

## **Копирование и перемещение листов**

В этой статье объясняется, как использовать Aspose.Cells для:

- [Копирование листа внутри книги](/cells/ru/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [Перемещение листа внутри книги](/cells/ru/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [Копирование листа между книгами](/cells/ru/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [Перемещение листа между книгами](/cells/ru/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **Копирование листа внутри книги**

Начальные шаги одинаковы для всех примеров.

1. Создайте две книги с некоторыми данными в Microsoft Excel. Для целей этого примера мы создали две новые книги в Microsoft Excel и ввели некоторые данные на листах.

- FirstWorkbook.xls (3 листа)
- SecondWorkbook.xls (1 лист).

  **FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Скачайте и установите Aspose.Cells:
   1. [Скачайте Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
   1. Распакуйте его на ваш компьютер для разработки.
      Все [Aspose](http://www.aspose.com/) компоненты при установке работают в режиме оценки. Режим оценки не имеет временных ограничений и вставляет только водяные знаки в созданные документы.
1. Создайте проект:
   1. Создайте проект в редакторе Java, таком как Eclipse, или создайте простую программу, используя текстовый редактор.
1. Добавьте путь к классу:
   1. Извлеките Aspose.Cells.jar и dom4j_1.6.1.jar из Aspose.Cells.zip.
   1. Установите classpath проекта в Eclipse:
      1. Выберите свой проект в Eclipse и щелкните меню **Проект**, затем **Свойства**.
      1. Выберите **Путь Java Build** слева в диалоговом окне, затем выберите вкладку Библиотеки,
      1. Нажмите **Добавить JARы** или **Добавить внешние JAR-файлы**, чтобы выбрать Aspose.Cells.jar и dom4j_1.6.1.jar и добавить их в пути сборки.

{{% alert color="primary" %}}

Или вы можете установить classpath при работе в командной строке в Windows.
Например:

{{< highlight java >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. Скопируйте лист внутри книги:
   Приведен ниже код, использованный для выполнения задачи. Он копирует лист Copy внутри FirstWorkbook.xls.

Запуск кода перемещает рабочий лист с именем Copy внутри FirstWorkbook.xls с новым именем Last Sheet.

**Файл вывода**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **Перемещение листа в книге Excel**

Ниже приведен код, используемый для выполнения этой задачи.

Запуск кода перемещает лист Move с индексом 1 на индекс 2 в FirstWorkbook.xls.

**Файл вывода**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **Копирование листа между книгами Excel**

Запуск кода копирует лист Copy в SecondWorkbook.xls с новым именем Sheet2.

**Файл вывода**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **Перемещение листа между книгами Excel**

Запуск кода перемещает лист move из FirstWorkbook.xls в SecondWorkbook.xls с новым именем Sheet3.

**Output FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**Output SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **Заключение**

{{% alert color="primary" %}}

В этой статье объясняется, как копировать и перемещать рабочие листы внутри и между книгами Excel с использованием Aspose.Cells.

Aspose.Cells получил выгоду от долгих исследований, разработки и тщательной настройки. Мы приветствуем ваши вопросы, комментарии и предложения на [форуме Aspose.Cells](https://forum.aspose.com/c/cells/9). Мы гарантируем оперативный ответ.

{{% /alert %}}

---
title: Создание сводных таблиц и сводных графиков
type: docs
weight: 10
url: /ru/java/create-pivot-tables-and-pivot-charts/
description: Создание сводных таблиц и сводных графиков с помощью API Aspose.Cells for Java.
keywords: excel создать сводную таблицу java, excel создать сводный график java, excel создать сводную таблицу и сводный график java, создать excel сводную таблицу java, создать excel сводный график java, создать excel сводную таблицу и сводный график java, java создать excel сводную таблицу и сводный график, как создать excel сводную таблицу и сводный график java
---

{{% alert color="primary" %}}

Сводная таблица - это интерактивная сводка записей. Например, у вас может быть сотни записей о счетах-фактурах в списке на листе. Сводная таблица может подсчитать счета-фактуры по клиенту, продукту или дате. С помощью Microsoft Excel можно быстро переставить информацию в сводной таблице, перетаскивая кнопки на новую позицию.

Сводный график - это интерактивное графическое представление данных в сводной таблице. Сводные графики были введены в Excel 2000. Использование сводного графика делает понимание данных еще проще, поскольку сводная таблица автоматически создает итоги и подитоги.

Aspose.Cells поддерживает [сводные таблицы](/cells/ru/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) и [сводные графики](/cells/ru/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **Добавление сводных таблиц и графиков**

Aspose.Cells предоставляет специальный набор классов, используемых для создания сводных таблиц. Эти классы используются для создания и установки объектов PivotTable, которые выступают в качестве основных строительных блоков объекта PivotTable:

- PivotField, поле в отчете сводной таблицы.
- PivotFields, коллекция всех объектов PivotField в сводной таблице.
- PivotTable, отчет PivotTable на листе.
- PivotTables, коллекция всех объектов PivotTable на листе.

### **Подготовка к использованию Aspose.Cells**

1. Скачайте и установите Aspose.Cells.Zip:
   1. [Скачайте Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
   1. Распакуйте его на ваш компьютер для разработки.
      Все [Aspose](http://www.aspose.com/) компоненты при установке работают в режиме оценки. Режим оценки не имеет временных ограничений и вставляет только водяные знаки в созданные документы.
1. Создайте проект
   1. Вы можете создать проект с помощью некоторого редактора Java, например, Eclipse, или создать простую программу, используя NotePad.
1. Добавьте путь класса:
   Для установки пути класса с помощью Eclipse:
   1. Извлеките Aspose.Cells.jar и dom4j_1.6.1.jar из Aspose.Cells.zip.
   1. Установите classpath проекта в Eclipse:
   1. Выберите свой проект в Eclipse, а затем щелкните меню Проект-Свойства.
   1. Выберите "Java Build Path" слева во всплывающем окне, затем выберите вкладку "Библиотеки", нажмите "Добавить JAR-файлы" или "Добавить внешние JAR-файлы" для выбора Aspose.Cells.jar и dom4j_1.6.1.jar и добавьте их в пути сборки.
   1. Напишите приложение для вызова API компонентов Aspose.
      Или вы можете установить его при выполнении в командной строке в Windows.

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **Создание сводной таблицы**

Для создания сводной таблицы с использованием Aspose.Cells:

1. Добавьте некоторые данные в ячейки листа с помощью метода PutValue/setValue объекта Cell. Вы также можете использовать файл шаблона, уже заполненный данными. Данные будут использоваться в качестве источника данных сводной таблицы.
1. Добавьте сводную таблицу на лист с помощью метода add коллекции PivotTables (инкапсулированной в объекте Worksheet).
1. Обратитесь к новому объекту PivotTable из коллекции PivotTables, передав его индекс.
1. Используйте любой из объектов сводной таблицы, инкапсулированных в объекте PivotTable, для управления таблицей.

Приведен пример кода. Выполнение этого кода создает новый файл: pivotTable_test.xls.

**Входные данные** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**Выходная сводная таблица**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Создание сводной диаграммы на основе сводной таблицы**

Для создания сводной диаграммы с помощью Aspose.Cells:

1. Добавьте диаграмму.
1. Установите источник данных диаграммы так, чтобы он ссылался на существующую сводную таблицу в электронной таблице.
1. Задайте другие атрибуты.

Ниже приведен код, используемый компонентом для выполнения этой задачи. Выполнение этого кода создает новый файл: pivotChart_test.xls.

**Лист сводной диаграммы**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Эта статья показывает, как создавать сводные таблицы и сводные диаграммы с использованием Aspose.Cells. Надеемся, это поможет вам использовать эти функции в ваших собственных сценариях.

Aspose.Cells воспользовался годами исследований, проектирования и тщательной настройки.

Мы ждем ваши вопросы, комментарии и предложения на [Форуме Aspose.Cells](https://forum.aspose.com/c/cells/9). Мы гарантируем оперативный ответ.

{{% /alert %}}

## Связанные статьи

- [Пользовательская сортировка в сводной таблице](/cells/ru/java/custom-sorting-in-pivot-table/)
- [Форматирование сводной таблицы](/cells/ru/java/formatting-pivot-table/)
- [Обновление и вычисление сводной таблицы с вычисляемыми элементами](/cells/ru/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Отключение лент сводной таблицы](/cells/ru/java/disable-pivot-table-ribbons/)


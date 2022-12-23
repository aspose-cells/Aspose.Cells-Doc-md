---
title: Создание сводных таблиц и сводных диаграмм
type: docs
weight: 10
url: /ru/java/create-pivot-tables-and-pivot-charts/
description: Создавайте сводные таблицы и сводные диаграммы с помощью Aspose.Cells for Java API.
keywords: excel create pivot table java, excel create pivot chart java, excel create pivot table and pivot chart java, create excel pivot table java, create excel pivot chart java, create excel pivot table and pivot chart java, java create excel pivot table and pivot chart, how to create excel pivot table and pivot chart java
---
{{% alert color="primary" %}}

Сводная таблица — это интерактивная сводка записей. Например, у вас могут быть сотни записей счетов в списке на листе. Сводная таблица может суммировать счета по клиентам, продуктам или датам. С Microsoft Excel можно быстро переупорядочить информацию в сводной таблице, перетаскивая кнопки в новое положение.

Сводная диаграмма — это интерактивное графическое представление данных в сводной таблице. Сводные диаграммы были представлены в Excel 2000. Использование сводных диаграмм еще больше упрощает понимание данных, поскольку сводная таблица автоматически создает промежуточные итоги и итоги.

 Aspose.Cells опоры[сводные таблицы](/cells/ru/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) и[сводные диаграммы](/cells/ru/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **Добавление сводных таблиц и диаграмм**

Aspose.Cells предоставляет специальный набор классов, используемых для создания сводных таблиц. Эти классы используются для создания и установки объектов сводной таблицы, которые действуют как основные строительные блоки объекта сводной таблицы:

- PivotField — поле в отчете сводной таблицы.
- PivotFields — коллекция всех объектов PivotField в сводной таблице.
- Сводная таблица — отчет сводной таблицы на листе.
- Сводные таблицы — коллекция всех объектов сводных таблиц на листе.

### **Подготовка к использованию Aspose.Cells**

1. Загрузите и установите Aspose.Cells.Zip:
   1. [Скачать Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. Разархивируйте его на своем компьютере для разработки.
 Все[Aspose](http://www.aspose.com/) компоненты при установке работают в ознакомительном режиме. Режим оценки не имеет ограничения по времени и только вставляет водяные знаки в создаваемые документы.
1. Создать проект
 1. Вы можете либо создать проект с помощью любого редактора Java, например, Eclipse, либо создать простую программу с помощью Блокнота.
1. Добавьте путь к классу:
 Чтобы установить путь к классу с помощью Eclipse:
1. Извлеките файлы Aspose.Cells.jar и dom4j_1.6.1.jar из Aspose.Cells.zip.
 1. Установите путь к классам проекта в Eclipse:
1. Выберите свой проект в Eclipse, а затем щелкните меню Project-Properties.
 1. Выберите «Java Путь сборки» в левой части всплывающего окна, затем выберите вкладку «Библиотеки», нажмите «Добавить JAR» или «Добавить внешние JAR», чтобы выбрать Aspose.Cells.jar и dom4j_1.6.1.jar и добавить их. в пути построения.
 1. Напишите приложение для вызова API компонентов Aspose.
 Или вы можете установить его во время выполнения в приглашении DOS в Windows.

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **Создание сводной таблицы**

Чтобы создать сводную таблицу с помощью Aspose.Cells:

1. Добавьте некоторые данные в ячейки листа, используя метод PutValue/setValue объекта Cell. Вы также используете файл шаблона, уже заполненный данными. Данные будут использоваться в качестве источника данных сводной таблицы.
1. Добавьте сводную таблицу на рабочий лист, вызвав метод добавления коллекции сводных таблиц (инкапсулированный в объекте рабочего листа).
1. Получите доступ к новому объекту сводной таблицы из коллекции сводных таблиц, передав его индекс.
1. Используйте любой из объектов сводной таблицы, инкапсулированных в объект сводной таблицы, для управления таблицей.

Пример кода приведен ниже. При выполнении кода создается новый файл: pivotTable_test.xls.

**Входные данные** 

![дело:изображение_альтернативный_текст](create-pivot-tables-and-pivot-charts_1.png)

**Выходная сводная таблица**

![дело:изображение_альтернативный_текст](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Создание сводной диаграммы на основе сводной таблицы**

Чтобы создать сводную диаграмму с помощью Aspose.Cells:

1. Добавьте диаграмму.
1. Установите PivotSource диаграммы для ссылки на существующую сводную таблицу в электронной таблице.
1. Установите другие атрибуты.

Ниже приведен код, используемый компонентом для выполнения задачи. При выполнении кода создается новый файл: pivotChart_test.xls.

**Лист сводной диаграммы**

![дело:изображение_альтернативный_текст](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

В этой статье показано, как создавать сводные таблицы и сводные диаграммы с помощью Aspose.Cells. Надеюсь, это поможет вам использовать эти функции в ваших собственных сценариях.

Aspose.Cells — результат многолетних исследований, проектирования и тщательной настройки.

 Будем рады вашим вопросам, комментариям и предложениям на[Aspose.Cells Форум](https://forum.aspose.com/c/cells/9). Мы гарантируем быстрый ответ.

{{% /alert %}}

## Статьи по Теме

- [Пользовательская сортировка в сводной таблице](/cells/ru/java/custom-sorting-in-pivot-table/)
- [Форматирование сводной таблицы](/cells/ru/java/formatting-pivot-table/)
- [Обновить и рассчитать сводную таблицу с вычисляемыми элементами](/cells/ru/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Отключить ленты сводной таблицы](/cells/ru/java/disable-pivot-table-ribbons/)


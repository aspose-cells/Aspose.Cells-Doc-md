---
title: Создать сводную таблицу
type: docs
weight: 10
url: /ru/java/create-pivot-table/
---
## **Создать сводную таблицу**

### **Создайте сводную таблицу, используя Aspose.Cells**

{{% alert color="primary" %}}

 С помощью Aspose.Cells можно добавлять сводные таблицы в электронные таблицы. Aspose.Cells имеет ряд специальных классов, используемых специально для создания сводных таблиц и управления ими. Эти классы используются для создания и установки свойств[**сводная таблица**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)объект, используемый в качестве строительных блоков сводной таблицы.

Объекты сводной таблицы:

- [**сводное поле**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): представляет поле в сводной таблице.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) он представляет собой набор всех[**сводное поле**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)объектов в сводной таблице.
- [**сводная таблица**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): представляет собой сводную таблицу.
- [**сводная таблицаколлекция**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): он представляет собой набор всех объектов сводной таблицы на рабочем листе.

{{% /alert %}}

### **Создание простой сводной таблицы**

Чтобы создать сводную таблицу с использованием Aspose.Cells, выполните следующие действия:

1.  Добавьте некоторые данные в ячейки рабочего листа с помощью[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) объекты[**установить значение**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)метод. Эти данные будут использоваться в качестве источника данных для сводной таблицы.
1. Добавьте сводную таблицу на рабочий лист, вызвав метод[**Добавлять**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add(com.aspose.cells.PivotTable,%20int,%20int,%20java.lang.String) ) метод[**сводная таблицаколлекция**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) класс, заключенный в[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)объект.
1.  Доступ к[**сводная таблица**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) объект из[**сводная таблицаколлекция**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) пройдя[**сводная таблица**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)показатель.
1.  Используйте любой из объектов сводной таблицы (описанных выше), инкапсулированных в[**сводная таблица**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)объект для управления сводной таблицей.

{{% alert color="primary" %}}

При назначении диапазона ячеек в качестве источника данных диапазон должен быть установлен от левого верхнего угла к правому нижнему. Например, "A1:C3" является допустимым; "C3:A1" недействителен.

{{% /alert %}}

В приведенном ниже примере кода показано, как создать простую сводную таблицу, следуя основным шагам, перечисленным выше. При выполнении кода на рабочий лист добавляется сводная таблица:

**Создание сводной таблицы на основе соответствующего поля**

![дело:изображение_альтернативный_текст](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}

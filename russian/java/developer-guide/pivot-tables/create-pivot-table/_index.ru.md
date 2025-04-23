---
title: Создание сводной таблицы
type: docs
weight: 10
url: /ru/java/create-pivot-table/
---

## **Создать сводную таблицу**

### **Создание сводной таблицы с помощью Aspose.Cells**

{{% alert color="primary" %}}

С помощью Aspose.Cells можно добавлять сводные таблицы в электронные таблицы. У Aspose.Cells есть несколько специальных классов, используемых специально для создания и управления сводными таблицами. Эти классы используются для создания и установки свойств объекта [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable), используемого в качестве строительных блоков сводной таблицы.

Объекты сводных таблиц:

- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): это представляет собой поле в сводной таблице.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): это представляет собой коллекцию всех объектов [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) в сводной таблице.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): это представляет собой сводную таблицу.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): это представляет собой коллекцию всех объектов сводных таблиц на листе.

{{% /alert %}}

### **Создание простой сводной таблицы**

Чтобы создать сводную таблицу с помощью Aspose.Cells, следуйте приведенным ниже шагам:

1. Добавьте некоторые данные в ячейки листа с помощью метода [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) объекта [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell). Эти данные будут использоваться в качестве источника данных для сводной таблицы.
1. Добавьте сводную таблицу на рабочий лист, вызвав метод [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet), инкапсулированный в объекте [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-java.lang.String-).
1. Получите объект [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) из [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection), передав индекс [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable).
1. Используйте любой из объектов сводной таблицы (объяснено выше), инкапсулированных в объекте [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable), для управления сводной таблицей.

{{% alert color="primary" %}}

При назначении диапазона ячеек в качестве источника данных диапазон должен быть установлен слева вверху и справа внизу. Например, "A1:C3" допустим; "C3:A1" недопустим.

{{% /alert %}}

Приведенный ниже пример кода показывает, как создать простую сводную таблицу, следуя основным шагам, перечисленным выше. При выполнении кода на листе добавляется сводная таблица:

**Создание сводной таблицы на основе соответствующего поля**

![todo:image_alt_text](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
{{< app/cells/assistant language="java" >}}

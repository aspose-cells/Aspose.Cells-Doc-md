---
title: Форматирование сводной таблицы
type: docs
weight: 60
url: /ru/java/formatting-pivot-table/
---

## **Внешний вид сводной таблицы**

[Как создать сводную таблицу](/cells/ru/java/create-pivot-table/) показывает, как создать простую сводную таблицу. В этой статье пойдет дальше и обсудит, как настроить внешний вид сводной таблицы, устанавливая свойства.

### **Настройка параметров формата сводной таблицы**

Класс [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) позволяет устанавливать различные параметры форматирования сводной таблицы.

#### **Установка типов автоформата и стиля сводной таблицы**

Приведенный ниже пример кода показывает, как установить тип автоформата и тип стиля сводной таблицы с использованием свойств [**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) и [**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Настройка параметров формата**

Приведенный ниже образец кода показывает, как установить ряд параметров форматирования для отчета сводной таблицы, включая добавление общих итогов для строк и столбцов.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **Настройка параметров форматирования полей сводной таблицы**

Помимо управления форматированием общей сводной таблицы, Aspose.Cells for Java позволяет тонко настраивать форматирование для строковых полей, столбцовых полей и полей страниц.

#### **Установка формата для полей строк, столбцов и страниц**

Приведенный ниже пример кода показывает, как получить доступ к полям строк, к определенной строке, установить итоги, применить автоматическую сортировку и использовать опцию автоматического отображения.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Установка формата полей данных**

Нижеприведенные строки кода иллюстрируют, как форматировать поля данных.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Изменение быстрого стиля сводной таблицы**

Приведенные ниже примеры кода показывают, как изменить быстрый стиль, примененный к сводной таблице.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Очистка полей сводной таблицы**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) имеет метод с именем [**clear()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear--), который очищает поля сводной таблицы. Используйте его для очистки полей сводной таблицы во всех областях, например странице, столбце, строке или данных.
Приведенный ниже образец кода показывает, как очистить все поля сводной таблицы в области данных.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Функция консолидации**

### **Применение функции консолидации к данным полей сводной таблицы**

Aspose.Cells можно использовать для применения функции консолидации к данным полей (или значениям) сводной таблицы. В Microsoft Excel можно щелкнуть правой кнопкой мыши поле значения, затем выбрать опцию **Настройки поля значений...**, а затем выбрать вкладку **Обобщение значений по**. Оттуда вы можете выбрать любую функцию консолидации, которая вам нравится, например, Сумма, Количество, Среднее, Максимум, Минимум, Произведение, Уникальное количество и т. д.

Aspose.Cells предоставляет перечисление [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) для поддержки следующих функций консолидации.

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**ConsolidationFunction.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT-NUMS)
- [**ConsolidationFunction.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT-COUNT)
- [**ConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**ConsolidationFunction.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD-DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD-DEVP)
- [**ConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

В следующем коде применяется функция консолидации **Среднее** к первому полю данных (или значению) и функция консолидации **Уникальное количество** ко второму полю данных (или значению).

{{% alert color="primary" %}}

Функция консолидации Уникальное количество поддерживается только Microsoft Excel 2013.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
{{< app/cells/assistant language="java" >}}

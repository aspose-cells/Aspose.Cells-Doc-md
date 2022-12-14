---
title: Форматирование сводной таблицы
type: docs
weight: 60
url: /ru/java/formatting-pivot-table/
---
## **Внешний вид сводной таблицы**

[Как создать сводную таблицу](/cells/ru/java/create-pivot-table/) показал, как создать простую сводную таблицу. Эта статья идет дальше и обсуждает, как настроить внешний вид сводной таблицы, установив свойства.

### **Настройка параметров формата сводной таблицы**

[**сводная таблица**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) class позволяет вам установить различные параметры форматирования для сводной таблицы.

#### **Установка типов AutoFormat и PivotTableStyle**

 В следующем примере кода показано, как задать тип автоматического формата и тип стиля сводной таблицы с помощью[**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) а также[**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType) характеристики.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Настройка параметров формата**

В приведенном ниже образце кода показано, как задать ряд параметров форматирования для отчета сводной таблицы, включая добавление общих итогов для строк и столбцов.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **Настройка параметров формата сводных полей**

Помимо управления форматированием всей сводной таблицы, Aspose.Cells for Java позволяет точно настроить форматирование полей строк, полей столбцов и полей страницы.

#### **Настройка формата полей строки, столбца и страницы**

В следующем примере кода показано, как получить доступ к полям строки, получить доступ к определенной строке, установить промежуточные итоги, применить автоматическую сортировку и использовать параметр autoShow.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Настройка формата полей данных**

Следующие строки кода иллюстрируют, как форматировать поля данных.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Изменение экспресс-стиля сводной таблицы**

В приведенных ниже примерах кода показано, как изменить экспресс-стиль, применяемый к сводной таблице.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Очистка сводных полей**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) имеет метод с именем[**Чисто()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear()), который очищает сводные поля. Используйте его для очистки сводных полей во всех областях, например, на странице, в столбце, в строке или в данных.
В приведенном ниже примере кода показано, как очистить все сводные поля в области данных.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Функция консолидации**

### **Применение ConsolidationFunction к полям данных сводной таблицы**

 Aspose.Cells можно использовать для применения ConsolidationFunction к полям данных (или полям значений) сводной таблицы. В Microsoft Excel вы можете щелкнуть правой кнопкой мыши поле значения и выбрать**Настройки поля значения...** вариант, а затем выберите вкладку**Суммировать значения по**. Оттуда вы можете выбрать любую функцию консолидации по вашему выбору, такую как сумма, количество, среднее, максимальное, минимальное, продукт, отчетливое количество и т. д.

 Aspose.Cells предоставляет[**Функция консолидации**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) перечисление для поддержки следующих функций консолидации.

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**Функция консолидации.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**Функция консолидации.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**Функция консолидации.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**Функция консолидации.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**Функция консолидации.МИН**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**Функция консолидации.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**Функция консолидации.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**Функция консолидации.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**Функция консолидации.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**Функция консолидации.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**Функция консолидации.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

 Применяется следующий код**Средний** функция консолидации в первое поле данных (или поле значения) и**DistinctCount** функция консолидации во второе поле данных (или поле значения).

{{% alert color="primary" %}}

Функция консолидации DistinctCount поддерживается только Microsoft Excel 2013.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}

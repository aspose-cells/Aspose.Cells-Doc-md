---
title: Форматирование сводной таблицы
type: docs
weight: 10
url: /ru/net/formatting-pivot-table/
---
## **Внешний вид сводной таблицы**

Как создать сводную таблицу объясняет, как создать простую сводную таблицу. В этой статье описывается, как настроить внешний вид сводной таблицы, установив различные свойства:

- Параметры формата сводной таблицы
- Параметры формата сводных полей
- Параметры формата поля данных

### **Настройка параметров формата сводной таблицы**

[**сводная таблица**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)class управляет общей сводной таблицей и может быть отформатирован несколькими способами.

#### **Установка типа автоформата**

Microsoft Excel предлагает ряд различных предустановленных форматов отчетов. Aspose.Cells также поддерживают эти параметры форматирования. Чтобы получить к ним доступ:

1.  Установлен[**Сводная таблица. IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) к**истинный**.
1.  Назначьте параметр форматирования из[**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype)перечисление.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **Настройка параметров формата**

В приведенном ниже примере кода показано, как отформатировать сводную таблицу, чтобы отобразить общие итоги для строк и столбцов, и как установить порядок полей отчета. Также показано, как установить строку клиента для нулевых значений.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **Форматирование Look and Feel вручную**

 Чтобы отформатировать внешний вид отчета сводной таблицы вручную, вместо использования предустановленных форматов отчета используйте[**Сводная таблица.Формат()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) а также[**Сводная таблица.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall)методы. Создайте объект стиля для желаемого форматирования, например:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **Настройка параметров формата сводного поля**

[**сводное поле**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)class представляет собой поле в сводной таблице и может быть отформатировано несколькими способами. Пример кода ниже показывает, как:

- Доступ к полям строки.
- Установка промежуточных итогов.
- Настройка автосортировки.
- Настройка автошоу.

#### **Настройка формата полей строки/столбца/страницы**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **Настройка формата полей данных**

В приведенном ниже примере кода показано, как задать форматы отображения и числовой формат для полей данных.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **Очистка сводных полей**

[**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) имеет метод с именем[**Чистый()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear)что позволяет очистить сводные поля. Используйте его, когда хотите очистить все сводные поля в областях, например, страница, столбец, строка или данные.
В приведенном ниже примере кода показано, как очистить все сводные поля в области данных.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}

---
title: Форматирование сводной таблицы
type: docs
weight: 10
url: /ru/net/formatting-pivot-table/
description: Как отформатировать сводную таблицу с помощью Aspose.Cells for Python via .NET.
keywords: Format pivot table.
---
##  **Внешний вид сводной таблицы**

Как создать сводную таблицу объясняет, как создать простую сводную таблицу. В этой статье описывается, как настроить внешний вид сводной таблицы, задав различные свойства:

- Параметры формата сводной таблицы
- Параметры формата сводных полей
- Параметры формата поля данных

###  **Настройка параметров формата сводной таблицы**

[**Сводная таблица**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)Класс управляет всей сводной таблицей и может быть отформатирован несколькими способами.

####  **Установка типа автоформата**

Microsoft Excel предлагает ряд различных предустановленных форматов отчетов. Aspose.Cells for Python via .NET также поддерживают эти параметры форматирования. Чтобы получить к ним доступ:

1.  Набор[**PivotTable.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/)на *истину**.
1.  Назначьте параметр форматирования из[**PivotTableAutoFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/)перечисление.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

####  **Настройка параметров формата**

В приведенном ниже примере кода показано, как отформатировать сводную таблицу для отображения общих итогов по строкам и столбцам, а также как установить порядок полей отчета. Он также показывает, как установить строку клиента для нулевых значений.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

####  **Форматирование внешнего вида вручную**

Чтобы отформатировать внешний вид отчета сводной таблицы вручную, вместо использования заранее установленных форматов отчета, используйте команду[**PivotTable.format_all(стиль)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) и[**PivotTable.format(строка, столбец, стиль)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/)методы. Создайте объект стиля для желаемого форматирования, например:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

###  **Настройка параметров формата сводного поля**

[**Сводное поле**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)class представляет поле в сводной таблице и может быть отформатирован несколькими способами. В приведенном ниже примере кода показано, как:

- Доступ к полям строк.
- Установка промежуточных итогов.
- Настройка автосортировки.
- Настройка автошоу.

####  **Настройка формата полей строки/столбца/страницы**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

###  **Настройка формата полей данных**

В приведенном ниже примере кода показано, как настроить форматы отображения и числовой формат для полей данных.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

###  **Очистка сводных полей**

[**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) имеет метод с именем[**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#)это позволяет очищать поля сводной таблицы. Используйте его, если хотите очистить все сводные поля в областях, например, на странице, столбце, строке или данных.
В приведенном ниже примере кода показано, как очистить все поля сводной таблицы в области данных.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}

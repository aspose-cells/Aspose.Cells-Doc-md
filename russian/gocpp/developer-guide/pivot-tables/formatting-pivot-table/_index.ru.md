---
title: Форматирование сводной таблицы с Golang через C++
linktitle: Форматирование сводной таблицы
type: docs
weight: 10
url: /ru/go-cpp/formatting-pivot-table/
description: Научитесь настраивать внешний вид сводных таблиц с помощью Aspose.Cells for C++.
---

## **Внешний вид сводной таблицы**

Как создать сводную таблицу объясняет, как создать простую сводную таблицу. В этой статье описано, как настроить внешний вид сводной таблицы, устанавливая различные свойства:

- Опции формата сводной таблицы
- Опции формата полей сводной таблицы
- Опции формата данных поля

### **Настройка параметров формата сводной таблицы**

Класс [**PivotTable**](https://reference.aspose.com/cells/go-cpp/pivottable/) контролирует общую сводную таблицу и может быть отформатирован различными способами.

#### **Установка типа автоформата**

Microsoft Excel предлагает множество предустановленных форматов отчетов. Aspose.Cells также поддерживает эти параметры форматирования. Чтобы получить к ним доступ:

1. Установите [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/go-cpp/pivottable/isautoformat/) в **true**.
1. Назначьте опцию форматирования из перечисления [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/go-cpp/pivottableautoformattype/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable.go" >}}
#### **Настройка параметров формата**

Образец кода ниже показывает, как отформатировать сводную таблицу для отображения итоговых сумм по строкам и столбцам, а также как задать порядок полей отчета. Он также показывает, как установить пользовательскую строку для null значений.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-1.go" >}}
#### **Форматирование внешнего вида вручную**

Для ручного форматирования вида отчета сводной таблицы вместо использования предустановленных форматов используйте методы [**PivotTable.Format()**](https://reference.aspose.com/cells/go-cpp/pivottable/format_pivotarea_style/) и [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/). Создайте объект стиля для желаемого форматирования, например:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-2.go" >}}
### **Настройка параметров формата поля сводной таблицы**

Класс [**PivotField**](https://reference.aspose.com/cells/go-cpp/pivotfield/) представляет собой поле в сводной таблице и может быть отформатировано несколькими способами. Приведенный ниже образец кода показывает, как:

- Получить строковые поля.
- Настроить итоги.
- Настроить автосортировку.
- Настроить автоотображение.

#### **Настройка формата полей строки/столбца/страницы**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-3.go" >}}
### **Установка формата полей данных**

Приведенный ниже образец кода показывает, как установить формат отображения и числовой формат для полей данных.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-4.go" >}}
### **Очистка полей сводной таблицы**

У класса [**PivotFieldCollection**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/) есть метод с именем [**Clear()**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/clear/), который позволяет очистить поля сводной таблицы. Используйте его, когда вам нужно очистить все поля сводной таблицы в областях, например страница, столбец, строка или данные.
Приведенный ниже образец кода показывает, как очистить все поля сводной таблицы в области данных.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-5.go" >}}

---
title: Установка режима расчета формул в книге Excel
description: В этой статье рассматривается, как установить режим вычисления формул в книге в Microsoft Excel с помощью библиотеки Aspose.Cells. Загрузив существующий файл Excel или создав новый файл Excel, мы можем использовать метод, предоставленный Aspose.Cells, для установки режима вычисления формул и получения результата. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, книга, режим вычисления формул, настройки
type: docs
weight: 110
url: /ru/net/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

В Microsoft Excel вы можете установить режим вычисления формул, то есть способ, которым происходит вычисление формул. Существуют три возможных значения:

- Автоматический - пересчитывать при изменении чего-либо и каждый раз при открытии книги.
- Автоматический, за исключением таблиц данных - пересчитывать при изменении чего-либо, но исключая таблицы данных.
- Ручной - пересчитывать только при явном запросе пользователя нажатием F9 или CTRL+ALT+F9, или при сохранении книги.

{{% /alert %}}

Для установки режима вычисления формул в Microsoft Excel:

1. Выберите **Формулы**, а затем **Параметры расчета**.
1. Выберите один из вариантов.

Aspose.Cells также позволяет установить **Режим вычисления формул** с использованием свойства режима [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode). Вы можете назначить ему перечисление [**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype), которое имеет одно из следующих значений:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}

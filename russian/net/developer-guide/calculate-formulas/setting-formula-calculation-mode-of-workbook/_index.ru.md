---
title: Настройка режима расчета формулы в рабочей книге
description: В этой статье рассказывается, как настроить режим вычисления формулы в книге в Excel Microsoft с библиотекой Aspose.Cells. Загрузив существующий файл Excel или создав новый файл Excel, мы можем использовать метод, предоставленный Aspose.Cells, чтобы установить режим расчета формулы и получить результат. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, workbook, formula calculation mode, settings
type: docs
weight: 110
url: /ru/net/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel позволяет задать режим расчета формул, то есть способ расчета формул. Возможны три значения:

- Автоматически — перерасчет при каждом изменении чего-либо и при каждом открытии книги.
- Автоматически, за исключением таблиц данных: перерасчет при каждом изменении, но таблицы данных не учитываются.
- Ручной — пересчет выполняется только тогда, когда пользователь явно запрашивает это, нажав F9 или CTRL+ALT+F9, или при сохранении книги.

{{% /alert %}}

Чтобы установить режим расчета формулы в Excel Microsoft:

1.  Выбирать**Формулы** а затем *Параметры расчета**.
1. Выберите один из вариантов.

 Aspose.Cells также позволяет установить**Режим расчета формулы** с использованием[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) свойство режима. Вы можете назначить ему[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)перечисление, которое имеет одно из следующих значений:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}

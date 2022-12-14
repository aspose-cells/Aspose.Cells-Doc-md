---
title: Настройка режима вычисления формулы в книге
type: docs
weight: 110
url: /ru/net/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel позволяет установить режим расчета формулы, то есть способ расчета формулы. Возможны три значения:

- Автоматически — пересчитывать всякий раз, когда что-то изменяется и каждый раз, когда открывается рабочая книга.
- Автоматически, за исключением таблиц данных — пересчитывать всякий раз, когда что-то изменяется, но исключая таблицы данных.
- Вручную — пересчитывать только тогда, когда пользователь явно запрашивает его, нажав F9 или CTRL+ALT+F9, или при сохранении книги.

{{% /alert %}}

Чтобы установить режим вычисления формулы в Microsoft Excel:

1.  Выбирать**Формулы** а потом**Варианты расчета**.
1. Выберите один из вариантов.

 Aspose.Cells также позволяет установить**Режим вычисления формулы** с использованием[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) свойство режима. Вы можете назначить ему[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)перечисление, имеющее одно из следующих значений:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}

---
title: Настройка режима вычисления формулы в книге
type: docs
weight: 130
url: /ru/java/setting-formula-calculation-mode-of-workbook/
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

 Aspose.Cells также позволяет установить**Режим вычисления формулы** с использованием[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode) имущество. Вы можете назначить ему[**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType)перечисление, имеющее одно из следующих значений:

- [**CalcModeType.АВТОМАТИЧЕСКИЙ**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

 В следующем примере кода сначала создается рабочая книга, а затем устанавливается режим расчета формулы**Руководство** и сохраняет книгу как выходной файл Excel на диске.

**Выходной файл. Обратите внимание на режим вычисления формулы.**

![дело:изображение_альтернативный_текст](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}

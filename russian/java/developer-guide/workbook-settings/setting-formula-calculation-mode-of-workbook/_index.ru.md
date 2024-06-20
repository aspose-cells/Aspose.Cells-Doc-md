---
title: Установка режима расчета формул в книге Excel
type: docs
weight: 130
url: /ru/java/setting-formula-calculation-mode-of-workbook/
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

Aspose.Cells также позволяет установить **Режим расчета формул** с использованием свойства [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode). Вы можете присвоить ему перечисление [**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType), которое имеет одно из следующих значений:

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

В следующем примере кода сначала создается книга, затем устанавливается режим расчета формул на **Ручной** и сохраняется книга как файл Excel на диске.

**Выходной файл. Обратите внимание на режим расчета формул.**

![todo:image_alt_text](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}

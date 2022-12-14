---
title: Укажите, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы.
type: docs
weight: 80
url: /ru/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}}

 Aspose.Cells обеспечивает[**PivotTable.IsExcel2003Совместимый**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)свойство, которое можно использовать, чтобы указать, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы. Если true, строка должна быть меньше или равна 255 символам, поэтому, если строка больше 255 символов, она будет усечена. Если**ЛОЖЬ** , строка не будет иметь вышеупомянутого ограничения. Значение по умолчанию**истинный**.

{{% /alert %}}

## **Укажите, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы.**

 В следующем примере кода объясняется использование[**PivotTable.IsExcel2003Совместимый**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) имущество. Исходная строка имеет длину 383 символа. Но когда[**PivotTable.IsExcel2003Совместимый**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) свойство установлено**истинный** и сводная таблица обновляется, данные ячейки B5 сводной таблицы усекаются и становятся 255 символов. Однако, когда[**PivotTable.IsExcel2003Совместимый**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) свойство установлено**ЛОЖЬ** и сводная таблица снова обновляется, данные ячейки B5 сводной таблицы не усекаются и остаются длиной 383 символа. Пожалуйста, прочтите комментарии внутри кода, чтобы лучше понять это свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}

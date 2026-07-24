---
title: Укажите, совместим ли сводная таблица с Excel2003 при обновлении сводной таблицы
type: docs
weight: 80
url: /ru/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет свойство [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible), которое может быть использовано для указания, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы. Если значение true, строка должна быть не более 255 символов, поэтому, если строка больше 255 символов, она будет усечена. Если **false**, строка не будет иметь вышеперечисленного ограничения. Значение по умолчанию - **true**.

{{% /alert %}}

## **Укажите, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы**

В следующем примере кода объясняется использование свойства [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible). Оригинальная строка имеет длину 383 символа. Но когда свойство [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) установлено **true** и обновляется сводная таблица, данные ячейки B5 сводной таблицы усекаются и становятся длиной 255 символов. Однако, когда свойство [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) установлено **false** и сводная таблица снова обновляется, данные ячейки B5 сводной таблицы не усекаются и остаются длиной 383 символа. Пожалуйста, прочтите комментарии внутри кода для лучшего понимания этого свойства.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

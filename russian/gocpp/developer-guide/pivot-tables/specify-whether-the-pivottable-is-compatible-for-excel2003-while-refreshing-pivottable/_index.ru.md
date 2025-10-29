---
title: Указать, совместима ли сводная таблица с Excel 2003 при обновлении с помощью Golang через C++
linktitle: Укажите совместимость с Excel 2003 в сводной таблице
type: docs
weight: 80
url: /ru/go-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Узнайте, как указать совместимость сводной таблицы с Excel 2003 с помощью Aspose.Cells for C++ при обновлении сводной таблицы.
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет свойство [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/), которое может быть использовано для указания, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы. Если значение true, строка должна быть не более 255 символов, поэтому, если строка больше 255 символов, она будет усечена. Если **false**, строка не будет иметь вышеперечисленного ограничения. Значение по умолчанию - **true**.

{{% /alert %}}

## **Укажите, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы**

В следующем примере кода объясняется использование свойства [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/). Оригинальная строка имеет длину 383 символа. Но когда свойство [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/) установлено **true** и обновляется сводная таблица, данные ячейки B5 сводной таблицы усекаются и становятся длиной 255 символов. Однако, когда свойство [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/) установлено **false** и сводная таблица снова обновляется, данные ячейки B5 сводной таблицы не усекаются и остаются длиной 383 символа. Пожалуйста, прочтите комментарии внутри кода для лучшего понимания этого свойства.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyWhetherThePivottableIsCompatibleForExcel2003WhileRefreshingPivottable.go" >}}

---
title: Укажите, совместим ли сводная таблица с Excel2003 при обновлении сводной таблицы
type: docs
weight: 80
url: /ru/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Эта статья показывает, как указать, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы с помощью Aspose.Cells для Python via .NET.
keywords: Aspose.Cells для Python Excel, библиотека Excel Python, укажите, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET предоставляет свойство [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/), которое можно использовать для указания совместимости сводной таблицы с Excel2003 при обновлении сводной таблицы. Если true, строка должна быть менее или равна 255 символам, поэтому, если строка превышает 255 символов, она будет усечена. Если **false**, строка не будет иметь вышеупомянутого ограничения. Значение по умолчанию - **true**.

{{% /alert %}}

## **Как указать, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы**

В следующем примере кода объясняется использование свойства [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/). Оригинальная строка имеет длину 383 символа. Но когда свойство [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) установлено **true** и обновляется сводная таблица, данные ячейки B5 сводной таблицы усекаются и становятся длиной 255 символов. Однако, когда свойство [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) установлено **false** и сводная таблица снова обновляется, данные ячейки B5 сводной таблицы не усекаются и остаются длиной 383 символа. Пожалуйста, прочтите комментарии внутри кода для лучшего понимания этого свойства.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}

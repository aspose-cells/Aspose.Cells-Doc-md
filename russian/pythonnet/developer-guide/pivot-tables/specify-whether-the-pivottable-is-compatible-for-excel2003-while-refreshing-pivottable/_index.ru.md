---
title: Укажите, совместима ли сводная таблица с Excel2003, при обновлении сводной таблицы.
type: docs
weight: 80
url: /ru/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: В этой статье показано, как указать, совместима ли сводная таблица с Excel2003, при обновлении сводной таблицы с помощью Aspose.Cells for Python via .NET.
keywords: Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET обеспечивает[**PivotTable.is_excel_2003_совместимый**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) Свойство, которое можно использовать, чтобы указать, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы. Если это правда, строка должна быть меньше или равна 255 символам, поэтому, если строка больше 255 символов, она будет усечена. Если *false**, строка не будет иметь вышеупомянутое ограничение. Значение по умолчанию верно**.

{{% /alert %}}

##  **Укажите, совместима ли сводная таблица с Excel2003, при обновлении сводной таблицы.**

 В следующем примере кода объясняется использование[**PivotTable.is_excel_2003_совместимый**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) свойство. Исходная строка имеет длину 383 символа. Но когда[**PivotTable.is_excel_2003_совместимый**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) свойство установлено**истинный** и сводная таблица обновляется, данные ячейки B5 сводной таблицы усекаются и становятся длиной 255 символов. Однако, когда[**PivotTable.is_excel_2003_совместимый**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) свойство установлено**ЛОЖЬ**и сводная таблица снова обновляется, данные ячейки B5 сводной таблицы не обрезаются и остаются длиной 383 символа. Пожалуйста, прочитайте комментарии внутри кода, чтобы лучше понять это свойство.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}

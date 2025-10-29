---
title: 设置公式  针对非英语用户的注意事项
type: docs
weight: 10
url: /zh/python-net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

 Aspose.Cells for Python via .NET 支持大部分微软Excel内的公式/函数。开发者可以通过API或 [designer spreadsheets](/cells/zh/net/what-is-a-designer-spreadsheet/) 使用这些公式。它支持大量的数学、字符串、布尔值、日期/时间、统计、数据库、查找和引用公式。这些公式应使用英语（美国）样式编写。

{{% /alert %}} 

## **非英语用户注意事项**
 使用Aspose.Cells for Python via .NET 时，非英语用户在创建公式时必须遵循的两个建议是：

1. 公式必须使用英语输入。例如，使用英语"=SUM()"而不是德语"=SUMME()"。
 1. 始终使用逗号（,）来分隔函数参数。在某些语言设置中，参数分隔符可能是分号（；），但Aspose.Cells for Python via .NET 使用英语样式的逗号。例如，应写成 "=IF (C5=0,0,C3/C4)"，而不是 "=IF(C5=0;0;C3/C4)"。

{{< app/cells/assistant language="python-net" >}}

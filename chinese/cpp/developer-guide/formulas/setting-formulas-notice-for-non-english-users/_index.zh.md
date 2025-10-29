---
title: 设置公式  非英语用户的注意事项（用 C++）
linktitle: 设置公式  针对非英语用户的注意事项
type: docs
weight: 10
url: /zh/cpp/setting-formulas-notice-for-non-english-users/
description: 学习如何在 Aspose.Cells for C++ 中为非英语用户设置符合英语（美国）风格的公式。
---

{{% alert color="primary" %}} 

Aspose.Cells 支持 Microsoft Excel 大部分的公式/函数。开发者可以通过 API 或 [设计者电子表格](/cells/zh/cpp/what-is-a-designer-spreadsheet/) 使用这些公式。Aspose.Cells 支持大量的数学、字符串、布尔、日期/时间、统计、数据库、查找及引用公式。这些公式应使用英语（美国）风格指定。

{{% /alert %}} 

## **非英语用户注意事项**
创建使用Aspose.Cells创建公式时，非英语用户必须遵循两个提示。

1. 公式必须使用英语输入。例如，使用英语"=SUM()"而不是德语"=SUMME()"。
1. 始终使用逗号(,)分隔函数参数。在某些语言选项或设置中，函数参数的分隔符是分号，但 Aspose.Cells 使用英语样式的逗号。例如，使用 "=IF (C5=0,0,C3/C4)"，而不是 "=IF(C5=0;0;C3/C4)"。
{{< app/cells/assistant language="cpp" >}}

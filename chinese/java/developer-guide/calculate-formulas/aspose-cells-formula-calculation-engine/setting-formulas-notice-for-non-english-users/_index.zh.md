---
title: 设置公式 - 非英语用户注意事项
type: docs
weight: 20
url: /zh/java/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells 支持 Microsoft Excel 中的大多数公式/函数。开发人员可以在 API 或[设计人员电子表格](/cells/zh/java/what-is-a-designer-spreadsheet/) 中使用这些公式。 Aspose.Cells 支持大量的数学、字符串、布尔、日期/时间、统计、数据库、查找和引用公式。 这些公式应使用英文(美式)格式进行指定。

使用Aspose.Cells创建公式时，非英语用户必须遵循两个提示：

1. 公式必须用英文输入。
   例如，使用英文"=SUM()"而不是德文"=SUMME()"。
1. 始终使用逗号(,)分隔函数参数。
   对于某些语言选项或设置，函数参数的分隔符是分号，但 Aspose.Cells 使用英文样式的逗号。例如，使用"=IF (C5=0,0,C3/C4)"而不是"=IF(C5=0;0;C3/C4)" 

{{% /alert %}}

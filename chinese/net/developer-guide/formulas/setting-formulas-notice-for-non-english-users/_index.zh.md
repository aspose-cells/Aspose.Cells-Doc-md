---
title: 设置公式 - 非英语用户须知
type: docs
weight: 10
url: /zh/net/setting-formulas-notice-for-non-english-users/
---
{{% alert color="primary" %}} 

Aspose.Cells 支持 Microsoft Excel 中的大部分公式/函数。开发人员可以将这些公式与 API 或[设计师电子表格](/cells/zh/net/what-is-a-designer-spreadsheet/)Aspose.Cells 支持大量的数学、字符串、布尔、日期/时间、统计、数据库、查找和参考公式。应使用英语（美国）样式指定公式。

{{% /alert %}} 
## **非英语用户须知**
使用 Aspose.Cells 创建公式时，非英语用户必须遵循两个提示：

1. 公式必须用英文输入。例如，使用英语“=SUM()”而不是德语“=SUMME()”。
1. 始终使用逗号 (,) 来分隔函数参数。对于某些语言选项或设置，功能参数的分隔符是分号，但 Aspose.Cells 使用英文逗号。例如，使用“=IF (C5=0,0,C3/C4)”而不是“=IF(C5=0;0;C3/C4)”

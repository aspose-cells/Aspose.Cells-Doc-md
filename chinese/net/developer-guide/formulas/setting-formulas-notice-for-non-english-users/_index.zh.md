---
title: 设置公式 - 非英语用户注意事项
type: docs
weight: 10
url: /zh/net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells 支持 Microsoft Excel 的大多数公式/函数。开发者可以在 API 或设计电子表格中使用这些公式。Aspose.Cells 支持大量数学、字符串、布尔值、日期/时间、统计、数据库、查找和引用型公式。这些公式应使用英语（美国）风格指定。

{{% /alert %}} 
## **非英语用户注意事项**
使用Aspose.Cells创建公式时，非英语用户必须遵循两个提示：

1. 公式必须用英语输入。例如，使用英文"=SUM()"而不是德文"=SUMME()"。
1. 总是使用逗号（,）分隔函数参数。对于某些语言选项或设置，函数参数的分隔符可能是分号，但Aspose.Cells使用英文风格逗号。例如，使用"=IF(C5=0,0,C3/C4)"而不是"=IF(C5=0;0;C3/C4)"。

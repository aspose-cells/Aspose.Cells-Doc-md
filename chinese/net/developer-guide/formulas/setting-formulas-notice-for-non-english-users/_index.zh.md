---
title: 设置公式  针对非英语用户的注意事项
type: docs
weight: 10
url: /zh/net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells支持Microsoft Excel的大多数公式/函数。开发人员可以使用这些公式与API或[设计者电子表格](/cells/zh/net/what-is-a-designer-spreadsheet/)一起使用。Aspose.Cells支持大量的数学、字符串、布尔、日期/时间、统计、数据库、查找和引用公式。公式应该使用英语（美国）风格指定。

{{% /alert %}} 
## **非英语用户注意事项**
创建使用Aspose.Cells创建公式时，非英语用户必须遵循两个提示。

1. 公式必须使用英语输入。例如，使用英语"=SUM()"而不是德语"=SUMME()"。
2. 始终使用逗号（，）来分隔函数参数。对于某些语言选项或设置，函数参数的分隔符可能是分号，但Aspose.Cells使用英语风格的逗号。例如，使用"=IF(C5=0,0,C3/C4)"而不是"=IF(C5=0;0;C3/C4)"。

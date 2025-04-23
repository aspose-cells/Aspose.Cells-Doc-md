---
title: 设置公式  针对非英语用户的注意事项
type: docs
weight: 20
url: /zh/java/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells支持大多数Microsoft Excel中的公式/函数。开发人员可以使用API或[设计师电子表格](/cells/zh/java/what-is-a-designer-spreadsheet/)使用这些公式。 Aspose.Cells支持庞大的数学、字符串、布尔、日期/时间、统计、数据库、查找和引用公式。这些公式应该使用英文(美式)样式指定。

创建使用Aspose.Cells创建公式时，非英语用户必须遵循两个提示。

1. 公式必须以英文输入。
   例如，使用英文"=SUM()"而不是德文"=SUMME()"。
1. 总是使用逗号(,)来分隔函数参数。
   对于某些语言选项或设置，函数参数的分隔符是分号，但Aspose.Cells使用英文风格的逗号。例如，使用"=IF (C5=0,0,C3/C4)"而不是"=IF(C5=0;0;C3/C4)"。 

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

---
title: 设置公式  非英语用户注意事项（Node.js + C++）
linktitle: 设置公式  针对非英语用户的注意事项
type: docs
weight: 10
url: /zh/nodejs-cpp/setting-formulas-notice-for-non-english-users/
---  

{{% alert color="primary" %}} 

Aspose.Cells 支持大部分Microsoft Excel中的公式/函数。开发者可以使用这些公式，结合API或[设计师电子表格](/cells/zh/nodejs-cpp/what-is-a-designer-spreadsheet/)。Aspose.Cells支持大量的数学、字符串、布尔值、日期/时间、统计、数据库、查找和引用公式。这些公式应使用英语（美国）风格指定。

{{% /alert %}} 

## **非英语用户注意事项**
创建使用Aspose.Cells创建公式时，非英语用户必须遵循两个提示。

1. 公式必须使用英语输入。例如，使用英语"=SUM()"而不是德语"=SUMME()"。
1. 始终使用逗号(,)分隔函数参数。在某些语言选项或设置中，函数参数的分隔符是分号，但 Aspose.Cells 使用英语样式的逗号。例如，使用 "=IF (C5=0,0,C3/C4)"，而不是 "=IF(C5=0;0;C3/C4)"。  
{{< app/cells/assistant language="nodejs-cpp" >}}

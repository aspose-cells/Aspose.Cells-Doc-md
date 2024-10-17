---
title: Setting Formulas - Notice for Non English Users
type: docs
weight: 10
url: /python-net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET supports most of the formulas/functions that are part of Microsoft Excel. Developers can use these formulas with either the API or [designer spreadsheets](/cells/net/what-is-a-designer-spreadsheet/). Aspose.Cells for Python via .NET supports a huge set of mathematical, string, Boolean, date/time, statistical, database, lookup and reference formulas. The formulas should be specified using English (US) style.

{{% /alert %}} 

## **Notice for Non English Users**
There are two tips that non-English users must follow when creating formulas with Aspose.Cells for Python via .NET:

1. Formulas must be entered in English. For example, use the English "=SUM()" not the German "=SUMME()".
1. Always use a comma (,) to delimit function parameters. For some language options or settings, the delimiter for function parameters is a semicolon but Aspose.Cells for Python via .NET uses the English style comma. For example, use "=IF (C5=0,0,C3/C4)" not "=IF(C5=0;0;C3/C4)"
{{< app/cells/assistant language="csharp" >}}

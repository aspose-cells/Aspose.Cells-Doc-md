---
title: إضافة حماية في ورقة العمل
type: docs
weight: 130
url: /ar/net/aspose-cells-griddesktop/adding-cell-protection-in-worksheet/
keywords: الجريد الأدنى,الحماية
description: يقدم هذا المقال كيفية حماية الخلايا في ورقة العمل في الجريد الأدنى.
---

{{% alert color="primary" %}} 

Aspose.Cells لجريد الأدنى يسمح لك بحماية الخلايا في ورقة العمل. أولاً، تحتاج إلى حماية ورقة العمل الخاصة بك، ثم يمكنك حماية الخلايا المرغوبة في ورقة العمل. من أجل حماية الورقة، يرجى ضبط خاصية **Worksheet.Protected** على true، ثم استخدام طريقة **Worksheet.SetProtected()** لحماية نطاق الخلايا.

{{% /alert %}} 
## **حماية الخلية باستخدام Aspose.Cells.GridDesktop**
الشيفرة العينية التالية تحمي كل الخلايا في النطاق **A1:B1** من ورقة العمل النشطة في الجريد الأدنى. عند النقر المزدوج على أي خلية في هذا النطاق، لن تتمكن من تحريرها. ستجعل هذه الخلايا للقراءة فقط.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}

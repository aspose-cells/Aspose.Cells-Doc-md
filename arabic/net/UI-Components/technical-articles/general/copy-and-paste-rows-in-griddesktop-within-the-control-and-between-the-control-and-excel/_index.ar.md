---
title: نسخ ولصق الصفوف في GridDesktop داخل عنصر التحكم وبين Control و Excel
type: docs
weight: 70
url: /ar/net/copy-and-paste-rows-in-griddesktop-within-the-control-and-between-the-control-and-excel/
---
{{% alert color="primary" %}} 

إذا كنت ترغب في تمكين نسخ ولصق الصفوف في GridDesktop ضمن عنصر التحكم أو بين control و excel ، فالرجاء ضبط الخاصية GridDesktop.ClipboardCopyPaste على true. يمكنك ضبط هذه الخاصية في وقت التصميم أو في الكود. القيمة الافتراضية لهذه الخاصية هي كاذبة. حاليًا ، يمكنه فقط نسخ قيم الخلية ولصقها ولن ينسخ أي إعداد آخر للخلية مثل التنسيق ونمط الحدود وما إلى ذلك.

{{% /alert %}} 
## **إعداد خاصية GridDesktop.ClipboardCopyPaste في Design Mode و Run Time**
 يعيّن نموذج التعليمات البرمجية التالي الخاصية GridDesktop.ClipboardCopyPaste بتنسيق**مدة العرض**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-CopyAndPasteRows-1.cs" >}}

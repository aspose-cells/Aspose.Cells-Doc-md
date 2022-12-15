---
title: قم بإضافة ورقة عمل أو إدراجها
type: docs
weight: 20
url: /ar/net/add-or-insert-a-worksheet/
---
{{% alert color="primary" %}} 

في هذا الموضوع ، سنناقش تقنيات إضافة أوراق العمل أو إدراجها في ملف Excel باستخدام Aspose.Cells.GridDesktop. الفرق بين إضافة أوراق العمل وإدراجها هو أنه بالإضافة إلى ذلك ، تتم إضافة ورقة العمل ببساطة في نهاية مجموعة أوراق العمل الخاصة بملف Excel ، لكن الإدراج يعني إضافة ورقة عمل إلى موضع معين في مجموعة أوراق العمل.

{{% /alert %}} 
## **إضافة ورقة عمل**
لإضافة ورقة عمل باستخدام Aspose.Cells.GridDesktop ، يرجى اتباع الخطوات التالية:

1. أضف Aspose.Cells.GridDesktop control إلى نموذج.
1. قم باستدعاء الأسلوب Add الخاص بمجموعة ورقة العمل في عنصر تحكم GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


تتوفر العديد من الإصدارات المحملة بشكل زائد من طريقة Add. باستخدام الإصدار الزائد أعلاه ، على سبيل المثال ، تتم إضافة ورقة عمل إلى ملف Excel باسم ورقة افتراضي. باستخدام إصدارات أخرى محملة بشكل زائد من طريقة Add ، من الممكن تحديد الاسم كما هو موضح أدناه في المثال.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **إدراج ورقة عمل**
لإدراج ورقة عمل باستخدام Aspose.Cells.GridDesktop ، يرجى اتباع الخطوات التالية:

1. قم باضافة Aspose.Cells.GridDesktop control الى نموذج.
1. قم باستدعاء الأسلوب Insert الخاص بمجموعة أوراق العمل في عنصر تحكم GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

هام: يدعم Microsoft Excel (97-2003 XLS) أوراق Excel بما يصل إلى 65536 صفًا و 256 عمودًا. Aspose.Cells.GridDesktop يتبع نفس المعايير. في Aspose.Cells.GridDesktop control ، يمكن للمطورين إضافة أو إدراج أوراق عمل تحتوي على صفوف وأعمدة أكثر من الحد القياسي ولكن عندما يحاولون حفظ بيانات الشبكة في ملف Excel ، سيتم طرح استثناء. هذا يعني أنه يمكن حفظ البيانات الموجودة في 65536 صفًا و 256 عمودًا فقط في ملف Excel XLS باستخدام Aspose.Cells.GridDesktop ، إذا كنت تستخدم تنسيق ملف XLSX (MS Excel 2007/2010) ، فلا يوجد مثل هذا القيد.

{{% /alert %}}

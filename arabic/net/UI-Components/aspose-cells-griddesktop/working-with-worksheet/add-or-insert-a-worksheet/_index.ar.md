---
title: إضافة أو إدراج ورقة عمل
type: docs
weight: 20
url: /ar/net/aspose-cells-griddesktop/add-or-insert-a-worksheet/
keywords: GridDesktop ، إدراج ، ورقة عمل ، إدراج ورقة عمل
description: يقدم هذا المقال كيفية إضافة أو إدراج ورقة عمل في GridDesktop.
---

{{% alert color="primary" %}} 

في هذا الموضوع، سنناقش التقنيات لإضافة أو إدراج ورقات عمل في ملف Excel باستخدام Aspose.Cells.GridDesktop. الفرق بين إضافة وإدراج الورقات العمل هو أنه بالإضافة، يتم ببساطة إضافة ورقة عمل في نهاية مجموعة ورقات العمل من ملف Excel، بينما إدراج يعني إضافة ورقة عمل إلى موقع محدد في مجموعة ورقات العمل.

{{% /alert %}} 
## **إضافة ورقة عمل**
لإضافة ورقة عمل باستخدام Aspose.Cells.GridDesktop، يُرجى اتباع الخطوات التالية:

1. أضف تحكم Aspose.Cells.GridDesktop إلى نموذج.
2. استدعاء طريقة Add في مجموعة الورقات في تحكم GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


تتوفر العديد من الإصدارات المتحملة لطريقة Add. باستخدام الإصدار المتحمل أعلاه، على سبيل المثال، يتم إضافة ورقة عمل إلى ملف Excel باسم ورقة افتراضي. باستخدام إصدارات أخرى من طريقة Add، من الممكن تعريف الاسم كما هو موضح أدناه في المثال.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **إدراج ورقة عمل**
لإدراج ورقة عمل باستخدام Aspose.Cells.GridDesktop، يرجى اتباع الخطوات التالية:

1. أضف تحكم Aspose.Cells.GridDesktop إلى نموذج.
1. استدعاء طريقة الإدراج في مجموعة الأوراق داخل عنصر التحكم GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

مهم: يدعم Microsoft Excel (XLS 97-2003) أوراق Excel بحتى 65,536 صف و 256 عمود. تتبع Aspose.Cells.GridDesktop نفس المعايير. في عنصر التحكم Aspose.Cells.GridDesktop، يمكن للمطورين إضافة أو إدراج أوراق عمل بمزيد من الصفوف والأعمدة من الحد القياسي ولكن عند محاولة حفظ بيانات الشبكة إلى ملف Excel، سيتم رمي استثناء. يعني ذلك أنه يمكن حفظ البيانات فقط التي تحتوي على 65,536 صف و 256 عمود إلى ملف Excel XLS باستخدام عنصر التحكم Aspose.Cells.GridDesktop. إذا استخدمت XLSX (MS Excel 2007/2010)، فليس هناك قيد من هذا القبيل.

{{% /alert %}}

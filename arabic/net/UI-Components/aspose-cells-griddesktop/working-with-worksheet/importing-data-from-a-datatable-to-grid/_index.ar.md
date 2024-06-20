---
title: استيراد البيانات من كائن DataTable إلى الشبكة
type: docs
weight: 50
url: /ar/net/aspose-cells-griddesktop/import-data-from-a-datatable-to-grid/
keywords: Aspose.Cells.GridDesktop، وارد، بيانات، جدول
description: يقدم هذا المقال كيفية استيراد البيانات في GridDesktop.
---

{{% alert color="primary" %}} 

منذ إطلاق إطار العمل .NET، قدمت مايكروسوفت طريقة ممتازة لتخزين البيانات في الوضع دون الاتصال في شكل كائن DataTable. مع فهم احتياجات المطورين، يدعم Aspose.Cells.GridDesktop أيضًا استيراد البيانات من كائن DataTable. يناقش هذا الموضوع كيفية القيام بذلك.

{{% /alert %}} 
## **مثال**
لتوريد محتويات جدول البيانات باستخدام عنصر تحكم Aspose.Cells.GridDesktop:

1. أضف تحكم Aspose.Cells.GridDesktop إلى نموذج.
1. إنشاء كائن DataTable الذي يحتوي على البيانات التي سيتم استيرادها.
1. الحصول على مرجع لورقة عمل مرغوبة.
1. استيراد محتويات جدول البيانات إلى ورقة العمل.
1. تعيين رؤوس الأعمدة لورقة العمل وفقًا لأسماء الأعمدة في جدول البيانات.
1. تعيين عرض الأعمدة، إن لزم الأمر.
1. عرض ورقة العمل.

في المثال الوارد أدناه، قمنا بإنشاء كائن DataTable وملأناه ببعض البيانات المسترجعة من جدول قاعدة بيانات بعنوان Products. وأخيرًا، قمنا باستيراد البيانات من ذلك الكائن DataTable إلى ورقة عمل مطلوبة باستخدام Aspose.Cells.GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}

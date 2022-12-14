---
title: استيراد البيانات من DataTable إلى الشبكة
type: docs
weight: 50
url: /ar/net/importing-data-from-a-datatable-to-grid/
---
{{% alert color="primary" %}} 

منذ إصدار .NET Framework ، قدم Microsoft طريقة ممتازة لتخزين البيانات في الوضع غير المتصل في شكل كائن DataTable. فهم احتياجات المطورين ، Aspose.Cells.GridDesktop يدعم أيضًا استيراد البيانات من جدول البيانات. يناقش هذا الموضوع كيفية القيام بذلك.

{{% /alert %}} 
## **مثال**
لاستيراد محتويات جدول البيانات باستخدام Aspose.Cells.GridDesktop control

1. أضف Aspose.Cells.GridDesktop control إلى نموذج.
1. قم بإنشاء كائن DataTable يحتوي على البيانات المراد استيرادها.
1. احصل على مرجع ورقة العمل المطلوبة.
1. قم باستيراد محتويات جدول البيانات إلى ورقة العمل.
1. قم بتعيين رؤوس الأعمدة في ورقة العمل وفقًا لأسماء الأعمدة في جدول البيانات.
1. اضبط عرض الأعمدة ، إذا رغبت في ذلك /
1. اعرض ورقة العمل.

في المثال الموضح أدناه ، قمنا بإنشاء كائن DataTable وملأناه ببعض البيانات التي تم جلبها من جدول قاعدة البيانات المسمى Products. أخيرًا ، قمنا باستيراد البيانات من كائن DataTable إلى ورقة العمل المطلوبة باستخدام Aspose.Cells.GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}

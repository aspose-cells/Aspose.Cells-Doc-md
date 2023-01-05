---
title: تصدير DataTable من GridWeb
type: docs
weight: 70
url: /ar/net/export-datatable-from-gridweb/
---
{{% alert color="primary" %}} 

[استيراد DataView إلى GridWeb](/cells/ar/net/import-dataview-to-gridweb/)تحدث عن استيراد محتويات DataView إلى عنصر التحكم Aspose.Cells.GridWeb. يناقش هذا الموضوع تصدير البيانات من عنصر تحكم Aspose.Cells.GridWeb إلى DataTable.

{{% /alert %}} 
## **تصدير بيانات ورقة العمل**
### **إلى DataTable محدد**
لتصدير بيانات ورقة العمل إلى كائن DataTable محدد:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج ويب الخاص بك.
1. إنشاء كائن DataTable محدد.
1. تصدير بيانات الخلايا المحددة إلى كائن DataTable المحدد.

يقوم المثال أدناه بإنشاء كائن DataTable محدد بأربعة أعمدة. يتم تصدير بيانات ورقة العمل بدءًا من الخلية الأولى مع عرض جميع الصفوف والأعمدة في ورقة العمل ، إلى كائن DataTable تم إنشاؤه بالفعل.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **إلى جدول بيانات جديد**
في بعض الأحيان ، لا تريد إنشاء كائن DataTable ولكنك تحتاج ببساطة إلى تصدير بيانات ورقة العمل إلى كائن DataTable جديد.

يحاول المثال أدناه طريقة مختلفة لإظهار استخدام طريقة التصدير. يأخذ مرجع ورقة العمل النشطة ويصدر البيانات الكاملة لورقة العمل هذه إلى كائن DataTable جديد. يمكن الآن استخدام كائن DataTable بأي طريقة تريدها. على سبيل المثال ، من الممكن ربط كائن DataTable بـ GridView لعرض البيانات.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}

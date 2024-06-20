---
title: تصدير جدول البيانات من GridWeb
type: docs
weight: 70
url: /ar/net/aspose-cells-gridweb/export-datatable-from-gridweb/
keywords: GridWeb، تصدير
description: تقدم هذه المقالة كيفية تصدير الجدول في GridWeb.
---

{{% alert color="primary" %}} 

[استيراد رأي البيانات إلى GridWeb](/cells/ar/net/aspose-cells-gridweb/import-dataview-to-gridweb/) تحدث عن استيراد محتويات رأي البيانات إلى عنصر التحكم Aspose.Cells.GridWeb. يناقش هذا الموضوع تصدير البيانات من عنصر التحكم Aspose.Cells.GridWeb إلى DataTable.

{{% /alert %}} 
## **تصدير بيانات ورقة العمل**
### **إلى DataTable محدد**
لتصدير بيانات ورقة العمل إلى كائن DataTable محدد:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى نموذج الويب الخاص بك.
1. أنشئ كائن DataTable محدد.
1. قم بتصدير بيانات الخلايا المحددة إلى كائن DataTable المحدد.

المثال أدناه يقوم بإنشاء كائن DataTable محدد يحتوي على أربعة أعمدة. يتم تصدير بيانات ورقة العمل ابتداءً من الخلية الأولى مع جميع الصفوف والأعمدة المرئية في ورقة العمل، إلى كائن DataTable تم إنشاؤه بالفعل.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **إلى DataTable جديد**
في بعض الأحيان، قد لا ترغب في إنشاء كائن DataTable ولكنك تحتاج ببساطة لتصدير بيانات ورقة العمل إلى كائن DataTable جديد.

المثال أدناه يحاول طريقة مختلفة لعرض استخدام الطريقة تصدير. يأخذ مثال الإشارة لورقة العمل النشطة ويصدر بيانات الورقة بأكملها إلى كائن DataTable جديد. بعد ذلك يمكن استخدام كائن DataTable بأي طريقة ترغب فيها. على سبيل المثال، يمكن ربط كائن DataTable بعنصر GridView لعرض البيانات.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}

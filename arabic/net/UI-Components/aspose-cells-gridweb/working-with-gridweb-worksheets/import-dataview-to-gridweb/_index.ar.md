---
title: استيراد DataView إلى GridWeb
type: docs
weight: 60
url: /ar/net/aspose-cells-gridweb/import-dataview-to-gridweb/
keywords: GridWeb، الاستيراد
description: يقدم هذا المقال كيفية استيراد البيانات في GridWeb.
---

{{% alert color="primary" %}} 

مع إصدار إطار عمل Microsoft .NET، تم تقديم طريقة جديدة لتخزين البيانات. الآن تحتوي أجهزة الـ DataSet، والكائنات DataTable والـ DataView على البيانات في وضع عدم الاتصال. هذه الكائنات مفيدة للغاية كمستودعات البيانات. باستخدام Aspose.Cells.GridWeb، من الممكن استيراد البيانات من كائنات DataTable أو DataView إلى ورقة العمل. يدعم Aspose.Cells.GridWeb فقط استيراد البيانات من كائن DataView، ولكن يمكن أيضًا استخدام كائن DataTable بشكل غير مباشر. دعنا نناقش هذه الميزة بالتفصيل.

{{% /alert %}} 
## **استيراد البيانات من DataView**
استيراد البيانات من كائن DataView باستخدام طريقة ImportDataView في عنصر التحكم GridWeb. قم بتمرير كائن DataView الذي ترغب في استيراد البيانات منه إلى طريقة ImportDataView. يمكن تحديد رأس العمود وأنماط البيانات أثناء الاستيراد.

{{% alert color="primary" %}} 

عندما يتم استيراد البيانات من كائن DataView، يتم إنشاء ورقة عمل جديدة لاحتواء البيانات المستوردة. تكون ورقة العمل بنفس اسم DataTable.

{{% /alert %}} 

**الناتج: البيانات المستوردة من كائن DataView إلى ورقة عمل جديدة** 

![todo:image_alt_text](import-dataview-to-gridweb_1.png)

تُعدل أعراض الأعمدة لإظهار جميع البيانات التي تحتوي عليها. عندما يتم استيراد البيانات من DataView، لا يتم ضبط أعراض الأعمدة تلقائيًا. يحتاج المستخدمون إلى ضبطها بأنفسهم. لضبط أعراض الأعمدة برمجيًا، راجع [تغيير حجم الصفوف والأعمدة](/cells/ar/net/aspose-cells-gridweb/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

إصدار مكمّل من طريقة ImportDataView يسمح للمطورين بتحديد اسم الورقة التي تحتوي على البيانات المستوردة وعدد محدد من الصفوف والأعمدة لاستيرادها من كائن DataView.

{{% /alert %}}

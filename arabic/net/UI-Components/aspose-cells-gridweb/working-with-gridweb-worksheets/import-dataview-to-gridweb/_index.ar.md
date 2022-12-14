---
title: استيراد DataView إلى GridWeb
type: docs
weight: 60
url: /ar/net/import-dataview-to-gridweb/
---
{{% alert color="primary" %}} 

مع إصدار Microsoft .NET Framework ، تم تقديم طريقة جديدة لتخزين البيانات. الآن كائنات DataSet و DataTable و DataView التي تخزن البيانات في وضع غير متصل بالشبكة. هذه الكائنات مفيدة جدًا كمستودعات للبيانات. باستخدام Aspose.Cells.GridWeb ، من الممكن استيراد البيانات من كائنات DataTable أو DataView إلى أوراق العمل. Aspose.Cells.GridWeb يدعم فقط استيراد البيانات من DataView. كائن ولكن يمكن أيضًا استخدام كائن DataTable بشكل غير مباشر. دعونا نناقش هذه الميزة بالتفصيل.

{{% /alert %}} 
## **استيراد البيانات من DataView**
استيراد البيانات من كائن DataView باستخدام أسلوب ImportDataView GridWorsheetCollection في عنصر التحكم GridWeb. قم بتمرير كائن DataView الذي تريد استيراد البيانات منه إلى أسلوب ImportDataView. من الممكن تحديد رأس العمود وأنماط البيانات أثناء الاستيراد.

{{% alert color="primary" %}} 

عند استيراد البيانات من كائن DataView ، يتم إنشاء ورقة عمل جديدة لاستيعاب البيانات المستوردة. يتم تسمية ورقة العمل بنفس تسمية DataTable.

{{% /alert %}} 

**الإخراج: البيانات المستوردة من DataView إلى ورقة عمل جديدة** 

![ما يجب القيام به: image_بديل_نص](import-dataview-to-gridweb_1.png)

 يتم ضبط عرض الأعمدة لإظهار كل البيانات التي تحتوي عليها. عند استيراد البيانات من DataView ، لا يتم ضبط عرض الأعمدة تلقائيًا. يحتاج المستخدمون إلى تعديلها بأنفسهم. لضبط عرض العمود برمجيًا ، راجع[تغيير حجم الصفوف والأعمدة](/cells/ar/net/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

يسمح إصدار محمّل بشكل زائد من أسلوب ImportDataView للمطورين بتحديد اسم الورقة التي تحتوي على البيانات المستوردة وعددًا محددًا من الصفوف والأعمدة للاستيراد من كائن DataView.

{{% /alert %}}

---
title: تنفيذ ميزة ربط البيانات لـ GridDesktop في أوراق الأعمال
type: docs
weight: 10
url: /ar/net/aspose-cells-griddesktop/implementing-data-binding-feature-in-worksheets/
keywords: ربط البيانات, الجدول الشبكي السطحي, البيانات, ربط
description: يقدم هذا المقال كيفية عمل ربط البيانات في الجدول الشبكي السطحي.
---

{{% alert color="primary" %}} 

ربط البيانات هو ميزة مثيرة مقدمة من إطار العمل Microsoft .NET. نحن نعلم أن عنصر التحكم DataGrid المقدم من Microsoft يدعم ربط البيانات, مما يعني أن DataGrid يمكن أن يتم ربطه بأي مصدر بيانات (باستخدام كائنات DataSet, DataTable و DataView). هذه الميزة جعلت حياة المطورين أسهل بكثير. بناءً على نفس المفهوم, يدعم Aspose.Cells.GridDesktop أيضًا ربط البيانات, مما يسمح للمطورين بربط ورق العمل بأي مصدر بيانات. يقوم هذا المقال باستكشاف هذه الميزة.

{{% /alert %}} 
## **إنشاء قاعدة بيانات عينية**
1. إنشاء قاعدة بيانات عينية للاستخدام مع المثال. لقد استخدمنا Microsoft Access لإنشاء قاعدة بيانات عينية تحتوي على جدول المنتجات (المخطط أدناه). 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. تمت إضافة ثلاث سجلات وهمية إلى جدول المنتجات.
   **السجلات في جدول المنتجات** 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **إنشاء تطبيق عيني**
الآن قم بإنشاء تطبيق سطح المكتب بسيط في Visual Studio وقم باتباع الخطوات التالية.

1. قم بسحب عنصر التحكم "GridControl" من صندوق الأدوات وإفلاته على النموذج.
1. إسقاط أربعة أزرار من صندوق الأدوات في أسفل النموذج وتعيين خاصية نصها كما يلي **ربط الورقة العمل**, **إضافة صف**, **حذف صف** و **تحديث إلى قاعدة البيانات** على التوالي.
## **إضافة مساحة الاسم وإعلان المتغيرات العالمية**
نظرًا لأن هذا المثال يستخدم قاعدة بيانات Microsoft Access, أضف مساحة الاسم System.Data.OleDb في أعلى الكود.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


يمكنك الآن استخدام الفئات الموجودة تحت هذه المساحة.

1. إعلان المتغيرات العالمية.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **ملء مجموعة البيانات بالبيانات من قاعدة البيانات**
الآن قم بالاتصال بقاعدة البيانات العينية لاحضار البيانات وملءها في كائن DataSet.

1. استخدم كائن OleDbDataAdapter للاتصال بقاعدة البيانات العينية وملء DataSet بالبيانات المحضرة من جدول المنتجات في قاعدة البيانات, كما هو موضح في الكود أدناه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **ربط ورقة العمل بكائن DataSet**
قم بربط ورقة العمل بجدول المنتجات في مجموعة البيانات:

1. الوصول إلى ورقة العمل المطلوبة.
1. ربط ورقة العمل بجدول منتجات DataSet.

أضف الكود التالي إلى حدث نقر زر "ربط ورقة العمل".



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **تحديد رؤوس الأعمدة لورقة العمل**
تحميل ورقة العمل المقترنة الآن بالبيانات بنجاح ولكن تم وسم رؤوس الأعمدة A ، B و C افتراضيًا. سيكون من الأفضل تعيين رؤوس الأعمدة إلى أسماء الأعمدة في جدول قاعدة البيانات.

لتعيين رؤوس الأعمدة لورقة العمل:

1. احصل على التسميات لكل عمود من DataTable (Products) في مجموعة البيانات.
1. قم بتعيين التسميات لرؤوس أعمدة ورقة العمل.

أضف الكود المكتوب في حدث نقر زر 'ربط ورقة العمل' بمقتطف الكود التالي. من خلال القيام بذلك ، سيتم استبدال رؤوس الأعمدة القديمة (A ، B و C) بـ ProductID ، ProductName و ProductPrice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **تخصيص عرض وأنماط الأعمدة**
لتحسين مظهر ورقة العمل بشكل إضافي ، يمكن تعيين عرض وأنماط الأعمدة. على سبيل المثال ، في بعض الأحيان ، قد تحتوي رأس العمود أو القيمة داخل العمود على عدد كبير جدًا من الأحرف التي لا تتناسب داخل الخلية. لحل مثل هذه المشاكل ، يدعم Aspose.Cells.GridDesktop تغيير عرض الأعمدة.

أضف الكود التالي إلى زر 'ربط ورقة العمل'. سيتم تخصيص عرض الأعمدة وفقًا للإعدادات الجديدة.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


تدعم Aspose.Cells.GridDesktop أيضًا تطبيق الأنماط المخصصة للأعمدة. الكود التالي ، المضاف إلى زر 'ربط ورقة العمل' ، يخصص أنماط الأعمدة لجعلها أكثر إشراقًا.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


الآن قم بتشغيل التطبيق وانقر فوق زر 'ربط ورقة العمل'.
## **إضافة الصفوف**
لإضافة صفوف جديدة إلى ورقة العمل ، استخدم طريقة إضافة الصف في فئة Worksheet. يتم إلحاق صف فارغ في الجزء السفلي ويتم إضافة DataRow جديد إلى مصدر البيانات (هنا ، يتم إضافة DataRow جديدة إلى DataTable لـ DataSet). يمكن للمطورين إضافة عدد غير محدود من الصفوف عن طريق استدعاء طريقة AddRow مرة أخرى ومرة أخرى. عند الانتهاء من إضافة صف ، يمكن للمستخدمين إدخال القيم فيه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **حذف الصفوف**
تدعم Aspose.Cells.GridDesktop أيضًا حذف الصفوف باستدعاء طريقة إزالة الصف في فئة ورقة العمل. يتطلب إزالة الصف باستخدام Aspose.Cells.GridDesktop مؤشر الصف الذي يجب حذفه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


أضف الكود التالي إلى زر 'حذف الصف' وقم بتشغيل التطبيق. يتم عرض عدد قليل من السجلات قبل حذف الصف. عند تحديد صف والنقر على زر 'حذف الصف' ، يتم إزالة الصف المحدد.
## **حفظ التغييرات في قاعدة البيانات**
أخيرًا، لحفظ أي تغييرات قام بها المستخدمون في ورقة البيانات إلى قاعدة البيانات، استخدم طريقة Update لكائن OleDbDataAdapter. تأخذ طريقة Update مصدر البيانات (مجموعة البيانات، الجدول وما إلى ذلك) لورقة البيانات لتحديث قاعدة البيانات.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1. أضف الكود أعلاه إلى زر **تحديث القاعدة البيانات**.
1. قم بتشغيل التطبيق.
1. قم بإجراء بعض العمليات على بيانات ورقة البيانات، مثلاً إضافة صفوف جديدة وتحرير أو إزالة البيانات الحالية.
1. ثم انقر على **تحديث القاعدة البيانات** لحفظ التغييرات في قاعدة البيانات.
1. تحقق من قاعدة البيانات لرؤية أن سجلات الجدول تم تحديثها وفقًا لذلك.

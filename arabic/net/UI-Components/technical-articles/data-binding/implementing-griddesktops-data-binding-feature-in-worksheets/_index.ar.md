---
title: تنفيذ ميزة ربط بيانات GridDesktop في أوراق العمل
type: docs
weight: 10
url: /ar/net/implementing-griddesktops-data-binding-feature-in-worksheets/
---
{{% alert color="primary" %}} 

يعد ربط البيانات ميزة مثيرة يقدمها Microsoft .NET Framework. نحن نعلم أن عنصر التحكم DataGrid الذي يقدمه Microsoft يدعم ربط البيانات ، مما يعني أنه يمكن ربط DataGrid بأي مصدر بيانات (باستخدام كائنات DataSet و DataTable و DataView). جعلت هذه الميزة حياة المطورين أسهل كثيرًا. استنادًا إلى نفس المفهوم ، يدعم Aspose.Cells.GridDesktop أيضًا ربط البيانات ، والذي يسمح للمطورين بربط أوراق العمل بأي مصدر بيانات. تستكشف هذه المقالة الميزة.

{{% /alert %}} 
## **إنشاء نموذج قاعدة بيانات**
1.  قم بإنشاء نموذج قاعدة بيانات لاستخدامها مع المثال. استخدمنا Microsoft Access لإنشاء نموذج قاعدة بيانات مع جدول المنتجات (المخطط أدناه).

![ما يجب القيام به: image_بديل_نص](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. تتم إضافة ثلاثة سجلات وهمية إلى جدول المنتجات.
   **السجلات في جدول المنتجات** 

![ما يجب القيام به: image_بديل_نص](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **قم بإنشاء نموذج تطبيق**
الآن قم بإنشاء تطبيق سطح مكتب بسيط في Visual Studio وقم بما يلي.

1. اسحب عنصر التحكم "GridControl" من مربع الأدوات وقم بإفلاته في النموذج.
1. قم بإسقاط أربعة أزرار من مربع الأدوات أسفل النموذج وقم بتعيين خاصية النص الخاصة بهم على أنها**ربط ووكشيت**, **اضف سطر**, **احذف صف** و**التحديث إلى قاعدة البيانات** على التوالى.
## **إضافة مساحة الاسم وإعلان المتغيرات العمومية**
لأن هذا المثال يستخدم قاعدة بيانات Microsoft Access ، أضف مساحة الاسم System.Data.OleDb في الجزء العلوي من التعليمات البرمجية.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


يمكنك الآن استخدام الفئات التي تم تجميعها ضمن مساحة الاسم هذه.

1. قم بتعريف المتغيرات العالمية.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **تعبئة مجموعة البيانات ببيانات من قاعدة البيانات**
اتصل الآن بقاعدة البيانات النموذجية لجلب البيانات وتعبئتها في كائن DataSet.

1. استخدم كائن OleDbDataAdapter للاتصال بعينة قاعدة البيانات الخاصة بنا وملء DataSet بالبيانات التي تم جلبها من جدول المنتجات في قاعدة البيانات ، كما هو موضح في الكود أدناه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **ورقة عمل ملزمة مع DataSet**
اربط ورقة العمل بجدول المنتجات في DataSet:

1. قم بالوصول إلى ورقة العمل المطلوبة.
1. اربط ورقة العمل بجدول منتجات DataSet.

 أضف التعليمات البرمجية التالية إلى ملف**ربط ورقة العمل** انقر فوق زر الحدث.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **تعيين رؤوس الأعمدة لورقة العمل**
تقوم ورقة العمل المرتبطة الآن بتحميل البيانات بنجاح ولكن رؤوس الأعمدة يتم تسميتها بشكل افتراضي A و B و C. سيكون من الأفضل تعيين رؤوس الأعمدة لأسماء الأعمدة في جدول قاعدة البيانات.

لتعيين رؤوس أعمدة ورقة العمل:

1. احصل على التسميات التوضيحية لكل عمود من DataTable (المنتجات) في DataSet.
1. قم بتعيين التسميات التوضيحية إلى رؤوس أعمدة ورقة العمل.

 قم بإلحاق الكود المكتوب في**ربط ورقة العمل** انقر فوق الزر مع مقتطف الشفرة التالي. من خلال القيام بذلك ، سيتم استبدال رؤوس الأعمدة القديمة (A و B و C) بـ ProductID و ProductName و ProductPrice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **تخصيص عرض وأنماط الأعمدة**
لتحسين مظهر ورقة العمل بشكل أكبر ، من الممكن تعيين عرض وأنماط الأعمدة. على سبيل المثال ، في بعض الأحيان ، يتكون رأس العمود أو القيمة الموجودة داخل العمود من عدد طويل من الأحرف التي لا يمكن احتواؤها داخل الخلية. لحل مثل هذه المشكلات ، يدعم Aspose.Cells.GridDesktop تغيير عرض الأعمدة.

 قم بإلحاق التعليمات البرمجية التالية بملف**ربط ورقة العمل** زر. سيتم تخصيص عرض العمود وفقًا للإعدادات الجديدة.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


 Aspose.Cells. يدعمGridDesktop أيضًا تطبيق الأنماط المهيأة على الأعمدة. الكود التالي ، الملحقة بامتداد**ربط ورقة العمل** الزر ، يخصص أنماط الأعمدة لجعلها أكثر قابلية للتقديم.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


 الآن قم بتشغيل التطبيق وانقر فوق ملف**ربط ورقة العمل** زر.
## **مضيفا الصفوف**
لإضافة صفوف جديدة إلى ورقة عمل ، استخدم طريقة AddRow لفئة ورقة العمل. يؤدي هذا إلى إلحاق صف فارغ في الجزء السفلي ويتم إضافة DataRow جديد إلى مصدر البيانات (هنا ، تتم إضافة DataRow جديد إلى DataTable الخاص بـ DataSet). يمكن للمطورين إضافة العديد من الصفوف كما يريدون عن طريق استدعاء طريقة AddRow مرارًا وتكرارًا. عند إضافة صف ، يمكن للمستخدمين إدخال القيم فيه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **حذف الصفوف**
Aspose.Cells.GridDesktop يدعم أيضًا حذف الصفوف عن طريق استدعاء طريقة RemoveRow لفئة ورقة العمل. تتطلب إزالة صف باستخدام Aspose.Cells.GridDesktop حذف فهرس الصف.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


 إضافة الكود أعلاه إلى**احذف صف** زر وتشغيل التطبيق. يتم عرض عدد قليل من السجلات قبل إزالة الصف. تحديد صف والنقر فوق**احذف صف** زر يزيل الصف المحدد.
## **حفظ التغييرات في قاعدة البيانات**
أخيرًا ، لحفظ أي تغييرات أجراها المستخدمون على ورقة العمل مرة أخرى إلى قاعدة البيانات ، استخدم طريقة تحديث كائن OleDbDataAdapter. تأخذ طريقة التحديث مصدر البيانات (DataSet و DataTable وما إلى ذلك) من ورقة العمل لتحديث قاعدة البيانات.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1.  أضف الكود أعلاه إلى**التحديث إلى قاعدة البيانات** زر.
1. قم بتشغيل التطبيق.
1. قم بإجراء بعض العمليات على بيانات ورقة العمل ، وربما إضافة صفوف جديدة وتحرير البيانات الموجودة أو إزالتها.
1.  ثم اضغط**التحديث إلى قاعدة البيانات** لحفظ التغييرات في قاعدة البيانات.
1. تحقق من قاعدة البيانات للتأكد من أنه تم تحديث سجلات الجدول وفقًا لذلك.

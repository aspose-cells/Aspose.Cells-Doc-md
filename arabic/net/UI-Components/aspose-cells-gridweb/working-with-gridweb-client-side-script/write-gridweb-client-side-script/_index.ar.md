---
title: اكتب البرنامج النصي من جانب عميل GridWeb
type: docs
weight: 10
url: /ar/net/write-gridweb-client-side-script/
---
{{% alert color="primary" %}} 

يمكن للمطورين كتابة برامج نصية من جانب العميل لعنصر التحكم Aspose.Cells.GridWeb. هذا يعني أنه من الممكن استدعاء جانب العميل لوظيفة JavaScript لأداء مهمة محددة متعلقة بالتحكم في GridWeb. على سبيل المثال ، يمكن للمطورين كتابة وظائف JavaScript لإرسال بيانات GridWeb إلى خادم أو إظهار رسالة تنبيه عند حدوث خطأ في التحقق من الصحة وما إلى ذلك.

يشرح هذا الموضوع هذه الميزة بمساعدة الأمثلة.

{{% /alert %}} 
## **كتابة البرامج النصية من جانب العميل لـ Aspose.Cells.GridWeb**
### **معلومات اساسية**
Aspose.Cells.GridWeb يوفر خاصيتين تم إنشاؤهما خصيصًا لدعم البرامج النصية من جانب العميل:

- OnSubmitClientFunction
- OnValidationErrorClientFunction

قم بإنشاء وظائف JavaScript في صفحة ASPX وقم بتعيين أسماء هذه الوظائف إلى خصائص OnSubmitClientFunction و OnValidationErrorClientFunction.

{{% alert color="primary" %}} 

يجب تحديد وظيفة JavaScript التي سيتم تعيينها لخاصية OnSubmitClientFunction بشكل صحيح كما هو موضح أدناه:

**جافا سكريبت**

{{< highlight "csharp" >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

حيث تمثل المعلمة [arg] الأمر الذي تم إنشاؤه بواسطة عنصر التحكم. يمكن أن يكون الأمر "حفظ" و "إرسال" و "تراجع" وما إلى ذلك والمعلمة [إلغاء تحرير] هي قيمة منطقية ، والتي تشير إلى ما إذا كان إدخال المستخدم قد تم إلغاؤه أم لا.

يتم استدعاء أي وظيفة JavaScript مخصصة لخاصية OnSubmitClientFunction في كل مرة بواسطة عنصر التحكم GridWeb قبل إرسال بيانات GridWeb إلى الخادم. وبالمثل ، إذا تم تعيين دالة لخاصية OnValidationErrorClientFunction ، فسيتم استدعاء هذه الوظيفة في كل مرة يحدث فيها خطأ في التحقق من الصحة.

{{% /alert %}} 
### **وظائف البرمجة النصية من جانب العميل**
Aspose.Cells.GridWeb يعرض أيضًا وظائف خاصة للبرمجة النصية من جانب العميل. يمكن استخدام هذه الوظائف في وظائف JavaScript للحصول على مزيد من التحكم في Aspose.Cells.GridWeb. تتضمن وظائف جانب العميل هذه ما يلي:

|**المهام**|**وصف**|
|:- |:- |
|updateData (منطقي إلغاء تحرير)|يقوم بتحديث كافة بيانات العميل لـ Aspose.Cells.GridWeb قبل إرسالها إلى الخادم. إذا كانت المعلمة CancelEdit صحيحة ، فإن GridWeb يتجاهل كل مدخلات المستخدم.|
|تحقق من صحة الكل ()|يُستخدم للتحقق مما إذا كانت هناك أية أخطاء في التحقق من صحة إدخال المستخدم. إذا كان هناك خطأ ، فإن الدالة ترجع خطأ ، وإلا تكون صحيحة.|
|إرسال (سلسلة أحرف ، منطقية إلغاء تحرير)|استدعاء هذه الوظيفة لإعادة النشر أو إرسال البيانات إلى الخادم. تؤدي هذه الوظيفة المهام التي تقوم بتحديث البيانات والتحقق من صحة إدخال المستخدم. يمكن لهذه الوظيفة أيضًا إطلاق حدث أمر على جانب الخادم. استخدم المعلمة arg لتمرير الأمر الخاص بك. على سبيل المثال: يتم استخدام الأمر SAVE للنقر فوق ملف**يحفظ** الزر الموجود على شريط الأوامر لعنصر التحكم GridWeb ثم الأمر CCMD: MYCOMMAND بإطلاق حدث CustomCommand.|
|setActiveCell (صف int ، عمود int)|يستخدم لتنشيط خلية معينة.|
|setCellValue (الصف int ، العمود int ، قيمة السلسلة)|تُستخدم لوضع قيمة لأي خلية محددة باستخدام أرقام الصفوف والأعمدة الخاصة بها.|
|getCellValue (الصف int ، العمود int)|ترجع قيمة أي خلية محددة.|
|getActiveRow ()|تُستخدم مع وظيفة getActiveColumn () لتحديد موضع الخلية النشطة.|
|getActiveColumn ()|تُستخدم مع وظيفة getActiveRow () لتحديد موضع الخلية النشطة.|
|getSelectRange ()|إرجاع النطاق المحدد الأخير.|
|setSelectRange ()|يختار النطاق المحدد.|
|clearSelections ()|يمسح كل التحديد باستثناء الخلية النشطة الحالية.|
|getCellsArray ()| يتم استخدامه مع الوظائف الأخرى ذات الصلة مثل getCellName () و getCellValueByCell () و getCellRow () و getCellColumn (). يرجى قراءة هذه المقالة لمزيد من المعلومات حول استخدام هذه الوظيفة:[اقرأ قيم خلايا GridWeb على جانب العميل](/cells/ar/net/read-the-values-of-the-gridweb-cells-on-client-side/)|
لإنشاء تطبيق اختبار يحتوي على برامج نصية من جانب العميل تعمل مع Aspose.Cells.GridWeb ، اتبع الخطوات التالية:

1. قم بإنشاء وظائف JavaScript ليتم استدعاؤها بواسطة GridWeb.
 ستتم إضافة هذه الوظائف إلى صفحات ASP.NET<script></script>بطاقة شعار.
1. قم بتعيين أسماء الدالات إلى الخاصيتين OnSubmitClientFunction و OnValidationErrorClientFunction.

يتم عرض إخراج مثال الكود أدناه:

**تمت إضافة التحقق إلى خلية C1** 

![ما يجب القيام به: image_بديل_نص](write-gridweb-client-side-script_1.png)

 أضف قيمة غير صالحة وانقر**يحفظ**. حدث خطأ في التحقق من الصحة وتم تنفيذ وظيفة ValidationErrorFunction.

**تم استدعاء ValidationErrorFunction عند حدوث خطأ في التحقق من الصحة** 

![ما يجب القيام به: image_بديل_نص](write-gridweb-client-side-script_2.png)

 حتى يتم إدخال قيمة صالحة ، لا يتم تقديم أي بيانات إلى الخادم. أدخل قيمة صالحة وانقر**يحفظ**. تم تنفيذ وظيفة التأكيد.

**تم استدعاء وظيفة ConfirmFunction قبل إرسال بيانات GridWeb إلى الخادم** 

![ما يجب القيام به: image_بديل_نص](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}

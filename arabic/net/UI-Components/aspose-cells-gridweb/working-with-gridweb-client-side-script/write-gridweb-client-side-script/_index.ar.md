---
title: كتابة سكريبت الجانب العميل لـ GridWeb
type: docs
weight: 10
url: /ar/net/aspose-cells-gridweb/write-gridweb-client-side-script/
keywords: GridWeb,client,js,javascript
description: يقدم هذا المقال كيفية العمل مع واجهات برمجة تطبيقات js العميلية في GridWeb.
---

{{% alert color="primary" %}} 

يمكن للمطورين كتابة سكريبتات الجانب العميل لعنصر تحكم Aspose.Cells.GridWeb. يعني هذا أنه من الممكن استدعاء دالة JavaScript في جانب العميل لأداء مهمة معينة تتعلق بعنصر تحكم GridWeb. على سبيل المثال، يمكن للمطورين كتابة دوال JavaScript لإرسال بيانات GridWeb إلى خادم أو عرض رسالة تنبيه عند حدوث خطأ في التحقق من الصحة وما إلى ذلك.

يشرح هذا الموضوع هذه الميزة بمساعدة الأمثلة.

{{% /alert %}} 
## **كتابة سكريبتات الجانب العميل لـ Aspose.Cells.GridWeb**
### **المعلومات الأساسية**
يوفر Aspose.Cells.GridWeb خاصيتين تم إنشاؤهما خصيصًا لدعم سكريبتات الجانب العميل:

- OnSubmitClientFunction
- OnValidationErrorClientFunction

قم بإنشاء دوال JavaScript في صفحة ASPX وتعيين أسماء هذه الدوال إلى خصائص OnSubmitClientFunction و OnValidationErrorClientFunction.

{{% alert color="primary" %}} 

يجب تعريف الدالة JavaScript التي سيتم تعيينها إلى خاصية OnSubmitClientFunction بشكل صحيح كما هو موضح أدناه:

**JavaScript**

{{< highlight csharp >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

حيث يمثل المعلمة [arg] الأمر الذي تم إنشاؤه بواسطة العنصر التحكم. يمكن أن يكون الأمر "Save", "Submit", "Undo" وما إلى ذلك، والمعلمة [cancelEdit] تعتبر قيمة بوليانية، تشير إلى ما إذا كان إدخال المستخدم تم إلغاؤه أم لا.

يتم استدعاء أي دالة JavaScript المعينة لخاصية OnSubmitClientFunction في كل مرة من قبل عنصر التحكم GridWeb قبل تقديم بيانات GridWeb إلى الخادم. بالمثل، إذا تم تعيين دالة إلى خاصية OnValidationErrorClientFunction فسيتم استدعاء تلك الدالة في كل مرة يحدث فيها خطأ في التحقق من الصحة.

{{% /alert %}} 
### **الدوال لسكريبتات الجانب العميل**
تكشف Aspose.Cells.GridWeb أيضًا عن دوال مصممة خصيصًا لسكريبتات الجانب العميل. يمكن استخدام هذه الدوال ضمن دوال JavaScript للحصول على مزيد من التحكم في Aspose.Cells.GridWeb. تشمل هذه الدوال الجانبية الخاصة الدوال التالية:

|**الدوال**|**الوصف**|
| :- | :- |
|updateData(bool cancelEdit)|يقوم بتحديث جميع بيانات العميل لـ Aspose.Cells.GridWeb قبل إرسالها إلى الخادم. إذا كان معلم الcancelEdit صحيحًا، فإن GridWeb يتجاهل كل إدخال مستخدم.|
|validateAll()|يتم استخدامه للتحقق مما إذا كانت هناك أخطاء في التحقق من الصحة في إدخال المستخدم. إذا كان هناك خطأ، فإن الوظيفة تعيد القيمة صحيح، وإلا تعيد القيمة خطأ.|
|submit(string arg, bool cancelEdit)|استدعاء هذه الوظيفة لإعادة تحميل البيانات أو إرسال البيانات إلى الخادم. تقوم هذه الوظيفة بأداء كل المهام المتمثلة في تحديث البيانات والتحقق من صحة إدخال المستخدم. يمكن لهذه الوظيفة أيضًا تشغيل حدث الأمر على جانب الخادم. استخدم المعلم arg لتمرير الأمر الخاص بك. على سبيل المثال: يتم استخدام الأمر SAVE للنقر فوق زر الحفظ على شريط الأوامر لعنصر تحكم GirdWeb وينشط الأمر CCMD: MYCOMMAND الأمر حدث مخصص.|
|setActiveCell(int row, int column)|تستخدم لتفعيل خلية معينة. |
|setCellValue(int row, int column, string value)|تستخدم لوضع قيمة في أي خلية محددة باستخدام أرقام صفها وعمودها. |
|getCellValue(int row, int column)|تُعيد قيمة أي خلية محددة. |
|getActiveRow()|تُستخدم بالاشتراك مع الوظيفة getActiveColumn() لتحديد موقع خلية نشطة. |
|getActiveColumn()|تُستخدم بالاشتراك مع الوظيفة getActiveRow() لتحديد موقع خلية نشطة. |
|getSelectRange()|تُعيد آخر نطاق تم تحديده. |
|setSelectRange()|تحدد النطاق المعطى. |
|clearSelections()|تُمسح كل التحديد باستثناء الخلية النشطة الحالية. |
|getCellsArray()|يُستخدم بالاشتراك مع وظائف ذات صلة أخرى مثل getCellName(), getCellValueByCell(), getCellRow() وgetCellColumn(). يرجى قراءة هذا المقال لمزيد من المعلومات بشأن استخدام هذه الوظيفة: [اقرأ قيم خلايا GridWeb على الجانب العميل](/cells/ar/net/aspose-cells-gridweb/read-the-values-of-the-gridweb-cells-on-client-side/)|
لإنشاء تطبيق اختبار يحتوي على النصوص الخاصة بالجانب العميل الذي يعمل مع Aspose.Cells.GridWeb، اتبع الخطوات التالية:

1. إنشاء الدوال التفاعلية في JavaScript التي يتم استدعاؤها بواسطة GridWeb.
   These functions will be added to the ASP.NET page's <script></script> tag.
1. تعيين أسماء الدوال إلى خصائص OnSubmitClientFunction و OnValidationErrorClientFunction.

تُظهر الناتج لمثال الكود أدناه:

**تم إضافة تحقق إلى خلية C1** 

![todo:image_alt_text](write-gridweb-client-side-script_1.png)

أضف قيمة غير صحيحة وانقر فوق **حفظ**. حدث خطأ في التحقق وتم تشغيل دالة الفحص الدقيق.

**تم استدعاء دالة الفحص الدقيق عند حدوث خطأ في التحقق** 

![todo:image_alt_text](write-gridweb-client-side-script_2.png)

حتى تقوم بإدخال قيمة صحيحة، لن يتم تقديم أية بيانات إلى الخادم. أدخل قيمة صحيحة وانقر فوق **حفظ**. سيتم تشغيل دالة التأكيد.

**تم استدعاء ConfirmFunction قبل إرسال بيانات GridWeb للخادم** 

![todo:image_alt_text](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}

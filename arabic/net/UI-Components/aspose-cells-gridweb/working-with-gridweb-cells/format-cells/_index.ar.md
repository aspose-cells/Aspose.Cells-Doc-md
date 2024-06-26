---
title: تنسيق الخلية
type: docs
weight: 40
url: /ar/net/aspose-cells-gridweb/format-grid-cell/
keywords: GridWeb، format، style
description: يقدم هذا المقال كيفية تعيين أو تطبيق تنسيق النمط لخلية (GridCell) في GridWeb.
---

{{% alert color="primary" %}} 

يقدم هذا الموضوع نقاشًا مفصلًا حول كيفية تنسيق الخلايا.

يغطي تنسيق الخلايا في وضع واجهة المستخدم الرسومية باستخدام مربع الأدوات النمطية للتحكم Aspose.Cells.GridWeb. كما يوضح كيفية تنسيق الخلايا برمجياً. يتم مناقشة إعدادات التنسيق المختلفة مثل الخط والحدود وتنسيق الأرقام، مع أمثلة موضحة.

{{% /alert %}} 
## **تنسيق الخلايا باستخدام مربع الأدوات النمطية**
يمكن تنسيق الخلايا [برمجياً](/cells/ar/net/aspose-cells-gridweb/format-cells/) ولكن أسهل طريقة لتنسيق الخلايا في تحكم Aspose.Cells.GridWeb بطريقة WYSIWYG هو باستخدام مربع الأدوات النمطية.

لاستخدام مربع الأدوات النمطية:
حدد نطاق الخلايا ثم انقر بزر الماوس الأيمن وحدد **تنسيق الخلية**. 

**تحديد تنسيق الخلية** 

![todo:image_alt_text](format-cells_1.png)



يتم عرض مربع الأنماط. 

**يُستخدم مربع الأنماط لتنسيق الخلايا** 

![todo:image_alt_text](format-cells_2.png)

يتيح مربع الأنماط للمستخدمين تنسيق الخلايا من خلال تخصيص إعدادات الخطوط والحدود.
### **تخصيص إعدادات الخطوط**
يمكنك تخصيص إعدادات الخطوط التالية باستخدام مربع الأنماط:

- اسم الخط، حدد الخط المرغوب من القائمة.
- نمط الخط، ضع نمطًا للخط مثل العريض، المائل وما إلى ذلك.
- حجم الخط، حدد حجم الخط بالنقاط.
- تحته خط، وضع خط تحت النص.
- تشطيب علوي، ضع تأثير تشطيب علوي على النص.
- محاذاة أفقية، حدد المحاذاة الأفقية.
- محاذاة رأسية، حدد المحاذاة الرأسية.
- لون الخط، حدد لونًا للخط.
- خلفية، حدد لون خلفية.

يمكنك التحقق من إعدادات الخط المحددة في منطقة معاينة صغيرة.

**إعدادات الخط المخصصة** 

![todo:image_alt_text](format-cells_3.png)
### **تخصيص إعدادات الحدود**
تتيح الأداة أيضًا للمستخدمين رسم حدود حول الخلايا من خلال تخصيص إعدادات الحدود في مربع الأنماط.

لعرض خيارات ذات صلة بالحدود:
انقر **حدود** في مربع الأنماط.
يتم عرض خيارات ذات صلة بالحدود. 

**خيارات الحدود في مربع النمط** 

![todo:image_alt_text](format-cells_4.png)

يمكن تحديد الخيارات الحدودية التالية من مربع النمط:

- نمط خط الحدود، حدد نمط الحدود مثل مستمر، متقطع وما إلى ذلك.
- عرض خط الحدود، حدد عرض الحدود بالبكسل.
- لون خط الحدود، حدد لون الخط.
- خطوط الحدود، حدد الترقيم والتوضيع لخطوط الحدود.

**إعدادات الحدود المخصصة** 

![todo:image_alt_text](format-cells_5.png)
### **تطبيق الإعدادات**
انقر على **موافق** في مربع النمط لتطبيق التغييرات.

**تطبيق إعدادات الخطوط والحدود** 

![todo:image_alt_text](format-cells_6.png)


## **تهيء الخلايا باستخدام واجهة تطبيق برمجية**
يمكن أيضًا تهيء الخلايا بشكل برمجي باستخدام واجهة تطبيق برمجية Aspose.Cells.GridWeb. تحتوي كل خلية على خاصية نمط، والتي تمثل كائن GridTableItemStyle. استخدم الخاصية نمط لتخصيص إعدادات الخطوط والحدود.
### **ضبط الخط**
لتخصيص إعدادات الخط برمجياً:

1. أضف تحكم Aspose.Cells.GridWeb إلى استمارة الويب.
1. الوصول إلى ورقة العمل.
1. قم بالوصول إلى الخلية التي تقوم بتهيئتها.
1. قم بالوصول إلى نمط الخلية.
1. قم بتعيين حجم الخط بالنقاط.
1. حدد نمط الخط.
1. قم بتعيين ألوان الخلفية والنص.
1. حدد محاذاة أفقية ورأسية.
1. عد النمط إلى الخلية.

**الناتج: إعدادات الخط المخصصة موضحة في A1** 

![todo:image_alt_text](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **تعيين الحدود**
يمكن تطبيق الحدود على الخلايا الفردية أو على نطاق معين.
#### **خلية واحدة**
لتعيين حدود خلية واحدة:

1. أضف تحكم Aspose.Cells.GridWeb إلى استمارة الويب.
1. الوصول إلى ورقة العمل.
1. الوصول إلى الخلية التي ترغب في تنسيقها.
1. الوصول إلى كائن النمط الخاص بالخلية.
1. حدد نمط الحدود.
1. حدد عرض الحدود بالبكسل.
1. حدد لون الحدود.
1. حدد النمط للخلية.

**إعدادات الحدود المخصصة على خلية واحدة** 

![todo:image_alt_text](format-cells_8.png)

{{% alert color="primary" %}} 

من الممكن تعيين أنماط مختلفة لكل خط حدود مع خصائص الخلية.TopBorderStyle، Style.BottomBorderStyle، Style.LeftBorderStyle، Style.RightBorderStyle.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **نطاق الخلايا**
لتعيين حدود على مجموعة من الخلايا:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج الويب الخاص بك
1. الوصول إلى ورقة العمل المطلوبة
1. إنشاء كائن من فئة WebBorderStyle
1. تعيين نمط الحد إلى صلب أو متقطع وما إلى ذلك
1. تعيين عرض الحد بالبكسل
1. تعيين لون الحد
1. تطبيق إعدادات الحد المخزنة في كائن WebBorderStyle على مجموعة محددة من الخلايا

**مجموعة من الخلايا مع إعدادات الحد المخصصة** 

![todo:image_alt_text](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **ضبط تنسيقات الأرقام**
تدعم Aspose.Cells.GridWeb ضبط تنسيقات الأرقام. هناك 59 تنسيق رقمي مدمج. لرؤيتها ، يرجى الرجوع إلى [قائمة التنسيقات الرقمية المدعومة](/cells/ar/net/aspose-cells-gridweb/list-of-supported-number-formats/).

جميع التنسيقات الرقمية المدمجة موجودة في تعداد NumberType. لاستخدام تنسيق رقم مدمج ، قم بتعيين NumberType باستخدام طريقة SetNumberType لكائن الخلية إلى تنسيق رقم من تعداد نوع الرقم.

لضبط تنسيق الرقم المخصص ، استخدم طريقة SetCustom للخلية.

**إعدادات تنسيق الرقم التطبيقية على B1 و B2** 

![todo:image_alt_text](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}

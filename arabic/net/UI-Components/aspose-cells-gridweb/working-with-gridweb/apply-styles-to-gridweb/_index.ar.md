---
title: تطبيق الأنماط على GridWeb
type: docs
weight: 20
url: /ar/net/aspose-cells-gridweb/apply-styles-to-gridweb/
keywords: GridWeb, style, styles
description: تقدم هذه المقالة كيفية تطبيق أو ضبط النمط في GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb لديها مظهرها وشعورها الافتراضي ولكن من الممكن تغيير مظهرها. Aspose.Cells.GridWeb توفر عدة خصائص لتمكين المطورين من السيطرة الكاملة على مظهرها. يناقش هذا الموضوع بعض تلك الخصائص.

{{% /alert %}} 
## **تطبيق أنماط محددة مسبقاً أو أنماط مخصصة على Aspose.Cells.GridWeb**
### **أنماط محددة مسبقاً**
لتوفير جهود المطورين، تقدم Aspose.Cells.GridWeb بعض الأنماط المحددة مسبقاً. ببساطة حدد نمطًا من القائمة لتطبيق النمط.

|**الأنماط**|**مخطط الألوان**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
عند اختيار نمط معين، يغير ذلك المظهر الكامل لعنصر التحكم GridWeb. يمكن للمطورين تحديد نمط محدد مسبقاً لتطبيق النمط على Grid أثناء تصميم الوقت ولكن يمكن أيضًا القيام بهذه المهمة أثناء التشغيل باستخدام واجهة برمجة التطبيق المرنة لـ Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

عنصر تحكم Aspose.Cells.GridWeb ممثل بواسطة فئة GridWeb.

{{% /alert %}} 

لتحديد نمط محدد مسبقًا:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى شكل ويب.
1. اختر نمطًا محدد مسبقاً لتطبيقه على العنصر التحكم.

يوفر عنصر التحكم GridWeb خاصية PresetStyle التي يمكن للمطورين تعيين أي نمط محدد مسبقًا مرغوب فيه.

تُظهر الناتج من مقتطف الكود أدناه. 

**عنصر تحكم GridWeb مع تطبيق نمط Colorful1 عليه** 

![todo:image_alt_text](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **نمط شريط الرأس**
إذا نظرت إلى عنصر تحكم GridWeb، ستلاحظ وجود شريط رأسين. أحدهما للأعمدة (وهو A و B و C و D وما إلى ذلك) والآخر للصفوف (وهو 1 و 2 و 3 و 4 وما إلى ذلك). تسمح Aspose.Cells.GridWeb للمطورين بالتحكم في مظهر هذه الشرائط الرأسية ويمكن للمطورين تعيين نمط الشريط الرأسي إما في وقت التصميم أو وقت التشغيل.

{{% alert color="primary" %}} 

يوفر عنصر تحكم GridWeb خاصية HeaderBarStyle التي تطبق نمطًا على كلا الشريطين الرأسيين للعنصر التحكم.

{{% /alert %}} 

المخرجات موضحة في المثال أدناه. 

تعديل نمط شريط الرأس 

![todo:image_alt_text](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **نمط شريط التبويب**
من الممكن تعيين نمط شريط التبويب. 

تعديل أنماط أشرطة التبويب النشطة وغير النشطة 

![todo:image_alt_text](apply-styles-to-gridweb_3.png)

في الشكل أعلاه، Sheet4 هو التبويب النشط لذا فإن مظهره يختلف عن باقي التبويبات، كما هو محدد في المثال أدناه.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **ملف نمط مخصص قابل لإعادة الاستخدام**
تدعم Aspose.Cells.GridWeb أيضًا الاحتفاظ بمظهرها أو إعدادات النمط في ملف. عندما تقوم بتعيين جميع خصائص المظهر لتحكم GridWeb، يمكنك حفظ هذه الخصائص أو الإعدادات إلى ملف على القرص. هذا النهج مفيد جدًا للمطورين لتوفير وقتهم وجهودهم من خلال إعادة استخدام إعداداتهم القديمة من ملف النمط بدلاً من تعيين جميع خصائص النمط للتحكم واحدة تلو الأخرى.
### **حفظ ملف النمط**
بمجرد الانتهاء من تعيين خصائص النمط، يمكنك حفظ إعدادات تكوين النمط الخاص بك في شكل ملف XML (وذلك لأن ملف النمط يتم تخزينه كملف XML) عن طريق استدعاء طريقة SaveCustomStyleFile لتحكم GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

يكون ملف النمط المحفوظ بتنسيق XML، لذا يمكن للمطورين أيضًا تحرير هذا الملف باستخدام أي محرر نصي إذا كان هناك رغبة في ذلك.

{{% /alert %}} 
### **تحميل ملف النمط**
لتطبيق إعدادات النمط من ملف نمط موجود على تحكم GridWeb، يمكن للمطورين تعيين مسار ملف النمط إلى خاصية CustomStyleFileName للتحكم. ولكن قبل القيام بذلك، يجب تعيين خصائص PresetStyle للتحكم إلى Custom. وذلك لأن ملف النمط يحتوي على معلومات نمط مخصصة تم تعريفها بالفعل من قبل مطور.

{{% alert color="primary" %}} 

من الممكن أيضًا تحميل أو حفظ ملف النمط باستخدام مصمم Aspose.Cells.GridWeb.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

مهم: تحميل ملف النمط إلى تحكم GridWeb لا يؤثر على إعدادات تنسيق الخلايا التابعة للتحكم.

{{% /alert %}} 
### **التنسيق القياسي لقالب النمط الخاص بالـ XML**
{{< highlight java >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}

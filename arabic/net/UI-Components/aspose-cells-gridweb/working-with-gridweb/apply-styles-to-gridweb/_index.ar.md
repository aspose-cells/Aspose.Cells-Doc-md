---
title: تطبيق الأنماط على GridWeb
type: docs
weight: 20
url: /ar/net/apply-styles-to-gridweb/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb له شكله وإحساسه الافتراضي ولكن من الممكن تغيير مظهره. Aspose.Cells.GridWeb يوفر العديد من الخصائص للسماح للمطورين بالتحكم الكامل في مظهره. هذا الموضوع يناقش بعض تلك الخصائص.

{{% /alert %}} 
## **تطبيق الأنماط المعدة مسبقًا أو المخصصة على Aspose.Cells.GridWeb**
### **الأنماط المحددة مسبقًا**
لتوفير جهود المطورين ، يقدم Aspose.Cells.GridWeb بعض الأنماط المحددة مسبقًا. ما عليك سوى تحديد نمط من القائمة لتطبيق النمط.

|**الأنماط**|**نظام الألوان**|
|:- |:- |
|معيار|فضة|
|ملون 1|ارتفع|
|ملون 2|أزرق|
|المهنية 1|ازرق سماوي|
|المهنية 2|مرة أخرى سماوي|
|تقليدي 1|داكن|
|تقليدي 2|رمادي|
|العادة|حسب الطلب|
عند تحديد نمط معين ، فإنه يغير المظهر الكامل لعنصر التحكم GridWeb. يمكن للمطورين تحديد نمط محدد مسبقًا ليتم تطبيقه على الشبكة أثناء وقت التصميم ولكن يمكن أيضًا إنجاز هذه المهمة في وقت التشغيل باستخدام API المرن من Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

Aspose.Cells. يتم تمثيل عنصر تحكم شبكة الويب بفئة GridWeb.

{{% /alert %}} 

لتحديد نمط محدد مسبقًا:

1. أضف Aspose.Cells.GridWeb control إلى نموذج ويب.
1. حدد نمطًا مُعدًا مسبقًا ليتم تطبيقه على عنصر التحكم.

يوفر عنصر التحكم GridWeb خاصية PresetStyle التي يمكن للمطورين تعيين أي نمط محدد مسبقًا مرغوب فيه.

 يتم عرض إخراج مقتطف الشفرة أدناه أدناه.

**يتم تطبيق التحكم في GridWeb بنمط Colorful1 عليه** 

![ما يجب القيام به: image_بديل_نص](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **نمط شريط الرأس**
إذا ألقيت نظرة على عنصر تحكم GridWeb ، ستلاحظ شريطين للرأس. واحد للأعمدة (أي A ، B ، C ، D إلخ) والآخر للصفوف (أي 1 ، 2 ، 3 ، 4 إلخ). Aspose.Cells.GridWeb يسمح للمطورين بالتحكم في مظهر أشرطة الرأس هذه. يمكن للمطورين تعيين نمط أشرطة الرأس إما في وقت التصميم أو وقت التشغيل.

{{% alert color="primary" %}} 

يوفر عنصر التحكم GridWeb خاصية HeaderBarStyle التي تطبق نمطًا على كل من أشرطة الرأس لعنصر التحكم.

{{% /alert %}} 

 يظهر هنا إخراج رمز المثال أدناه.

**نمط معدل لشريط الرأس** 

![ما يجب القيام به: image_بديل_نص](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **نمط شريط الجدولة**
 من الممكن ضبط نمط شريط علامات التبويب.

**الأنماط المعدلة لأشرطة علامات التبويب النشطة وغير النشطة** 

![ما يجب القيام به: image_بديل_نص](apply-styles-to-gridweb_3.png)

في الشكل أعلاه ، تعتبر الورقة 4 هي علامة التبويب النشطة لذا يختلف مظهرها عن علامات التبويب الأخرى ، كما هو محدد في مثال الكود أدناه.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **ملف نمط مخصص قابل لإعادة الاستخدام**
Aspose.Cells.GridWeb يدعم أيضًا الاستمرار في إعدادات المظهر أو النمط الخاص به إلى ملف. عندما تقوم بتعيين كافة خصائص المظهر لعنصر التحكم GridWeb ، يمكنك حفظ هذه الخصائص أو الإعدادات في ملف قرص. يعد هذا الأسلوب مفيدًا جدًا للمطورين لتوفير وقتهم وجهودهم من خلال إعادة استخدام تكوينات النمط القديم من ملف نمط بدلاً من تعيين جميع خصائص النمط (أو المظهر) لعنصر التحكم واحدة تلو الأخرى.
### **حفظ ملف النمط**
بمجرد الانتهاء من تعيين خصائص النمط ، يمكنك حفظ إعدادات تكوين النمط في شكل ملف XML (ذلك لأن ملف النمط هذا مخزن كملف XML) عن طريق استدعاء أسلوب SaveCustomStyleFile لعنصر التحكم GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

ملف النمط المحفوظ بتنسيق XML ، لذلك يمكن للمطورين أيضًا تحرير هذا الملف باستخدام أي محرر نصوص ، إذا رغبت في ذلك.

{{% /alert %}} 
### **تحميل ملف النمط**
لتطبيق إعدادات النمط من ملف نمط موجود للتحكم في GridWeb ، يمكن للمطورين تعيين مسار ملف النمط إلى خاصية CustomStyleFileName لعنصر التحكم. ولكن ، قبل القيام بذلك ، يجب تعيين خاصية PresetStyle للتحكم إلى Custom. وذلك لأن ملف النمط هذا يحتوي على معلومات نمط مخصصة تم تعريفها بالفعل من قبل المطور.

{{% alert color="primary" %}} 

من الممكن أيضًا تحميل ملف النمط أو حفظه باستخدام Aspose.Cells.GridWeb Designer.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

هام: لا يؤثر تحميل ملف النمط في عنصر تحكم GridWeb على إعدادات التنسيق لخلايا عنصر التحكم.

{{% /alert %}} 
### **التنسيق القياسي لقالب نمط XML**
{{< highlight "java" >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}

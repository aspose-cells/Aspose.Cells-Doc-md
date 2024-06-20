---
title: إدارة الروابط الفائقة في ورقة العمل
type: docs
weight: 100
url: /ar/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/
keywords: GridWeb، ارتباط تشعب
description: يقدم هذا المقال كيفية العمل مع ارتباط التشعب في GridWeb.
---

{{% alert color="primary" %}} 

يناقش هذا الموضوع أنواع الروابط الفعلية المعتمدة في Aspose.Cells.GridWeb وكيفية إدارتها برمجياً. يمكن استخدام الروابط الفعلية إما لإنشاء روابط إلى عناوين الويب أو لإجراء استدعاء مرتجع إلى خادم.

{{% /alert %}} 
## **العمل مع روابط فائقة**
### **أنواع الروابط الفعلية**
عموما، تدعم Aspose.Cells.GridWeb الروابط الفائقة التالية:

- [روابط URL](/cells/ar/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/): روابط فائقة يمكن ربطها بعناوين URL على الويب.
- [روابط النص](/cells/ar/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/): روابط URL تطبق على النص.
- [روابط الصورة](/cells/ar/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/): روابط URL تطبق على الصور.
- [روابط أوامر الخلية](/cells/ar/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/): روابط فائقة ترسل البيانات إلى خادم. تعمل مثل الزر الذي يشغل حدثاً في الخادم عند النقر.

توضح الأقسام أدناه استخدام جميع أنواع الروابط الفائقة بالتفصيل. كما تناقش كيفية الوصول إليها أو إزالتها.
### **إضافة الروابط المختصرة**

#### **روابط النص الفائقة**
روابط URL الفائقة تبدو مشابهة إلى حد ما للروابط الفائقة البسيطة التي تراها عادةً على مواقع الويب. تعمل رابط URL الفائقة مثل مرساة في الخلية. كلما تم النقر عليها، تتنقل إلى صفحة ويب أو تفتح نافذة متصفح جديدة.

هناك أنواع مختلفة من روابط URL الفائقة:

- روابط نصية.
- روابط صور.

يمكن للمطورين تحديد صورة للرابط الفائق. إذا لم يتم تحديد صورة، يتم إنشاء رابط نصي؛ وإلا يتم إنشاء رابط صورة.


##### **روابط النصوص**
لإضافة رابط نصي إلى ورقة العمل:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى نموذج الويب الخاص بك.
1. الوصول إلى ورقة العمل.
1. إضافة ارتباط هايبرلينك إلى خلية في ورقة العمل.
1. تعيين النص الذي سيظهر في الخلية.
1. تعيين عنوان URL للارتباط.
1. تعيين الهدف للارتباط الهايبرلينك، إذا كان ذلك مرغوبًا.
1. تعيين تلميح الأداة إذا كان مرغوبًا.

{{% alert color="primary" %}} 

ملاحظة: يمكن تعيين هدف الرابط الهايبرلينك إلى _self، _top أو _parent لفتح عناوين الويب في نافذة جديدة ، الحالية أو العلوية على التوالي.

{{% /alert %}} 

المثال أدناه يضيف رابطين هايبرلينك إلى ورقة عمل. أحدهما ليس له هدف بينما الآخر معين إلى _parent.

**الناتج: روابط نصية مضافة إلى ورقة العمل** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **روابط الصور**
لإضافة رابط صورة:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى نموذج الويب الخاص بك.
1. الوصول إلى ورقة العمل.
1. إضافة رابط تشعبي إلى خلية.
1. تعيين عنوان URL للصورة التي ستُعرض كارتباط.
1. تعيين عنوان URL للارتباط.
1. تعيين تلميح الأداة إذا كان مرغوبًا.
1. تعيين نص الارتباط التشعبي، إذا كان مرغوبًا.

**الإخراج: تمت إضافة روابط الصور إلى ورقة العمل** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

Setting the image hyperlink's AltText fills a similar function as setting an <ALT> tag in HTML. The text is displayed only if the hyperlinked image is not displayed. (For example, if the image isn't at the specified location.) If the image of the second hyperlink is not found, the output of the code snippet below would look as follows.

**تعذر العثور على الصورة لعنوان URL للصورة** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **روابط الأوامر الخلية**
روابط الخلية الخاصة بالأوامر الخلية هي نوع خاص من الروابط التشعبية التي تشغل حدث على الخادم بدلاً من فتح صفحة ويب. يمكن للمطورين إضافة رمز إلى الحدث على الخادم والقيام بأي مهمة عند النقر على الرابط التشعبي. تمكن هذه الميزة المطورين من إنشاء تطبيقات تفاعلية أكثر.

لإضافة رابط تشعبي للخلية:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى نموذج الويب الخاص بك.
1. الوصول إلى ورقة العمل.
1. إضافة رابط تشعبي إلى خلية.
1. تعيين أمر الرابط التشعبي إلى أي قيمة مرغوبة.
   تستخدم القيمة من قبل معالج الأحداث رابط التشعبي للتعرف عليه.
1. تعيين تلميح الأداة إذا كان مرغوبًا.
1. تعيين عنوان URL للصورة التي سيتم عرضها كارتباط.

**تمت إضافة رابط تشعبي إلى ورقة العمل** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **معالجة الأحداث لروابط الأوامر الخلية**
يحتاج المطورون إلى إنشاء معالج حدث لحدث CellCommand لعنصر التحكم GridWeb من أجل تنفيذ المهام المحددة عند النقر على رابط الأمر الخلية المحدد. يوفر معالج الحدث CellCommand نوع الخاصية CellEventArgs التي تقدم خاصية الوسيط. استخدم خاصية الوسيط لتعريف رابط تشعبي معين من خلال مقارنة قيمة أمره.

المثال أدناه ينشئ معالج حدث لرابط الأمر الخلية الذي تم إنشاؤه في الكود أعلاه. تم تعيين أمر CellCommand للرابط بالنقر. لذا، في معالج الحدث، قم بالتحقق منه أولاً ومن ثم أضف الكود الذي يعرض رسالة في الخلية A6.

يتم استدعاء معالج الأحداث عند النقر على الرابط التشعبي.

**الإخراج: تمت إضافة نص إلى الخلية A6 عند النقر على الرابط التشعبي** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **الوصول إلى الروابط التشعبية**
للوصول إلى ارتباط تشعبي موجود:

1. الوصول إلى الخلية التي تحتوي عليه.
1. الحصول على مرجع الخلية.
1. تمرير المرجع إلى طريقة الوصول إلى الارتباط التشعبي في مجموعة الارتباطات الخاصة للوصول إلى الارتباط التشعبي.
1. تعديل خصائص الارتباط التشعبي.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **إزالة الروابط التشعبية**
لإزالة ارتباط تشعبي:

1. الوصول إلى ورقة العمل النشطة.
1. إزالة ارتباط تشعبي باستخدام طريقة الإزالة في مجموعة الارتباطات الخاصة.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}

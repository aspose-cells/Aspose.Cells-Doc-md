---
title: التكبير أو التصغير على ورقة العمل في GridDesktop
type: docs
weight: 160
url: /ar/net/aspose-cells-griddesktop/zoom-in-or-out-on-the-worksheet-in-griddesktop/
keywords: GridDesktop,zoom,zoom in,zoom out
description: يقدم هذا المقال كيفية التكبير أو التصغير في GridDesktop.
---

{{% alert color="primary" %}} 

أحيانًا ، عند العمل مع بياناتك ، قد ترغب في تكبير محتويات الشاشة دون تغيير حجم الخط فعلياً. على سبيل المثال ، قد تكون قد قمت بتنسيق نصك بحيث يستخدم خطًا صغيرًا. (هذا غالبًا ما يكون ضروريًا للحصول على جميع معلوماتك في النسخة المطبوعة.) عند العمل في ورقة العمل ، لكن الخط يصعب القراءة لأنه صغير جدًا.

في برنامج Microsoft Excel ، يتوفر مُنزلق التكبير للتكبير والتصغير من المستندات بسرعة وسهولة. يكون مُنزلق التكبير عادة في الزاوية السفلية اليمنى من نافذة البرنامج.

كما يسمح Aspose.Cells أيضًا للمطورين بتعيين عامل التكبير لورقة العمل ، بحيث يجب أن تظهر المحتويات وفقًا للقيمة المئوية المرجوة.

{{% /alert %}} 
## **التكبير أو التصغير باستخدام Aspose.Cells.GridDesktop**
يوفر Aspose.Cells فئة Aspose.Cells.GridDesktop.Worksheet التي تحتوي على مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. لتعيين عامل تكبير ورقة العمل ، استخدم خاصية Zoom لفئة Worksheet. يتم تعيين عامل التكبير عن طريق تعيين قيمة رقمية (صحيحة) لخاصية Zoom.

نقوم ببناء مُنزلق التكبير مثل MS Excel باستخدام عنصر التحكم TrackBar (.NET). في مشروع WinForm ، نضع عنصر تحكم Aspose.Cells.GridDesktop من الصندوق الأدوات إلى النموذج ونحدد بعض الخصائص لتعيين اسمه وحجمه أو جوانب أخرى وفقًا لذلك. الآن ، نضع عنصر تحكم الـ TrackBar @ الزاوية السفلية اليمنى أسفل عنصر تحكم GridDesktop ، نضع أيضًا عنصر تحكم Label الذي سيريك القيمة المئوية التي تحددها عبر مقبض عنصر التحكم TrackBar. نضيف سطورًا نسبية من الكود في حدث التمرير الخاص بـ TrackBar ، بحيث عند التمرير على عنصر تحكم Trackbar ، يجب أن يكبر أو يصغر GridDesktop لإظهار البيانات/ المحتويات فيه.

أدناه مثال كامل يوضح كيفية استخدام خاصية التكبير لتعيين عامل التكبير لورقة العمل النشطة في GridDesktop. نقوم أولاً بإدخال ملف Excel نموذجي إلى GridDesktop.

قم بكتابة الكود أدناه في حدث Load للنموذج لتعيين ملف قالب Excel في GridDesktop وقيمة trackbar.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


الآن انسخ الكود أدناه داخل حدث التمرير وقم بتشغيل التطبيق. ستلاحظ أن تحريك شريط التتبع سيغير خاصية التكبير لورقة العمل.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}

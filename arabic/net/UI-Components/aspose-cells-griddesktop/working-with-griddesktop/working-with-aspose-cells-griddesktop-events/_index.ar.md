---
title: العمل مع أحداث Aspose.Cells.GridDesktop
type: docs
weight: 30
url: /ar/net/aspose-cells-griddesktop/work-with-aspose-cells-griddesktop-events/
keywords: GridDesktop, event, events
description: يقدم هذا المقال كيفية استخدام الأحداث في GridDesktop.
---

{{% alert color="primary" %}} 

تُستخدم الأحداث لإرسال الإشعارات عندما يحدث تغيير في تحكم أو فئة معينة. يحتوي Aspose.Cells.GridDesktop على العديد من الأحداث التي يتم استخدامها لتنفيذ مهام محددة عند حدوث تغييرات معينة في التحكم. يوفر هذا الموضوع مقدمة لجميع الأحداث المدعومة من قبل تحكم Aspose.Cells.GridDesktop ويشرح كيفية التعامل مع هذه الأحداث.

{{% /alert %}} 
## **مقدمة**
يدعم تحكم Aspose.Cells.GridDesktop العديد من الأحداث التي توفر مزيدًا من التحكم في أداء العمليات عند تنشئة الأحداث المحددة. أدناه قائمة كاملة بالأحداث المدعومة من قبل تحكم Aspose.Cells.GridDesktop.

{{% alert color="primary" %}} 

لا تتضمن هذه القائمة تلك الأحداث التي يتم وراثتها من فئة التحكم Control.

{{% /alert %}} 

|**الأحداث**|**الوصف**|
| :- | :- |
|BeforeCalculate| يحدث قبل حساب الصيغة في الجدول.|
|BeforeLoadFile| يحدث قبل تحميل المصنف من الملف.|
|ColumnHeaderClick|يحدث عند النقر على رأس العمود.|
|ColumnHeaderDoubleClick|يحدث عند النقر المزدوج على رأس العمود.|
|CellDataChanged|حدث يحدث عند تغيير البيانات أو القيمة داخل خلية الجدول. يمكن أيضًا تشغيل هذا الحدث إذا تم تغيير قيمة الخلية برمجيًا باستخدام خاصية القيمة أو طريقة SetCellValue لـ GridCell.
|CellButtonClick|يحدث عند النقر على زر الخلية.
|CellCheckedChanged|يحدث عند تغيير خاصية التحقق من الصحة لخانة الاختيار داخل الخلية.
|CellSelectedIndexChanged|يحدث عند تغيير الفهرس المحدد لخلية القائمة المنسدلة.
|CellClick|يحدث عند نقر على خلية الجدول.
|CellDoubleClick|يحدث عند النقر المزدوج على خلية الجدول. |
|CellKeyPressed|يحدث عند الضغط على مفتاح أثناء تركيز الخلية. إذا كنت ترغب في إنشاء معالج حدث لحدث CellKeyPressed، فقم بضبط خاصية Handled لوسيطة CellKeyEventArgs على true لمنع عنصر تحكم GridDesktop من معالجة حدث المفتاح.
|AfterInsertColumns|يحدث عند إدراج عمود. يمكنك الحصول على فهرس العمود باستخدام خاصية Index لوسيطة Aspose.Cells.GridDesktop.WorksheetEventArgs.
|AfterInsertRows|يحدث عند إدراج صف. يمكنك الحصول على فهرس الصف باستخدام خاصية Index لوسيطة Aspose.Cells.GridDesktop.WorksheetEventArgs.
|FailLoadFile| يحدث عند فشل تحميل الدفتر.
|FinishCalculate| يحدث بعد حساب الصيغة في الدفتر.
|FinishLoadFile| يحدث عند تحميل الدفتر.
|FocusedCellChanged| يحدث كلما تغير تركيز الخلية.
|RowHeaderClick| يحدث عند نقر رأس الصف.
|RowHeaderDoubleClick| يحدث عند نقر مزدوج على رأس الصف.
|RowColumnHiddenChanged| يحدث عند تغيير حالة إخفاء الصف أو العمود.
|SelectedSheetIndexChanged| يحدث عندما يختار المستخدم ورقة عمل جديدة، أي عندما يتغير ورقة العمل المحددة من ورقة عمل إلى أخرى. يمكن أيضًا تشغيل هذا الحدث برمجيًا إذا تغيرت خاصية ActiveSheetIndex لعنصر تحكم GridDesktop.
## **معالجة أحداث الجدول**
لأداء عملية معينة عند تشغيل حدث معين، أنشئ معالج حدث. يقوم معالج الحدث بأداء مهمة معينة عندما يتم تشغيل حدث معين. فيما يلي تهيئة معالج حدث للتعامل مع حدث جدول بسيط باستخدام Visual Studio.NET.

**الخطوة 1: اختيار حدث لعنصر تحكم Aspose.Cells.GridDesktop**

1. في Visual Studio، حدد عنصر تحكم Aspose.Cells.GridDesktop وافتح صندوق حوار **الخصائص** الخاص به.
1. انقر على علامة التبويب **الأحداث**.
1. حدد حدثًا (على سبيل المثال، يتم اختيار حدث **CellClick** لهذا المثال).

**الخطوة 2: إنشاء معالج الأحداث**

1. انقر نقرًا مزدوجًا فوق الحدث المحدد في صندوق حوار **الخصائص**.
عندما يتم نقر مزدوج على الحدث، يتم إنشاء معالج الأحداث من قبل Visual Studio.NET. يظهر الكود الذي أنشأه المصمم والذي يوضح أن الحدث تم إنشاؤه لعنصر تحكم GridControl.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


الآن أضف الكود لتنفيذ العملية المرغوبة داخل معالج الأحداث. في هذا المثال، قمنا بإضافة سطر من الكود يعرض صندوق رسالة للإشعارات. 
انظر إلى معالج الأحداث الذي أضافته Visual Studio إلى حدث CellClick لعنصر تحكم GridDesktop. سيبدو شيئًا مشابه للكود أدناه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**الخطوة 3: تشغيل التطبيق**

1. قم ببناء التطبيق وتشغيله.
1. كلما تم النقر على خلية الجدول، يظهر صندوق رسالة برسالة "تم النقر على الخلية".

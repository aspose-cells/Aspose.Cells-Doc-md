---
title: العمل مع Aspose.Cells.GridDesktop Events
type: docs
weight: 30
url: /ar/net/working-with-aspose-cells-griddesktop-events/
---
{{% alert color="primary" %}} 

تُستخدم الأحداث لإرسال إشعارات عند حدوث تغيير في عنصر تحكم أو فصل دراسي. Aspose.Cells.GridDesktop العديد من الأحداث التي يتم استخدامها لتنفيذ مهام محددة عند حدوث تغييرات معينة في عنصر التحكم. يقدم هذا الموضوع مقدمة لجميع الأحداث التي يدعمها Aspose.Cells.GridDesktop ويشرح كيف يمكن التعامل مع هذه الأحداث.

{{% /alert %}} 
## **مقدمة**
يدعم التحكم Aspose.Cells.GridDesktop العديد من الأحداث التي توفر مزيدًا من التحكم لإجراء العمليات عند بدء أحداث معينة. يوجد أدناه قائمة كاملة بالأحداث التي يدعمها Aspose.Cells.GridDesktop control.

{{% alert color="primary" %}} 

لا تتضمن هذه القائمة الأحداث التي ورثتها Aspose.Cells.GridDesktop من فئة التحكم.

{{% /alert %}} 

|**الأحداث**|**وصف**|
|:- |:- |
|قبل الحساب|يحدث قبل حساب الصيغة في المصنف.|
|BeforeLoadFile|يحدث قبل تحميل المصنف من ملف.|
|ColumnHeaderClick|يحدث عند النقر فوق رأس العمود.|
|ColumnHeaderDoubleClick|يحدث عند النقر المزدوج فوق رأس العمود.|
|CellDataChanged|يحدث عند تغيير البيانات أو القيمة داخل خلية الشبكة. يمكن أيضًا تشغيل هذا الحدث إذا تم تغيير قيمة الخلية برمجيًا باستخدام خاصية القيمة أو طريقة SetCellValue لشبكة GridCell.|
|CellButtonClick|يحدث عند النقر فوق زر الخلية.|
|CellCheckedChanged|يحدث عندما يتم تغيير خانة اختيار الخاصية المحددة للخلية.|
|CellSelectedIndexChanged|يحدث عند تغيير الخاصية SelectedIndex لمربع التحرير والسرد الخلية.|
|سيل كليك|يحدث عند النقر فوق خلية الشبكة.|
|CellDoubleClick|يحدث عند النقر المزدوج فوق خلية الشبكة.|
|CellKeyPressed|يحدث عند الضغط على مفتاح أثناء التركيز على الخلية. إذا كنت ترغب في إنشاء معالج حدث لحدث CellKeyPressed ، فقم بتعيين الخاصية Handled لوسيطة CellKeyEventArgs إلى true لمنع عنصر تحكم GridDesktop من معالجة الحدث الرئيسي.|
|AfterInsertColumns|يحدث عند إدراج عمود. يمكنك الحصول على فهرس العمود باستخدام خاصية فهرس الوسيطة Aspose.Cells.GridDesktop.WorksheetEventArgs.|
|AfterInsertRows|يحدث عند إدراج صف. يمكنك الحصول على فهرس الصف باستخدام خاصية فهرس الوسيطة Aspose.Cells.GridDesktop.WorksheetEventArgs.|
|FailLoadFile|يحدث عند فشل تحميل المصنف.|
|FinishCalculate|يحدث بعد حساب الصيغة في المصنف.|
|FinishLoadFile|يحدث عند تحميل المصنف.|
|مركزة الخلية|يحدث كلما تغير تركيز الخلية.|
|RowHeaderClick|يحدث عند النقر فوق رأس الصف.|
|RowHeaderDoubleClick|يحدث عند النقر المزدوج فوق رأس الصف.|
|RowColumnHiddenChanged|يحدث عند تغيير حالة الصف أو العمود المخفي.|
|SelectedSheetIndexChanged|يحدث عندما يحدد المستخدم ورقة عمل جديدة ، أي عندما تتغير الورقة المحددة من ورقة عمل إلى أخرى. يمكن أيضًا تشغيل هذا الحدث برمجيًا إذا تغيرت الخاصية ActiveSheetIndex لعنصر التحكم GridDesktop.|
## **معالجة أحداث الشبكة**
لإجراء عملية محددة عند بدء حدث معين ، قم بإنشاء معالج حدث. يقوم معالج الأحداث بتنفيذ مهمة معينة عند تشغيل حدث معين. أدناه ، تم إعداد معالج الحدث للتعامل مع حدث الشبكة البسيط باستخدام Visual Studio.NET.

**الخطوة 1: تحديد حدث Aspose.Cells.GridDesktop Control**

1. في Visual Studio ، حدد Aspose.Cells.GridDesktop control وافتحه**الخصائص**الحوار.
1.  انقر على**الأحداث** التبويب.
1.  حدد حدثًا. (على سبيل المثال ، ملف**سيل كليك** تم تحديد الحدث).

**الخطوة 2: إنشاء معالج الأحداث**

1.  انقر نقرًا مزدوجًا فوق حدث محدد في ملف**الخصائص**الحوار.
1. عند النقر مرتين على الحدث ، يتم إنشاء معالج الحدث بواسطة Visual Studio.NET. فيما يلي رمز تم إنشاؤه بواسطة المصمم والذي يوضح أن حدثًا تم إنشاؤه للتحكم في GridControl.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


 أضف الآن رمزًا لإجراء العملية المطلوبة داخل معالج الأحداث. في هذا المثال ، أضفنا سطرًا من التعليمات البرمجية يعرض مربع رسالة للإشعارات.
ألق نظرة على معالج الأحداث الذي أضافه Visual Studio إلى حدث CellClick للتحكم في GridDesktop. سيبدو مثل الرمز أدناه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**الخطوة 3: تشغيل التطبيق**

1. بناء وتشغيل التطبيق.
1. عند النقر فوق خلية شبكة ، يظهر مربع رسالة بالرسالة "تم النقر على Cell".

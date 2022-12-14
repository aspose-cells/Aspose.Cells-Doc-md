---
title: العمل مع GridWeb انقر نقرا مزدوجا فوق الأحداث
type: docs
weight: 80
url: /ar/net/working-with-gridweb-double-click-events/
---
{{% alert color="primary" %}} 

يحتوي Aspose.Cells.GridWeb على ثلاثة أنواع من أحداث النقر المزدوج:

- CellDoubleClick ، يتم تشغيله عند النقر نقرًا مزدوجًا على خلية.
- ColumnDoubleClick ، يتم تشغيله عند النقر نقرًا مزدوجًا فوق رأس العمود.
- RowDoubleClick ، يتم تشغيله عند النقر نقرًا مزدوجًا فوق رأس صف.

يناقش هذا الموضوع كيفية تمكين أحداث النقر المزدوج في Aspose.Cells.GridWeb. كما يناقش إنشاء معالجات الأحداث لهذه الأحداث.

{{% /alert %}} 
## **تمكين أحداث النقر المزدوج**
يمكن تمكين جميع أنواع أحداث النقر المزدوج من جانب العميل عن طريق تعيين خاصية EnableDoubleClickEvent للتحكم في GridWeb إلى true.

{{% alert color="primary" %}} 

بشكل افتراضي ، يتم تعيين الخاصية EnableDoubleClickEvent على false. هذا يعني أن أحداث النقر المزدوج لا يتم تمكينها افتراضيًا. لتنفيذ مثل هذه الأحداث ، قم أولاً بتمكين الميزة.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



بمجرد تمكين النقر المزدوج فوق الأحداث ، من الممكن إنشاء معالجات الأحداث لأي أحداث انقر نقرًا مزدوجًا عليها. تؤدي معالجات الأحداث هذه مهامًا محددة عند تشغيل حدث نقر مزدوج معين.
## **معالجة أحداث النقر المزدوج**
لإنشاء معالج حدث في Visual Studio:

1.  انقر نقرًا مزدوجًا فوق حدث في ملف**الأحداث** قائمة في جزء الخصائص.

في هذا المثال ، قمنا بتطبيق معالجات الأحداث للعديد من أحداث النقر المزدوج.
### **انقر نقرًا مزدوجًا فوق Cell**
يوفر معالج الحدث للحدث CellDoubleClick وسيطة من النوع CellEventArgs ، والتي توفر المعلومات الكاملة للخلية التي تم النقر عليها نقرًا مزدوجًا.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **انقر نقرًا مزدوجًا فوق رأس العمود**
يوفر معالج الحدث لحدث ColumnDoubleClick وسيطة من النوع RowColumnEventArgs الذي يوفر رقم الفهرس للعمود للرأس الذي تم النقر فوقه نقرًا مزدوجًا ومعلومات أخرى.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **انقر نقرًا مزدوجًا فوق رأس الصف**
يوفر معالج الحدث للحدث RowDoubleClick وسيطة من النوع RowColumnEventArgs الذي يوفر رقم الفهرس للصف الخاص بالرأس الذي تم النقر فوقه نقرًا مزدوجًا والمعلومات الأخرى ذات الصلة.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}

---
title: العمل مع أحداث النقر المزدوج في GridWeb
type: docs
weight: 80
url: /ar/net/aspose-cells-gridweb/gridweb-double-click-event/
keywords: GridWeb، نقر مزدوج، حدث النقر، حدث
description: يقدم هذا المقال كيفية استخدام حدث النقر المزدوج في GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb يحتوي على ثلاثة أنواع من أحداث النقر المزدوج:

- CellDoubleClick، تنشأ عندما يتم النقر المزدوج على خلية.
- ColumnDoubleClick، تنشأ عندما يتم النقر المزدوج على رأس العمود.
- RowDoubleClick، تنشأ عندما يتم النقر المزدوج على رأس الصف.

يناقش هذا الموضوع كيفية تمكين أحداث النقر المزدوج في Aspose.Cells.GridWeb. كما يناقش إنشاء معالجي الأحداث لهذه الأحداث.

{{% /alert %}} 
## **تمكين أحداث النقر المزدوج**
يمكن تمكين جميع أنواع أحداث النقر المزدوج على الجانب العميلي عن طريق ضبط خاصية EnableDoubleClickEvent لعنصر تحكم GridWeb على true.

{{% alert color="primary" %}} 

بشكل افتراضي، يتم ضبط خاصية EnableDoubleClickEvent على القيمة false. وهذا يعني أن أحداث النقر المزدوج غير ممكّنة بشكل افتراضي. لتنفيذ مثل هذه الأحداث، يجب تمكين الميزة أولاً.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



بمجرد تمكين أحداث النقر المزدوج، يمكن إنشاء معالجين للأحداث لأي من حوادث النقر المزدوج. يقوم هذان المعالجان بتنفيذ مهام محددة عند حدوث أي حدث نقر مزدوج معين.
## **معالجة أحداث النقر المزدوج**
لإنشاء معالج حدث في Visual Studio:

1. انقر نقرًا مزدوجًا على الحدث في قائمة **الأحداث** في نافذة الخصائص.

على سبيل المثال، قمنا بتنفيذ معالجين لأحداث النقر المزدوج المختلفة.
### **نقر مزدوج على الخلية**
يوفر معالج الحدث لحدث CellDoubleClick وسيطًا من نوع CellEventArgs، الذي يوفر المعلومات الكاملة عن الخلية التي تم النقر عليها.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **نقر مزدوج في رأس العمود**
يوفر معالج الحدث لحدث ColumnDoubleClick وسيطًا من نوع RowColumnEventArgs الذي يوفر رقم الفهرس للعمود الذي تم النقر عليه ومعلومات أخرى.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **نقر مزدوج في رأس الصف**
يوفر معالج الحدث لحدث RowDoubleClick وسيطًا من نوع RowColumnEventArgs الذي يوفر رقم الفهرس للصف الذي تم النقر عليه ومعلومات أخرى ذات صلة.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}

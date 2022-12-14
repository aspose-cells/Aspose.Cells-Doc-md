---
title: عرض وإخفاء أشرطة التمرير
type: docs
weight: 140
url: /ar/net/display-and-hide-scroll-bars/
---
{{% alert color="primary" %}}

تُعد أشرطة التمرير مفيدة للتنقل في محتويات جداول البيانات العريضة والعميقة ، أي التي تحتوي على العديد من الصفوف والأعمدة. تدعم معظم التطبيقات نوعين من شريط التمرير:

- شريط التمرير العمودي
- شريط التمرير الأفقي

تم العثور على كلاهما في Microsoft Excel.

يوفر Aspose.Cell's GridDesktop API أشرطة تمرير أفقية ورأسية للتمرير عبر محتويات ورقة العمل. مع Aspose.Cells.GridDesktop APIs ، يمكن للمطورين التحكم في رؤية كل من أشرطة التمرير هذه.

{{% /alert %}}

## **التحكم في رؤية شريط التمرير**

للتحكم في رؤية شريط التمرير في GridDesktop ، استخدم خصائص IsVerticalScrollBarVisible و IsHorizontalScrollBarVisible. توضح الأمثلة أدناه كيفية إخفاء وإظهار أشرطة التمرير.

### **نماذج البرمجة: إخفاء أشرطة التمرير**

لإخفاء أشرطة التمرير ، اضبط الخصائص التي تتحكم في الرؤية على false.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-HideScrollbars.cs" >}}

### **نماذج البرمجة: جعل أشرطة التمرير مرئية**

لجعل أشرطة التمرير مرئية ، قم بتعيين الخصائص التي تتحكم في الرؤية على "صواب".

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-ShowScrollbars.cs" >}}

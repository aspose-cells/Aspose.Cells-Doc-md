---
title: الخط الافتراضي ولون الخط لـ GridDesktop
type: docs
weight: 70
url: /ar/net/aspose-cells-griddesktop/default-font-and-font-color-of-the-griddesktop/
keywords: GridDesktop، الخط، اللون
description: يقدم هذا المقال موجزًا عن الخط الافتراضي ولون الخط في GridDesktop.
---

## **سيناريوهات الاستخدام المحتملة**
أحيانًا، ترغب في تغيير الخط الافتراضي ولون الخط لـ GridDesktop. يُرجى استخدام الخاصيتين التاليتين لهذا الغرض. يمكنك الوصول إلى هذه الخصائص خلال تصميم الوقت أو في الوقت التشغيلي وفقًا لاحتياجاتك.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **تغيير الخط الافتراضي ولون الخط في وقت التصميم**
اللقطة الشاشية التالية توضح كيفية تغيير الخط الافتراضي ولون الخط لـ GridDesktop في وقت التصميم.

![todo:image_alt_text](default-font-and-font-color-of-the-griddesktop_1.png)
## **تغيير الخط الافتراضي ولون الخط في وقت التشغيل**
الشيفرة العينية التالية توضح كيفية تغيير الخط الافتراضي ولون الخط لـ GridDesktop في وقت التشغيل.

{{< highlight java >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}

---
title: الخط الافتراضي ولون الخط لشبكة GridDesktop
type: docs
weight: 70
url: /ar/net/default-font-and-font-color-of-the-griddesktop/
---
## **سيناريوهات الاستخدام الممكنة**
في بعض الأحيان ، تريد تغيير الخط الافتراضي ولون الخط في GridDesktop. الرجاء استخدام الخاصيتين التاليتين لهذا الغرض. يمكنك الوصول إلى هذه الخصائص في وقت التصميم أو في وقت التشغيل حسب احتياجاتك.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **تغيير الخط الافتراضي ولون الخط في وقت التصميم**
توضح لقطة الشاشة التالية كيفية تغيير الخط الافتراضي ولون الخط في GridDesktop في وقت التصميم.

![ما يجب القيام به: image_بديل_نص](default-font-and-font-color-of-the-griddesktop_1.png)
## **تغيير الخط الافتراضي ولون الخط في وقت التشغيل**
يوضح نموذج التعليمات البرمجية التالي كيفية تغيير الخط الافتراضي ولون الخط في GridDesktop في وقت التشغيل.

{{< highlight "java" >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}

---
title: سمات وألوان Excel
type: docs
weight: 130
url: /ar/java/excel-2007-themes-and-colors/
---
{{% alert color="primary" %}}

توفر النسق مظهرًا موحدًا مع أنماط مسماة وتأثيرات رسومية وكائنات أخرى مستخدمة في مصنف. على سبيل المثال ، يبدو نمط Accent1 مختلفًا في نسق Office و Apex. في كثير من الأحيان ، تقوم بتطبيق نسق المستند ثم تعديله حسب احتياجاتك.

**تطبيق السمات في Microsoft Excel**

![ما يجب القيام به: image_بديل_نص](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **الحصول على ألوان النسق وتعيينها**

توفر واجهات برمجة التطبيقات Aspose.Cells ميزات لتخصيص السمات والألوان. فيما يلي بعض الطرق والخصائص التي تنفذ ألوان النسق.

- يمكن استخدام خاصية Style.ForegroundThemeColor لتعيين لون المقدمة.
- يمكن استخدام خاصية Style.BackgroundThemeColor لتعيين لون الخلفية.
- يمكن استخدام خاصية Font.ThemeColor لتعيين لون الخط.
- يمكن استخدام طريقة Workbook.getThemeColor للحصول على لون النسق.
- يمكن استخدام طريقة Workbook.setThemeColor لتعيين لون النسق.

يوضح المثال التالي كيفية الحصول على ألوان النسق وتعيينها.

يستخدم المثال التالي ملف قالب XLSX ، ويحصل على ألوان لأنواع مختلفة من ألوان النسق ، ويغير الألوان ويحفظ ملف Excel Microsoft.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **تخصيص السمات**

يوضح المثال التالي كيفية تطبيق السمات المخصصة بالألوان التي تريدها. يستخدم المثال نموذج ملف تم إنشاؤه يدويًا في Microsoft Excel 2007.

**ملف قالب CustomThemeColor.xlsx**

![ما يجب القيام به: image_بديل_نص](excel-2007-themes-and-colors_2.png)

يقوم المثال التالي بتحميل ملف قالب XLSX ، وتحديد الألوان لأنواع ألوان السمة المختلفة ، وتطبيق الألوان المخصصة وحفظ ملف Excel.

**الملف الذي تم إنشاؤه بألوان النسق المخصصة**

![ما يجب القيام به: image_بديل_نص](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **استخدام ألوان النسق**

يطبق المثال التالي ألوان المقدمة والخط للخلية بناءً على أنواع ألوان النسق الافتراضي (للمصنف). كما أنه يحفظ ملف Excel على القرص.

يتم إنشاء الإخراج التالي عند تنفيذ التعليمات البرمجية.

**يتم تطبيق ألوان النسق على الخلية D3 من ورقة العمل** 

![ما يجب القيام به: image_بديل_نص](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **موضوعات مسبقة**
- [استخراج بيانات الموضوع من ملف Excel](/cells/ar/java/extract-theme-data-from-excel-file/)

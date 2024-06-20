---
title: ثيمات وألوان إكسل
type: docs
weight: 130
url: /ar/java/excel-2007-themes-and-colors/
---

{{% alert color="primary" %}}

توفر المواضيع مظهرًا موحدًا مع أنماط مسماة وتأثيرات بصرية وكائنات أخرى مستخدمة في دفتر العمل. على سبيل المثال، يبدو نمط Accent1 مختلفًا في الموضوعات Office وApex. غالبًا ما تطبق موضوع مستند ومن ثم تقوم بتعديله حسب احتياجاتك.

**تطبيق الموضوعات في Microsoft Excel**

![todo:image_alt_text](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **الحصول على الألوان وتعيين الموضوع**

توفر واجهات برمجة التطبيق لـ Aspose.Cells ميزات لتخصيص الموضوعات والألوان. فيما يلي بعض الطرق والخصائص التي تنفذ ألوان الموضوع.

- يمكن استخدام خاصية Style.ForegroundThemeColor لتعيين لون الخلفية.
- يمكن استخدام خاصية Style.BackgroundThemeColor لتعيين لون الخلفية.
- يمكن استخدام خاصية Font.ThemeColor لتعيين لون الخط.
- يمكن استخدام طريقة Workbook.getThemeColor للحصول على لون من الموضوع.
- يمكن استخدام طريقة Workbook.setThemeColor لتعيين لون الموضوع.

المثال التالي يوضح كيفية الحصول على وتعيين ألوان الثيم.

المثال التالي يستخدم ملف XLSX قالب، يحصل على الألوان لأنواع مختلفة من الألوان الثيم، يقوم بتغيير الألوان ويحفظ ملف Microsoft Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **تخصيص السمات**

يظهر المثال التالي كيفية تطبيق سمات مخصصة بألوانك المفضلة. يستخدم المثال ملف قالب عينة تم إنشاؤه يدويًا في Microsoft Excel 2007.

**ملف القالب CustomThemeColor.xlsx**

![todo:image_alt_text](excel-2007-themes-and-colors_2.png)

المثال التالي يحمل ملف XLSX قالبيًا، يحدد الألوان لأنواع مختلفة من الألوان الثيمية، بالإضافة إلى تطبيق الألوان المخصصة وحفظ ملف إكسيل.

**الملف المولّد بألوان سمات مخصصة**

![todo:image_alt_text](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **استخدام ألوان السمة**

المثال التالي يطبق ألوان الخلفية والخط لخلية استنادًا إلى أنواع ألوان الثيمة الافتراضية (للجدول). يحفظ أيضًا ملف إكسيل على القرص.

يتم إنشاء الإخراج التالي عند تنفيذ الكود.

**الألوان السمة المطبّقة على خلية D3 من ورقة العمل** 

![todo:image_alt_text](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **مواضيع متقدمة**
- [استخراج بيانات الثيم من ملف Excel](/cells/ar/java/extract-theme-data-from-excel-file/)

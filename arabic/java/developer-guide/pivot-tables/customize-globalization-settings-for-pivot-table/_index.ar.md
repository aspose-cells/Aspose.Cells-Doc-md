---
title: تخصيص إعدادات العولمة للجدول المحوري
type: docs
weight: 20
url: /ar/java/customize-globalization-settings-for-pivot-table/
---
## **سيناريوهات الاستخدام الممكنة**

 في بعض الأحيان تريد تخصيص ملف*الإجمالي المحوري ، الإجمالي الفرعي ، الإجمالي الكلي ، كل العناصر ، العناصر المتعددة ، تسميات الأعمدة ، تسميات الصفوف ، القيم الفارغة*نص حسب متطلباتك. يسمح لك Aspose.Cells بتخصيص إعدادات العولمة للجدول المحوري للتعامل مع مثل هذه السيناريوهات. يمكنك أيضًا استخدام هذه الميزة لتغيير التسميات إلى لغات أخرى مثل العربية والهندية والبولندية وما إلى ذلك.

## **تخصيص إعدادات العولمة للجدول المحوري**

 يوضح نموذج التعليمات البرمجية التالي كيفية تخصيص إعدادات العولمة للجدول المحوري. يخلق فئة*CustomPivotTableGlobalizationSettings* مشتق من فئة أساسية[**العولمة الإعدادات**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) ويتجاوز جميع الأساليب الضرورية. تقوم هذه الطرق بإرجاع النص المخصص لملف*الإجمالي المحوري ، الإجمالي الفرعي ، الإجمالي الكلي ، كل العناصر ، العناصر المتعددة ، تسميات الأعمدة ، تسميات الصفوف ، القيم الفارغة* . ثم يقوم بتعيين كائن من هذه الفئة إلى[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) منشأه. يقوم الكود بتحميل ملف[ملف اكسل المصدر](40468491.xlsx) الذي يحتوي على الجدول المحوري ، يقوم بتحديث بياناته وحسابها وحفظها كملف[إخراج ملف PDF](40468490.pdf) . توضح لقطة الشاشة التالية تأثير نموذج التعليمات البرمجية على ملف PDF الناتج. كما ترى في لقطة الشاشة ، تحتوي أجزاء مختلفة من الجدول المحوري الآن على نص مخصص يتم إرجاعه بواسطة الطرق المتجاوزة لـ[**العولمة الإعدادات**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)صف دراسي.

![ما يجب القيام به: image_بديل_نص](customize-globalization-settings-for-pivot-table_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}

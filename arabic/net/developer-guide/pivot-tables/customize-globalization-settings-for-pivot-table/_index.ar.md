---
title: تخصيص إعدادات العولمة للجدول المحوري
type: docs
weight: 50
url: /ar/net/customize-globalization-settings-for-pivot-table/
---
##  **سيناريوهات الاستخدام المحتملة**

 في بعض الأحيان تريد تخصيص*الإجمالي المحوري، الإجمالي الفرعي، الإجمالي الكلي، كافة العناصر، العناصر المتعددة، تسميات الأعمدة، تسميات الصفوف، القيم الفارغة*النص وفقا لمتطلباتك. Aspose.Cells يسمح لك بتخصيص إعدادات العولمة للجدول المحوري للتعامل مع مثل هذه السيناريوهات. يمكنك أيضًا استخدام هذه الميزة لتغيير التسميات إلى لغات أخرى مثل العربية والهندية والبولندية وما إلى ذلك.

##  **تخصيص إعدادات العولمة للجدول المحوري**

يشرح نموذج التعليمات البرمجية التالي كيفية تخصيص إعدادات العولمة للجدول المحوري. إنه يخلق فئة*إعدادات العولمة CustomPivotTable* مشتقة من فئة أساسية[**إعدادات العولمة المحورية**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)ويتجاوز جميع أساليبه الضرورية. تقوم هذه الطرق بإرجاع النص المخصص لـ *الإجمالي المحوري، والإجمالي الفرعي، والإجمالي الكلي، وجميع العناصر، والعناصر المتعددة، وتسميات الأعمدة، وتسميات الصفوف، والقيم الفارغة*. ثم يقوم بتعيين كائن هذه الفئة إلى[**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/) ملكية. يقوم الكود بتحميل[ملف اكسيل المصدر](40468488.xlsx) الذي يحتوي على الجدول المحوري، ويقوم بتحديث وحساب بياناته وحفظها باسمه[الإخراج PDF](40468487.pdf) ملف. توضح لقطة الشاشة التالية تأثير نموذج التعليمات البرمجية على الإخراج PDF. كما ترون في لقطة الشاشة، تحتوي أجزاء مختلفة من الجدول المحوري الآن على نص مخصص تم إرجاعه بواسطة الطرق التي تم تجاوزها[**إعدادات العولمة المحورية**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)فصل.

![ما يجب القيام به:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}

---
title: تخصيص إعدادات العالمية لجدول محوري
type: docs
weight: 50
url: /ar/net/customize-globalization-settings-for-pivot-table/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان ترغب في تخصيص *إجمالي الجدول المحوري، الإجمالي الفرعي، الإجمالي الكلي، جميع العناصر، العناصر المتعددة، تسميات الأعمدة، تسميات الصفوف، القيم الفارغة* نصوص وفقًا لمتطلباتك. تتيح لك Aspose.Cells تخصيص إعدادات العالمية للجدول المحوري للتعامل مع مثل هذه السيناريوات. يمكنك أيضًا استخدام هذه الميزة لتغيير التسميات إلى لغات أخرى مثل العربية والهندية والبولندية، إلخ.

## **تخصيص إعدادات العالمية لجدول محوري**

يشرح الكود العيني التالي كيفية تخصيص إعدادات التعميم لجدول الدوران. ينشئ فئة *CustomPivotTableGlobalizationSettings* مستمدة من فئة القاعدة [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/) ويعيد جميع الأساليب الضرورية الخاصة بها. تُعيد هذه الأساليب النص المخصص لـ *إجمالي الجدول الدوري، الجدول الدوري الفرعي، الجدول الدوري الكبير، جميع العناصر، عناصر متعددة، تسميات الأعمدة، تسميات الصفوف، القيم الفارغة*. ثم يُعين الكائن لهذه الفئة على خاصية [**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/). يحمل الكود ملف إكسل مصدري يحتوي على الجدول الدوراني، يقوم بتحديث بياناته وحساباته ويحفظه كملف [PDF الإخراج](40468487.pdf). تُظهر اللقطة الشاشية التالية تأثير الشفرة العينية على ملف الإخراج بصيغة PDF. كما ترون في اللقطة الشاشية، الأجزاء المختلفة من الجدول الدوراني تحتوي الآن على نص مخصص يتم إرجاعه بوساطة الأساليب المحلية لفئة [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/).

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}

---
title: تخصيص إعدادات العالمية لجدول محوري
type: docs
weight: 20
url: /ar/java/customize-globalization-settings-for-pivot-table/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان ترغب في تخصيص *إجمالي الجدول المحوري، الإجمالي الفرعي، الإجمالي الكلي، جميع العناصر، العناصر المتعددة، تسميات الأعمدة، تسميات الصفوف، القيم الفارغة* نصوص وفقًا لمتطلباتك. تتيح لك Aspose.Cells تخصيص إعدادات العالمية للجدول المحوري للتعامل مع مثل هذه السيناريوات. يمكنك أيضًا استخدام هذه الميزة لتغيير التسميات إلى لغات أخرى مثل العربية والهندية والبولندية، إلخ.

## **تخصيص إعدادات العالمية لجدول محوري**

يشرح الكود المصدر التالي كيفية تخصيص إعدادات العالمية لجدول المحور. ينشئ فئة *CustomPivotTableGlobalizationSettings* مشتقة من الفئة الأساسية [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) وتعيد جميع الطرق المطلوبة. تعيد هذه الطرق النص المخصص لـ *الإجمالي الجدولي، الإجمالي الفرعي، الإجمالي الكلي، جميع العناصر، العناصر المتعددة، تسميات الأعمدة، تسميات الصفوف، القيم الفارغة*. ثم يعين كائن هذه الفئة لخاصية [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings). الكود يحمل [ملف الإكسل المصدر](40468491.xlsx) الذي يحتوي على جدول الدوران ويقوم بتحديث بياناته وحسابها ثم يحفظه كـ [ملف PDF الإخراجي](40468490.pdf). يوضح اللقطة الفوتوغرافية التالية تأثير الكود المصدري على الناتج بتأثير العديد من جزء الجدول المحوري الذي يعود نصه الى الطرق المعدلة للفئة [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings).

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}

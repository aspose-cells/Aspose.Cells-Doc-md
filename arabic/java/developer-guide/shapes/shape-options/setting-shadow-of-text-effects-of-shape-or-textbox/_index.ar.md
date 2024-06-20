---
title: ضبط الظلال لتأثيرات النص للشكل أو مربع النص
type: docs
weight: 670
url: /ar/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}} 

يمكنك ضبط **الظلال** ل**تأثيرات النص** لأي شكل أو مربع نص. الرجاء استخدام خاصية [Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody). يقدم إعداد نص الشكل ويُرجع [FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection). بعد الوصول إلى [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) منه، يرجى ضبط **الظل** عبر خاصية [FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType). هذه الخاصية من نوع [PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType) وتحتوي على قيم متعددة. بعض هذه هي

- [التحويل_القطري_للأسفل_اليمين](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [التحويل_للأسفل](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [التحويل_القطري_للأعلى_اليمين](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [الداخل_الأيسر](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [الداخل_المركز](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [المنظور_القطري_الأعلى_الأيسر](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [المنظور_القطري_الأعلى_الأيمن](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **ضبط ظلال تأثيرات النص للشكل أو مربع النص**
تُظهر اللقطة المصغرة التالية [ملف الإكسل الناتج](5473446.xlsx) الذي تم إنشاؤه باستخدام رمز العينة التالي. تُظهر اللقطة المصغرة أيضًا قيمة **الظل** التي تم ضبطها كـ **الظل السفلي**.

![todo:image_alt_text](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}

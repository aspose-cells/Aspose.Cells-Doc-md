---
title: تعيين ظل تأثيرات النص للشكل أو مربع النص
type: docs
weight: 670
url: /ar/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}} 

 يمكنك ضبط ملف**ظل** من**تأثيرات النص** من أي شكل أو مربع نص. الرجاء استخدام[الشكل والنص الجسم](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody) منشأه. يقدم إعداد نص الشكل والعودة[FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection) . بعد الوصول[إعداد الخط](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) منه ، يرجى ضبط**ظل** عبر[FontSetting.getTextOptions (). getShadow (). setPresetType ()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType) منشأه. هذه الخاصية من النوع[PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType)التي لها عدة قيم. بعض هؤلاء

- [عوض_قطري_أسفل اليمين](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [OFFSET_BOTTOM](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [عوض_قطري_فوق على اليمين](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [INSIDE_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [INSIDE_CENTER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [إنطباع_قطري_اليسار العلوي](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [إنطباع_قطري_UPPER_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **تعيين ظل تأثيرات النص للشكل أو مربع النص**
تُظهر لقطة الشاشة التالية ملف[ملف اكسل الناتج](5473446.xlsx) تم إنشاؤه باستخدام نموذج التعليمات البرمجية التالي. تُظهر لقطة الشاشة أيضًا قيمة ملف**ظل** الذي تم تعيينه كـ**تعويض القاع**.

![ما يجب القيام به: image_بديل_نص](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}

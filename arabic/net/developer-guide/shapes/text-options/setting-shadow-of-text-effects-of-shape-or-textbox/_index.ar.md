---
title: تعيين ظل تأثيرات النص للشكل أو مربع النص
type: docs
weight: 250
url: /ar/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}}

 يمكنك ضبط ملف**ظل** من**تأثيرات النص** من أي شكل أو مربع نص. الرجاء استخدام[**الشكل والنص الجسم**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody) منشأه. يقدم إعداد نص الشكل والعودة[**إعداد الخط**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) أشياء. بعد الوصول إليه ، يرجى ضبط**ظل** عبر[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) منشأه. هذه الخاصية من النوع[**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype)التي لها عدة قيم. بعض هؤلاء

- الإزاحة قطري سفلي لليمين
- OffsetBottom
- OffsetDiagonalTopRight
- داخل اليسار
- داخل المركز
- منظور قطري أعلى اليسار
- منظور قطري منخفض يمين

{{% /alert %}}

يوضح مقتطف الشفرة التالي استخدام[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype)لتعيين تأثيرات الظل للنص في Shape أو TextBox.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}

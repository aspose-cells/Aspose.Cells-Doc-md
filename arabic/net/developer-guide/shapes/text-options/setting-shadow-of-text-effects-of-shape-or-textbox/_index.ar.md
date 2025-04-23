---
title: ضبط الظلال لتأثيرات النص للشكل أو مربع النص
type: docs
weight: 250
url: /ar/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

يمكنك ضبط **الظلال** لـ **تأثيرات النص** لأي شكل أو مربع نص. يرجى استخدام الخاصية [**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody). يقدم ضبط نص الشكل ويعيد [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) كائنات. بعد الوصول إليها، يرجى ضبط **الظلال** عبر الخاصية [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype). هذه الخاصية من نوع [**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype) الذي يحتوي على عدة قيم. بعض هذه القيم هي

- إزاحة قطرية لأسفل اليمين
- إزاحة لأسفل
- إزاحة قطرية لأعلى اليمين
- داخل اليسار
- داخل الوسط
- زاوية رؤية قطرية العلوي الأيسر
- زاوية رؤية قطرية السفلي الأيمن

{{% /alert %}}

المقتطف التالي يوضح استخدام الخاصية [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) لضبط ظلال تأثيرات النص للشكل أو مربع النص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

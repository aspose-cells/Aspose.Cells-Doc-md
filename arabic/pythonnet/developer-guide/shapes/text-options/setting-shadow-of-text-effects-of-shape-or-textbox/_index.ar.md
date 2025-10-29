---
title: ضبط الظلال لتأثيرات النص للشكل أو مربع النص
type: docs
weight: 250
url: /ar/python-net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

يمكنك ضبط **الظلال** لـ **تأثيرات النص** لأي شكل أو مربع نص. يرجى استخدام الخاصية [**Shape.text_body**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_body). يقدم ضبط نص الشكل ويعيد [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) كائنات. بعد الوصول إليها، يرجى ضبط **الظلال** عبر الخاصية [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type). هذه الخاصية من نوع [**PresetShadowType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/presetshadowtype/) الذي يحتوي على عدة قيم. بعض هذه القيم هي

- OFFSET_DIAGONAL_BOTTOM_RIGHT
- OFFSET_BOTTOM
- OFFSET_DIAGONAL_TOP_RIGHT
- INSIDE_LEFT
- INSIDE_CENTER
- المنظور القطري العلوي الأيسر
- المنظور القطري العلوي الأيمن

{{% /alert %}}

المقتطف التالي يوضح استخدام الخاصية [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type) لضبط ظلال تأثيرات النص للشكل أو مربع النص.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SettingTextEffectsShadowOfShapeOrTextbox-1.py" >}}
{{< app/cells/assistant language="python-net" >}}

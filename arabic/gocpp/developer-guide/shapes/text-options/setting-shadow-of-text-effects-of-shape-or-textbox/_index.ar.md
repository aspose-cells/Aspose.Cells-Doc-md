---
title: تعيين ظل تأثيرات النص للشكل أو مربع النص باستخدام Golang عبر C++
linktitle: تعيين ظل تأثيرات النص
type: docs
weight: 250
url: /ar/go-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: تعلم كيفية ضبط ظل تأثيرات النص للأشكال أو مربعات النص باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 يمكنك تعيين **ظل** **تأثيرات النص** لأي شكل أو مربع نص. يرجى استخدام خاصية [**Shape.GetTextBody()**](https://reference.aspose.com/cells/go-cpp/shape/gettextbody/). فهي تعرض إعداد نص الشكل وتعيد كائنات [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/). بعد الوصول إليها، يرجى تعيين **الظل** عبر خاصية [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/). هذه الخاصية من نوع [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) الذي يحتوي على عدة قيم، منها:

- إزاحة قطرية لأسفل اليمين
- إزاحة لأسفل
- إزاحة قطرية لأعلى اليمين
- داخل اليسار
- داخل الوسط
- زاوية رؤية قطرية العلوي الأيسر
- زاوية رؤية قطرية السفلي الأيمن

{{% /alert %}}

يُظهر مقتطف الكود التالي استخدام خاصية [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/go-cpp/shadoweffect/getpresettype/) لضبط ظل تأثيرات النص في الشكل أو مربع النص.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingShadowOfTextEffectsOfShapeOrTextbox.go" >}}

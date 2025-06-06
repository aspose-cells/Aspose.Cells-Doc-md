---
title: كيفية إنشاء مخططات الأسهم باستخدام C++
linktitle: كيفية إنشاء رسومات الأسهم
description: مخططات الأسهم هي نوع معين من الرسوم البيانية يُستخدم لتعقب التغيرات في سعر الأصول المتداولة.
keywords: إنشاء رسومات الأسهم، Aspose.Cells، تصور البيانات السوقية، تحليل الأسواق، دليل خطوة بخطوة.
type: docs
weight: 71
url: /ar/cpp/how-to-create-stock-charts/
---

{{% alert color="primary" %}}

سيخبرك هذ الفقرة كيفية إنشاء رسم بياني للأسهم، والذي يتضمن أربعة أنواع:
- **HLC** - ارتفاع - قاع - إغلاق.
- **OHLC** - فتح - ارتفاع - قاع - إغلاق.
- **VHLC** - حجم - ارتفاع - قاع - إغلاق.
- **VOHLC** - حجم - فتح - ارتفاع - قاع - إغلاق.

{{% /alert %}}

## **ما هو مخطط الأسهم؟**

مخططات الأسهم هي نوع معين من الرسوم البيانية يُستخدم لتعقب التغيرات في سعر الأصول المتداولة، مثل السلع والأسهم والعملات الرقمية. تتيح لك رؤية القيم العليا والدنيا مع مرور الوقت، بالإضافة إلى القيم الافتتاحية والإغلاقية في رسم بياني واحد. تقدم Aspose.Cells أربعة مخططات أسهم، ولكي تستخدمها، يجب أن يكون لديك مجموعات البيانات الصحيحة وتحديد الأعمدة بالترتيب الصحيح.

توفر مجموعة البيانات التالية معلومات التداول اليومية لسهم. سنستخدم هذه البيانات لإنشاء أربعة أنواع من مخططات الأسهم: مخطط السهم العالي-المنخفض-الإغلاق (HLC)، مخطط الافتتاح-الأعلى-الأدنى-الإغلاق (OHLC)، مخطط الحجم العالي-المنخفض-الإغلاق (VHLC)، ومخطط الحجم الافتتاحي-الأعلى-الأدنى-الإغلاق (VOHLC).

![todo:image_alt_text](stock.chart.data.png)

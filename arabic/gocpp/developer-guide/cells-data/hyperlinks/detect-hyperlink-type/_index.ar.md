---
title: اكتشاف نوع الرابط التشعبي باستخدام Golang عبر C++
linktitle: اكتشاف نوع الرابط الفائق
type: docs
weight: 160
url: /ar/go-cpp/detect-hyperlink-type/
description: تعلم كيفية اكتشاف نوع الرابط التشعبي من خلال API Aspose.Cells for C++.
keywords: اكتشاف نوع الروابط التشعبية, كشف نوع الروابط التشعبية, الحصول على نوع الروابط التشعبية
---

## **كشف نوع الروابط التشعبية**

يمكن أن يحتوي ملف إكسل على أنواع مختلفة من الرابط الشعبي مثل الرابط الخارجي، مرجع الخلية، مسار الملف، الخ. Aspose.Cells تدعم ميزة كشف نوع الرابط. تتمثل أنواع الروابط التشعبية في تقديم فئة  [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/) زمرة التعداد. تحتوي فئة التعداد  [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/) على الأعضاء التالية.

- الخارجي: رابط خارجي
- مسار الشكل: مسار ملف\مجلد محلي بالكامل.
- البريد الإلكتروني: بريد إلكتروني
- مرجع الخلية: ربط الخلية أو النطاق المسمى.

للتحقق من نوع الرابط التشعبي، توفر فئة  [**Hyperlink**](https://reference.aspose.com/cells/go-cpp/hyperlink/) خاصية  [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/) بنوع العود. الشيفة النصية التالية توضح استخدام خاصية  [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/) عن طريق استخدام هذا الملف  [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) مثلاً.

### كود المصدر

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType.go" >}}
الناتج التالي الذي تم إنشاؤه بواسطة مقتطف الكود أعلاه.

### إخراج الكونسول
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType-1.go" >}}

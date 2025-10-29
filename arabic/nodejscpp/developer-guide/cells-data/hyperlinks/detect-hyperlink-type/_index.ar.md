---
title: اكتشاف نوع الرابط الفائق
type: docs
weight: 160
url: /ar/nodejs-cpp/detect-hyperlink-type/
description: تعلم كيفية الكشف عن نوع الرابط التشعبي عبر واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: الكشف عن نوع الرابط التشعبي عبر Node.js باستخدام C++، تحديد نوع الرابط التشعبي عبر Node.js باستخدام C++، الحصول على نوع الرابط التشعبي عبر Node.js باستخدام C++
---

## **كشف نوع الروابط التشعبية**

يمكن أن تحتوي ملفات إكسل على أنواع مختلفة من الروابط التشعبية مثل الخارجية، مرجع الخلية، مسار الملف، وغيرها. يدعم Aspose.Cells for Node.js via C++ ميزة الكشف عن نوع الرابط التشعبي. يتم تمثيل أنواع الروابط التشعبية بواسطة تعداد [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype). يشتمل تعداد [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) على الأعضاء التالية.

- خارجي: رابط خارجي
- مسار الملف: المسار الكامل والنسبي إلى الملفات/المجلدات.
- بريد إلكتروني: Email
- مرجع الخلية: رابط إلى خلية أو نطاق مسمى.

للتحقق من نوع الرابط التشعبي، توفر فئة [**Hyperlink**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink) طريقة [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) مع نوع العودة [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype). يوضح مقتطف الشفرة التالي استخدام طريقة [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) باستخدام ملف Excel المصدر [94896195.xlsx].

### كود المصدر

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-DetectHyperlinkType.js" >}}


الناتج التالي الذي تم إنشاؤه بواسطة مقتطف الكود أعلاه.

### إخراج الكونسول
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
{{< app/cells/assistant language="nodejs-cpp" >}}

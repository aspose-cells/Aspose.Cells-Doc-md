---
title: اكتشاف نوع الرابط الفائق
type: docs
weight: 160
url: /ar/python-net/detect-hyperlink-type/
description: تعلم كيفية كشف نوع الرابط من خلال واجهة برمجة التطبيقات Aspose.Cells for Python via .NET.
keywords: مكتبة Python Excel، كشف نوع الرابط، كشف نوع الرابط باستخدام Python، الحصول على نوع الرابط.
---

## **اكتشاف نوع الرابط الفائق**

يمكن أن يحتوي ملف Excel على أنواع مختلفة من الروابط مثل الروابط الخارجية، الإشارة إلى الخلية، المسار الخاص بالملف، إلخ. تدعم Aspose.Cells for Python via .NET ميزة كشف نوع الرابط. يتمثل أنواع الروابط بواسطة تعداد [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype). ويحتوي تعداد [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype) على الأعضاء التالية.

- الخارجي: الرابط الخارجي
- المسار_إلى_الملف: المسار المحلي والكامل للملفات\المجلدات.
- البريد_الإلكتروني: البريد الإلكتروني
- CELL_REFERENCE: الارتباط بخلية أو نطاق مسمى.

للتحقق من نوع الرابط التشعبي، توفر فئة  [**Hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink) خاصية  [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/) بنوع العود. الشيفة النصية التالية توضح استخدام خاصية  [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/) عن طريق استخدام هذا الملف  [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype) مثلاً.

### كود المصدر

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DetectLinkTypes-1.py" >}}

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
{{< app/cells/assistant language="python-net" >}}

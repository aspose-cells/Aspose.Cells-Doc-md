---
title: اكتشاف نوع الرابط الفائق
type: docs
weight: 160
url: /ar/net/detect-hyperlink-type/
description: تعلم كيفية كشف نوع الروابط التشعبية من خلال واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: اكتشاف نوع الروابط التشعبية, كشف نوع الروابط التشعبية, الحصول على نوع الروابط التشعبية
---

## **اكتشاف نوع الرابط الفائق**

يمكن أن يحتوي ملف إكسل على أنواع مختلفة من الرابط الشعبي مثل الرابط الخارجي، مرجع الخلية، مسار الملف، الخ. Aspose.Cells تدعم ميزة كشف نوع الرابط. تتمثل أنواع الروابط التشعبية في تقديم فئة  [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype) زمرة التعداد. تحتوي فئة التعداد  [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype) على الأعضاء التالية.

- الخارجي: رابط خارجي
- مسار الشكل: مسار ملف\مجلد محلي بالكامل.
- البريد الإلكتروني: بريد إلكتروني
- مرجع الخلية: ربط الخلية أو النطاق المسمى.

للتحقق من نوع الرابط التشعبي، توفر فئة  [**Hyperlink**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) خاصية  [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) بنوع العود. الشيفة النصية التالية توضح استخدام خاصية  [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) عن طريق استخدام هذا الملف  [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype) مثلاً.

### كود المصدر

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

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

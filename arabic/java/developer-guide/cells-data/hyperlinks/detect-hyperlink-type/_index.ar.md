---
title: اكتشاف نوع الرابط الفائق
type: docs
weight: 180
url: /ar/java/detect-hyperlink-type/
---

## **اكتشاف نوع الرابط الفائق**

ملف Excel يمكن أن يحتوي على أنواع مختلفة من الروابط الفائقة مثل الروابط الخارجية، مراجع الخلية، مسارات الملفات، وما إلى ذلك. يدعم Aspose.Cells ميزة اكتشاف نوع الرابط الفائق. يتمثل أنواع الروابط الفائقة في تمثيلات الإحصاءات [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). وتحتوي تمثيلات الإحصاءات [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType) على الأعضاء التالية.

- [**EXTERNAL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): رابط خارجي
- [**FILE_PATH**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH): الطريق المحلية والمسار الكامل إلى الملفات\المجلدات.
- [**EMAIL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): بريد إلكتروني
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): الرابط إلى خلية أو نطاق مسمى.

للتحقق من نوع الارتباط التشعبي، توفر فئة [**Hyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) خاصية [**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) بنوع عودة [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). يظهر الكود البرمجي التالي استخدام الخاصية [**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) باستخدام هذا [ملف إكسل المصدر](LinkTypes.xlsx).

## كود المصدر

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

الناتج التالي الذي تم إنشاؤه بواسطة مقتطف الكود أعلاه.

## مخرج الكونسول
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```

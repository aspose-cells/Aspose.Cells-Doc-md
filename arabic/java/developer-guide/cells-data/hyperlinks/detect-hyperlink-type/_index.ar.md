---
title: كشف نوع الارتباط التشعبي
type: docs
weight: 180
url: /ar/java/detect-hyperlink-type/
---
## **كشف نوع الارتباط التشعبي**

يمكن أن يحتوي ملف Excel على أنواع مختلفة من الارتباطات التشعبية مثل الارتباطات التشعبية الخارجية ، ومرجع الخلية ، ومسار الملف ، وما إلى ذلك. يدعم Aspose.Cells الميزة لاكتشاف نوع الارتباط التشعبي. يتم تمثيل أنواع الارتباطات التشعبية بواسطة ملف[**نوع الهدف**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)تعداد. ال[**نوع الهدف**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)التعداد له الأعضاء التالية أسماؤهم.

- [**خارجي**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): رابط خارجي
- [**مسار الملف**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH): المسار المحلي والكامل للملفات \ المجلدات.
- [**البريد الإلكتروني**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): بريد إلكتروني
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): ارتباط بالخلية أو النطاق المسمى.

للتحقق من نوع الارتباط التشعبي ، يجب أن يكون ملف[**ارتباط تشعبي**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) فئة توفر أ[**نوع الرابط**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) مع نوع إرجاع[**نوع الهدف**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). يوضح مقتطف الشفرة التالي استخدام ملف[**نوع الرابط**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)الملكية باستخدام هذا[ملف اكسل المصدر](LinkTypes.xlsx).

## مصدر الرمز

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

التالي هو الناتج الناتج عن مقتطف الشفرة الوارد أعلاه.

## إخراج وحدة التحكم
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```

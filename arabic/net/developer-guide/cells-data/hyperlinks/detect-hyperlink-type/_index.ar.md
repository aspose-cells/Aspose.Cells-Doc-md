---
title: كشف نوع الارتباط التشعبي
type: docs
weight: 160
url: /ar/net/detect-hyperlink-type/
description: تعرف على كيفية اكتشاف نوع الارتباط التشعبي من خلال Aspose.Cells for .NET API.
keywords: Detect hyperlink type, Detect the type of hyperlink, Get the type of hyperlink
---
##  **كشف نوع الارتباط التشعبي**

 يمكن أن يحتوي ملف Excel على أنواع مختلفة من الارتباطات التشعبية مثل الارتباطات الخارجية ومرجع الخلية ومسار الملف وما إلى ذلك. ويدعم Aspose.Cells ميزة اكتشاف نوع الارتباط التشعبي. يتم تمثيل أنواع الارتباطات التشعبية بواسطة[**نوع الوضع المستهدف**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)تعداد. ال[**نوع الوضع المستهدف**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)التعداد لديه الأعضاء التالية أسماؤهم.

- خارجي: رابط خارجي
- FilePath: المسار المحلي والكامل إلى الملفات\المجلدات.
- البريد الإلكتروني: البريد الإلكتروني
- مرجع الخلية: ارتباط بالخلية أو النطاق المسمى.

 للتحقق من نوع الارتباط التشعبي،[**الارتباط التشعبي**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) يوفر الفصل أ[**نوع الرابط**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) خاصية مع نوع الإرجاع[**نوع الوضع المستهدف**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). يوضح مقتطف التعليمات البرمجية التالي استخدام[**نوع الرابط**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)الملكية باستخدام هذا[ملف اكسيل المصدر](94896195.xlsx).

###  مصدر الرمز

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

ما يلي هو الإخراج الناتج عن مقتطف الشفرة المذكور أعلاه.

###  إخراج وحدة التحكم
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```

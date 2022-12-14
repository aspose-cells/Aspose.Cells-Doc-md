---
title: كشف نوع الارتباط التشعبي
type: docs
weight: 160
url: /ar/net/detect-hyperlink-type/
---
## **كشف نوع الارتباط التشعبي**

 يمكن أن يحتوي ملف Excel على أنواع مختلفة من الارتباطات التشعبية مثل الارتباطات التشعبية الخارجية ، ومرجع الخلية ، ومسار الملف ، وما إلى ذلك. يدعم Aspose.Cells الميزة لاكتشاف نوع الارتباط التشعبي. يتم تمثيل أنواع الارتباطات التشعبية بواسطة ملف[**نوع الهدف**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)تعداد. ال[**نوع الهدف**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)التعداد له الأعضاء التالية أسماؤهم.

- خارجي: رابط خارجي
- مسار الملف: المسار المحلي والكامل للملفات / المجلدات.
- البريد الإلكتروني: البريد الإلكتروني
- CellReference: ارتباط بالخلية أو النطاق المسمى.

 للتحقق من نوع الارتباط التشعبي ، يجب أن يكون ملف[**ارتباط تشعبي**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) فئة توفر أ[**نوع الرابط**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) مع نوع إرجاع[**نوع الهدف**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). يوضح مقتطف الشفرة التالي استخدام ملف[**نوع الرابط**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)الملكية باستخدام هذا[ملف اكسل المصدر](94896195.xlsx).

### مصدر الرمز

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

التالي هو الناتج الناتج عن مقتطف الشفرة الوارد أعلاه.

### إخراج وحدة التحكم
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```

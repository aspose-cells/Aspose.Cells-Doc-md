---
title: قم بتغيير الخط على أحرف Unicode المحددة فقط أثناء الحفظ في PDF
type: docs
weight: 260
url: /ar/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}} 

 لا يمكن عرض بعض أحرف Unicode بواسطة الخط المحدد من قبل المستخدم. أحد هذه الأحرف Unicode هو**واصلة غير فاصلة** (U + 2011) ورقم Unicode الخاص به هو 8209. لا يمكن عرض هذا الحرف مع**تايمز نيو رومان** ، ولكن يمكن عرضها مع خطوط أخرى مثل**Arial Unicode MS**.

عند ظهور مثل هذا الحرف داخل بعض الكلمات أو الجمل الموجودة بخط معين مثل Times New Roman ، فإن Aspose.Cells يغير خط الكلمة أو الجملة بأكملها إلى الخط الذي يمكن أن يعرض هذا الحرف مثل Arial Unicode إلى MS.

ومع ذلك ، يعد هذا سلوكًا غير مرغوب فيه لبعض المستخدمين ويريدون فقط تغيير خط الحرف المحدد بدلاً من تغيير خط الكلمة أو الجملة بأكملها.

للتعامل مع هذه المشكلة ، يوفر Aspose.Cells خاصية PdfSaveOptions.IsFontSubstitutionCharGranularity التي يجب تعيينها على صواب بحيث لا يتم تغيير سوى خط الحرف المحدد غير القابل للعرض إلى الخط القابل للعرض وبقية الكلمة أو الجملة في الخط الأصلي.

{{% /alert %}} 
## **مثال**
تقارن لقطة الشاشة التالية بين ملفي PDF الناتج اللذين تم إنشاؤهما بواسطة نموذج التعليمات البرمجية أدناه.

يتم إنشاء أحدهما بدون تعيين خاصية PdfSaveOptions.IsFontSubstitutionCharGranularity والآخر تم إنشاؤه بعد تعيين خاصية PdfSaveOptions.IsFontSubstitutionCharGranularity إلى true.

كما ترى في ملف Pdf الأول ، تم تغيير خط الجملة بالكامل من Times New Roman إلى Arial Unicode MS بسبب الواصلة غير الفاصلة. بينما في ملف PDF الثاني ، تم تغيير خط Non-Breaking Hyphen فقط.

|**أول ملف PDF**|
|:- |
|![ما يجب القيام به: image_بديل_نص](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**ملف PDF الثاني**|
|:- |
|![ما يجب القيام به: image_بديل_نص](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **عينة من الرموز**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}




---
title: تغيير الخط فقط في الأحرف اليونيكود المحددة أثناء الحفظ إلى PDF
type: docs
weight: 260
url: /ar/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}} 

بعض الحروف اليونيكود لا يمكن عرضها بواسطة الخط المحدد من قبل المستخدم. إحدى هذه الرموز اليونيكودية هي **بنطلون متقطع** (U+2011) ورقمها اليونيكود هو 8209. لا يمكن عرض هذه الرمز بواسطة **تايمز نيو رومان** ، ولكن يمكن عرضها بخطوط أخرى مثل **Arial Unicode MS**.

عندما يحدث مثل هذا الحرف داخل بعض الكلمات أو الجمل التي تكون في خط معين مثل Times New Roman ، يقوم Aspose.Cells بتغيير الخط الخاص بالكلمة أو الجملة بأكملها إلى الخط الذي يمكن عرض هذا الحرف مثل Arial Unicode to MS.

ومع ذلك ، هذا السلوك غير مرغوب فيه بالنسبة لبعض المستخدمين ويريدون أن يتم تغيير خط الحرف المحدد فقط بدلاً من تغيير خط الكلمة أو الجملة بأكملها.

للتعامل مع هذه المشكلة ، يوفر Aspose.Cells خاصية PdfSaveOptions.IsFontSubstitutionCharGranularity يجب تعيينها كـ true بحيث يتم تغيير الخط الخاص بالحرف المحدد الذي لا يمكن عرضه إلى الخط الذي يمكن عرضه ويجب أن تظل بقية الكلمة أو الجملة في الخط الأصلي.

{{% /alert %}} 
## **مثال**
الصورة المرفقة تقارن بين ملفي PDF الناتجين من الشفرة النموذجية التالية.

أحدهما تم إنشاؤه دون ضبط خاصية PdfSaveOptions.IsFontSubstitutionCharGranularity والآخر تم إنشاؤه بعد ضبط الخاصية PdfSaveOptions.IsFontSubstitutionCharGranularity على قيمة صحيحة.

كما يمكن رؤيته في الملف الأول بصيغة PDF، تغيرت الخطوط لكامل الجملة من Times New Roman إلى Arial Unicode MS بسبب الواصلة غير المنقطة. في حين أن في الملف الثاني بصيغة PDF، تغيرت خطوط الواصلة غير المنقطة فقط.

|**ملف PDF الأول**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**ملف PDF الثاني**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **الكود المثالي**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}




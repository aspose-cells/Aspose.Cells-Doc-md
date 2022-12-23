---
title: قم بتغيير الخط على أحرف Unicode المحددة فقط أثناء الحفظ في PDF
type: docs
weight: 150
url: /ar/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}}

 لا يمكن عرض بعض أحرف Unicode بواسطة الخط المحدد من قبل المستخدم. أحد هذه الأحرف Unicode هو**واصلة غير فاصلة** (U + 2011) ورقم Unicode الخاص به هو 8209. لا يمكن عرض هذا الحرف مع**تايمز نيو رومان** ، ولكن يمكن عرضها مع خطوط أخرى مثل**Arial Unicode MS**.

عندما يحدث مثل هذا الحرف داخل بعض الكلمات أو الجمل الموجودة في خط معين مثل Times New Roman ، فإن Aspose.Cells يغير خط الكلمة أو الجملة بأكملها إلى الخط الذي يمكن أن يعرض هذا الحرف مثل Arial Unicode إلى MS.

ومع ذلك ، يعد هذا سلوكًا غير مرغوب فيه لبعض المستخدمين ويريدون فقط تغيير خط الحرف المحدد بدلاً من تغيير خط الكلمة أو الجملة بأكملها.

 للتعامل مع هذه المشكلة ، يوفر Aspose.Cells[**PdfSaveOptions.setFontSubstitutionCharGranularity ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) الخاصية التي يجب تعيينها**حقيقي** بحيث يتم تغيير خط الحرف المحدد غير القابل للعرض فقط ويظل خط بقية الكلمة أو الجملة كما هو.

{{% /alert %}}

## **مثال**

 تقارن لقطة الشاشة التالية بين ملفي PDF الناتج اللذين تم إنشاؤهما بواسطة نموذج التعليمات البرمجية أدناه. تم إنشاء واحد بدون تحديد[**PdfSaveOptions.setFontSubstitutionCharGranularity ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) الخاصية والآخر تم إنشاؤه بعد تعيين[**PdfSaveOptions.setFontSubstitutionCharGranularity ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) ملكية ل**حقيقي**. كما ترى في أول PDF ، تم تغيير خط الجملة بأكملها من Times New Roman إلى Arial Unicode MS بسبب واصلة غير فاصلة. بينما في PDF الثاني ، تم تغيير خط Non-Breaking Hyphen فقط.

![ما يجب القيام به: image_بديل_نص](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}

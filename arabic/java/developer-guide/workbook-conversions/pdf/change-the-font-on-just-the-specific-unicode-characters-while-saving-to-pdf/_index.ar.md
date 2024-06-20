---
title: تغيير الخط فقط في الأحرف اليونيكود المحددة أثناء الحفظ إلى PDF
type: docs
weight: 150
url: /ar/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}}

بعض الأحرف اليونيكود غير قابلة للعرض بواسطة الخط المحدد من قبل المستخدم. أحد الأحرف اليونيكود هو **الشرطة الغير قابلة للانفصال** (U+2011) ورقمه اليونيكود هو 8209. هذا الحرف لا يمكن عرضه باستخدام الخط **تايمز نيو رومان**, ولكن يمكن عرضه بالخطوط الأخرى مثل **أريال يونيكود ام اس**.

عند حدوث هذا الحرف داخل كلمة أو جملة معينة في خطوط معينة مثل تايمز نيو رومان, فإن Aspose.Cells يغير خط الكلمة أو الجملة بأكملها إلى الخط الذي يمكن عرض هذا الحرف مثل أريال يونيكود ام اس.

ومع ذلك، هذا سلوك غير مرغوب فيه بالنسبة لبعض المستخدمين ويرغبون في تغيير خط الحرف المحدد فقط بدلاً من تغيير خط الكلمة أو الجملة بأكملها.

للتعامل مع هذه المشكلة، يوفر Aspose.Cells خاصية [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) يجب ضبطها على **صحيح** حتى يتم تغيير خط الحرف المحدد الذي لا يمكن عرضه فقط ويبقى خط بقية الكلمة أو الجملة على حاله.

{{% /alert %}}

## **مثال**

يقارن اللقطة الملتقطة التالية بين اثنين من ملفات PDF الناتجة المولَّدة بواسطة الرمز البرمجي عينة أدناه. تم إنشاء أحدهما دون ضبط [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) والآخر تم إنشاؤه بعد ضبط خاصية [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) على **صحيح**. كما يمكنك رؤية في الملف الأول من عينات PDF، تم تغيير خط الجملة بأكملها من تايمز نيو رومان إلى أريال يونيكود ام اس بسبب الشرطة الغير قابلة للانفصال. في حين في الملف الثاني، تم تغيير خط الشرطة الغير قابلة للانفصال فقط.

![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}

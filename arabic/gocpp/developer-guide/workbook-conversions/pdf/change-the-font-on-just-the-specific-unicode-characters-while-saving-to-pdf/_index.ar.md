---
title: تغيير الخط على أحرف يونيكود محددة فقط عند الحفظ إلى PDF باستخدام Golang عبر C++
linktitle: تغيير خط حروف اليونيكود
type: docs
weight: 260
url: /ar/go-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: تعلم كيفية تغيير خط أحرف يونيكود معينة عند الحفظ إلى PDF باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

بعض الأحرف اليونيكود غير قابلة للعرض بواسطة الخط المحدد من قبل المستخدم. أحد الأحرف اليونيكود هو **الشرطة الغير قابلة للانفصال** (U+2011) ورقمه اليونيكود هو 8209. هذا الحرف لا يمكن عرضه باستخدام الخط **تايمز نيو رومان**, ولكن يمكن عرضه بالخطوط الأخرى مثل **أريال يونيكود ام اس**.

 عندما يظهر مثل هذا الحرف داخل كلمة أو جملة معينة والتي تكون مكتوبة بخط معين مثل Times New Roman، فإن Aspose.Cells يغير خط الكلمة أو الجملة بأكملها إلى خط يمكنه عرض هذا الحرف مثل Arial Unicode MS.

 ومع ذلك، هذا سلوك غير مرغوب لبعض المستخدمين، ويريدون فقط تغيير خط الحرف المحدد بدلاً من تغيير خط الكلمة أو الجملة بأكملها.

 للتعامل مع هذه المشكلة، يوفر Aspose.Cells خاصية `PdfSaveOptions.IsFontSubstitutionCharGranularity`، والتي يجب ضبطها على `true` بحيث يتغير خط الحرف المحدد الذي لا يمكن عرضه إلى خط قابل للعرض، ويظل باقي الكلمة أو الجملة في الخط الأصلي.

{{% /alert %}}

## **مثال**

الصورة المرفقة تقارن بين ملفي PDF الناتجين من الشفرة النموذجية التالية.

تم توليد واحد بدون ضبط خاصية `PdfSaveOptions.IsFontSubstitutionCharGranularity`، والآخر بعد ضبطها على `true`.

 كما هو موضح في ملف PDF الأول، تغير خط الجملة بأكملها من Times New Roman إلى Arial Unicode MS بسبب الشرطة غير الفاصلة. بينما في الملف الثاني، تغير فقط خط الشرطة غير الفاصلة.

|**ملف PDF الأول**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**ملف PDF الثاني**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheFontOnJustTheSpecificUnicodeCharactersWhileSavingToPdf.go" >}}

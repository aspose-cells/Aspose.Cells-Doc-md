---
title: سمات العناوين والنص الأساسي للسمات
linktitle: سمات العناوين والنص الأساسي للسمات
description: Aspose.Cells هي مكتبة Node.js للعمل مع ملفات جداول البيانات. تدعم تعيين خطوط النموذج للرأس والجسم في مستندات Excel، مما يتيح للمستخدمين تخصيص مظهر وأسلوب المستند. ستقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells للعمل مع خطوط النموذج للرأس والجسم في مستندات Excel.
keywords: Aspose.Cells، مستند Excel، عنوان، جسم، خط النموذج، المظهر، النمط، Node.js عبر C++
type: docs
weight: 120
url: /ar/nodejs-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

سيتم تغيير الخط الافتراضي تلقائيًا عند تغيير إعداد المنطقة.

إذا تم تغيير الخط الافتراضي، ستتم أيضًا تغيير ارتفاع الصف وعرض العمود، وقد يؤدي ذلك إلى تخريب تخطيط الصفحة.

ما الذي تسبب تغيير الخط الافتراضي؟

إذا تم ضبط خط السمة في Excel، فإن Excel سيقوم تلقائيًا بالتبديل بين خطوط مختلفة استنادًا إلى بيئة اللغة الحالية.

{{% /alert %}}

## **سمات العناوين والنص الأساسي للسمات في Excel**

في Excel، حدد علامة التبويب الصفحة الرئيسية، انقر على مربع اختيار خطوط النص، سترى "خطوط النموذج" مع خطين: Calibri Light (عناوين) و Calibri (الجسم) على الأعلى مع إعداد المنطقة باللغة الإنجليزية.

**![سمات الخطوط](Theme-Fonts.png)**

إذا تم اختيار خط النموذج، فسيقع اسم الخط بشكل مختلف في مناطق مختلفة. إذا كنت لا تريد أن يتغير الخط تلقائيًا في المناطق المختلفة، لا تحدد خطي النموذج.

## **تغيير خطوط العناوين والجسد برمجياً**
باستخدام Aspose.Cells for Node.js via C++، يمكننا التحقق مما إذا كان الخط الافتراضي هو خط نموذج أو تعيين خط النموذج بواسطة [**Font.setSchemeType(FontSchemeType)**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSchemeType-fontschemetype-) طريقة.

يعرض رمز النموذج التالي كيفية التلاعب بخط النموذج.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-HeadingsAndBodyThemeFont.js" >}}



## **الحصول ديناميكيًا على خط السمة المحلي برمجياً**
في بعض الأحيان، يكون خوادمنا وأجهزة المستخدمين غير في نفس الإقليم. كيف يمكننا الحصول على نفس الخط الذي يرغب المستخدمون فيه لمعالجة الملف؟

يجب تعيين إعدادات المنطقة الخاصة بالنظام قبل تحميل الملف باستخدام [**LoadOptions.setRegion(CountryCode)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setRegion-countrycode-) طريقة.

يعرض الشيفرة النموذجية التالية كيفية الحصول على خط سمة محلي.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetLocalThemeFont.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}

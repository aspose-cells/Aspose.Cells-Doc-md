---
title: تعطيل CSS عند الحفظ إلى HTML باستخدام Golang عبر C++
linktitle: تعطيل CSS عند الحفظ إلى HTML
type: docs
weight: 320
url: /ar/go-cpp/disable-css-while-saving-to-html/
description: تعلم كيفية تعطيل CSS أثناء حفظ ملفات Excel إلى HTML باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel الخاص بك إلى صفحة HTML واحدة، عادةً ستكون عناصر CSS مضمنة داخل ملف HTML وتقع في قسم HEAD. إذا أرفقت هذا الملف كمحتوى/جسم لبريد إلكتروني، ستتم إزالة عناصر CSS بواسطة معظم عملاء البريد الإلكتروني، مما يؤدي إلى عرض غير صحيح. الإصدار 24.12 من Aspose.Cells يقدم خيارًا يسمح لك بتعطيل CSS بشكل اختياري، مما يتيح تطبيق الأنماط مباشرة داخل عناصر HTML نفسها. إذا كنت ترغب في تعيين HTML كمحتوى/جسم البريد الإلكتروني، يرجى استخدام الخاصية [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/) وتعيينها إلى **true**.

## **تعطيل CSS عند الحفظ إلى HTML**

يزودك المثال التالي بكود يوضح استخدام الخاصية [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/).

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableCssWhileSavingToHtml.go" >}}

---
title: تفعيل خصائص CSS المخصصة عند الحفظ إلى HTML باستخدام Golang عبر C++
linktitle: تمكين خصائص CSS المخصصة عند الحفظ إلى HTML
type: docs
weight: 320
url: /ar/go-cpp/enable-css-custom-properties-while-saving-to-html/
description: تعلم كيف تمكّن خصائص CSS المخصصة عند حفظ ملفات Excel إلى HTML باستخدام Aspose.Cells for C++. تحسين الأداء من خلال تقليل بيانات الصورة الزائدة.
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel الخاص بك إلى HTML، وفي حالة وجود تكرارات متعددة لصورة base64 واحدة، مع الخاصية المخصصة، يحتاج البيانات لمرَّة واحدة فقط، مما يُحسّن أداء HTML الناتج. يرجى استخدام الخاصية [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getenablecsscustomproperties/) وتعيينها إلى **true** عند الحفظ إلى HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **تمكين خصائص CSS المخصصة أثناء الحفظ إلى HTML**

يوضح المثال التالي استخدام الخاصية [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getenablecsscustomproperties/). تُظهر لقطة الشاشة تأثير هذه الخاصية عند عدم تعيينها إلى **true**. يرجى تنزيل ملف Excel التجريبي [الملف](50528260.xlsx) المستخدم في هذا الكود وملف HTML المخرج [الملف](50528261.zip) للاطلاع عليه كمصدر مرجعي.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnableCssCustomPropertiesWhileSavingToHtml.go" >}}

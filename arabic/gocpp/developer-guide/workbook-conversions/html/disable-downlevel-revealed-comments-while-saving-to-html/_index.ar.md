---
title: تعطيل التعليقات المكشوفة من الأسفل عند الحفظ إلى HTML باستخدام Golang عبر C++
linktitle: تعطيل التعليقات المكشوفة على مستوى أدنى
type: docs
weight: 20
url: /ar/go-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: القضاء على التعليقات المكشوفة من الأسفل عند حفظ ملفات إكسل إلى HTML باستخدام Aspose.Cells مع Golang عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel إلى HTML، يكشف Aspose.Cells عن تعليقات الشرط على مستوى أدنى. هذه التعليقات الشرطية تهم بشكل رئيسي إصدارات أقدم من Internet Explorer ولا تهم المتصفحات الحديثة. يمكنك قراءتها بالتفصيل على الرابط التالي.

- [تعليق شرطي - تعليق شرطي مكشوف على مستوى أقل](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

 يسمح لك Aspose.Cells بالتخلص من هذه التعليقات المكشوفة على مستوى أدنى عن طريق تعيين الخاصية [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/) إلى **true**.

## **تعطيل كشف التعليقات عند الاستخدام التسلسلي لأسفل عند الحفظ في HTML**

يوضح المثال التالي استخدام خاصية [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/). تُظهر لقطة الشاشة تأثير هذه الخاصية عند عدم تعيينها إلى true. يرجى تنزيل ملف Excel النموذجي [الملف التجريبي](50528257.xlsx) المستخدم في هذا الكود وملف HTML الناتج [المخرجات](50528258.zip) للاطلاع عليهما كمصدر مرجعي.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableDownlevelRevealedCommentsWhileSavingToHtml.go" >}}

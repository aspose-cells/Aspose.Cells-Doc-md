---
title: تعطيل التعليقات المكشوفة على مستوى أقل أثناء الحفظ إلى HTML
type: docs
weight: 20
url: /ar/python-net/disable-downlevel-revealed-comments-while-saving-to/
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف إكسل كصفحة HTML، يكشف Aspose.Cells for Python via .NET عن تعليقات الشرط الموسعة للأصناف المنخفضة. هذه التعليقات الشرطية تتعلق في الغالب بالإصدارات القديمة من Internet Explorer وليست ذات أهمية للمتصفحات الحديثة. يمكنك الاطلاع عليها بالتفصيل عبر الرابط التالي.

- [تعليق شرطي - تعليق شرطي مكشوف على مستوى أقل](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

يسمح Aspose.Cells for Python via .NET لك بإزالة هذه التعليقات المخفية المنخفضة عبر تعيين الخاصية [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments) إلى **true**.

## **تعطيل كشف التعليقات عند الاستخدام التسلسلي لأسفل عند الحفظ في HTML**

الكود البرمجي التالي يُظهر استخدام الخاصية [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments) . تُظهر اللقطة الشاشة تأثير هذه الخاصية عندما لا يتم تعيينها على true. الرجاء تحميل [ملف الإكسل العيني](50528257.xlsx) المستخدم في هذا الكود و[ملف HTML الناتج](50528258.zip) الذي تم إنشاؤه به للإشارة.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}

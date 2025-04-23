---
title: تعطيل التعليقات المكشوفة على مستوى أقل أثناء الحفظ إلى HTML
type: docs
weight: 20
url: /ar/net/disable-downlevel-revealed-comments-while-saving-to/
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel الخاص بك إلى HTML، يكشف Aspose.Cells التعليقات الشرطية على مستوى أقل. تكون هذه التعليقات الشرطية ذات صلة بالغالب لإصدارات Internet Explorer القديمة ولا علاقة لها بمتصفحات الويب الحديثة. يمكنك قراءة المزيد عنها بالتفصيل في الرابط التالي.

- [تعليق شرطي - تعليق شرطي مكشوف على مستوى أقل](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

يسمح Aspose.Cells لك بالتخلص من هذه التعليقات الشرطية المكشوفة على مستوى أقل عن طريق تعيين الخاصية [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) إلى **true**.

## **تعطيل كشف التعليقات عند الاستخدام التسلسلي لأسفل عند الحفظ في HTML**

الكود البرمجي التالي يُظهر استخدام الخاصية [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) . تُظهر اللقطة الشاشة تأثير هذه الخاصية عندما لا يتم تعيينها على true. الرجاء تحميل [ملف الإكسل العيني](50528257.xlsx) المستخدم في هذا الكود و[ملف HTML الناتج](50528258.zip) الذي تم إنشاؤه به للإشارة.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
{{< app/cells/assistant language="csharp" >}}

---
title: تعطيل الكشف عن التعليقات ذات المستوى الأدنى أثناء الحفظ في HTML
type: docs
weight: 20
url: /ar/python-java/disable-downlevel-revealed-comments-while-saving-to/
---
## **تعطيل الكشف عن التعليقات ذات المستوى الأدنى أثناء الحفظ في HTML**
عند تحويل ملف Excel إلى HTML ، يضيف Aspose.Cells التعليقات الشرطية ذات المستوى الأدنى في ملف HTML الناتج. ترتبط هذه التعليقات الشرطية في الغالب بالإصدارات القديمة من Internet Explorer وليست ذات صلة بالمتصفحات الحديثة. للحصول على معلومات إضافية حول التعليقات الشرطية ذات المستوى الأدنى ، يرجى زيارة الرابط التالي

[تعليق شرطي - تعليق شرطي ذو مستوى أدنى](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

لإزالة التعليقات الشرطية ذات المستوى الأدنى ، يوفر Aspose.Cells الامتداد[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)منشأه. وضع[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) الملكية ل**حقيقي**سيزيل التعليقات الشرطية ذات المستوى الأدنى في ملف HTML الناتج.

تُظهر الصورة التالية التعليقات الشرطية ذات المستوى الأدنى والتي ستتم إزالتها في ملف HTML الناتج

![ما يجب القيام به: image_بديل_نص](Disable-Downlevel-Revealed-Comments.png)
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}

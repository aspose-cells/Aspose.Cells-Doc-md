---
title: تعطيل التعليقات المكشوفة على مستوى أقل أثناء الحفظ إلى HTML
type: docs
weight: 20
url: /ar/python-java/disable-downlevel-revealed-comments-while-saving-to/
---

## **تعطيل كشف التعليقات عند الاستخدام التسلسلي لأسفل عند الحفظ في HTML**
عند تحويل ملف Excel إلى HTML، يضيف Aspose.Cells تعليقات شرطية مكشوفة الإصدار في ملف HTML الناتج. هذه التعليقات الشرطية غالبًا ما تكون ذات صلة بالإصدارات القديمة من Internet Explorer وغير ذات صلة في المتصفحات الحديثة. للحصول على معلومات إضافية حول تعليقات شرطية مكشوفة الإصدار، يرجى زيارة الرابط التالي

[تعليق شرطي - تعليق مشروط مكشوف](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

لإزالة تعليقات شرطية مكشوفة الإصدار، يوفر Aspose.Cells خاصية [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments). ضبط الخاصية [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) إلى **True** سيزيل تعليقات المستخدم مكشوفة الإصدار في ملف HTML الناتج.

الصورة التالية تظهر تعليقات المستخدم مكشوفة الإصدار التي سيتم إزالتها في ملف HTML الناتج

![todo:image_alt_text](Disable-Downlevel-Revealed-Comments.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}

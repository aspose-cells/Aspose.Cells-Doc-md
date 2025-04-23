---
title: تعطيل التعليقات المكشوفة على مستوى أقل أثناء الحفظ إلى HTML
type: docs
weight: 20
url: /ar/java/disable-downlevel-revealed-comments-while-saving-to-html/
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel الخاص بك إلى HTML، ثم Aspose.Cells تظهر Downlevel Conditional Comments. تكون هذه التعليقات الشرطية ذات الصعود المستوى غالبًا ما تكون ذات صلة بالإصدارات القديمة من Internet Explorer وغير متعلقة بمتصفحات الويب الحديثة. يمكنك قراءة المزيد عنها بالتفصيل في الرابط التالي.

- [تعليق شرطي - تعليق شرطي مكشوف على مستوى أقل](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

تسمح Aspose.Cells لك بالتخلص من هذه التعليقات ذات الصعود المستوى من خلال تعيين ال[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments) الخاصية إلى **true**.

## **تعطيل كشف التعليقات عند الاستخدام التسلسلي لأسفل عند الحفظ في HTML**

عينة الكود التالية توضح استخدام ال[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments) الخاصية. توضح اللقطة الشاشية تأثير هذه الخاصية عندما لا تكون مُعينة إلى **true**. الرجاء تحميل ملف الإكسل العينة المُستخدم في هذا الكود وملف الـ[HTML الناتج](50528266.zip) الخاص به من أجل المرجع.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
{{< app/cells/assistant language="java" >}}

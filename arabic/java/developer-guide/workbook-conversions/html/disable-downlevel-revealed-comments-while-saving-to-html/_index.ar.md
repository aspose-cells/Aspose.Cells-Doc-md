---
title: تعطيل الكشف عن التعليقات ذات المستوى الأدنى أثناء الحفظ في HTML
type: docs
weight: 20
url: /ar/java/disable-downlevel-revealed-comments-while-saving-to-html/
---
## **سيناريوهات الاستخدام الممكنة**

عندما تقوم بحفظ ملف Excel الخاص بك في HTML ، فإن Aspose.Cells يكشف عن التعليقات الشرطية ذات المستوى الأدنى. ترتبط هذه التعليقات الشرطية في الغالب بالإصدارات القديمة من Internet Explorer ولا صلة لها بمتصفحات الويب الحديثة. يمكنك أن تقرأ عنها بالتفصيل على الرابط التالي.

- [تعليق شرطي - تعليق شرطي ذو مستوى أدنى](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

يسمح لك Aspose.Cells بإزالة هذه التعليقات التي تم الكشف عنها ذات المستوى الأدنى بتعيين[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)ملكية ل**حقيقي**.

## **تعطيل الكشف عن التعليقات ذات المستوى الأدنى أثناء الحفظ في HTML**

يُظهر نموذج التعليمات البرمجية التالي استخدام[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)خاصية. تُظهر لقطة الشاشة تأثير هذه الخاصية عندما لا يتم تعيينها على**حقيقي**. يرجى تنزيل ملف[نموذج لملف Excel](50528267.xlsx)المستخدمة في هذا الرمز و[الإخراج HTML](50528266.zip)الملف الذي تم إنشاؤه بواسطته كمرجع.

![ما يجب القيام به: image_بديل_نص](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}

---
title: تعطيل الكشف عن التعليقات ذات المستوى الأدنى أثناء الحفظ في HTML
type: docs
weight: 20
url: /ar/net/disable-downlevel-revealed-comments-while-saving-to/
---
## **سيناريوهات الاستخدام الممكنة**

عندما تقوم بحفظ ملف Excel الخاص بك إلى HTML ، فإن Aspose.Cells يكشف عن التعليقات الشرطية ذات المستوى الأدنى. هذه التعليقات الشرطية ذات صلة في الغالب بالإصدارات الأقدم من Internet Explorer ولا صلة لها بمتصفحات الويب الحديثة. يمكنك أن تقرأ عنها بالتفصيل على الرابط التالي.

- [تعليق شرطي - تعليق شرطي ذو مستوى أدنى](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

يسمح لك Aspose.Cells بإزالة هذه التعليقات التي تم الكشف عنها ذات المستوى الأدنى بتعيين[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) الملكية ل**حقيقي**.

## **تعطيل الكشف عن التعليقات ذات المستوى الأدنى أثناء الحفظ في HTML**

يُظهر نموذج التعليمات البرمجية التالي استخدام[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) منشأه. تُظهر لقطة الشاشة تأثير هذه الخاصية عند عدم تعيينها على "صواب". يرجى تنزيل ملف[نموذج لملف Excel](50528257.xlsx) المستخدمة في هذا الرمز و[إخراج HTML](50528258.zip) ولدت به كمرجع.

![ما يجب القيام به: image_بديل_نص](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}

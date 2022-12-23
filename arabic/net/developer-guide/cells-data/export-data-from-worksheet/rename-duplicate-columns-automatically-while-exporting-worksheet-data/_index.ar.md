---
title: أعد تسمية الأعمدة المكررة تلقائيًا أثناء تصدير بيانات ورقة العمل
type: docs
weight: 250
url: /ar/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
---
## **سيناريوهات الاستخدام الممكنة**

يواجه المستخدم أحيانًا مشكلة تكرار الأعمدة أثناء تصدير البيانات من ورقة العمل إلى جدول البيانات. لا يمكن أن يحتوي DataTable على أعمدة مكررة ، لذا يجب إعادة تسمية الأعمدة المكررة قبل أن تتمكن من تصدير بيانات ورقة العمل إلى جدول البيانات. يمكن لـ Aspose.Cells إعادة تسمية الأعمدة المكررة آليًا وفقًا للإستراتيجية المحددة بواسطتك[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) خاصية. إذا حددت[**إعادة تسمية الإستراتيجية**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) سيتم إعادة تسمية الأعمدة مثل العمود 1 والعمود 2 والعمود 3 وما إلى ذلك ، وإذا حددت ذلك[**إعادة تسمية الإستراتيجية**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy)حرفًا ، سيتم إعادة تسمية الأعمدة مثل العمود أ ، والعمود ب ، والعمود ج ، وما إلى ذلك.

## **أعد تسمية الأعمدة المكررة تلقائيًا أثناء تصدير بيانات ورقة العمل**

 يضيف نموذج التعليمات البرمجية التالي بعض البيانات في الأعمدة الثلاثة الأولى من ورقة العمل ولكن جميع الأعمدة لها نفس الاسم ، أي*الناس* . ثم يقوم بتصدير البيانات من ورقة العمل إلى جدول البيانات عن طريق التحديد[**إعادة تسمية الإستراتيجية**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).رسائل الاستراتيجية. يقوم بعد ذلك بطباعة أسماء أعمدة جدول البيانات الذي تم إنشاؤه بواسطة Aspose.Cells. توضح لقطة الشاشة التالية جدول البيانات مع البيانات المصدرة في المتخيل. كما ترى ، تمت إعادة تسمية الأعمدة المكررة إلى PeopleA و PeopleB وما إلى ذلك.

![ما يجب القيام به: image_بديل_نص](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **إخراج وحدة التحكم**

هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه كمرجع.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}

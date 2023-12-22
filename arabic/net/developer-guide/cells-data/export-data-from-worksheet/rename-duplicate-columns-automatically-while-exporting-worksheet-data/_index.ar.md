---
title: إعادة تسمية الأعمدة المكررة تلقائيًا أثناء تصدير بيانات ورقة العمل
type: docs
weight: 250
url: /ar/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: تعرف على كيفية إعادة تسمية الأعمدة المكررة تلقائيًا أثناء تصدير بيانات ورقة العمل من خلال Aspose.Cells for .NET API.
keywords: Rename duplicate columns while exporting worksheet data, Rename duplicate columns automatically while exporting  data to DataTable
---
##  **سيناريوهات الاستخدام المحتملة**

 يواجه المستخدم أحيانًا مشكلة الأعمدة المكررة أثناء تصدير البيانات من ورقة العمل إلى جدول البيانات. لا يمكن أن يحتوي DataTable على أعمدة مكررة، لذا يجب إعادة تسمية الأعمدة المكررة قبل أن تتمكن من تصدير بيانات ورقة العمل إلى جدول البيانات. Aspose.Cells يمكنه إعادة تسمية الأعمدة المكررة تلقائيًا وفقًا للاستراتيجية التي حددتها[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) ملكية. إذا قمت بتحديد[**استراتيجية إعادة التسمية**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) رقم، ستتم إعادة تسمية الأعمدة مثل column1، column2، column3، الخ وإذا قمت بتحديد[**استراتيجية إعادة التسمية**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter، ثم ستتم إعادة تسمية الأعمدة مثل columnA، columnB، columnC، إلخ.

##  **إعادة تسمية الأعمدة المكررة تلقائيًا أثناء تصدير بيانات ورقة العمل**

يضيف نموذج التعليمات البرمجية التالي بعض البيانات في الأعمدة الثلاثة الأولى من ورقة العمل ولكن كافة الأعمدة لها نفس الاسم، أي *الأشخاص*. ثم يقوم بتصدير البيانات من ورقة العمل إلى جدول البيانات عن طريق التحديد[**استراتيجية إعادة التسمية**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).استراتيجية الرسالة. ثم يقوم بطباعة أسماء أعمدة جدول البيانات الذي تم إنشاؤه بواسطة Aspose.Cells. تعرض لقطة الشاشة التالية جدول البيانات مع البيانات المصدرة في المصور. كما ترون، تمت إعادة تسمية الأعمدة المكررة إلى PeopleA وPeopleB وما إلى ذلك.

![ما يجب القيام به:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

##  **إخراج وحدة التحكم**

فيما يلي إخراج وحدة التحكم لنموذج التعليمات البرمجية أعلاه كمرجع.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}

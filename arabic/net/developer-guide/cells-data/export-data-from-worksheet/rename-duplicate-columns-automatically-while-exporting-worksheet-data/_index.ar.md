---
title: إعادة تسمية الأعمدة المُكررة تلقائيًا أثناء تصدير بيانات ورقة العمل
type: docs
weight: 250
url: /ar/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: تعلم كيفية إعادة تسمية الأعمدة المُكررة تلقائيًا أثناء تصدير بيانات ورقة العمل من خلال واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: إعادة تسمية الأعمدة المكررة أثناء تصدير بيانات ورقة العمل، إعادة تسمية الأعمدة المكررة تلقائيًا أثناء تصدير البيانات إلى جدول البيانات
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان يواجه المستخدم مشكلة في الأعمدة المكررة أثناء تصدير البيانات من ورقة العمل إلى جدول البيانات. لا يمكن لجدول البيانات أن يحتوي على أعمدة مكررة لذا يجب إعادة تسمية الأعمدة المكررة قبل تصدير بيانات ورقة العمل إلى جدول البيانات. يمكن لـ Aspose.Cells إعادة تسمية الأعمدة المكررة تلقائيًا وفقًا لاستراتيجية محددة من قبلك باستخدام الخاصية [**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy). إذا حددت [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Digit، سيتم إعادة تسمية الأعمدة مثل column1، column2، column3، وما إلى ذلك، وإذا حددت [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter، فسيتم إعادة تسمية الأعمدة مثل columnA، columnB، columnC، وما إلى ذلك.

## **إعادة تسمية الأعمدة المكررة تلقائيًا أثناء تصدير بيانات ورقة العمل**

يضيف الكود العيني التالي بعض البيانات في الأعمدة الثلاثة الأولى للورقة ولكن جميع الأعمدة لها نفس الاسم أي *People*. ثم يصدر البيانات من الورقة إلى جدول البيانات عن طريق تحديد الاستراتيجية [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter. ثم يقوم بطباعة أسماء الأعمدة في جدول البيانات الذي تم إنشاؤه بواسطة Aspose.Cells. يظهر اللقطة الشاشية التالية جدول البيانات مع البيانات المصدرة في المُصَوِّر. كما يمكنك رؤية أن الأعمدة المُكررة قد تمت إعادة تسميتها لتصبح PeopleA، PeopleB وما إلى ذلك.

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **مخرجات الوحدة**

إليك الناتج المكتوب على وحدة الإخراج القياسية للكود العيني أعلاه كمرجع.

{{< highlight java >}}

People

PeopleA

PeopleB

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

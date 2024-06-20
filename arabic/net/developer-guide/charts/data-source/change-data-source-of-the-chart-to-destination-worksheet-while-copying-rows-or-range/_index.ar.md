---
title: تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق
description: تعلم كيفية تغيير مصدر البيانات للرسم البياني إلى ورقة عمل وجهة أثناء نسخ الصفوف أو النطاق في Aspose.Cells for .NET. سيوضح دليلنا لك كيفية تحديث نطاق البيانات للرسم البياني وربطه بورقة العمل المستهدفة، مما يضمن عكس الصفوف أو النطاق بدقة في الرسم البياني.
keywords: Aspose.Cells for .NET، الرسم البياني، مصدر البيانات، ورقة العمل الوجهة، صفوف، نطاق، نسخ، تحديث، نطاق البيانات، ربط.
type: docs
weight: 440
url: /ar/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **سيناريوهات الاستخدام المحتملة**

عند نسخ الصفوف أو النطاق الذي يحتوي على رسوم بيانية إلى ورقة عمل جديدة، فإن مصدر البيانات للرسم البياني لا يتغير. على سبيل المثال، إذا كان مصدر بيانات الرسم البياني يُساوي =Sheet1!$A$1:$B$4، فبعد نسخ الصفوف أو النطاق إلى ورقة العمل الجديدة، سيظل مصدر البيانات هو نفسه أي أنه =Sheet1!$A$1:$B$4. ولا يزال يُشير إلى ورقة العمل القديمة أي Sheet1. وهذا هو أيضًا السلوك في Microsoft Excel. ولكن إذا كنت ترغب في أن يشير إلى ورقة العمل الوجهة الجديدة، فيرجى استخدام خاصية [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) وتعيينها إلى **صحيح** أثناء استدعاء الطريقة [**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index). الآن إذا كانت ورقة العمل الوجهة هي DestSheet، فإن مصدر بيانات الرسم البياني الخاص بك سيتغير من =Sheet1!$A$1:$B$4 إلى =DestSheet!$A$1:$B$4.

## **تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق**

يشرح الكود النموذجي التالي استخدام الخاصية [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) أثناء نسخ الصفوف أو النطاق الذي يحتوي على رسوم بيانية إلى ورقة عمل جديدة. يستخدم الكود ملف الإكسل النموذجي]5113699.xlsx] ويولد ملف الإكسل الناتج]5113697.xlsx[.

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}

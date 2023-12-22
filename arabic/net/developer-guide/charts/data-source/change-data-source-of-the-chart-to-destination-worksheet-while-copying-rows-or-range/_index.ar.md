---
title: قم بتغيير مصدر بيانات المخطط إلى ورقة عمل الوجهة أثناء نسخ الصفوف أو النطاق
description: تعرف على كيفية تغيير مصدر بيانات المخطط إلى ورقة عمل الوجهة أثناء نسخ الصفوف أو النطاق في Aspose.Cells for .NET. سيوضح لك دليلنا كيفية تحديث نطاق بيانات المخطط وربطه بورقة العمل الوجهة، مع التأكد من أن الصفوف المنسوخة أو النطاق ينعكس بدقة في الرسم البياني.
keywords: Aspose.Cells for .NET, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.
type: docs
weight: 440
url: /ar/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
##  **سيناريوهات الاستخدام المحتملة**

عند نسخ صفوف أو نطاق يحتوي على مخططات إلى ورقة عمل جديدة، فإن مصدر بيانات المخطط لا يتغير. على سبيل المثال، إذا كان مصدر بيانات المخطط هو =Sheet1!$A$1:$B$4، فبعد نسخ الصفوف أو النطاق إلى ورقة عمل جديدة، سيظل مصدر البيانات كما هو، أي =Sheet1!$A$1:$B$4. لا يزال يشير إلى ورقة العمل القديمة، أي الورقة 1. وهذا أيضًا هو السلوك في Microsoft Excel. ولكن إذا كنت تريد أن تشير إلى ورقة عمل الوجهة الجديدة، فيرجى استخدام[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)الملكية وتعيينها على**حقيقي** أثناء الاتصال بـ[**Cells.نسخ الصفوف()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)طريقة. الآن، إذا كانت ورقة العمل الوجهة هي DestSheet، فسيتغير مصدر بيانات المخطط من =Sheet1!$A$1:$B$4 إلى =DestSheet!$A$1:$B$4.

##  **قم بتغيير مصدر بيانات المخطط إلى ورقة عمل الوجهة أثناء نسخ الصفوف أو النطاق**

يشرح نموذج التعليمات البرمجية التالي استخدام[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) الخاصية أثناء نسخ الصفوف أو النطاق الذي يحتوي على المخططات إلى ورقة عمل جديدة. يستخدم الكود[عينة من ملف اكسل](5113699.xlsx) ويولد[إخراج ملف إكسل](5113697.xlsx).

![ما يجب القيام به:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}

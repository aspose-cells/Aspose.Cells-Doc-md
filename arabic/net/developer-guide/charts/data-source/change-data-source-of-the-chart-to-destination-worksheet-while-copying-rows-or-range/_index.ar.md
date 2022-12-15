---
title: قم بتغيير مصدر بيانات المخطط إلى ورقة عمل الوجهة أثناء نسخ الصفوف أو النطاق
type: docs
weight: 440
url: /ar/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **سيناريوهات الاستخدام الممكنة**

عندما تنسخ صفوفًا أو نطاقًا يحتوي على مخططات إلى ورقة عمل جديدة ، فلن يتغير مصدر بيانات المخطط. على سبيل المثال ، إذا كان مصدر بيانات المخطط هو = Sheet1! $ A $ 1: $ B $ 4 ، فبعد نسخ الصفوف أو النطاق إلى ورقة عمل جديدة ، سيظل مصدر البيانات كما هو ، أي = Sheet1! $ A $ 1: $ B $ 4. لا يزال يشير إلى ورقة العمل القديمة مثل الورقة 1. هذا أيضًا هو السلوك في Microsoft Excel. ولكن إذا كنت تريد أن تشير إلى ورقة عمل الوجهة الجديدة ، فيرجى استخدام ملحق[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)الملكية وضبطها على**حقيقي** أثناء استدعاء[**Cells.CopyRows ()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)طريقة. الآن إذا كانت ورقة العمل الوجهة الخاصة بك هي DestSheet ، فسيتغير مصدر بيانات المخطط الخاص بك من = Sheet1! $ A $ 1: $ B $ 4 إلى = DestSheet! $ A $ 1: $ B $ 4.

## **قم بتغيير مصدر بيانات المخطط إلى ورقة عمل الوجهة أثناء نسخ الصفوف أو النطاق**

 يشرح نموذج التعليمات البرمجية التالي استخدام[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) الخاصية أثناء نسخ الصفوف أو النطاق الذي يحتوي على مخططات إلى ورقة عمل جديدة. يستخدم الرمز[نموذج ملف اكسل](5113699.xlsx) ويولد ال[ملف اكسل الناتج](5113697.xlsx).

![ما يجب القيام به: image_بديل_نص](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}

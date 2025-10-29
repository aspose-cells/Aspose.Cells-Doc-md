---  
title: تغيير مصدر بيانات الرسم البياني إلى ورقة الهدف أثناء نسخ الصفوف أو النطاق باستخدام Golang عبر C++  
description: تعلم كيفية تغيير مصدر بيانات المخطط إلى ورقة الهدف أثناء نسخ الصفوف أو النطاق في Aspose.Cells for C++. دليلنا سيرٌي كيف تقوم بتحديث مدى بيانات المخطط وربطه بورقة الهدف، لضمان أن تظهر الصفوف أو النطاق المنسوخ بدقة في المخطط.  
keywords: Aspose.Cells for C++، رسم بياني، مصدر البيانات، ورقة الهدف، الصفوف، النطاق، النسخ، التحديث، مدى البيانات، الربط.  
type: docs  
weight: 440  
url: /ar/go-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **سيناريوهات الاستخدام المحتملة**

عند نسخ الصفوف أو النطاق الذي يحتوي على مخططات إلى ورقة عمل جديدة، فإن مصدر البيانات للمخطط لا يتغير. على سبيل المثال، إذا كان مصدر البيانات للمخطط =Sheet1!$A$1:$B$4، فبعد نسخ الصفوف أو النطاق إلى ورقة جديدة، سيظل المصدر كما هو، وهو =Sheet1!$A$1:$B$4. لا يزال يشير إلى ورقة العمل القديمة، وهي Sheet1. هذا هو السلوك أيضًا في Microsoft Excel. ولكن إذا أردت أن يشير إلى ورقة العمل الجديدة، يرجى استخدام الخاصية [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/go-cpp/copyoptions/getrefertodestinationsheet/) وتعيينها إلى **true** أثناء استدعاء الطريقة [**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/). الآن، إذا كانت ورقة العمل الهدف هي DestSheet، فإن مصدر البيانات لمخططك سيتغير من =Sheet1!$A$1:$B$4 إلى =DestSheet!$A$1:$B$4.

## **تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق**

يوضح الكود النموذجي التالي استخدام الخاصية [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/go-cpp/copyoptions/getrefertodestinationsheet/) أثناء نسخ الصفوف أو النطاق الذي يحتوي على مخططات إلى ورقة عمل جديدة. يستخدم الكود ملف Excel النموذجي (5113699.xlsx) ويولد ملف Excel الناتج (5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeDataSourceOfTheChartToDestinationWorksheetWhileCopyingRowsOrRange.go" >}}

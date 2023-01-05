---
title: تصفية نوع البيانات أثناء تحميل المصنف من ملف القالب
type: docs
weight: 680
url: /ar/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}} 

 في بعض الأحيان ، تريد تحديد نوع البيانات التي يجب تحميلها عند إنشاء المصنف من ملف قالب. يمكن أن تؤدي تصفية البيانات المحملة إلى تحسين الأداء لغرضك الخاص ، خاصة عند استخدام[واجهات برمجة تطبيقات LightCells](/cells/ar/java/using-lightcells-api/) . الرجاء استخدام[LoadOptions.getLoadFilter (). setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) خاصية لهذا الغرض.

{{% /alert %}} 
## **تصفية نوع البيانات أثناء تحميل المصنف من ملف قالب**
يقوم نموذج التعليمات البرمجية التالي بتحميل كائنات الشكل فقط أثناء تحميل المصنف من ملف[ملف نموذجي](5472556.xlsx)والتي يمكنك تنزيلها من الرابط المحدد.

تُظهر لقطة الشاشة التالية ملف[ملف نموذجي](5472556.xlsx) المحتويات ويوضح أيضًا أنه لن يتم تحميل البيانات باللون الأحمر والخلفية الصفراء نظرًا لأن ملف[LoadOptions.getLoadFilter (). setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions)تم تعيين الخاصية على[LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![ما يجب القيام به: image_بديل_نص](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

تُظهر لقطة الشاشة التالية ملف[الإخراج PDF](5472554.pdf) والتي يمكنك تنزيلها من الرابط المحدد. هنا يمكنك أن ترى ، البيانات باللون الأحمر والخلفية الصفراء غير موجودة ولكن جميع الأشكال موجودة.

![ما يجب القيام به: image_بديل_نص](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}

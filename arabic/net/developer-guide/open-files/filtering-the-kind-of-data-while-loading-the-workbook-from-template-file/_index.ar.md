---
title: تصفية نوع البيانات أثناء تحميل المصنف من ملف القالب
type: docs
weight: 400
url: /ar/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}}

 في بعض الأحيان ، تريد تحديد نوع البيانات التي يجب تحميلها عند إنشاء المصنف من ملف القالب. يمكن أن تؤدي تصفية البيانات المحملة إلى تحسين الأداء لغرضك الخاص ، خاصة عند استخدام[واجهات برمجة تطبيقات LightCells](/cells/ar/net/using-lightcells-api/) . الرجاء استخدام[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) خاصية لهذا الغرض.

{{% /alert %}}

يقوم نموذج التعليمات البرمجية التالي بتحميل كائنات الشكل فقط أثناء تحميل المصنف من ملف[ملف نموذجي](5115552.xlsx) والتي يمكنك تنزيلها من الرابط المحدد. تُظهر لقطة الشاشة التالية ملف[ملف نموذجي](5115552.xlsx)المحتويات ويوضح أيضًا أن البيانات باللون الأحمر والخلفية الصفراء لن يتم تحميلها بسبب[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)تم تعيين الخاصية على[**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![ما يجب القيام به: image_بديل_نص](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

تُظهر لقطة الشاشة التالية ملف[الإخراج PDF](5115555.pdf) والتي يمكنك تنزيلها من الرابط المحدد. هنا يمكنك أن ترى ، البيانات باللون الأحمر والخلفية الصفراء غير موجودة ولكن جميع الأشكال موجودة.

![ما يجب القيام به: image_بديل_نص](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}

---
title: تصفية نوع البيانات أثناء تحميل ورق العمل من ملف النموذج
type: docs
weight: 680
url: /ar/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}} 

في بعض الأحيان، ترغب في تحديد نوع البيانات التي يجب تحميلها عند بناء ورق العمل من ملف النموذج. يمكن أن تُحسن تصفية البيانات المحملة الأداء لجيهتك الخاصة، خاصةً عند استخدام [LightCells APIs](/cells/ar/java/using-lightcells-api/). يرجى استخدام الخاصية [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) لهذا الغرض.

{{% /alert %}} 
## **تصفية نوع البيانات أثناء تحميل ورق العمل من ملف النموذج**
تحميل الشكل فقط أثناء تحميل ورق العمل من [ملف النموذج](5472556.xlsx) الذي يمكنك تنزيله من الرابط المعطى.

تُظهر اللقطة الشاشية التالية محتويات [ملف النموذج](5472556.xlsx) وتشرح أيضًا أن البيانات باللون الأحمر والخلفية الصفراء لن يتم تحميلها لأن الخاصية [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) تم تعيينها إلى [LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

تُظهر اللقطة الشاشية التالية [PDF الناتج](5472554.pdf) الذي يمكنك تنزيله من الرابط المعطى. هنا يمكنك أن ترى، البيانات باللون الأحمر والخلفية الصفراء غير موجودة ولكن جميع الأشكال موجودة.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}

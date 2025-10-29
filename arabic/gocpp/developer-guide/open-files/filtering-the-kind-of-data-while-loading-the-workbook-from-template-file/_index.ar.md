---
title: تصفية نوع البيانات أثناء تحميل دفتر العمل من ملف القالب باستخدام Golang عبر C++
linktitle: تصفية البيانات أثناء تحميل دفتر العمل
type: docs
weight: 400
url: /ar/go-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: تعلم كيفية تصفية أنواع بيانات معينة أثناء تحميل دفتر عمل من ملف قالب باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

 أحيانًا، تريد تحديد نوع البيانات الذي يجب تحميله عند إنشاء دفتر العمل من ملف القالب. يمكن أن يؤدي تصفية البيانات المحملة إلى تحسين الأداء لغرضك الخاص، خاصة عند استخدام [واجهة برمجة تطبيقات LightCells](/cells/ar/cpp/using-lightcells-api/). يرجى استخدام الخاصية [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) لهذا الغرض.

{{% /alert %}}

يقوم الكود العيني التالي بتحميل كائنات الشكل فقط أثناء تحميل الدفتر من ملف النموذج الذي يمكنك تحميله من الرابط المتوفر. توضح اللقطة الشاشية التالية محتويات ملف النموذج وتشرح أيضًا أنه لن يتم تحميل البيانات ذات اللون الأحمر والخلفية الصفراء لأن الخاصية [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) تم تعيينها على [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

تُظهر اللقطة الشاشية التالية ال [PDF الناتج](5115555.pdf) الذي يمكنك تحميله من الرابط المقدم. هنا يمكنك أن ترى، البيانات ذات اللون الأحمر والخلفية الصفراء غير موجودة لكن جميع الأشكال موجودة.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilteringTheKindOfDataWhileLoadingTheWorkbookFromTemplateFile.go" >}}

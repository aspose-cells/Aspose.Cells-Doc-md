---
title: تصفية نوع البيانات أثناء تحميل ورق العمل من ملف النموذج
type: docs
weight: 400
url: /ar/python-net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

أحيانًا، تريد تحديد نوع البيانات الذي يجب تحميله عند بناء دفتر العمل من ملف النموذج. يمكن أن يؤدي تصفية البيانات المحملة إلى تحسين الأداء لغايتك الخاصة. يرجى استخدام خاصية [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) لهذا الغرض.

{{% /alert %}}

يقوم الكود العيني التالي بتحميل كائنات الشكل فقط أثناء تحميل الدفتر من ملف النموذج الذي يمكنك تحميله من الرابط المتوفر. توضح اللقطة الشاشية التالية محتويات ملف النموذج وتشرح أيضًا أنه لن يتم تحميل البيانات ذات اللون الأحمر والخلفية الصفراء لأن الخاصية [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) تم تعيينها على [**LoadDataFilterOptions.SHAPE**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

تُظهر اللقطة الشاشية التالية ال [PDF الناتج](5115555.pdf) الذي يمكنك تحميله من الرابط المقدم. هنا يمكنك أن ترى، البيانات ذات اللون الأحمر والخلفية الصفراء غير موجودة لكن جميع الأشكال موجودة.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDataWhileLoadingWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}

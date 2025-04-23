---
title: تصفية نوع البيانات أثناء تحميل ورق العمل من ملف النموذج
type: docs
weight: 400
url: /ar/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

أحيانًا، ترغب في تحديد نوع البيانات التي يجب تحميلها عند بناء الدفتر من ملف النموذج. يمكن أن يحسن تصفية البيانات المحملة الأداء لأغراضك الخاصة، خصوصًا عند استخدام APIs الخفيفة. يرجى استخدام خاصية [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) لهذا الغرض.

{{% /alert %}}

يقوم الكود العيني التالي بتحميل كائنات الشكل فقط أثناء تحميل الدفتر من ملف النموذج الذي يمكنك تحميله من الرابط المتوفر. توضح اللقطة الشاشية التالية محتويات ملف النموذج وتشرح أيضًا أنه لن يتم تحميل البيانات ذات اللون الأحمر والخلفية الصفراء لأن الخاصية [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) تم تعيينها على [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

تُظهر اللقطة الشاشية التالية ال [PDF الناتج](5115555.pdf) الذي يمكنك تحميله من الرابط المقدم. هنا يمكنك أن ترى، البيانات ذات اللون الأحمر والخلفية الصفراء غير موجودة لكن جميع الأشكال موجودة.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

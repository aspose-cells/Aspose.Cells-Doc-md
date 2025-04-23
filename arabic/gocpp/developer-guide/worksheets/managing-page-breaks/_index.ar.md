---
title: إدارة فواصل الصفحات
type: docs
weight: 30
url: /ar/go-cpp/managing-page-breaks/
---

{{% alert color="primary" %}}

وفقًا للتعريف، فإن فاصل الصفحة هو المكان في تدفق النص حيث تنتهي صفحة وتبدأ الصفحة التالية. يتيح Microsoft Excel للمستخدمين إضافة فواصل صفحات في أي خلية محددة من ورقة العمل.

في الموقع الذي يتم إضافة فاصل الصفحة إليه، يتم التوقف عند الصفحة ويتم طباعة كل بقية البيانات بعد فاصل الصفحة على الصفحة التالية أثناء الطباعة. ببساطة، تقسم فواصل الصفحات ورقة العمل إلى صفحات متعددة وفقًا لمواصفاتك. يمكنك أيضًا إضافة فواصل صفحات إلى الأوراق الخاصة بك أثناء التشغيل باستخدام Aspose.Cells. تتيح Aspose.Cells للمطورين إضافة نوعين من فواصل الصفحات:

- فاصل صفحات أفقي
- فاصل صفحات عمودي

في بقية النقاش، سنصف كيف يمكنك إضافة فواصل صفحات أفقية أو عمودية إلى أوراق العمل الخاصة بك باستخدام Aspose.Cells.

{{% /alert %}}

## **كسرات الصفحة**

توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook) التي تمثل ملف Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook) على مجموعة [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection) تتيح الوصول إلى كل ورقة عمل في الملف.

تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). توفر فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) مجموعة واسعة من الطرق المستخدمة لإدارة ورقة العمل. لإضافة فواصل الصفحات، استخدم طريقة [AddPageBreaks](https://reference.aspose.com/cells/go-cpp/worksheet/addpagebreaks) من فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/).

### **إضافة فواصل الصفحات**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingPageBreaks.go" >}}

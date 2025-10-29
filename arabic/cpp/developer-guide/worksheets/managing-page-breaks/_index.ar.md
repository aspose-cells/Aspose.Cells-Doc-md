---
title: إدارة فواصل الصفحات
type: docs
weight: 30
url: /ar/cpp/managing-page-breaks/
---

{{% alert color="primary" %}} 

وفقًا للتعريف، فإن فاصل الصفحة هو المكان في تدفق النص حيث تنتهي صفحة وتبدأ الصفحة التالية. يتيح Microsoft Excel للمستخدمين إضافة فواصل صفحات في أي خلية محددة من ورقة العمل.

في الموقع الذي يتم إضافة فاصل الصفحة إليه، يتم التوقف عند الصفحة ويتم طباعة كل بقية البيانات بعد فاصل الصفحة على الصفحة التالية أثناء الطباعة. ببساطة، تقسم فواصل الصفحات ورقة العمل إلى صفحات متعددة وفقًا لمواصفاتك. يمكنك أيضًا إضافة فواصل صفحات إلى الأوراق الخاصة بك أثناء التشغيل باستخدام Aspose.Cells. تتيح Aspose.Cells للمطورين إضافة نوعين من فواصل الصفحات:

- فاصل صفحات أفقي
- فاصل صفحات عمودي

في بقية النقاش، سنصف كيف يمكنك إضافة فواصل صفحات أفقية أو عمودية إلى أوراق العمل الخاصة بك باستخدام Aspose.Cells.

{{% /alert %}} 
## **كسرات الصفحة**
توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) التي تمثل ملف Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) على مجموعة [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

ورقة العمل ممثلة بالفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) . توفر الفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة واسعة من الأساليب المستخدمة لإدارة ورقة العمل. لإضافة فواصل الصفحات، استخدم الأسلوب [AddPageBreaks](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) للفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) .
### **إضافة فواصل الصفحات**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}

---
title: ضبط الهوامش
type: docs
weight: 20
url: /ar/python-net/setting-margins/
description: في هذا المقال، ستتعلم كيفية ضبط هوامش ورقة عمل Excel باستخدام الشيفرة البرمجية المثالية. ستتعلم أيضًا كيفية ضبط الهوامش بشكل برمجي لمركز الصفحة، وهوامش الرأس والقاع لإعداد الصفحة باستخدام واجهة برمجة التطبيقات لـ Aspose.Cells لـ Python via .NET.
keywords: مكتبة Python Excel، ضبط هوامش ورقة عمل Excel لتكون في المركز، ضبط هوامش رأس الصفحة والقاع باستخدام Python.
---

{{% alert color="primary" %}}

Aspose.Cells لـ Python via .NET يدعم تمامًا خيارات إعداد الصفحة في Microsoft Excel. قد تحتاج المطورين إلى تكوين إعدادات إعداد الصفحة لورقات العمل للتحكم في عملية الطباعة. يناقش هذا الموضوع كيفية استخدام Aspose.Cells لـ Python via .NET لضبط هوامش الصفحة.

{{% /alert %}}

## **كيفية ضبط الهوامش**

توفر Aspose.Cells لـ Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، تمثل ملف Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) الخاصية [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) المستخدمة لتعيين خيارات إعداد الصفحة لورقة عمل. السمة [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup) هي كائن من فئة [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) التي تمكّن المطورين من تعيين خيارات تخطيط الصفحة المختلفة لورقة العمل المطبوعة. الفئة [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) توفر خصائص وطرق مختلفة يمكن استخدامها لتعيين خيارات إعداد الصفحة.

## **كيفية ضبط هوامش الصفحة**

تعيين هوامش الصفحة (اليسار، اليمين، الأعلى، الأسفل) باستخدام أعضاء فئة [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). ويُدرج بعض الطرق الواردة أدناه والتي تُستخدم لتحديد الهوامش الصفحية:

- [**left_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/left_margin/)
- [**right_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/right_margin/)
- [**top_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/top_margin/)
- [**bottom_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/bottom_margin/)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-1.py" >}}

## **كيفية التوسط على الصفحة**

من الممكن توسيط شيء ما على الصفحة أفقيًا ورأسيًا. لهذا الغرض، هناك بعض الأعضاء المفيدة في الفئة [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) مثل [**center_horizontally**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_horizontally/) و [**center_vertically**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_vertically/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.py" >}}

## **كيفية ضبط هوامش رأس وقاع**

تعيين هوامش الرأس والتذييل باستخدام أعضاء فئة [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) مثل [**header_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/header_margin) و [**footer_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/footer_margin).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.py" >}}

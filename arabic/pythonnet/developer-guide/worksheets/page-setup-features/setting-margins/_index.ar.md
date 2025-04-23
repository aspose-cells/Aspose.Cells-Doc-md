---
title: ضبط الهوامش
type: docs
weight: 20
url: /ar/python-net/setting-margins/
description: في هذا المقال، سوف تتعلم كيفية ضبط هوامش ورقة عمل Excel باستخدام رمز نمونه. ستتعلم أيضاً كيفية تعيين الهوامش برمجياً لمركز الصفحة، هوامش الرأس والتذييل في إعداد الصفحة باستخدام API Aspose.Cells for Python via .NET.
keywords: مكتبة إكسل في بايثون، تعيين هوامش ورقة العمل في إكسل إلى الوسط، تعيين هوامش الرأس والتذييل لورقة العمل باستخدام بايثون.
---

{{% alert color="primary" %}}

يدعم Aspose.Cells for Python via .NET بشكل كامل خيارات إعداد الصفحة في مايكروسوفت إكسل. قد يحتاج المطورون إلى تكوين إعدادات إعداد الصفحة لأوراق العمل للتحكم في عملية الطباعة. يناقش هذا الموضوع كيفية استخدام Aspose.Cells لـ Python via .NET لتكوين هوامش الصفحة.

{{% /alert %}}

## **كيفية تعيين الهوامش**

يوفر Aspose.Cells لـ Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف الإكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) الخاصية [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup/) المستخدمة لتعيين خيارات إعداد الصفحة لورقة عمل. السمة [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup) هي كائن من فئة [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) التي تمكّن المطورين من تعيين خيارات تخطيط الصفحة المختلفة لورقة العمل المطبوعة. الفئة [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) توفر خصائص وطرق مختلفة يمكن استخدامها لتعيين خيارات إعداد الصفحة.

## **كيفية تعيين هوامش الصفحة**

تعيين هوامش الصفحة (اليسار، اليمين، الأعلى، الأسفل) باستخدام أعضاء فئة [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). ويُدرج بعض الطرق الواردة أدناه والتي تُستخدم لتحديد الهوامش الصفحية:

- [**left_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/left_margin/)
- [**right_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/right_margin/)
- [**top_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/top_margin/)
- [**bottom_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/bottom_margin/)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-1.py" >}}

## **كيفية التوسيط على الصفحة**

من الممكن توسيط شيء ما على الصفحة أفقيًا ورأسيًا. لهذا الغرض، هناك بعض الأعضاء المفيدة في الفئة [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) مثل [**center_horizontally**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_horizontally/) و [**center_vertically**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_vertically/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.py" >}}

## **كيفية تعيين هوامش الرأس والتذييل**

تعيين هوامش الرأس والتذييل باستخدام أعضاء فئة [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) مثل [**header_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/header_margin) و [**footer_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/footer_margin).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.py" >}}

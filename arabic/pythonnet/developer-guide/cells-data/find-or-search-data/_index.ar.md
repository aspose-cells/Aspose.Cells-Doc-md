---
title: البحث عن البيانات أو البحث
type: docs
weight: 50
url: /ar/python-net/find-or-search-data/
description: تعلم كيفية العثور على الخلايا في ورقة العمل التي تحتوي على بيانات محددة من خلال Aspose.Cells for Python via .NET API.
keywords: مكتبة Python Excel، البحث في البيانات بواسطة Python، البحث في البيانات بواسطة Python، البحث في الخلايا التي تحتوي على صيغة باستخدام Python، البحث في الخلايا التي تحتوي على صيغة بواسطة Python، البحث في البيانات أو الصيغ باستخدام FindOptions في Python، البحث في البيانات أو الصيغ باستخدام FindOptions في Python، العثور على البيانات أو الأصيغ التي تحتوي على قيمة أو رقم معينة بواسطة Python، البحث في الخلايا التي تحتوي على بيانات معينة بواسطة Python
---

{{% alert color="primary" %}}

يسمح Microsoft Excel للمستخدمين بالعثور على الخلايا في ورقة العمل التي تحتوي على بيانات محددة.

{{% /alert %}}

## **العثور على الخلايا التي تحتوي على بيانات محددة**

### **استخدام Microsoft Excel**

يسمح Microsoft Excel للمستخدمين بالعثور على الخلايا في ورقة العمل التي تحتوي على بيانات محددة. إذا قمت باختيار **تحرير** من قائمة **العثور** في Microsoft Excel، سترى مربع حوار حيث يمكنك تحديد قيمة البحث.

هنا، نبحث عن القيمة "البرتقال". تسمح Aspose.Cells أيضًا للمطورين بالعثور على الخلايا في ورقة العمل التي تحتوي على القيم المحددة.

### **استخدام Aspose.Cells**

توفر Aspose.Cells فئةً تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) التي تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) عدة طرق للعثور على الخلايا في ورقة العمل التي تحتوي على بيانات محددة من قبل المستخدم. يتم مناقشة بعض هذه الطرق أدناه بمزيد من التفصيل.

{{% alert color="primary" %}}

تعيد جميع طرق البحث مراجع الخلايا التي تحتوي على البيانات المحددة.

{{% /alert %}}

## **العثور على الخلايا التي تحتوي على صيغة**

يمكن للمطورين العثور على صيغة محددة في ورقة العمل عن طريق استدعاء الطريقة [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) من كجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). عادةً ما تقبل الطريقة [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) ثلاثة معاملات:

- **ما هي:** الكائن الذي يجب البحث عنه. يجب أن يكون النوع int,double,DateTime,string,bool.
- **previous_cell:** الخلية السابقة التي تحتوي على نفس الكائن. يمكن تعيين هذا المعلمة على قيمة null إذا كان البحث من البداية.
- **find_options:** خيارات للعثور على الكائن المطلوب.

تستخدم الأمثلة أدناه بيانات ورقة العمل لممارسة طرق البحث:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingFormula-1.py" >}}

## **العثور على البيانات أو الصيغ باستخدام FindOptions**

من الممكن العثور على القيم المحددة باستخدام طريقة [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) من مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) بمساعدة [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions) مختلفة. عادةً ما تقبل الطريقة [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) المعاملات التالية:

- **ما هي:**، البيانات أو القيمة التي يتعين البحث عنها.
- **الخلية_السابقة**, الخلية الأخيرة التي احتوت على نفس القيمة. يمكن تعيين هذا المعلمة إلى قيمة null عند البحث من البداية.
- **find_options**, find options.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingDataOrFormulasUsingFindOptions-1.py" >}}

## **العثور على الخلايا التي تحتوي على قيمة سلسلة أو رقم محدد**

من الممكن العثور على القيم النصية المحددة من خلال استدعاء نفس الطريقة [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) الموجودة في مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) بمختلف [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions).

حدد الخصائص [**FindOptions.look_in_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_in_type/) و [**FindOptions.look_at_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_at_type/). يوضح الكود المثال التالي كيفية استخدام هذه الخصائص للعثور على الخلايا بعدد متنوع من السلاسل حسب **البداية** أو **الوسط** أو **النهاية** من سلسلة الخلية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingStringValueOrNumber-1.py" >}}

## **مواضيع متقدمة**
- [العثور على الخلايا ذات النمط المحدد](/cells/ar/python-net/find-cells-with-specific-style/)
- [العثور عما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة](/cells/ar/python-net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [البحث عن البيانات باستخدام القيم الأصلية](/cells/ar/python-net/search-data-using-original-values/)
{{< app/cells/assistant language="python-net" >}}

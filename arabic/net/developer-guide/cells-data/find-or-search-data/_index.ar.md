---
title: البحث عن البيانات أو البحث
type: docs
weight: 50
url: /ar/net/find-or-search-data/
description: تعلم كيفية البحث عن الخلايا في ورقة عمل تحتوي على بيانات محددة من خلال API Aspose.Cells for .NET
keywords: البحث عن البيانات، البحث عن البيانات، البحث عن الخلايا التي تحتوي على صيغة، البحث عن الخلايا التي تحتوي على صيغة، البحث عن البيانات أو الصيغ باستخدام FindOptions، البحث عن البيانات أو الصيغ باستخدام FindOptions، العثور على البيانات أو البيانات المحددة باستخدام قيمة سلسلة أو رقم محدد، البحث عن الخلايا التي تحتوي على البيانات المحددة
---

{{% alert color="primary" %}}

يسمح Microsoft Excel للمستخدمين بالعثور على الخلايا في ورقة العمل التي تحتوي على بيانات محددة.

{{% /alert %}}

## **العثور على الخلايا التي تحتوي على بيانات محددة**

### **استخدام Microsoft Excel**

يسمح Microsoft Excel للمستخدمين بالعثور على الخلايا في ورقة العمل التي تحتوي على بيانات محددة. إذا قمت باختيار **تحرير** من قائمة **العثور** في Microsoft Excel، سترى مربع حوار حيث يمكنك تحديد قيمة البحث.

هنا، نبحث عن القيمة "البرتقال". تسمح Aspose.Cells أيضًا للمطورين بالعثور على الخلايا في ورقة العمل التي تحتوي على القيم المحددة.

### **استخدام Aspose.Cells**

توفر Aspose.Cells فئةً تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) التي تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) عدة طرق للعثور على الخلايا في ورقة العمل التي تحتوي على بيانات محددة من قبل المستخدم. يتم مناقشة بعض هذه الطرق أدناه بمزيد من التفصيل.

{{% alert color="primary" %}}

تعيد جميع طرق البحث مراجع الخلايا التي تحتوي على البيانات المحددة.

{{% /alert %}}

## **العثور على الخلايا التي تحتوي على صيغة**

يمكن للمطورين العثور على صيغة محددة في ورقة العمل عن طريق استدعاء الطريقة [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) من كجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). عادةً ما تقبل الطريقة [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) ثلاثة معاملات:

- **الكائن:** الكائن الذي يتم البحث عنه. يجب أن يكون النوع int، double، DateTime، string، bool.
- **الخلية السابقة:** الخلية السابقة بنفس الكائن. يمكن تعيين هذا المعلمة إلى قيمة null إذا كنا نبحث من البداية.
- FindOptions: خيارات للعثور على الكائن المطلوب.

تستخدم الأمثلة أدناه بيانات ورقة العمل لممارسة طرق البحث:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **العثور على البيانات أو الصيغ باستخدام FindOptions**

من الممكن العثور على القيم المحددة باستخدام طريقة [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) من مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) بمساعدة [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) مختلفة. عادةً ما تقبل الطريقة [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) المعاملات التالية:

- **قيمة البحث**, البيانات أو القيمة التي يتم البحث عنها.
- **الخلية السابقة**, آخر خلية احتوت على نفس القيمة. يمكن تعيين هذه المعلمة إلى قيمة null عند البحث من البداية.
- **خيارات البحث**, خيارات البحث.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **العثور على الخلايا التي تحتوي على قيمة سلسلة أو رقم محدد**

من الممكن العثور على القيم النصية المحددة من خلال استدعاء نفس الطريقة [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) الموجودة في مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) بمختلف [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

حدد الخصائص [**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) و [**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype). يوضح الكود المثال التالي كيفية استخدام هذه الخصائص للعثور على الخلايا بعدد متنوع من السلاسل حسب **البداية** أو **الوسط** أو **النهاية** من سلسلة الخلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **مواضيع متقدمة**
- [العثور على الخلايا ذات النمط المحدد](/cells/ar/net/find-cells-with-specific-style/)
- [العثور عما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة](/cells/ar/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [البحث عن البيانات باستخدام القيم الأصلية](/cells/ar/net/search-data-using-original-values/)
{{< app/cells/assistant language="csharp" >}}

---
title: البحث عن البيانات أو البحث عنها
type: docs
weight: 50
url: /ar/net/find-or-search-data/
description: تعرف على كيفية البحث عن الخلايا أو البحث عنها في ورقة عمل تحتوي على بيانات محددة من خلال Aspose.Cells for .NET API.
keywords: Find data, Search data, Find Cells Containing a Formula, Search Cells Containing a Formula, Find Data or Formulas using FindOptions, Search Data or Formulas using FindOptions, Find or Search Cells Containing Specified String Value or Number, Find or Search cells contains specified data
---
{{% alert color="primary" %}}

Microsoft يتيح Excel للمستخدمين العثور على خلايا في ورقة عمل تحتوي على بيانات محددة.

{{% /alert %}}

##  **العثور على Cells يحتوي على بيانات محددة**

###  **باستخدام Microsoft اكسل**

 Microsoft يتيح Excel للمستخدمين العثور على خلايا في ورقة عمل تحتوي على بيانات محددة. إذا قمت بتحديد**يحرر** من**يجد** في Microsoft Excel، سيظهر لك مربع حوار يمكنك من خلاله تحديد قيمة البحث.

نحن هنا نبحث عن القيمة "البرتقال". Aspose.Cells يسمح أيضًا للمطورين بالعثور على خلايا تحتوي على قيم محددة في ورقة العمل.

###  **باستخدام Aspose.Cells**

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يحتوي الفصل على أ[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) المجموعة التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة التي تمثل كافة الخلايا في ورقة العمل. ال[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)توفر المجموعة عدة طرق للعثور على الخلايا في ورقة عمل تحتوي على بيانات محددة من قبل المستخدم. وتتم مناقشة عدد قليل من هذه الأساليب أدناه بمزيد من التفصيل.

{{% alert color="primary" %}}

تقوم كافة أساليب البحث بإرجاع مراجع الخلايا التي تحتوي على البيانات المحددة للبحث.

{{% /alert %}}

##  **العثور على Cells يحتوي على صيغة**

 يمكن للمطورين العثور على صيغة محددة في ورقة العمل عن طريق استدعاء[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة[**يجد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) طريقة. عادة،[**يجد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)تقبل الطريقة ثلاث معلمات:

- **هدف:**الكائن المراد البحث عنه. يجب أن يكون النوع int,double,DateTime,string,bool.
- **الخلية السابقة:**الخلية السابقة بنفس الكائن. يمكن ضبط هذه المعلمة على قيمة فارغة في حالة البحث من البداية.
- FindOptions: خيارات للعثور على الكائن المطلوب.

تستخدم الأمثلة أدناه بيانات ورقة العمل لممارسة أساليب البحث:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

##  **البحث عن البيانات أو الصيغ باستخدام FindOptions**

 من الممكن العثور على قيم محددة باستخدام[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة[**يجد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) طريقة مع مختلف[**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . عادة،[**يجد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)تقبل الطريقة المعلمات التالية:

- *قيمة البحث**، البيانات أو القيمة المراد البحث عنها.
- *الخلية السابقة**، الخلية الأخيرة التي تحتوي على نفس القيمة. يمكن ضبط هذه المعلمة على قيمة فارغة عند البحث من البداية.
- *البحث عن الخيارات**، خيارات البحث.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

##  **العثور على Cells يحتوي على قيمة أو رقم سلسلة محدد**

 من الممكن العثور على قيم سلسلة محددة عن طريق الاتصال بها[**يجد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) الطريقة وجدت في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) جمع مع مختلف[**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 حدد ال[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) و[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) ملكيات. يوضح رمز المثال التالي كيفية استخدام هذه الخصائص للعثور على خلايا تحتوي على عدد مختلف من السلاسل في**بداية** أو في**مركز** أو في**نهاية** من سلسلة الخلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

##  **مواضيع متقدمة**
- [ابحث عن Cells بأسلوب محدد](/cells/ar/net/find-cells-with-specific-style/)
- [اكتشف ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة](/cells/ar/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [البحث عن البيانات باستخدام القيم الأصلية](/cells/ar/net/search-data-using-original-values/)

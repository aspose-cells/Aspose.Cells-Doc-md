---
title: البحث عن البيانات أو البحث عنها
type: docs
weight: 50
url: /ar/net/find-or-search-data/
---
{{% alert color="primary" %}}

Microsoft يسمح Excel للمستخدمين بالعثور على خلايا في ورقة عمل تحتوي على بيانات محددة.

{{% /alert %}}

## **ايجاد Cells يتضمن بيانات محددة**

### **باستخدام Microsoft إكسل**

Microsoft يسمح Excel للمستخدمين بالعثور على خلايا في ورقة عمل تحتوي على بيانات محددة. إذا اخترت**يحرر** من**تجد** القائمة في Microsoft Excel ، سترى مربع حوار حيث يمكنك تحديد قيمة البحث.

هنا ، نبحث عن قيمة "البرتقال". يسمح Aspose.Cells أيضًا للمطورين بالعثور على خلايا في ورقة العمل تحتوي على قيم محددة.

### **باستخدام Aspose.Cells**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة تمثل جميع الخلايا في ورقة العمل. ال[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)توفر المجموعة عدة طرق للعثور على الخلايا في ورقة عمل تحتوي على بيانات محددة من قبل المستخدم. تتم مناقشة عدد قليل من هذه الأساليب أدناه بمزيد من التفصيل.

{{% alert color="primary" %}}

ترجع جميع طرق البحث مراجع الخلايا التي تحتوي على البيانات المحددة للبحث.

{{% /alert %}}

## **إيجاد Cells الذي يحتوي على صيغة**

 يمكن للمطورين العثور على صيغة محددة في ورقة العمل عن طريق استدعاء[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة[**تجد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) طريقة. عادةً ما يكون ملف[**تجد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)تقبل الطريقة ثلاث معاملات:

- **هدف:**الكائن المطلوب البحث عنه. يجب أن يكون النوع int ، double ، DateTime ، string ، bool.
- **الخلية السابقة:**الخلية السابقة بنفس الكائن. يمكن ضبط هذه المعلمة على قيمة خالية في حالة البحث من البداية.
- FindOptions: خيارات للعثور على الكائن المطلوب.

تستخدم الأمثلة أدناه بيانات ورقة العمل لممارسة طرق البحث:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **البحث عن البيانات أو الصيغ باستخدام FindOptions**

 من الممكن العثور على قيم محددة باستخدام[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة[**تجد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) طريقة مختلفة[**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . عادةً ما يكون ملف[**تجد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)تقبل الطريقة المعلمات التالية:

- **قيمة البحث**، البيانات أو القيمة المراد البحث عنها.
- **الخلية السابقة**، وهي الخلية الأخيرة التي تحتوي على نفس القيمة. يمكن ضبط هذه المعلمة على قيمة خالية عند البحث من البداية.
- **ابحث عن الخيارات**، خيارات البحث.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **إيجاد Cells يتضمن قيمة أو رقم سلسلة محدد**

 من الممكن العثور على قيم سلسلة محددة عن طريق استدعاء نفس[**تجد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) الطريقة الموجودة في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) جمع مع مختلف[**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 حدد ال[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) و[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype)الخصائص. يوضح رمز المثال التالي كيفية استخدام هذه الخصائص للعثور على خلايا ذات عدد متنوع من السلاسل في**بداية** أو في**المركز** أو في**نهاية** من سلسلة الخلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **موضوعات مسبقة**
- [ابحث عن Cells بأسلوب خاص](/cells/ar/net/find-cells-with-specific-style/)
- [ابحث عما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة](/cells/ar/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [البحث في البيانات باستخدام القيم الأصلية](/cells/ar/net/search-data-using-original-values/)

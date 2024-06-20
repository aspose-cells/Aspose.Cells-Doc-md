---
title: تنسيق وتعديل النطاقات المسماة
type: docs
weight: 85
url: /ar/net/format-and-modify-named-ranges/
---

## **تنسيق النطاقات**

### **ضبط لون الخلفية وسمات الخط لنطاق مسمى**

لتطبيق التنسيق، قم بتعريف كائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) لتحديد إعدادات النمط وتطبيقه على كائن [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).

المثال التالي يوضح كيفية ضبط لون التعبئة الصلبة (لون الظل) مع إعدادات الخط إلى نطاق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **إضافة حدود إلى نطاق مسمى**

من الممكن إضافة حدود إلى مجموعة من الخلايا بدلاً من خلية واحدة فقط. يوفر كائن [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) طريقة [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) التي تأخذ المعلمات التالية لإضافة حد لنطاق الخلايا:

- نوع الحد، نوع الحد، المحدد من تعداد [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)
- نمط الخط، نمط الخط، المحدد من تعداد [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)
- لون، لون الخط، المحدد من تعداد الألوان

يظهر المثال التالي كيفية تعيين حد للنطاق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

المثال التالي يوضح كيفية ضبط حدود حول كل خلية في النطاق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **إعادة تسمية نطاق مسمى**

يُتيح Aspose.Cells لك إعادة تسمية النطاق المسمى حسب احتياجاتك. يُمكنك الحصول على النطاق المسمى وإعادة تسميته باستخدام السمة [**Name.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text). يوضح المثال التالي كيفية إعادة تسمية نطاق مسمى.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **اتحاد النطاقات**

يوفر Aspose.Cells الطريقة [**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union) لاتخاذ الاتحاد للنطاقات، تُعيد الطريقة كائن [*ArrayList*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8). يوضح المثال التالي كيفية اتخاذ الاتحاد للنطاقات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **تقاطع النطاقات**

يوفر Aspose.Cells الطريقة [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) لتقاطع نطاقين. تُعيد الطريقة كائن [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). للتحقق مما إذا كان نطاق يتقاطع مع نطاق آخر، استخدم الطريقة [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) التي تُعيد قيمة بوليانية. يوضح المثال التالي كيفية تقاطع النطاقات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **دمج الخلايا في النطاق المسمى**

يوفر Aspose.Cells الطريقة [**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) لدمج الخلايا في النطاق. يوضح المثال التالي كيفية دمج الخلايا الفردية في نطاق مسمى.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **إزالة نطاق مسمى**

توفر Aspose.Cells الطريقة [**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) لمحو اسم النطاق. لمسح محتويات النطاق، استخدم الطريقة [**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index). يوضح المثال التالي كيفية إزالة نطاق مسمى مع محتوياته.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}

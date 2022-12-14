---
title: تنسيق وتعديل النطاقات المسماة
type: docs
weight: 85
url: /ar/net/format-and-modify-named-ranges/
---
## **تنسيق النطاقات**

### **تعيين لون الخلفية وخصائص الخط إلى نطاق مسمى**

 لتطبيق التنسيق ، حدد ملف[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) لتحديد إعدادات النمط وتطبيقها على ملف[**نطاق**](https://reference.aspose.com/cells/net/aspose.cells/range)هدف.

يوضح المثال التالي كيفية تعيين لون تعبئة خالص (لون التظليل) باستخدام إعدادات الخط إلى نطاق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **إضافة حدود إلى نطاق مسمى**

 من الممكن إضافة حدود إلى نطاق من الخلايا بدلاً من خلية واحدة فقط. ال[**نطاق**](https://reference.aspose.com/cells/net/aspose.cells/range) كائن يوفر[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)طريقة تأخذ المعلمات التالية لإضافة حد إلى نطاق الخلايا:

-  نوع الحد ونوع الحد المحدد من ملف[**نوع الحدود**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)تعداد.
-  نمط الخط ، نمط الخط المحدد من ملف[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)تعداد.
- اللون ، لون الخط ، المحدد من تعداد اللون.

يوضح المثال التالي كيفية تعيين حد مخطط إلى نطاق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

يوضح المثال التالي كيفية تعيين الحدود حول كل خلية في النطاق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **إعادة تسمية نطاق مسمى**

 Aspose.Cells يسمح لك بإعادة تسمية نطاق مسمى لحاجتك. يمكنك الحصول على النطاق المسمى وإعادة تسميته باستخدام[**الاسم**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text)ينسب. يوضح المثال التالي كيفية إعادة تسمية نطاق مسمى.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **اتحاد النطاقات**

 يوفر Aspose.Cells[**النطاق. الاتحاد**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union)طريقة لأخذ الاتحاد للنطاقات ، تقوم الطريقة بإرجاع[*ArrayList*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8)هدف. يوضح المثال التالي كيفية أخذ الاتحاد للنطاقات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **تقاطع النطاقات**

 يوفر Aspose.Cells ملف[**المدى**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) طريقة لتقاطع نطاقين. تقوم الطريقة بإرجاع ملف[**نطاق**](https://reference.aspose.com/cells/net/aspose.cells/range) هدف. للتحقق مما إذا كان النطاق يتقاطع مع نطاق آخر ، استخدم[**المدى**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)الطريقة التي تُرجع قيمة منطقية. يوضح المثال التالي كيفية تقاطع النطاقات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **ادمج Cells في النطاق المحدد**

 يوفر Aspose.Cells[**Range.Merge ()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)طريقة لدمج الخلايا في النطاق. يوضح المثال التالي كيفية دمج الخلايا الفردية لنطاق مسمى.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **إزالة نطاق مسمى**

 يوفر Aspose.Cells ملف[**NameCollection.RemoveAt ()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) طريقة لمسح اسم النطاق. لمسح محتويات النطاق ، استخدم[**Cells. ClearRange ()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index)طريقة. يوضح المثال التالي كيفية إزالة نطاق مسمى بمحتوياته.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}

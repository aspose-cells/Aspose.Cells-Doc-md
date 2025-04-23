---
title: دمج الملفات
type: docs
weight: 20
url: /ar/net/merge-files/
---

## **مقدمة**

توفر Aspose.Cells طرقًا مختلفة لدمج الملفات. يمكن استخدام الطريقة [**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) لدمج عدة دفاتر عمل بيانات وتنسيقات وصيغ، كما يمكن استخدام الطريقة [**Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index) لنسخ أوراق العمل إلى دفتر عمل جديد. تُستخدم هذه الطرق بسهولة وهي فعالة، ولكن إذا كنت تمتلك الكثير من الملفات لدمجها، قد تجد أنها تستهلك الكثير من موارد النظام. لتجنب ذلك، استخدم الطريقة الثابتة [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)، وهي الطريقة الأكثر كفاءة لدمج العديد من الملفات.

## **دمج الملفات باستخدام Aspose.Cells**

يوضح الكود العيني التالي كيفية دمج الملفات الكبيرة باستخدام الطريقة [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles). يأخذ ملفين بسيطين ولكن كبيرين فقط، Book1.xls و Book2.xls. يتضمن الملفات بيانات مهيأة وصيغ فقط.

{{% alert color="primary" %}}

تدعم الطريقة [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) فقط دمج البيانات والأنماط والتنسيقات والصيغ. قد لا يتم دمج الكائنات مثل الرسوم البيانية والصور والتعليقات أو الكائنات الأخرى باستخدام هذه الطريقة. علاوة على ذلك، يتم استخدام ملف مخزن مؤقت لتخزين البيانات المؤقتة للعملية.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

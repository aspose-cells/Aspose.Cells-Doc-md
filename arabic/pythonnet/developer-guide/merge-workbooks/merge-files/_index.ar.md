---
title: دمج الملفات
type: docs
weight: 20
url: /ar/python-net/merge-files/
---

## **مقدمة**

يوفر Aspose.Cells for Python via .NET طرقًا مختلفة لدمج الملفات. للملفات البسيطة التي تحتوي على بيانات وتنسيقات وصيغ، يمكن استخدام طريقة [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) لدمج عدة ملفات عمل، ويمكن استخدام طريقة [**Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy) لنسخ أوراق العمل إلى ملف عمل جديد. هذه الطرق سهلة الاستخدام وفعالة، ولكن إذا كان لديك العديد من الملفات لدمجها، فقد تكتشف أنها تستهلك الكثير من موارد النظام. لتجنب ذلك، استخدم الطريقة الثابتة [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files)، وهي وسيلة أكثر كفاءة لدمج عدة ملفات.

## **دمج الملفات باستخدام Aspose.Cells for Python via .NET**

يوضح الكود العيني التالي كيفية دمج الملفات الكبيرة باستخدام الطريقة [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files). يأخذ ملفين بسيطين ولكن كبيرين فقط، Book1.xls و Book2.xls. يتضمن الملفات بيانات مهيأة وصيغ فقط.

{{% alert color="primary" %}}

تدعم الطريقة [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files) فقط دمج البيانات والأنماط والتنسيقات والصيغ. قد لا يتم دمج الكائنات مثل الرسوم البيانية والصور والتعليقات أو الكائنات الأخرى باستخدام هذه الطريقة. علاوة على ذلك، يتم استخدام ملف مخزن مؤقت لتخزين البيانات المؤقتة للعملية.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CellsHelperClass-MergeFiles-1.py" >}}


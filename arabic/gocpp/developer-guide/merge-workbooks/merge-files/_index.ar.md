---
title: دمج الملفات باستخدام Golang عبر C++
linktitle: دمج الملفات
type: docs
weight: 20
url: /ar/go-cpp/merge-files/
description: تعلم كيفية دمج ملفات إكسل بكفاءة باستخدام Aspose.Cells for C++.
---

## **مقدمة**

يوفر Aspose.Cells طرقًا مختلفة لدمج الملفات. للملفات البسيطة التي تحتوي على بيانات، تنسيقات، وصيغ، يمكن استخدام طريقة [**Workbook.Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) لدمج عدة دفاتر عمل، ويمكن استخدام طريقة [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) لنسخ أوراق العمل إلى دفتر عمل جديد. هذه الطرق سهلة الاستخدام وفعالة، ولكن إذا كان لديك الكثير من الملفات للدمج، قد تجد أنها تستهلك الكثير من موارد النظام. لتجنب ذلك، استخدم الطريقة الثابتة [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/)، وهو أسلوب أكثر كفاءة لدمج عدة ملفات.

## **دمج الملفات باستخدام Aspose.Cells**

يوضح رمز المثال التالي كيفية دمج ملفات كبيرة باستخدام أسلوب [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/). يأخذ ملفين بسيطين لكن كبيرين، Book1.xls وBook2.xls. تحتوي الملفات على بيانات وصيغ منسقة فقط.

{{% alert color="primary" %}}

طريقة [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/) تدعم فقط دمج البيانات والأنماط والتنسيقات والصيغ. قد لا يتم دمج كائنات مثل الرسوم البيانية والصور والتعليقات أو كائنات أخرى باستخدام هذه الطريقة. علاوة على ذلك، يتم استخدام ملف مخزن مؤقت لتخزين البيانات المؤقتة للعملية.

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeFiles.go" >}}

---
title: إصدار موارد غير مُدارة للمصنف باستخدام Golang عبر C++
linktitle: تحرير الموارد غير المُدارة لدفتر العمل
type: docs
weight: 310
url: /ar/go-cpp/release-unmanaged-resources-of-the-workbook/
description: تعلم كيفية تحرير الموارد غير المُدارة لكتاب العمل باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

يوفر Aspose.Cells الأسلوب [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) لتحرير الموارد غير المُدارة لكائن [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). نمط التخلص يُستخدم فقط للكائنات التي تصل إلى الموارد غير المُدارة، مثل مقابض الملف والأنابيب، مقابض التسجيل، مقابض الانتظار أو المؤشرات إلى مجموعات من الذاكرة غير المُدارة. وذلك لأن مجمع المخلفات فعّال لاسترداد الكائنات المُدارة غير المستخدمة بشكل كبير، ولكنه غير قادر على استرداد الكائنات غير المُدارة.

{{% /alert %}}

يطبق كائن [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) الآن واجهة *IDisposable* التي تحتوي على طريقة واحدة [**Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/). يمكنك إما استدعاء طريقة [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) مباشرة أو يمكنك استخدام بيان *Using* لاستدعاء هذه الطريقة تلقائيًا.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReleaseUnmanagedResourcesOfTheWorkbook.go" >}}

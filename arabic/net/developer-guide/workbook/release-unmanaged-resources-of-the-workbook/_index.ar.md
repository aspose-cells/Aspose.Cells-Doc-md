---
title: تحرير الموارد غير المُدارة لدفتر العمل
type: docs
weight: 310
url: /ar/net/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}}

يوفر Aspose.Cells الأسلوب [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) لتحرير الموارد غير المُدارة لكائن [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). نمط التخلص يُستخدم فقط للكائنات التي تصل إلى الموارد غير المُدارة، مثل مقابض الملف والأنابيب، مقابض التسجيل، مقابض الانتظار أو المؤشرات إلى مجموعات من الذاكرة غير المُدارة. وذلك لأن مجمع المخلفات فعّال لاسترداد الكائنات المُدارة غير المستخدمة بشكل كبير، ولكنه غير قادر على استرداد الكائنات غير المُدارة.

{{% /alert %}}

يُنفذ كائن [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الآن واجهة *System.IDisposable* التي تحتوي على الأسلوب الوحيد [**Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose). يمكنك إما استدعاء الأسلوب [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) مباشرة أو استخدام البيان Using لاستدعاء هذا الأسلوب تلقائياً.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
{{< app/cells/assistant language="csharp" >}}

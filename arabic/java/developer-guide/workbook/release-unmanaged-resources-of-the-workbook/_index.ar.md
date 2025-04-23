---
title: تحرير الموارد غير المُدارة لدفتر العمل
type: docs
weight: 290
url: /ar/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

توفر Aspose.Cells طريقة [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) لتحرير الموارد غير المُدارة للكائن [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). يُستخدم نمط التخلص فقط للأشياء التي تصل إلى الموارد غير المُدارة، مثل مقابض الملفات والأنابيب، ومقابض السجل، ومقابض الانتظار أو المؤشرات إلى كتل من الذاكرة غير المُدارة. وذلك لأن جامع القمامة فعال جدًا في استرداد الكائنات المُدارة غير المستخدمة، لكنه غير قادر على استرداد الكائنات غير المُدارة.

{{% /alert %}} 
## **إطلاق موارد المصنف العمل غير المُدارة**
يعرض الكود النموذجي التالي كيفية استخدام طريقة [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
{{< app/cells/assistant language="java" >}}

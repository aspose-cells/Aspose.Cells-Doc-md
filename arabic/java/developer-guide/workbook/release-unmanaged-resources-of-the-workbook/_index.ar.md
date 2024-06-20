---
title: تحرير الموارد غير المُدارة لدفتر العمل
type: docs
weight: 290
url: /ar/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

توفر Aspose.Cells طريقة [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) لإطلاق موارد المصنف العمل غير المُدارة لكائن [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). تُستخدم النمط المتحرر فقط للكائنات التي تصل إلى الموارد غير المُدارة ، مثل مقابض الملف والأنابيب ومقابض التسجيل ومقابض الانتظار أو المؤشرات على مجموعات ذاكرة غير مُدارة. هذا لأن المجمع الضاغط فعال جدًا في استرداد الكائنات المُدارة غير المستخدمة ، ولكنه غير قادر على استرداد الكائنات غير المُدارة.

{{% /alert %}} 
## **إطلاق موارد المصنف العمل غير المُدارة**
يظهر الكود المثالي التالي كيفية استخدام أسلوب [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}

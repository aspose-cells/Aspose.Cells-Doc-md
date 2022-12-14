---
title: الافراج عن الموارد غير المدارة من المصنف
type: docs
weight: 290
url: /ar/java/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}} 

 يوفر Aspose.Cells[Workbook.dispose ()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\) ) طريقة لتحرير الموارد غير المدارة من[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)هدف. يتم استخدام نمط التخلص فقط للكائنات التي تصل إلى موارد غير مُدارة ، مثل مقابض الملفات والأنابيب أو مقابض التسجيل أو مقابض الانتظار أو المؤشرات الخاصة بكتل من الذاكرة غير المُدارة. هذا لأن جامع القمامة فعال للغاية في استعادة الكائنات المدارة غير المستخدمة ، لكنه غير قادر على استعادة الكائنات غير المُدارة.

{{% /alert %}} 
## **الافراج عن الموارد غير المدارة من المصنف**
يُظهر نموذج التعليمات البرمجية التالي كيفية الاستفادة من ملحق[Workbook.dispose ()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) طريقة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}

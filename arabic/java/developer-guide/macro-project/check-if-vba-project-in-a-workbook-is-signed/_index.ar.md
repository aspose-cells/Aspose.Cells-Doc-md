---
title: التحقق مما إذا كان مشروع VBA في كتاب عمل موقع بالتوقيع
type: docs
weight: 40
url: /ar/java/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

يمكنك التحقق مما إذا كان مشروع VBA الخاص بك موقعًا أم لا باستخدام Microsoft Excel عبر الأمر **Tools > Digital Signatures...**. بالمثل, يمكنك التحقق منه بشكل برمجي باستخدام طريقة Aspose.Cells [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned).

{{% /alert %}}

## **التحقق مما إذا كان مشروع VBA في مصنف عمل موقعًا**

الكود التالي يحمل الكتاب ويتحقق مما إذا كان مشروع VBA الخاص به موقع بالتوقيع باستخدام خاصية [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned). ستعيد الخاصية **true** إذا كان المشروع موقع بالتوقيع وإلا ستعيد **false**.

## كود عينة

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
{{< app/cells/assistant language="java" >}}

---
title: تحقق مما إذا كان مشروع VBA في مصنف تم توقيعه
type: docs
weight: 40
url: /ar/java/check-if-vba-project-in-a-workbook-is-signed/
---
{{% alert color="primary" %}}

 يمكنك التحقق مما إذا كان مشروع VBA الخاص بك موقّعًا أم لا باستخدام Microsoft Excel عبر**أدوات> تواقيع رقمية ...** أمر القائمة. وبالمثل ، يمكنك التحقق منه برمجيًا باستخدام Aspose.Cells[**Workbook.getVbaProject (). isSigned ()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) طريقة.

{{% /alert %}}

## **تحقق مما إذا كان مشروع VBA في مصنف تم توقيعه**

 تقوم الكود التالي بتحميل المصنف والتحقق مما إذا كان مشروع VBA الخاص به قد تم توقيعه باستخدام[**Workbook.getVbaProject (). isSigned ()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)منشأه. سوف يعود الممتلكات**حقيقي** إذا تم التوقيع على المشروع وإلا فإنه سيعود**خاطئة**.

## عينة من الرموز

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}

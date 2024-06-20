---
title: Bir Çalışmada VBA Projesinin İmzalı Olup Olmadığını Kontrol Edin
type: docs
weight: 40
url: /tr/java/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Microsoft Excel'i kullanarak **Araçlar > Dijital İmzalar...** menü komutunu kullanarak VBA projesinin imzalı olup olmadığını kontrol edebilirsiniz. Benzer şekilde, Aspose.Cells [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) yöntemini kullanarak programlı olarak da kontrol edebilirsiniz.

{{% /alert %}}

## **Çalışma Kitabındaki VBA projesinin imzalı olup olmadığını kontrol edin**

Aşağıdaki kod, çalışbook yükler ve [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) özelliğini kullanarak VBA projesinin imzalı olup olmadığını kontrol eder. Proje imzalıysa **true** döndürecek, aksi takdirde **false** döndürecektir.

## Örnek Kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}

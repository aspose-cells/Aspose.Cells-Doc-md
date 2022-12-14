---
title: Çalışma Kitabındaki VBA projesinin İmzalı olup olmadığını kontrol edin
type: docs
weight: 40
url: /tr/java/check-if-vba-project-in-a-workbook-is-signed/
---
{{% alert color="primary" %}}

 VBA projenizin imzalı olup olmadığını Microsoft Excel üzerinden kontrol edebilirsiniz.**Araçlar > Dijital İmzalar...** menü komutu. Benzer şekilde, Aspose.Cells'i kullanarak programlı olarak kontrol edebilirsiniz.[**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) yöntem.

{{% /alert %}}

## **Çalışma Kitabındaki VBA projesinin İmzalı olup olmadığını kontrol edin**

 Aşağıdaki kod, çalışma kitabını yükler ve VBA projesinin kullanılarak imzalanıp imzalanmadığını kontrol eder.[**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)Emlak. mülk geri dönecek**doğru** proje imzalanırsa aksi takdirde geri döner**yanlış**.

## Basit kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}

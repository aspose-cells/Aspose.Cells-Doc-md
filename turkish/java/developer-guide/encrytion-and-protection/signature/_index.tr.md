---
title: Dijital İmzaları Atama ve Doğrulama
linktitle: İmza
type: docs
weight: 100
url: /tr/java/assign-and-validate-digital-signatures/
description: Excel dosyası dijital imzası, doğrulama. Bir Excel dosyasının içeriğinin doğruluğunu korumak için, Aspose.Cells for .Net ile C# kodları kullanarak dijital bir imza ekleyebilirsiniz.
---

{{% alert color="primary" %}}

Dijital imza, bir çalışma kitabı dosyasının geçerli olduğunu ve hiç kimsenin onu değiştirmediğini garanti eder. Microsoft Office paketi ile birlikte gönderilen **SELFCERT** aracını veya başka bir aracı kullanarak kişisel bir dijital imza oluşturabilirsiniz. Hatta bir dijital imza satın alabilirsiniz. Bir dijital imza oluşturduktan veya edindikten sonra, çalışma kitabınıza eklemelisiniz. Bir dijital imza eklemek, bir zarfı mühürlemekle benzerdir. Bir zarf mühürlenmişse, içeriğinin kimse tarafından bozulmadığı konusunda bir düzeyde güvenceye sahipsiniz demektir.

Aspose.Cells for Java API, yaygın speadsheet'leri imzalamak ve doğrulamak için [**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) ve [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) sınıflarını sağlar.

{{% /alert %}}

## **Speadsheet'leri İmzalama**

İmzalama işlemi yukarıda tartışılan bir sertifikaya ihtiyaç duyar. Sertifikanın yanı sıra, speadsheet'leri başarılı bir şekilde imzalamak için gerekli olan şifresi de olmalıdır.

Aşağıdaki kod parçası, Aspose.Cells for Java API'sını kullanarak bir elektronik tabloya imza atma işleminin kullanımını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

Belirtilen parola, sertifika parolasıyla eşleşmiyorsa, bir *javax.crypto.BadPaddingException* türünde istisna atanır.

{{% /alert %}}

## **Tabloların Doğrulanması**

Aşağıdaki kod parçası, Aspose.Cells for Java API kullanımını tablonun doğrulanması için göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
{{< app/cells/assistant language="java" >}}

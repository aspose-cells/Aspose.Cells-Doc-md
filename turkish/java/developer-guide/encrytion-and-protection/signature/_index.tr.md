---
title: Dijital İmzaları Atama ve Doğrulama
linktitle: İmza
type: docs
weight: 100
url: /tr/java/assign-and-validate-digital-signatures/
description: Excel dosyası dijital imza, doğrulama. Bir çalışma kitabının Excel dosyası içeriğinin orijinalliğini korumak için .Net için Aspose.Cells ile C# kodlarını kullanarak dijital imza ekleyebilirsiniz.
---
{{% alert color="primary" %}}

 Dijital imza, çalışma kitabı dosyasının geçerli olduğunu ve kimsenin dosyayı değiştirmediğini garanti eder. kullanarak kişisel bir dijital imza oluşturabilirsiniz.**SELFCERT** Microsoft Office paketi veya başka herhangi bir araçla gönderilen araç. Dijital imza bile satın alabilirsiniz. Bir dijital imza oluşturduktan veya aldıktan sonra, bunu çalışma kitabınıza eklemeniz gerekir. Dijital imza eklemek, bir zarfı mühürlemeye benzer. Bir zarf mühürlü olarak gelirse, içeriğinin kimsenin kurcalanmadığına dair bir dereceye kadar güvenceye sahip olursunuz.

 Aspose.Cells for Java API[**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) & [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) elektronik tabloları imzalamak ve doğrulamak için sınıflar.

{{% /alert %}}

## **Elektronik Tabloları İmzalamak**

İmzalama işlemi, yukarıda tartışıldığı gibi bir sertifika gerektirir. Sertifikanın yanı sıra, Aspose.Cells API'i kullanarak e-tabloları başarılı bir şekilde imzalamak için kişinin şifresine de sahip olması gerekir.

Aşağıdaki kod parçacığı, bir elektronik tabloyu imzalamak için Aspose.Cells for Java API kullanımını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

 Belirtilen parolanın sertifika parolasıyla eşleşmemesi durumunda, bir istisna türü*javax.crypto.BadPaddingException* atılacak.

{{% /alert %}}

## **Elektronik Tabloları Doğrulama**

Aşağıdaki kod parçacığı, elektronik tabloyu doğrulamak için Aspose.Cells for Java API kullanımını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}

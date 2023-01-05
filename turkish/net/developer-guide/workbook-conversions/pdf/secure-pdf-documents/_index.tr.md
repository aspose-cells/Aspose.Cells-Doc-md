---
title: Güvenli PDF Belgeler
type: docs
weight: 120
url: /tr/net/secure-pdf-documents/
---
{{% alert color="primary" %}}

Bazen geliştiricilerin şifrelenmiş PDF dosyalarıyla çalışması gerekir. Örneğin, belgeleri yalnızca herkesin açamaması veya belge içeriğinin yazdırılıp çıkarılamayacağını veya ayıklanabileceğini kısıtlamak istememesi için kullanıcı ve sahip parolalarıyla güvenceye almaları gerekir.

Bu makalede, elektronik tabloları PDF'e kaydederken PDF güvenlik seçeneklerinin nasıl geçileceği açıklanmaktadır.

{{% /alert %}}

 Aspose.Cells şunları sağlar:[**Aspose.Cells.Rendering.PdfSecurity**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity) güvenlikle çalışmak için ad alanı. Aşağıdaki örnek kod, PDF'lerin Aspose.Cells ile nasıl güvenli hale getirileceğini açıklamaktadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

 Elektronik tablo formüller içeriyorsa, aramak en iyisidir[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)PDF'e dönüştürülmeden hemen önce. Bu, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}

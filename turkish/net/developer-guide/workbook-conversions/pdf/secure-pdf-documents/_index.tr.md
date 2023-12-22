---
title: Güvenli PDF Belgeler
type: docs
weight: 120
url: /tr/net/secure-pdf-documents/
---
{{% alert color="primary" %}}

Bazen geliştiricilerin şifrelenmiş PDF dosyalarıyla çalışması gerekir. Örneğin:

- Belgeleri sahip ve kullanıcı parolalarıyla koruyun, böylece herkes açamaz.
- Belge açıldıktan sonra belgeye yönelik kısıtlamaları veya izinleri ayarlayın. örneğin belge içeriğinin yazdırılıp yazdırılamayacağını veya çıkartılabileceğini kısıtlayın.

Bu makalede, e-tabloları PDF'e kaydederken PDF güvenlik seçeneklerinin nasıl aktarılacağı açıklanmaktadır.

{{% /alert %}}

 Aspose.Cells sağlar[**PdfGüvenlikSeçenekleri**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)güvenlikle çalışmak için. PDF'e kaydederken sahip ve kullanıcı şifrelerini ayarlayabilirsiniz. Şifrelenmiş PDF belgesini görüntülemek üzere açmak için sahip şifresi veya kullanıcı şifresi gerekecektir.

- Kullanıcı şifresi null veya boş dize olabilir, bu durumda PDF belgesini açarken kullanıcıdan şifre istenmeyecektir.
- PDF numaralı belgenin doğru sahip şifresiyle açılması, belgeye tam erişime (herhangi bir erişim kısıtlaması belirtilmeden) olanak tanır.
- PDF numaralı belgenin doğru kullanıcı şifresi ile açılması (veya kullanıcı şifresi olmayan bir belgenin açılması), belirtilen izinler doğrultusunda sınırlı erişime izin vermektedir.

Aşağıdaki örnek kod, PDF'lerin Aspose.Cells ile nasıl güvence altına alınacağını açıklamaktadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

 Elektronik tablo formüller içeriyorsa, aramak en iyisidir.[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) PDF'e dönüştürülmeden hemen önce. Bu, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}

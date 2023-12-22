---
title: Güvenli PDF Belgeler
type: docs
weight: 260
url: /tr/java/secure-pdf-documents/
description: Excel dosyalarından dönüştürürken PDF dosyalarının güvenliğini sağlayın. Bu makalede, Aspose.Cells for Java API ile Excel'den güvenli PDF dosyasının oluşturulması gösterilmektedir.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

Bazen geliştiricilerin şifrelenmiş PDF dosyalarıyla çalışması gerekir. Örneğin:

- Belgeleri sahip ve kullanıcı parolalarıyla koruyun, böylece herkes açamaz.
- Belge açıldıktan sonra belgeye yönelik kısıtlamaları veya izinleri ayarlayın. örneğin belge içeriğinin yazdırılıp yazdırılamayacağını veya çıkartılabileceğini kısıtlayın.

Bu makalede, e-tabloları PDF'e kaydederken PDF güvenlik seçeneklerinin nasıl aktarılacağı açıklanmaktadır.

{{% /alert %}}

 Aspose.Cells sağlar[**PdfGüvenlikSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/)güvenlikle çalışmak için. PDF'e kaydederken sahip ve kullanıcı şifrelerini ayarlayabilirsiniz. Şifrelenmiş PDF belgesini görüntülemek üzere açmak için sahip şifresi veya kullanıcı şifresi gerekecektir.

- Kullanıcı şifresi null veya boş dize olabilir, bu durumda PDF belgesini açarken kullanıcıdan şifre istenmeyecektir.
- PDF numaralı belgenin doğru sahip şifresiyle açılması, belgeye tam erişime (herhangi bir erişim kısıtlaması belirtilmeden) olanak tanır.
- PDF numaralı belgenin doğru kullanıcı şifresi ile açılması (veya kullanıcı şifresi olmayan bir belgenin açılması), belirtilen izinler doğrultusunda sınırlı erişime izin vermektedir.

Aşağıdaki örnek kod, Aspose.Cells for Java API ile güvenli PDF dosyalarının nasıl oluşturulacağını açıklamaktadır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 Elektronik tablo formüller içeriyorsa, aramak en iyisidir.[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()PDF'e dönüştürülmeden hemen önce. Bu, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}

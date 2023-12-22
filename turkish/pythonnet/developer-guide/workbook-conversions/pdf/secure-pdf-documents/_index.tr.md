---
title: Güvenli PDF Belgeler
type: docs
weight: 120
url: /tr/python-net/secure-pdf-documents/
description: E-tabloları Aspose.Cells for Python via .NET API ile PDF'e kaydederken PDF güvenlik seçeneklerini nasıl aktaracağınızı öğrenin.
keywords: Python write security options to pdf, encrypt PDF document 
---
{{% alert color="primary" %}}

Bazen geliştiricilerin şifrelenmiş PDF dosyalarıyla çalışması gerekir. Örneğin:

- Belgeleri sahip ve kullanıcı parolalarıyla koruyun, böylece herkes açamaz.
- Belge açıldıktan sonra belgeye yönelik kısıtlamaları veya izinleri ayarlayın. örneğin belge içeriğinin yazdırılıp yazdırılamayacağını veya çıkartılabileceğini kısıtlayın.

Bu makalede, e-tabloları PDF'e kaydederken PDF güvenlik seçeneklerinin nasıl aktarılacağı açıklanmaktadır.

{{% /alert %}}

 Aspose.Cells for Python via .NET sağlar[**PdfGüvenlikSeçenekleri**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)güvenlikle çalışmak için. PDF'e kaydederken sahip ve kullanıcı şifrelerini ayarlayabilirsiniz. Şifrelenmiş PDF belgesini görüntülemek üzere açmak için sahip şifresi veya kullanıcı şifresi gerekecektir.

- Kullanıcı şifresi null veya boş dize olabilir, bu durumda PDF belgesini açarken kullanıcıdan şifre istenmeyecektir.
- PDF numaralı belgenin doğru sahip şifresiyle açılması, belgeye tam erişime (herhangi bir erişim kısıtlaması belirtilmeden) olanak tanır.
- PDF numaralı belgenin doğru kullanıcı şifresi ile açılması (veya kullanıcı şifresi olmayan bir belgenin açılması), belirtilen izinler doğrultusunda sınırlı erişime izin vermektedir.

Aşağıdaki örnek kod, PDF'lerin Aspose.Cells for Python via .NET ile nasıl güvence altına alınacağını açıklamaktadır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

 Elektronik tablo formüller içeriyorsa, aramak en iyisidir.[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) PDF'e dönüştürülmeden hemen önce. Bu, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}

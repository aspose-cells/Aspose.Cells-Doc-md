---
title: Güvenli PDF Belgeleri
type: docs
weight: 120
url: /tr/python-net/secure-pdf-documents/
description: Aspose.Cells for Python via .NET API sı ile elektronik tabloları PDF olarak kaydederken PDF güvenlik seçeneklerini nasıl geçireceğinizi öğrenin.
keywords: Python da PDF ye güvenlik seçenekleri yazma, PDF belgesini şifreleme 
---

{{% alert color="primary" %}}

Bazı durumlarda, geliştiriciler şifrelenmiş PDF dosyalarıyla çalışmak zorunda kalabilir. Örneğin:

- Belgeleri sahip ve kullanıcı şifreleri ile güvence altına almak, böylece herkes tarafından açılamamasını sağlamak.
- Doküman açıldıktan sonra kısıtlamalar veya izinler belirlemek. Örneğin: doküman içeriğinin yazdırılabilir veya çıkarılabilir olup olmadığını sınırlamak.

Bu makale, elektronik tabloları PDF'ye kaydederken PDF güvenlik seçeneklerini nasıl geçireceğinizi açıklar.

{{% /alert %}}

Python için Aspose.Cells via .NET, güvenlikle çalışmak için [**PdfSecurityOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) sağlar. PDF'ye kaydederken sahibi ve kullanıcı şifrelerini ayarlayabilirsiniz. Şifreler PDF belgesini görüntülemek için gereklidir.

- Kullanıcı şifresi null veya boş dize olabilir, bu durumda kullanıcıdan PDF belgesini açarken herhangi bir parola gerekli olmayacaktır.
- Doğru sahip parolasıyla PDF belgesinin doğru şekilde açılması belgeye tam erişim (belirtilen herhangi bir erişim kısıtlaması olmadan) sağlar.
- Doğru kullanıcı parolasıyla PDF belgesinin doğru şekilde açılması (veya herhangi bir kullanıcı parolası olmayan bir belgenin açılması) belirtilen izinlerle sınırlı erişim sağlar.

Aşağıdaki örnek kod, Aspose.Cells için Python via .NET ile PDF'leri nasıl güvence altına alacağınızı açıklar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

Eğer elektronik tablo formüller içeriyorsa, PDF olarak dışa aktarmadan hemen önce [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)çağrısı yapmak en iyisidir. Böylece formüle bağlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}

---
title: Golang ile C++ kullanarak Güvenli PDF Belgeleri
linktitle: Güvenli PDF Belgeleri
type: docs
weight: 120
url: /tr/go-cpp/secure-pdf-documents/
description: Aspose.Cells kullanarak Golang ile C++ üzerinden PDF belgelerini sahip ve kullanıcı şifreleri ile nasıl güvenli hale getireceğinizi öğrenin.
---

{{% alert color="primary" %}}

Bazı durumlarda, geliştiriciler şifrelenmiş PDF dosyalarıyla çalışmak zorunda kalabilir. Örneğin:

- Belgeleri sahip ve kullanıcı şifreleri ile güvence altına almak, böylece herkes tarafından açılamamasını sağlamak.
- Doküman açıldıktan sonra kısıtlamalar veya izinler belirlemek. Örneğin: doküman içeriğinin yazdırılabilir veya çıkarılabilir olup olmadığını sınırlamak.

Bu makale, elektronik tabloları PDF'ye kaydederken PDF güvenlik seçeneklerini nasıl geçireceğinizi açıklar.

{{% /alert %}}

 Aspose.Cells, güvenlikle ilgili işler için [**PdfSecurityOptions**](https://reference.aspose.com/cells/go-cpp/pdfsecurityoptions/) sağlar. PDF'ye kaydederken sahibi ve kullanıcı şifreleri ayarlayabilirsiniz. Şifreler, şifreli PDF dosyasını görüntülemek için gerekli olacaktır.

- Kullanıcı şifresi null veya boş dize olabilir, bu durumda kullanıcıdan PDF belgesini açarken herhangi bir parola gerekli olmayacaktır.
Doğru sahip şifresi ile PDF belgeyi açmak belgeye tam erişim sağlar (belirtilen herhangi bir erişim kısıtlaması olmadan).
- Doğru kullanıcı parolasıyla PDF belgesinin doğru şekilde açılması (veya herhangi bir kullanıcı parolası olmayan bir belgenin açılması) belirtilen izinlerle sınırlı erişim sağlar.

Aşağıdaki örnek kod, Aspose.Cells ile PDF'leri güvence altına alma işlemi hakkında bilgi verir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SecurePdfDocuments.go" >}}
{{% alert color="primary" %}}

Eğer elektronik tablo formüller içeriyorsa, PDF'ye dönüştürmeden hemen önce [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) çağrılması en iyisidir. Bu, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin gösterilmesini sağlar.

{{% /alert %}}

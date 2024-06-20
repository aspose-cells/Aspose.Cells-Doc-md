---
title: Güvenli PDF Belgeleri
type: docs
weight: 260
url: /tr/java/secure-pdf-documents/
description: Excel dosyalarından dönüştürürken PDF dosyalarını güvenli hale getirin. Bu makale, Aspose.Cells for Java API sinden Excel den güvenli PDF dosyası oluşturmayı göstermektedir.
keywords: java ile güvenli pdf belgeleri, güvenli pdf belgeleri, excelden güvenli pdf, java ile excelden güvenli pdf, excelden şifreli pdf ye dönüştür, java ile excelden şifreli pdf ye dönüştür, excel den şifreli pdf ye dönüştür, java ile excel den şifreli pdf ye dönüştür, excel den şifreli pdf ye dönüştürme java, excel den şifreli pdf ye dönüştürme
---

{{% alert color="primary" %}}

Bazı durumlarda, geliştiriciler şifrelenmiş PDF dosyalarıyla çalışmak zorunda kalabilir. Örneğin:

- Belgeleri sahip ve kullanıcı şifreleri ile güvence altına almak, böylece herkes tarafından açılamamasını sağlamak.
- Doküman açıldıktan sonra kısıtlamalar veya izinler belirlemek. Örneğin: doküman içeriğinin yazdırılabilir veya çıkarılabilir olup olmadığını sınırlamak.

Bu makale, elektronik tabloları PDF'ye kaydederken PDF güvenlik seçeneklerini nasıl geçireceğinizi açıklar.

{{% /alert %}}

Aspose.Cells, güvenlikle çalışma imkanı sunar. PDF'ye kaydederken sahip ve kullanıcı şifrelerini ayarlayabilirsiniz. Şifrelenmiş PDF belgesini görüntülemek için sahip veya kullanıcı parolaları gereklidir.

- Kullanıcı şifresi null veya boş dize olabilir, bu durumda kullanıcıdan PDF belgesini açarken herhangi bir parola gerekli olmayacaktır.
- Doğru sahip parolasıyla PDF belgesinin doğru şekilde açılması belgeye tam erişim (belirtilen herhangi bir erişim kısıtlaması olmadan) sağlar.
- Doğru kullanıcı parolasıyla PDF belgesinin doğru şekilde açılması (veya herhangi bir kullanıcı parolası olmayan bir belgenin açılması) belirtilen izinlerle sınırlı erişim sağlar.

Aşağıdaki örnek kod, Aspose.Cells for Java API'si ile güvenli PDF dosyaları oluşturmayı açıklar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

Eğer elektronik tablo formüller içeriyorsa, bunu PDF'e dönüştürmeden hemen önce [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--)'ı çağırmanız en iyisidir. Bu, formül bağımlı değerlerin yeniden hesaplanmasını ve doğru değerlerin PDF'de gösterilmesini sağlar.

{{% /alert %}}

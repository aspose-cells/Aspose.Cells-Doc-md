---
title: Güvenli PDF Belgeleri
type: docs
weight: 120
url: /tr/net/secure-pdf-documents/
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

Aşağıdaki örnek kod, Aspose.Cells ile PDF'leri güvence altına alma işlemi hakkında bilgi verir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

Eğer elektronik tablo formüller içeriyorsa, PDF olarak dışa aktarmadan hemen önce [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)çağrısı yapmak en iyisidir. Böylece formüle bağlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

---
title: Node.js üzerinden C++ kullanarak PDF Güvenliği Sağla
linktitle: Güvenli PDF Belgeleri
type: docs
weight: 120
url: /tr/nodejs-cpp/secure-pdf-documents/
description: PDF belgelerini sahibi ve kullanıcı şifreleri kullanarak nasıl güvenli hale getireceğinizi ve PDF dosyaları için izinleri ayarlayacağınızı Aspose.Cells for Node.js via C++ ile öğrenin.
---

{{% alert color="primary" %}}

Bazı durumlarda, geliştiriciler şifrelenmiş PDF dosyalarıyla çalışmak zorunda kalabilir. Örneğin:

- Belgeleri sahip ve kullanıcı şifreleri ile güvence altına almak, böylece herkes tarafından açılamamasını sağlamak.
- Doküman açıldıktan sonra kısıtlamalar veya izinler belirlemek. Örneğin: doküman içeriğinin yazdırılabilir veya çıkarılabilir olup olmadığını sınırlamak.

Bu makale, elektronik tabloları PDF'ye kaydederken PDF güvenlik seçeneklerini nasıl geçireceğinizi açıklar.

{{% /alert %}}

 Aspose.Cells, güvenlikle ilgili işler için [**PdfSecurityOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/) sağlar. PDF'ye kaydederken sahibi ve kullanıcı şifreleri ayarlayabilirsiniz. Şifreler, şifreli PDF dosyasını görüntülemek için gerekli olacaktır.

- Kullanıcı şifresi boş veya null olabilir; bu durumda, PDF dosyasını açarken kullanıcıdan şifre istenmez.
Doğru sahip şifresi ile PDF belgeyi açmak belgeye tam erişim sağlar (belirtilen herhangi bir erişim kısıtlaması olmadan).
- Doğru kullanıcı parolasıyla PDF belgesinin doğru şekilde açılması (veya herhangi bir kullanıcı parolası olmayan bir belgenin açılması) belirtilen izinlerle sınırlı erişim sağlar.

Aşağıdaki örnek kod, Aspose.Cells ile PDF'leri güvence altına alma işlemi hakkında bilgi verir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const saveOption = new AsposeCells.PdfSaveOptions();
saveOption.setSecurityOptions(new AsposeCells.PdfSecurityOptions());

saveOption.getSecurityOptions().setUserPassword("user");
saveOption.getSecurityOptions().setOwnerPassword("owner");
saveOption.getSecurityOptions().setExtractContentPermission(false);
saveOption.getSecurityOptions().setPrintPermission(false);

workbook.save(path.join(dataDir, "securepdf_test.out.pdf"), saveOption);
```

{{% alert color="primary" %}}

Eğer elektronik tablo formüller içeriyorsa, PDF olarak dışa aktarmadan hemen önce [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)çağrısı yapmak en iyisidir. Böylece formüle bağlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}

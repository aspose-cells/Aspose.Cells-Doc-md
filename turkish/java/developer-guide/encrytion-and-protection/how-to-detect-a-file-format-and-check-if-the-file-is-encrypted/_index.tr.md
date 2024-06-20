---
title: Bir Dosya Biçimini Algılamak ve Dosyanın Şifreli Olup Olmadığını Kontrol Etme
type: docs
weight: 2000
url: /tr/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

Bazen dosyayı açmadan önce dosyanın biçimini algılamanız gerekebilir çünkü dosya uzantısı dosya içeriğinin uygun olduğunu garanti etmez. Dosya şifreli olabilir (şifre korumalı bir dosya) bu yüzden doğrudan okunamaz veya okumamalıyız. Aspose.Cells, belgeleri işlemek için kullanabileceğiniz [**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat(java.io.InputStream)) statik yöntemini ve bazı ilgili API'leri sunar.

{{% /alert %}}

## **Dosya Biçimini Algılamak ve Dosyanın Şifreli Olup Olmadığını Kontrol Etmek İçin Java Kodu**

Aşağıdaki örnek kod, dosya biçimini (dosya yolu kullanarak) algılamanın ve uzantısını kontrol etmenin nasıl yapıldığını göstermektedir. Ayrıca dosyanın şifreli olup olmadığını belirleyebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}

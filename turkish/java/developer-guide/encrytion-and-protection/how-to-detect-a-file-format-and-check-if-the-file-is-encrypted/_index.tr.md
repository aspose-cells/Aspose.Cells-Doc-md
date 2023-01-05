---
title: Bir Dosya Formatını Algılama ve Dosyanın Şifreli Olup Olmadığını Kontrol Etme
type: docs
weight: 2000
url: /tr/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 Dosya uzantısı dosya içeriğinin uygun olduğunu garanti etmediğinden, bazen dosyayı açmadan önce biçimini algılamanız gerekir. Dosya şifrelenmiş olabilir (parola korumalı bir dosya), bu nedenle doğrudan okunamaz veya okumamalıyız. Aspose.Cells şunları sağlar:[**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat(java.io.InputStream)statik yöntem ve belgeleri işlemek için kullanabileceğiniz bazı ilgili API'ler.

{{% /alert %}}

## **Java kodu, Dosya Biçimini Tespit Etmek ve Dosyanın Şifreli Olup Olmadığını Kontrol Etmek İçin**

Aşağıdaki örnek kod, bir dosya biçiminin (dosya yolunu kullanarak) nasıl algılanacağını ve uzantısının nasıl kontrol edileceğini gösterir. Dosyanın şifrelenip şifrelenmediğini de belirleyebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}

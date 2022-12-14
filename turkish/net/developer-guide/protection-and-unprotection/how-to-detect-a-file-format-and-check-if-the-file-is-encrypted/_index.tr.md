---
title: Bir Dosya Formatını Algılama ve Dosyanın Şifreli Olup Olmadığını Kontrol Etme
type: docs
weight: 2700
url: /tr/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 Dosya uzantısı dosya içeriğinin uygun olduğunu garanti etmediğinden, bazen dosyayı açmadan önce biçimini algılamanız gerekir. Dosya şifrelenmiş olabilir (parola korumalı bir dosya), bu nedenle doğrudan okunamaz veya okumamalıyız. Aspose.Cells şunları sağlar:[**FileFormatUtil.DetectFileFormat()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) belgeleri işlemek için kullanabileceğiniz statik yöntem ve bazı ilgili API'ler.

{{% /alert %}}

Aşağıdaki örnek kod, bir dosya biçiminin (dosya yolunu kullanarak) nasıl algılanacağını ve uzantısının nasıl kontrol edileceğini gösterir. Dosyanın şifrelenip şifrelenmediğini de belirleyebilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}

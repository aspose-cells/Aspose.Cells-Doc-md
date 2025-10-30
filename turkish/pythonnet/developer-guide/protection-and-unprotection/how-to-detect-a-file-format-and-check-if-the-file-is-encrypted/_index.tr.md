---
title: Bir Dosya Biçimini Algılamak ve Dosyanın Şifreli Olup Olmadığını Kontrol Etme
type: docs
weight: 2700
url: /tr/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

Bazen, dosyanın içeriğinin uygun olup olmadığını garanti etmeyen dosya uzantısına sahip olmasından dolayı, bir dosya açmadan önce biçimini tespit etmeniz gerekir. Dosya şifrelenmiş olabilir (şifre korumalı bir dosya) ya da doğrudan okunmamalıdır. Aspose.Cells for Python via .NET, [**FileFormatUtil.detect_file_format()**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/detect_file_format) statik metodunu ve belge işlemede kullanabileceğiniz bazı ilgili API'leri sağlar.

{{% /alert %}}

Aşağıdaki örnek kod, dosya biçimini (dosya yolu kullanarak) algılamanın ve uzantısını kontrol etmenin nasıl yapıldığını göstermektedir. Ayrıca dosyanın şifreli olup olmadığını belirleyebilirsiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DetectFileFormatAndEncryption.py" >}}

{{< app/cells/assistant language="python-net" >}}

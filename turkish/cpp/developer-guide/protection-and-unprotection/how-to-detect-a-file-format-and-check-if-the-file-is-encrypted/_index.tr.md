---
title: Bir Dosya Formatını Nasıl Tespit Eder ve Dosyanın Şifreli olup olmadığını C++ ile Kontrol Ederiz
linktitle: Bir Dosya Biçimini Algılamak ve Dosyanın Şifreli Olup Olmadığını Kontrol Etme
type: docs
weight: 2700
url: /tr/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Aspose.Cells ile C++ kullanarak dosyanın formatını tespit etmeyi ve şifreli olup olmadığını kontrol etmeyi öğrenin.
---

{{% alert color="primary" %}}

Bazen dosyayı açmadan önce formatını tespit etmeniz gerekir çünkü dosya uzantısı, içeriğin uygun olduğunu garanti etmez. Dosya şifreli olabilir (parola korumalı dosya) veya doğrudan okunamayabilir. Aspose.Cells, belge işlemenize olanak sağlayan [**FileFormatUtil::DetectFileFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) statik yöntemi ve bazı ilgili API'ler sağlar.

{{% /alert %}}

Aşağıdaki örnek kod, dosya biçimini (dosya yolu kullanarak) algılamanın ve uzantısını kontrol etmenin nasıl yapıldığını göstermektedir. Ayrıca dosyanın şifreli olup olmadığını belirleyebilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Detect file format
    FileFormatInfo info = FileFormatUtil::DetectFileFormat(srcDir + u"Book1.xlsx");

    // Gets the detected load format
    std::cout << "The spreadsheet format is: " << FileFormatUtil::LoadFormatToExtension(info.GetLoadFormat()).ToUtf8() << std::endl;

    // Check if the file is encrypted
    std::cout << "The file is encrypted: " << (info.IsEncrypted() ? "true" : "false") << std::endl;

    Aspose::Cells::Cleanup();
}
```

---
title: Hur man upptäcker filformat och kontrollerar om filen är krypterad med C++
linktitle: Hur man upptäcker ett filformat och kontrollerar om filen är krypterad
type: docs
weight: 2700
url: /sv/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Lär dig hur man upptäcker formatet på en fil och kontrollerar om den är krypterad med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Ibland måste du upptäcka filformatet innan du öppnar det eftersom filändelsen inte garanterar att filens innehåll är lämpligt. Filen kan vara krypterad (lösenordsskyddad fil), så den kan inte läsas direkt, eller så bör vi inte läsa den. Aspose.Cells tillhandahåller den statiska metoden [**FileFormatUtil::DetectFileFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) och några relaterade API:er som du kan använda för att bearbeta dokument.

{{% /alert %}}

Följande exempelkod illustrerar hur man upptäcker ett filformat (med hjälp av filvägen) och kontrollerar dess förlängning. Du kan också avgöra om filen är krypterad.

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
{{< app/cells/assistant language="cpp" >}}

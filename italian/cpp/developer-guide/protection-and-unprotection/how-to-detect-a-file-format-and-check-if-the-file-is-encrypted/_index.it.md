---
title: Come rilevare il formato di un file e verificare se il file è criptato con C++
linktitle: Come individuare un formato di file e verificare se il file è criptato
type: docs
weight: 2700
url: /it/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Impara come rilevare il formato di un file e verificare se è criptato usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A volte è necessario rilevare il formato di un file prima di aprirlo perché l'estensione del file non garantisce che il contenuto del file sia appropriato. Il file potrebbe essere criptato (protetto da password) quindi non può essere letto direttamente, o non dovremmo leggerlo. Aspose.Cells fornisce il metodo statico [**FileFormatUtil::DetectFileFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) e alcune API correlate che puoi usare per elaborare i documenti.

{{% /alert %}}

Il seguente codice di esempio illustra come individuare un formato di file (utilizzando il percorso del file) e verificare la sua estensione. È anche possibile determinare se il file è criptato.

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

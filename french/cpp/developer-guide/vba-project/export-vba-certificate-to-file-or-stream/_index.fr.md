---
title: Exporter le certificat VBA vers un fichier ou un flux avec C++
linktitle: Exporter le certificat VBA dans un fichier ou un flux
type: docs
weight: 90
url: /fr/cpp/export-vba-certificate-to-file-or-stream/
description: Apprenez comment exporter un certificat numérique VBA vers un fichier ou un flux mémoire en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'exporter le certificat numérique VBA vers un flux tel qu'un fichier ou un flux mémoire. Vous pouvez accéder aux données brutes du certificat numérique VBA en utilisant la propriété [**Workbook.GetCertRawData()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getcertrawdata/).

{{% /alert %}}

## **Exporter le certificat VBA vers un fichier ou un flux en C++**

Veuillez consulter le code d'exemple suivant qui enregistre les données brutes du certificat VBA dans un fichier. Vous pouvez télécharger le [fichier Excel d'exemple utilisé dans ce code](5115031.xlsm) à partir du lien fourni.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleVBAProjectSigned.xlsm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Retrieve bytes data of Digital Certificate of VBA Project
    Vector<uint8_t> certBytes = workbook.GetVbaProject().GetCertRawData();

    // Save Certificate Data into FileStream
    U16String outputFilePath = outDir + u"Cert_out_";
    std::ofstream outFile(outputFilePath.ToUtf8(), std::ios::binary);
    if (outFile.is_open())
    {
        outFile.write(reinterpret_cast<const char*>(certBytes.GetData()), certBytes.GetLength());
        outFile.close();
    }

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}

---
title: Comment détecter un format de fichier et vérifier si le fichier est crypté avec C++
linktitle: Comment détecter un format de fichier et vérifier si le fichier est chiffré
type: docs
weight: 2700
url: /fr/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Apprenez comment détecter le format d un fichier et vérifier s il est crypté à l aide d Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Parfois, vous devez détecter le format d'un fichier avant de l'ouvrir parce que l'extension du fichier ne garantit pas que le contenu est approprié. Le fichier pourrait être crypté (un fichier protégé par mot de passe), ce qui empêche sa lecture directe, ou nous ne devrions pas le lire. Aspose.Cells fournit la méthode statique [**FileFormatUtil::DetectFileFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) et quelques API pertinentes que vous pouvez utiliser pour traiter les documents.

{{% /alert %}}

L'exemple de code suivant illustre comment détecter un format de fichier (en utilisant le chemin du fichier) et vérifier son extension. Vous pouvez également déterminer si le fichier est chiffré.

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

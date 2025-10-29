---
title: Enregistrer le fichier dans l objet de réponse avec C++
linktitle: Enregistrement du fichier dans l objet de réponse
type: docs
weight: 50
url: /fr/cpp/saving-file-to-response-object/
description: Apprenez comment enregistrer des fichiers dynamiquement et les envoyer directement au navigateur d un client en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells permet de manipuler des fichiers. Cet article explique les différentes façons de sauvegarder des fichiers dans un objet de réponse.

{{% /alert %}}

## **Enregistrer le fichier dans l'objet Response**

Il est également possible de générer un fichier dynamiquement et de l'envoyer directement vers un navigateur client. Pour ce faire, utilisez une version surchargée spéciale de la méthode [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) qui accepte les paramètres suivants:

- Objet **HttpResponse**.
- Nom du fichier.
- [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/), le type de disposition de contenu du fichier de sortie.
- [**SaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/saveoptions/), le type de format de fichier.

L'énumération [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/) détermine si le fichier envoyé au navigateur fournit l'option de s'ouvrir directement dans le navigateur ou dans une application associée à .xls/.xlsx ou une autre extension.

L'énumération contient les types de sauvegarde prédéfinis suivants :

|**Type**|**Description**|
| :- | :- |
|Pièce jointe|Envoie la feuille de calcul au navigateur et l'ouvre dans une application en tant que pièce jointe associée à .xls/.xlsx ou autres extensions.|
|Incorporée|Envoie le document au navigateur et offre la possibilité de sauvegarder la feuille de calcul sur le disque ou l'ouvrir dans le navigateur.|

### **Fichiers XLS**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Save in Excel2003 XLS format
    U16String outputPath = outDir + u"output.xls";
    XlsSaveOptions saveOptions;
    workbook.Save(outputPath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Fichiers XLSX**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook;

    // Save in Xlsx format
    OoxmlSaveOptions saveOptions;
    workbook.Save(outputFilePath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Fichiers PDF**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of output PDF file
    U16String outputPdf = outDir + u"output.pdf";

    // Creating a Workbook object
    Workbook workbook;

    // Save in Pdf format
    PdfSaveOptions saveOptions;
    workbook.Save(outputPdf, saveOptions);

    Aspose::Cells::Cleanup();
}
```

### **Remarque**

En raison de l'objet "System.Web.HttpResponse" qui n'est pas inclus dans .NET5 et .Netstandard,
Cette fonction n'existe donc pas dans la version Aspose.Cells .NET5 et .Netstandard, vous pouvez vous référer au code suivant pour sauvegarder le fichier dans le flux, puis effectuer l'opération sur le flux.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}

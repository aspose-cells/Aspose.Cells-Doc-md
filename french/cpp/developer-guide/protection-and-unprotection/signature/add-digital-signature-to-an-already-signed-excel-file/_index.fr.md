---
title: Ajouter une signature numérique à un fichier Excel déjà signé avec C++
linktitle: Ajouter une signature numérique à un fichier Excel déjà signé
type: docs
weight: 20
url: /fr/cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Apprenez comment ajouter des signatures numériques à des fichiers Excel signés en utilisant Aspose.Cells for C++. Maintenez l intégrité du document avec plusieurs signatures.
keywords: Ajouter une signature numérique à un fichier Excel déjà signé, signatures numériques C++, sécurité du document Excel
---

## **Scénarios d'utilisation possibles**

Aspose.Cells fournit la méthode [**Workbook::AddDigitalSignature(DigitalSignatureCollectionPtr digitalSignatureCollection)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) pour ajouter des signatures numériques à des fichiers Excel déjà signés.

{{% alert color="primary" %}}

Veuillez noter qu'en ajoutant une signature numérique à un document Excel déjà signé : si le document original a été généré par Aspose.Cells, cela fonctionne correctement. Cependant, si le document a été créé par d'autres moteurs (par exemple Microsoft Excel), Aspose.Cells for C++ ne pourra pas préserver la structure exacte du fichier après chargement et enregistrement, ce qui peut invalider les signatures existantes.

{{% /alert %}}

## **Comment ajouter une signature numérique à un fichier Excel déjà signé**

L'extrait de code suivant montre comment utiliser [**Workbook::AddDigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) pour ajouter des signatures numériques à des fichiers Excel signés. Le [fichier Excel d'exemple](50528280.xlsx) est pré-signé. Le [fichier de sortie](50528281.xlsx) montre le résultat. Nous utilisons un certificat de démonstration [AsposeDemo.pfx](50528279.pfx) avec le mot de passe **aspose**.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Certificate and workbook paths
    U16String certFilePath = srcDir + u"AsposeDemo.pfx";
    U16String inputFilePath = srcDir + u"sampleDigitallySignedByCells.xlsx";
    U16String outputFilePath = outDir + u"outputDigitallySignedByCells.xlsx";

    // Load digitally signed workbook
    Workbook workbook(inputFilePath);

    // Create digital signature collection
    DigitalSignatureCollection dsCollection;

    // Create digital signature using PFX certificate
    U16String password = u"aspose";
    U16String comments = u"Aspose.Cells added new digital signature in existing digitally signed workbook.";
    DigitalSignature signature(certFilePath, password, comments, Date());

    // Add signature to collection
    dsCollection.Add(signature);

    // Apply digital signatures to workbook
    workbook.AddDigitalSignature(dsCollection);

    // Save modified workbook
    workbook.Save(outputFilePath);

    std::cout << "Digital signature added successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}

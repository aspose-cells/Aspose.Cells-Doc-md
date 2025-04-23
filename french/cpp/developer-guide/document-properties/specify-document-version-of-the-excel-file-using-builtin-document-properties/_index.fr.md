---
title: Spécifier la version du document Excel à l aide des propriétés de document intégrées en C++
linktitle: Spécifier la version du document
type: docs
weight: 20
url: /fr/cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Apprenez comment spécifier la version d un fichier Excel en utilisant les propriétés de document intégrées avec Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez modifier le **Numéro de version** d'un fichier Excel en cliquant avec le bouton droit sur le fichier, en sélectionnant Propriétés > Détails, puis en modifiant le champ **Numéro de version**. Utilisez la propriété [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/) pour le changer de manière programmatique avec les API Aspose.Cells.

## **Spécifier la version du document du fichier Excel à l'aide des propriétés de document intégrées**

Le code d'exemple suivant crée un classeur et modifie ses propriétés de document intégrées, notamment Titre, Auteurs et Numéro de version. Veuillez consulter le [fichier Excel de sortie](64716811.xlsx) généré par le code et la capture d'écran qui montre la modification du numéro de version avec la propriété [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Properties;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access built-in document property collection
    BuiltInDocumentPropertyCollection bdpc = wb.GetBuiltInDocumentProperties();

    // Set the title
    bdpc.SetTitle(u"Aspose File Format APIs");

    // Set the author
    bdpc.SetAuthor(u"Aspose APIs Developers");

    // Set the document version
    bdpc.SetDocumentVersion(u"Aspose.Cells Version - 18.3");

    // Save the workbook in xlsx format
    wb.Save(u"outputSpecifyDocumentVersionOfExcelFile.xlsx", SaveFormat::Xlsx);

    std::cout << "Document properties set and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

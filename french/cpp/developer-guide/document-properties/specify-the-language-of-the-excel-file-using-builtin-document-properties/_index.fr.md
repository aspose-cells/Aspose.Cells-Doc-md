---
title: Spécifier la langue du fichier Excel en utilisant les propriétés de document intégrées avec C++
linktitle: Spécifier la langue du fichier Excel
type: docs
weight: 30
url: /fr/cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
description: Apprenez comment changer la langue d un fichier Excel de manière programmatique en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez changer la langue d'un fichier Excel en cliquant avec le bouton droit sur le fichier, en sélectionnant Propriétés > Détails, puis en modifiant le champ Langue. Utilisez la propriété [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/) pour le changer de manière programmatique avec les API Aspose.Cells.

## **Spécifier la langue du fichier Excel en utilisant les propriétés de document intégrées**

Le code d'exemple suivant crée un classeur et modifie sa propriété de document intégrée nommée Langue. Veuillez voir le [fichier Excel de sortie](64716891.xlsx) généré par le code et la capture d'écran montrant le champ Langue modifié par la propriété [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Code d'exemple**

```c++
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

    // Set the language of the Excel file
    bdpc.SetLanguage(u"German, French");

    // Save the workbook in xlsx format
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx", SaveFormat::Xlsx);

    std::cout << "Language set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

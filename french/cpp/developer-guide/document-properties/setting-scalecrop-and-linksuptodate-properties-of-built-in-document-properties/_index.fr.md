---
title: Définir les propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées avec C++
linktitle: Définir les propriétés ScaleCrop et LinksUpToDate
type: docs
weight: 320
url: /fr/cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Apprenez comment définir les propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**
[GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) et [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) sont deux propriétés étendues intégrées définies dans le format OpenXml. Leur usage est le suivant :

## **1) ScaleCrop**
Cet élément indique le mode d'affichage de la vignette du document. Définissez cet élément sur **TRUE** pour activer le redimensionnement de la vignette du document à l'affichage. Définissez cet élément sur **FALSE** pour activer le rognage de la vignette du document afin de montrer uniquement les sections qui s'adaptent à l'affichage.

Les valeurs possibles pour cet élément sont définies par le type de données booléen du schéma XML W3C.

## **2) LinksUpToDate**
Cet élément indique si les hyperliens dans un document sont à jour. Définissez cet élément sur **TRUE** pour indiquer que les hyperliens sont mis à jour. Définissez cet élément sur **FALSE** pour indiquer que les hyperliens sont obsolètes.

Les valeurs possibles pour cet élément sont définies par le type de données booléen du schéma XML W3C.

## **Capture d'écran montrant ces propriétés dans le fichier app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Définir les propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées**
Le code d'exemple suivant définit les propriétés intégrées étendues [GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) et [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) du classeur. Veuillez vérifier le fichier Excel de sortie [généré avec ce code](5115500.xlsx), le changer en extension .zip, en extraire le contenu et voir le fichier app.xml comme indiqué dans la capture d'écran ci-dessus.

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

    // Instantiating a Workbook object.
    Workbook workbook;

    // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
    workbook.GetBuiltInDocumentProperties().SetScaleCrop(true);
    workbook.GetBuiltInDocumentProperties().SetLinksUpToDate(true);

    // Saving the Excel file.
    workbook.Save(outDir + u"output.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}

---
title: Utiliser des parties XML personnalisées dans Aspose.Cells avec C++
linktitle: Utiliser des parties XML personnalisées
type: docs
weight: 390
url: /fr/cpp/use-custom-xml-parts-in-aspose-cells/
description: Apprenez à utiliser programmatique­ment les parties XML personnalisées dans les fichiers Excel en utilisant Aspose.Cells avec C++.
---

## Utilisation de parties XML personnalisées dans Aspose.Cells

Les parties XML personnalisées sont des données XML stockées par différentes applications comme SharePoint à l'intérieur d'un fichier Excel. Ces données sont consommées par diverses applications qui en ont besoin. Microsoft Excel n'utilise pas ces données, il n'y a donc pas d'interface graphique pour les ajouter. Vous pouvez voir ces données en changeant l'extension de **.xlsx** en **.zip** puis en l'ouvrant avec **WinZip**. Vous pouvez également ouvrir le fichier ZIP avec tout utilitaire tiers comme WinRAR ou WinZip. Les données se trouvent dans le dossier **customXml**.

Vous pouvez ajouter des parties XML personnalisées en utilisant Aspose.Cells via la méthode [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/).

Le code d'exemple suivant utilise la méthode [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) pour ajouter le **Book Catalog XML**, dont le nom est **BookStore**. L'image suivante montre le résultat de ce code. Comme vous pouvez le voir, le Book Catalog XML est ajouté à l'intérieur du nœud BookStore, qui est le nom de cette propriété.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Code C++ pour utiliser les parties XML personnalisées

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

    // The sample XML that will be injected to Workbook
    U16String booksXML = uR"(<catalog>
   <book>
      <title>Complete C#</title>
      <price>44</price>
   </book>
   <book>
      <title>Complete Java</title>
      <price>76</price>
   </book>
   <book>
      <title>Complete SharePoint</title>
      <price>55</price>
   </book>
   <book>
      <title>Complete PHP</title>
      <price>63</price>
   </book>
   <book>
      <title>Complete VB.NET</title>
      <price>72</price>
   </book>
</catalog>)";

    // Create an instance of Workbook class
    Workbook workbook;

    // Add Custom XML Part to ContentTypePropertyCollection
    workbook.GetContentTypeProperties().Add(u"BookStore", booksXML);

    // Save the resultant spreadsheet
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Custom XML part added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Article connexe

- [Ajout de propriétés personnalisées visibles dans le panneau d'informations du document](/cells/fr/cpp/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="cpp" >}}

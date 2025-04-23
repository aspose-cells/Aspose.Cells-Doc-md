---
title: Ajout de propriétés personnalisées visibles dans le panneau d informations sur le document avec C++
linktitle: Ajout de propriétés personnalisées visibles dans le volet Informations sur le document
type: docs
weight: 300
url: /fr/cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Apprenez comment ajouter des propriétés personnalisées visibles dans le panneau d informations sur le document en utilisant Aspose.Cells avec C++.
---

## **Ajout de propriétés personnalisées visibles dans le volet Informations sur le document**

Aspose.Cells peut être utilisé pour ajouter des propriétés personnalisées à l'intérieur de l'objet classeur qui sont visibles dans le volet Informations sur le document. Vous pouvez ouvrir le volet Informations sur le document dans Microsoft Excel en utilisant les commandes du menu Fichier > Infos > Propriétés > Afficher le volet Document.

Veuillez utiliser la méthode [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) pour ajouter une propriété personnalisée qui sera visible dans le Panneau d'informations sur le document.

Le code d'exemple suivant ajoute deux propriétés personnalisées. La première propriété n'a pas de type, et la seconde a un type DateTime. Une fois que vous ouvrez le fichier Excel généré par ce code, vous verrez ces deux propriétés dans le Panneau d'informations sur le document.

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

    // Create workbook object with specified format
    Workbook workbook(FileFormatType::Xlsx);

    // Add simple property without any type
    workbook.GetContentTypeProperties().Add(u"MK31", u"Simple Data");

    // Add date time property with type
    workbook.GetContentTypeProperties().Add(u"MK32", u"04-Mar-2015", u"DateTime");

    // Save the workbook
    workbook.Save(srcDir + u"AddingCustomPropertiesVisible_out.xlsx");

    std::cout << "Custom properties added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Article connexe**

{{% alert color="primary" %}}

- [Utiliser des parties XML personnalisées dans Aspose.Cells](/cells/fr/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}

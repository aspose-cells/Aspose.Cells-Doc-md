---
title: Ajout de propriétés personnalisées visibles dans le panneau d informations du document avec Node.js via C++
linktitle: Ajout de propriétés personnalisées visibles dans le volet Informations sur le document
type: docs
weight: 300
url: /fr/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Apprenez à ajouter des propriétés personnalisées à un objet classeur en utilisant Aspose.Cells for Node.js via C++. Ces propriétés peuvent être visualisées dans le Panneau d informations sur le document.
---

## **Ajout de propriétés personnalisées visibles dans le volet Informations sur le document**

Aspose.Cells for Node.js via C++ peut être utilisé pour ajouter des propriétés personnalisées à l'intérieur de l'objet classeur qui sont visibles dans le Panneau d'informations sur le document. Vous pouvez ouvrir le Panneau d'informations sur le document dans Microsoft Excel via Fichier > Infos > Propriétés > Afficher le panneau du document.

Veuillez utiliser la méthode [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/#add-string-string-) pour ajouter une propriété personnalisée qui sera visible dans le Panneau d'informations sur le document.

Le code d'exemple suivant ajoute deux propriétés personnalisées. La première propriété n'a pas de type, et la seconde a un type DateTime. Une fois que vous ouvrez le fichier Excel généré par ce code, vous verrez ces deux propriétés dans le Panneau d'informations sur le document.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Add simple property without any type
workbook.getContentTypeProperties().add("MK31", "Simple Data");

// Add date time property with type
workbook.getContentTypeProperties().add("MK32", "04-Mar-2015", "DateTime");

// Save the workbook
workbook.save(path.join(dataDir, "AddingCustomPropertiesVisible_out.xlsx"));
```

### **Article connexe**

{{% alert color="primary" %}}

- [Utiliser des parties XML personnalisées dans Aspose.Cells](/cells/fr/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}

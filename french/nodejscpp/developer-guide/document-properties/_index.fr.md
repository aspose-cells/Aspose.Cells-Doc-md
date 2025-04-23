---
title: Gérer les propriétés du document avec Node.js via C++
linktitle: Propriétés de document
type: docs
weight: 80
url: /fr/nodejs-cpp/managing-document-properties/
description: Apprenez à gérer les propriétés du document via les API Aspose.Cells for Node.js via C++.
keywords: Comment gérer les propriétés du document en Node.js via C++, obtenir ou définir des propriétés de document en utilisant Node.js via C++, ajouter ou supprimer des propriétés de document via Node.js via C++, insérer ou supprimer des propriétés de document avec Node.js via C++, comment accéder aux propriétés du document en utilisant les API Aspose.Cells for Node.js via C++.
---


## **Introduction**

Microsoft Excel permet d'ajouter des propriétés aux fichiers de feuille de calcul. Ces propriétés de document fournissent des informations utiles et sont divisées en 2 catégories comme détaillé ci-dessous.

- Propriétés système définies (intégrées) : Les propriétés intégrées contiennent des informations générales sur le document telles que le titre du document, le nom de l'auteur, les statistiques du document, etc.
- Propriétés utilisateur définies (personnalisées) : Propriétés personnalisées définies par l'utilisateur final sous forme de paire nom-valeur.

{{% alert color="primary" %}}

Le point le plus important à savoir sur les propriétés intégrées et personnalisées est que les propriétés intégrées peuvent être consultées et modifiées, mais pas créées ou supprimées. Cependant, les propriétés personnalisées peuvent être créées et gérées.

{{% /alert %}}

## **Comment gérer les propriétés de document à l'aide de Microsoft Excel**

Microsoft Excel permet de gérer les propriétés du document des fichiers Excel de manière WYSIWYG. Veuillez suivre les étapes ci-dessous pour ouvrir la boîte de dialogue **Propriétés** dans Excel 2016.

1. Dans le menu **Fichier**, sélectionnez **Infos**.

|**Sélection du menu Infos**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. Cliquez sur le titre **Propriétés** et sélectionnez "Propriétés avancées".

|**Cliquez pour sélectionner les propriétés avancées**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Gérez les propriétés de document du fichier.

|**Boîte de dialogue des propriétés**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
Dans la boîte de dialogue des propriétés, il y a différents onglets, comme Général, Résumé, Statistiques, Contenu et Personnalisés. Chaque onglet aide à configurer différents types d'informations liées au fichier. L'onglet Personnalisé est utilisé pour gérer les propriétés personnalisées.

## **Comment travailler avec les propriétés de document à l'aide d'Aspose.Cells**

Les développeurs peuvent gérer dynamiquement les propriétés de document à l'aide des API Aspose.Cells. Cette fonctionnalité aide les développeurs à stocker des informations utiles avec le fichier, telles que la date de réception du fichier, le traitement, l'horodatage, etc.

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ écrit directement les informations sur l'API et le numéro de version dans les documents de sortie. Par exemple, lors de la conversion d'un document en PDF, Aspose.Cells for Node.js via C++ remplit le champ **Application** avec la valeur 'Aspose.Cells' et le champ **PDF Producer** avec la valeur, par exemple 'Aspose.Cells v17.9'.

Veuillez noter que vous ne pouvez pas demander à Aspose.Cells for Node.js via C++ de modifier ou supprimer ces informations des documents de sortie.

{{% /alert %}}

### **Comment accéder aux propriétés de document**

Les API Aspose.Cells supportent les deux types de propriétés de document, intégrées et personnalisées. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) de Aspose.Cells représente un fichier Excel et, comme un fichier Excel, la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) peut contenir plusieurs feuilles, chacune représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) tandis que la collection de feuilles est représentée par la classe [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection).

Utiliser [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) pour accéder aux propriétés du document du fichier comme décrit ci-dessous.

- Pour accéder aux propriétés de document intégrées, utilisez [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--).
- Pour accéder aux propriétés de document personnalisées, utilisez [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--).

Les deux, [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--) et [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--), renvoient l'instance de [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/). Cette collection contient [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) objets, chacun représentant une propriété de document intégrée ou personnalisée.

Il appartient à l'application de déterminer comment accéder à une propriété, c'est-à-dire en utilisant l'index ou le nom de la propriété à partir de [**DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/) comme illustré ci-dessous.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property by using the property name
const customProperty1 = customProperties.get("ContentTypeId");
console.log(`${customProperty1.getName()} ${customProperty1.getValue()}`);

// Accessing the same custom document property by using the property index
const customProperty2 = customProperties.get(0);
console.log(`${customProperty2.getName()} ${customProperty2.getValue()}`);
```

La classe [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) permet de récupérer le nom, la valeur et le type de la propriété du document :

- Pour obtenir le nom de la propriété, utilisez [**DocumentProperty.getName()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getName--).
- Pour obtenir la valeur de la propriété, utilisez [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--) retourne la valeur sous forme d'un Objet.
- Pour obtenir le type de la propriété, utilisez [**DocumentProperty.getType()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getType--). Cela retourne une des valeurs d'énumération de [**PropertyType**](https://reference.aspose.com/cells/nodejs-cpp/propertytype/). Après avoir obtenu le type de propriété, utilisez l'une des méthodes **DocumentProperty.ToXXX** pour obtenir la valeur du type approprié au lieu d'utiliser [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). Les méthodes **DocumentProperty.ToXXX** sont décrites dans le tableau ci-dessous.

{{% alert color="primary" %}}

La classe [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) fournit également un ensemble de méthodes qui retournent les valeurs d'autres types de données.

{{% /alert %}}

|**Nom du membre**|**Description**|**Méthode ToXXX**|
| :- | :- | :- |
|Boolean|Le type de données de la propriété est Boolean|ToBool|
|Date|Le type de données de la propriété est DateTime. Notez que Microsoft Excel ne stocke que la partie date, aucune heure ne peut être stockée dans une propriété personnalisée de ce type|ToDateTime|
|Float|Le type de données de la propriété est Double|ToDouble|
|Number|Le type de données de la propriété est Int32|ToInt|
|String| Le type de donnée de la propriété est string|ToString|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property
const customProperty1 = customProperties.get(0);

// Storing the value of the document property as an object
const objectValue = customProperty1.getValue();

// Accessing a custom document property
const customProperty2 = customProperties.get(1);

// Checking the type of the document property and then storing the value of the
// document property according to that type
if (customProperty2.getType() === AsposeCells.PropertyType.String) {
const value = customProperty2.getValue().toString();
console.log(`${customProperty2.getName()} : ${value}`);
}
```

### **Comment ajouter ou supprimer des propriétés de document personnalisées**

Comme nous l'avons décrit précédemment au début de ce sujet, les développeurs ne peuvent pas ajouter ou supprimer des propriétés intégrées car ces propriétés sont système-définies, mais il est possible d'ajouter ou de supprimer des propriétés personnalisées car celles-ci sont définies par l'utilisateur.

### **Comment ajouter des propriétés personnalisées**

Les API Aspose.Cells ont exposé la méthode [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) pour la classe [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/) afin d'ajouter des propriétés personnalisées à la collection. La méthode [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) ajoute la propriété au fichier Excel et retourne une référence à la nouvelle propriété de document sous forme d'objet [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Adding a custom document property to the Excel file
customProperties.add("Publisher", "Aspose");

// Saving resultant spreadsheet
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **Comment configurer la propriété de document personnalisée “Lien vers le contenu”**

Pour créer une propriété personnalisée liée au contenu d'une plage donnée, appelez la méthode [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) en passant le nom de la propriété et la source. Vous pouvez vérifier si une propriété est configurée comme liée au contenu en utilisant la propriété [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#isLinkedToContent--). De plus, il est également possible d'obtenir la plage source en utilisant la propriété [**getSource()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getSource--) de la classe [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/).

Nous utilisons un fichier modèle Microsoft Excel simple dans l'exemple. Le classeur a une plage nommée définie étiquetée **MyRange** qui fait référence à une valeur de cellule.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate an object of Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getWorksheets().getCustomDocumentProperties();

// Add link to content.
customProperties.addLinkToContent("Owner", "MyRange");

// Accessing the custom document property by using the property name
const customProperty1 = customProperties.get("Owner");

// Check whether the property is linked to content
const isLinkedToContent = customProperty1.isLinkedToContent();

// Get the source for the property
const source = customProperty1.getSource();

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **Comment supprimer des propriétés personnalisées**

Pour supprimer des propriétés personnalisées avec Aspose.Cells, appelez la méthode [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/#remove-string-) et transmettez le nom de la propriété du document à supprimer.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Removing a custom document property
customProperties.remove("Publisher");

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

## **Sujets avancés**
- [Ajout de propriétés personnalisées visibles dans le volet Informations sur le document](/cells/fr/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Définition des propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées.](/cells/fr/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Spécifier la version du document du fichier Excel à l'aide des propriétés de document intégrées](/cells/fr/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Spécifier la langue du fichier Excel en utilisant les propriétés de document intégrées](/cells/fr/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

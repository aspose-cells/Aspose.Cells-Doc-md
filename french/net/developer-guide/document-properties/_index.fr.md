---
title: Gérer les propriétés de document
linktitle: Propriétés de document
type: docs
weight: 80
url: /fr/net/managing-document-properties/
description: Apprenez à gérer les propriétés de document via les API Aspose.Cells for NET.
keywords: Comment gérer les propriétés de document en C#, Obtenir ou définir les propriétés de document en utilisant C#, Ajouter ou supprimer des propriétés de document via C#, Insérer ou supprimer des propriétés de document avec C#, Comment accéder aux propriétés de document en utilisant les API Aspose.Cells for NET.
---


## **Introduction**

Microsoft Excel permet d'ajouter des propriétés aux fichiers de feuille de calcul. Ces propriétés de document fournissent des informations utiles et sont divisées en 2 catégories comme détaillé ci-dessous.

- Propriétés système définies (intégrées) : Les propriétés intégrées contiennent des informations générales sur le document telles que le titre du document, le nom de l'auteur, les statistiques du document, etc.
- Propriétés utilisateur définies (personnalisées) : Propriétés personnalisées définies par l'utilisateur final sous forme de paire nom-valeur.

{{% alert color="primary" %}}

Le point le plus important à savoir sur les propriétés intégrées et personnalisées est que les propriétés intégrées peuvent être consultées et modifiées, mais pas créées ou supprimées. Cependant, les propriétés personnalisées peuvent être créées et gérées.

{{% /alert %}}

## **Comment gérer les propriétés de document à l'aide de Microsoft Excel**

Microsoft Excel vous permet de gérer les propriétés de document des fichiers Excel de manière WYSIWYG. Veuillez suivre les étapes ci-dessous pour ouvrir la boîte de dialogue **Propriétés** dans Excel 2016.

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

Aspose.Cells for .NET écrit directement les informations sur l'API et le numéro de version dans les documents de sortie. Par exemple, lors du rendu du document au format PDF, Aspose.Cells for .NET remplit le champ **Application** avec la valeur 'Aspose.Cells' et le champ **Producteur PDF** avec la valeur, par exemple, 'Aspose.Cells v17.9'.

Veuillez noter que vous ne pouvez pas demander à Aspose.Cells for .NET de modifier ou supprimer ces informations des documents de sortie.

{{% /alert %}}

### **Comment accéder aux propriétés de document**

Les API Aspose.Cells prennent en charge les deux types de propriétés de document, intégrées et personnalisées. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) d'Aspose.Cells représente un fichier Excel et, comme un fichier Excel, la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) peut contenir plusieurs feuilles de calcul, chacune représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet), tandis que la collection de feuilles de calcul est représentée par la classe [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection).

Utilisez [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) pour accéder aux propriétés de document du fichier comme décrit ci-dessous.

- Pour accéder aux propriétés de document intégrées, utilisez [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
- Pour accéder aux propriétés de document personnalisées, utilisez [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

Les méthodes [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) et [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) renvoient l'instance de [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Cette collection contient [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) objets, chacun représentant une seule propriété de document intégrée ou personnalisée.

Il appartient à l'exigence de l'application de savoir comment accéder à une propriété, c'est-à-dire; en utilisant l'index ou le nom de la propriété de [**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection) comme démontré dans l'exemple ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

La classe [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) permet de récupérer le nom, la valeur et le type de la propriété du document:

- Pour obtenir le nom de la propriété, utilisez [**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
- Pour obtenir la valeur de la propriété, utilisez [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) renvoie la valeur en tant qu'objet.
- Pour obtenir le type de propriété, utilisez [**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type). Cela renvoie l'une des valeurs d'énumération [**PropertyType**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype). Après avoir obtenu le type de propriété, utilisez l'une des méthodes **DocumentProperty.ToXXX** pour obtenir la valeur du type approprié au lieu d'utiliser [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). Les méthodes **DocumentProperty.ToXXX** sont décrites dans le tableau ci-dessous.

{{% alert color="primary" %}}

La classe [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) fournit également un ensemble de méthodes qui renvoient les valeurs d'autres types de données.

{{% /alert %}}

|**Nom du membre**|**Description**|**Méthode ToXXX**|
| :- | :- | :- |
|Boolean|Le type de données de la propriété est Boolean|ToBool|
|Date|Le type de données de la propriété est DateTime. Notez que Microsoft Excel ne stocke que la partie date, aucune heure ne peut être stockée dans une propriété personnalisée de ce type|ToDateTime|
|Float|Le type de données de la propriété est Double|ToDouble|
|Number|Le type de données de la propriété est Int32|ToInt|
|String|Le type de données de la propriété est String|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **Comment ajouter ou supprimer des propriétés de document personnalisées**

Comme nous l'avons décrit précédemment au début de ce sujet, les développeurs ne peuvent pas ajouter ou supprimer des propriétés intégrées car ces propriétés sont système-définies, mais il est possible d'ajouter ou de supprimer des propriétés personnalisées car celles-ci sont définies par l'utilisateur.

### **Comment ajouter des propriétés personnalisées**

Les API Aspose.Cells ont exposé la méthode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) pour la classe [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) afin d'ajouter des propriétés personnalisées à la collection. La méthode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) ajoute la propriété au fichier Excel et renvoie une référence pour la nouvelle propriété de document en tant qu'objet [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **Comment configurer la propriété de document personnalisée “Lien vers le contenu”**

Pour créer une propriété personnalisée liée au contenu d'une plage donnée, appelez la méthode [**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) et passez le nom de la propriété et la source. Vous pouvez vérifier si une propriété est configurée comme étant liée au contenu en utilisant la propriété [**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent). De plus, il est également possible d'obtenir la plage source en utilisant la propriété [**Source**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) de la classe [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty).

Nous utilisons un fichier modèle Microsoft Excel simple dans l'exemple. Le classeur a une plage nommée définie étiquetée **MyRange** qui fait référence à une valeur de cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **Comment supprimer des propriétés personnalisées**

Pour supprimer des propriétés personnalisées à l'aide d'Aspose.Cells, appelez la méthode [**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove) et transmettez le nom de la propriété du document à supprimer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **Sujets avancés**
- [Ajout de propriétés personnalisées visibles dans le volet Informations sur le document](/cells/fr/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Définition des propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées.](/cells/fr/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Spécifier la version du document du fichier Excel à l'aide des propriétés de document intégrées](/cells/fr/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Spécifier la langue du fichier Excel en utilisant les propriétés de document intégrées](/cells/fr/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

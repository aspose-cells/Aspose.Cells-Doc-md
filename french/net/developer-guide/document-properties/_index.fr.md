---
title: Gérer les propriétés du document
linktitle: Propriétés du document
type: docs
weight: 80
url: /fr/net/managing-document-properties/
description: Gérez les propriétés de document des fichiers de feuille de calcul.
---
## **Introduction**

Microsoft Excel offre la possibilité d'ajouter des propriétés aux fichiers de feuille de calcul. Ces propriétés de document fournissent des informations utiles et sont divisées en 2 catégories comme détaillé ci-dessous.

- Propriétés définies par le système (intégrées) : les propriétés intégrées contiennent des informations générales sur le document telles que le titre du document, le nom de l'auteur, les statistiques du document, etc.
- Propriétés définies par l'utilisateur (personnalisées) : propriétés personnalisées définies par l'utilisateur final sous la forme d'une paire nom-valeur.

{{% alert color="primary" %}}

Le point le plus important à savoir sur les propriétés intégrées et personnalisées est que les propriétés intégrées peuvent être consultées et modifiées, mais pas créées ou supprimées. Cependant, des propriétés personnalisées peuvent être créées et gérées.

{{% /alert %}}

## **Gestion des propriétés du document à l'aide de Microsoft Excel**

 Microsoft Excel vous permet de gérer les propriétés de document des fichiers Excel de manière WYSIWYG. Veuillez suivre les étapes ci-dessous pour ouvrir le**Propriétés** boîte de dialogue dans Excel 2016.

1.  Du**Dossier** menu, sélectionnez**Info**.

|**Sélection du menu d'informations**|
|:- |
|![tâche : image_autre_texte](managing-document-properties_1.png)|
1.  Cliquer sur**Propriétés** rubrique et sélectionnez "Propriétés avancées".

|**Cliquer sur la sélection des propriétés avancées**|
|:- |
|![tâche : image_autre_texte](managing-document-properties_2.png)|
1. Gérer les propriétés de document du fichier.

|**Boîte de dialogue Propriétés**|
|:- |
|![tâche : image_autre_texte](managing-document-properties_3.png)|
Dans la boîte de dialogue Propriétés, il existe différents onglets, tels que Général, Résumé, Statistiques, Contenu et Personnalisés. Chaque onglet permet de configurer différents types d'informations relatives au fichier. L'onglet Personnalisé est utilisé pour gérer les propriétés personnalisées.

## **Utilisation des propriétés du document à l'aide de Aspose.Cells**

Les développeurs peuvent gérer dynamiquement les propriétés du document à l'aide des API Aspose.Cells. Cette fonctionnalité aide les développeurs à stocker des informations utiles avec le fichier, telles que la date de réception, le traitement, l'horodatage, etc.

{{% alert color="primary" %}}

 Aspose.Cells for .NET écrit directement les informations sur API et le numéro de version dans les documents de sortie. Par exemple, lors du rendu du document au format PDF, Aspose.Cells for .NET remplit**Application** champ avec la valeur 'Aspose.Cells' et**Producteur PDF** champ avec la valeur, par exemple 'Aspose.Cells v17.9'.

Veuillez noter que vous ne pouvez pas demander au Aspose.Cells for .NET de modifier ou de supprimer ces informations des documents de sortie.

{{% /alert %}}

### **Accéder aux propriétés du document**

Aspose.Cells Les API prennent en charge les deux types de propriétés de document, intégrées et personnalisées. Aspose.Cells'[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe représente un fichier Excel et, comme un fichier Excel, la[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe peut contenir plusieurs feuilles de calcul, chacune représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe alors que la collection de feuilles de calcul est représentée par la[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)classer.

 Utilisez le[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)pour accéder aux propriétés du document du fichier comme décrit ci-dessous.

-  Pour accéder aux propriétés de document intégrées, utilisez[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  Pour accéder aux propriétés de document personnalisées, utilisez[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 Les deux[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) et[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) renvoie l'instance de[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Cette collection contient[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)objets, chacun représentant une seule propriété de document intégrée ou personnalisée.

 C'est à l'exigence de l'application comment accéder à une propriété, c'est-à-dire; en utilisant l'index ou le nom de la propriété de la[**DocumentPropertyCollectionDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)comme le montre l'exemple ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

 La[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)class permet de récupérer le nom, la valeur et le type de la propriété du document :

-  Pour obtenir le nom de la propriété, utilisez[**DocumentProperty.NameDocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  Pour obtenir la valeur de la propriété, utilisez[**DocumentProperty.ValueDocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.ValueDocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)renvoie la valeur en tant qu'objet.
-  Pour obtenir le type de propriété, utilisez[**DocumentProperty.TypeDocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . Cela renvoie l'un des[**Type de propriété**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype) valeurs d'énumération. Après avoir obtenu le type de propriété, utilisez l'un des**DocumentProperty.ToXXX** méthodes pour obtenir la valeur du type approprié au lieu d'utiliser[**DocumentProperty.ValueDocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) . La**DocumentProperty.ToXXX**méthodes sont décrites dans le tableau ci-dessous.

{{% alert color="primary" %}}

 La[**PropriétéDocument**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)La classe fournit également un ensemble de méthodes qui renvoient les valeurs d'autres types de données.

{{% /alert %}}

|**Nom de membre**|**La description**|**Méthode ToXXX**|
|:- |:- |:- |
|booléen|Le type de données de la propriété est booléen|ToBool|
|Date|Le type de données de la propriété est DateTime. Notez que Microsoft Excel stocke uniquement<br>la partie date, aucune heure ne peut être stockée dans une propriété personnalisée de ce type|ÀDateHeure|
|Flotteur|Le type de données de la propriété est Double|Doubler|
|Numéro|Le type de données de la propriété est Int32|ToInt|
|Chaîne de caractères|Le type de données de la propriété est String|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **Ajout ou suppression de propriétés de document personnalisées**

Comme nous l'avons décrit précédemment au début de cette rubrique, les développeurs ne peuvent pas ajouter ou supprimer des propriétés intégrées car ces propriétés sont définies par le système, mais il est possible d'ajouter ou de supprimer des propriétés personnalisées car elles sont définies par l'utilisateur.

### **Ajout de propriétés personnalisées**

 Aspose.Cells Les API ont exposé le[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) méthode pour la[**CustomDocumentPropertyCollectionCustomDocumentPropertyCollectionCustomDocumentPropertyCollectionCustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) class afin d'ajouter des propriétés personnalisées à la collection. La[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) La méthode ajoute la propriété au fichier Excel et renvoie une référence pour la nouvelle propriété de document en tant que[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)objet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **Configuration de la propriété personnalisée "Lien vers le contenu"**

 Pour créer une propriété personnalisée liée au contenu d'une plage donnée, appelez le[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) méthode et passez le nom de la propriété et la source. Vous pouvez vérifier si une propriété est configurée comme étant liée au contenu à l'aide de la[**DocumentProperty.IsLinkedToContentDocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) propriété. De plus, il est également possible d'obtenir la plage source à l'aide de la[**La source**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) propriété de la[**PropriétéDocument**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)classer.

 Nous utilisons un simple fichier Excel modèle Microsoft dans l'exemple. Le classeur a une plage nommée définie étiquetée**MaPlage** qui fait référence à une valeur de cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **Suppression des propriétés personnalisées**

 Pour supprimer les propriétés personnalisées à l'aide de Aspose.Cells, appelez le[**DocumentPropertyCollection.RemoveDocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)méthode et transmettez le nom de la propriété de document à supprimer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **Sujets avancés**
- [Ajout de propriétés personnalisées visibles dans le panneau Informations sur le document](/cells/fr/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Définition des propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées](/cells/fr/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Spécifiez la version du document du fichier Excel à l'aide des propriétés de document intégrées](/cells/fr/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Spécifiez la langue du fichier Excel à l'aide des propriétés de document intégrées](/cells/fr/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

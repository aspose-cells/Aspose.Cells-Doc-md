---
title: Gérer les propriétés du document
linktitle: Propriétés du document
type: docs
weight: 80
url: /fr/net/managing-document-properties/
description: Découvrez comment gérer les propriétés du document via les API Aspose.Cells pour NET.
keywords: How to Manage Document Properties in C#, Get or Set Document Properties using C#, Add or Delete Document Properties via C#, Insert or Remove Document Properties with C#, How to Access Document Properties using Aspose.Cells for NET APIs.
---
##  **Introduction**

Microsoft Excel offre la possibilité d'ajouter des propriétés aux fichiers de feuilles de calcul. Ces propriétés de document fournissent des informations utiles et sont divisées en 2 catégories comme détaillé ci-dessous.

- Propriétés définies par le système (intégrées) : les propriétés intégrées contiennent des informations générales sur le document telles que le titre du document, le nom de l'auteur, les statistiques du document, etc.
- Propriétés définies par l'utilisateur (personnalisées) : propriétés personnalisées définies par l'utilisateur final sous la forme d'une paire nom-valeur.

{{% alert color="primary" %}}

Le point le plus important à connaître sur les propriétés intégrées et personnalisées est que les propriétés intégrées sont accessibles et modifiables, mais pas créées ou supprimées. Toutefois, des propriétés personnalisées peuvent être créées et gérées.

{{% /alert %}}

##  **Comment gérer les propriétés d'un document à l'aide d'Excel Microsoft**

 Microsoft Excel vous permet de gérer les propriétés des fichiers Excel de manière WYSIWYG. Veuillez suivre les étapes ci-dessous pour ouvrir le**Propriétés** boîte de dialogue dans Excel 2016.

1.  Du**Déposer** menu, sélectionnez *Info**.

|**Sélection du menu Informations**|
| :- |
|![tâche : image_alt_text](managing-document-properties_1.png)|
1.  Cliquer sur**Propriétés** et sélectionnez "Propriétés avancées".

|**Cliquer sur Sélection des propriétés avancées**|
| :- |
|![tâche : image_alt_text](managing-document-properties_2.png)|
1. Gérez les propriétés du document du fichier.

|**Boîte de dialogue Propriétés**|
| :- |
|![tâche : image_alt_text](managing-document-properties_3.png)|
Dans la boîte de dialogue Propriétés, il existe différents onglets, comme Général, Résumé, Statistiques, Contenu et Douanes. Chaque onglet permet de configurer différents types d'informations liées au fichier. L'onglet Personnalisé est utilisé pour gérer les propriétés personnalisées.

##  **Comment travailler avec les propriétés du document à l'aide de Aspose.Cells**

Les développeurs peuvent gérer dynamiquement les propriétés du document à l'aide des API Aspose.Cells. Cette fonctionnalité aide les développeurs à stocker des informations utiles avec le fichier, telles que la date à laquelle le fichier a été reçu, traité, horodaté, etc.

{{% alert color="primary" %}}

 Aspose.Cells for .NET écrit directement les informations sur API et le numéro de version dans les documents de sortie. Par exemple, lors du rendu du document vers PDF, Aspose.Cells for .NET remplit**Application** champ avec la valeur 'Aspose.Cells' et**PDF Producteur** champ avec la valeur, par exemple 'Aspose.Cells v17.9'.

Veuillez noter que vous ne pouvez pas demander au Aspose.Cells for .NET de modifier ou de supprimer ces informations des documents de sortie.

{{% /alert %}}

###  **Comment accéder aux propriétés du document**

 Les API Aspose.Cells prennent en charge les deux types de propriétés de document, intégrées et personnalisées. Aspose.Cells'[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe représente un fichier Excel et, comme un fichier Excel, la[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) La classe peut contenir plusieurs feuilles de calcul, chacune représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe alors que la collection de feuilles de calcul est représentée par le[**Collection de feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)classe.

 Utilisez le[**Collection de feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)pour accéder aux propriétés du document du fichier comme décrit ci-dessous.

- Pour accéder aux propriétés intégrées du document, utilisez[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  Pour accéder aux propriétés du document personnalisé, utilisez[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 Les deux[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) et[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) renvoyer l'instance de[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Cette collection contient[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)objets, dont chacun représente une seule propriété de document intégrée ou personnalisée.

 Il appartient aux exigences de la demande de savoir comment accéder à une propriété, c'est-à-dire ; en utilisant l'index ou le nom de la propriété du[**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)comme le démontre l’exemple ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

 Le[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)La classe permet de récupérer le nom, la valeur et le type de la propriété du document :

-  Pour obtenir le nom de la propriété, utilisez[**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  Pour obtenir la valeur de la propriété, utilisez[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)renvoie la valeur sous forme d'objet.
-  Pour obtenir le type de propriété, utilisez[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . Cela renvoie l'un des[**Type de propriété**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype)valeurs d'énumération. Après avoir obtenu le type de propriété, utilisez l'un des**DocumentProperty.ToXXX** méthodes pour obtenir la valeur du type approprié au lieu d’utiliser[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) . Le**DocumentProperty.ToXXX**Les méthodes sont décrites dans le tableau ci-dessous.

{{% alert color="primary" %}}

 Le[**Propriété du document**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)La classe fournit également un ensemble de méthodes qui renvoient les valeurs d'autres types de données.

{{% /alert %}}

|**Nom de membre**|**Description**|**Méthode ToXXX**|
| :- | :- | :- |
|Booléen|Le type de données de la propriété est booléen|ÀBool|
|Date| Le type de données de la propriété est DateTime. Notez que Microsoft Excel stocke uniquement<br>la partie date, aucune heure ne peut être stockée dans une propriété personnalisée de ce type|ÀDateHeure|
|Flotter|Le type de données de la propriété est Double|Doubler|
|Nombre|Le type de données de la propriété est Int32|VersInt|
|String|Le type de données de la propriété est String|VersChaîne|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

###  **Comment ajouter ou supprimer des propriétés de document personnalisées**

Comme nous l'avons décrit précédemment au début de cette rubrique, les développeurs ne peuvent pas ajouter ou supprimer de propriétés intégrées car ces propriétés sont définies par le système, mais il est possible d'ajouter ou de supprimer des propriétés personnalisées car celles-ci sont définies par l'utilisateur.

###  **Comment ajouter des propriétés personnalisées**

 Aspose.Cells Les API ont exposé le[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) méthode pour le[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) classe afin d’ajouter des propriétés personnalisées à la collection. Le[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) La méthode ajoute la propriété au fichier Excel et renvoie une référence pour la nouvelle propriété du document en tant que[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)objet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

###  **Comment configurer la propriété personnalisée « Lien vers le contenu »**

 Pour créer une propriété personnalisée liée au contenu d'une plage donnée, appelez la commande[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) méthode et transmettez le nom et la source de la propriété. Vous pouvez vérifier si une propriété est configurée comme liée au contenu à l'aide de l'outil[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) propriété. De plus, il est également possible d'obtenir la plage source en utilisant le[**Source**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) propriété du[**Propriété du document**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)classe.

Nous utilisons un simple fichier Excel modèle Microsoft dans l’exemple. Le classeur a une plage nommée définie étiquetée**Ma gamme** qui fait référence à une valeur de cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

###  **Comment supprimer les propriétés personnalisées**

 Pour supprimer des propriétés personnalisées à l'aide du Aspose.Cells, appelez le[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)et transmettez le nom de la propriété du document à supprimer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

##  **Sujets avancés**
- [Ajout de propriétés personnalisées visibles dans le panneau d'informations sur le document](/cells/fr/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Définition des propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées](/cells/fr/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Spécifier la version du document du fichier Excel à l'aide des propriétés de document intégrées](/cells/fr/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Spécifiez la langue du fichier Excel à l'aide des propriétés du document intégrées](/cells/fr/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

---
title: Gestion des propriétés du document
type: docs
weight: 10
url: /fr/java/managing-document-properties/
---
## **Introduction**

Microsoft Excel offre la possibilité d'ajouter des propriétés aux fichiers de feuille de calcul. Ces propriétés de document fournissent des informations utiles et sont divisées en 2 catégories comme détaillé ci-dessous.

- Propriétés définies par le système (intégrées) : les propriétés intégrées contiennent des informations générales sur le document telles que le titre du document, le nom de l'auteur, les statistiques du document, etc.
- Propriétés définies par l'utilisateur (personnalisées) : propriétés personnalisées définies par l'utilisateur final sous la forme d'une paire nom-valeur.

{{% alert color="primary" %}}

Le point le plus important à savoir sur les propriétés intégrées et personnalisées est que les propriétés intégrées peuvent être consultées et modifiées, mais ne peuvent pas être créées ou supprimées, cependant, les propriétés de document personnalisées peuvent être créées et gérées.

{{% /alert %}}

## **Gestion des propriétés du document à l'aide de Microsoft Excel**

 Microsoft Excel permet de gérer les propriétés de document des fichiers Excel de manière WYSIWYG. Veuillez suivre les étapes ci-dessous pour ouvrir le**Propriétés** boîte de dialogue dans Excel 2016.

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

 Aspose.Cells for Java écrit directement les informations sur API et le numéro de version dans les documents de sortie. Par exemple, lors du rendu du document au format PDF, Aspose.Cells for Java remplit**Application** champ avec la valeur 'Aspose.Cells' et**Producteur PDF** champ avec la valeur, par exemple 'Aspose.Cells for Java v17.9'.

Veuillez noter que vous ne pouvez pas demander au Aspose.Cells for Java de modifier ou de supprimer ces informations des documents de sortie.

{{% /alert %}}

### **Accéder aux propriétés du document**

Aspose.Cells Les API prennent en charge les deux types de propriétés de document, intégrées et personnalisées. Aspose.Cells'[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe représente un fichier Excel et, comme un fichier Excel, la[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe peut contenir plusieurs feuilles de calcul, chacune représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe alors que la collection de feuilles de calcul est représentée par la[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)classer.

 Utilisez le[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)pour accéder aux propriétés du document du fichier comme décrit ci-dessous.

-  Pour accéder aux propriétés de document intégrées, utilisez[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
-  Pour accéder aux propriétés de document personnalisées, utilisez le[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

 Les deux[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) et[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) renvoie une instance de[**DocumentPropertyCollectionDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) . Cette collection contient[**PropriétéDocument**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)objets, chacun représentant une seule propriété de document intégrée ou personnalisée.

 C'est à l'exigence de l'application comment accéder à une propriété, c'est-à-dire; en utilisant l'index ou le nom de la propriété de la[**DocumentPropertyCollectionDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)comme le montre l'exemple ci-dessous.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

 La[**PropriétéDocument**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)class permet de récupérer le nom, la valeur et le type de la propriété du document :

-  Pour obtenir le nom de la propriété, utilisez[**DocumentProperty.NameDocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
-  Pour obtenir la valeur de la propriété, utilisez[**DocumentProperty.ValueDocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.ValueDocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value)renvoie la valeur en tant qu'objet.
-  Pour obtenir le type de propriété, utilisez[**DocumentProperty.TypeDocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type) . Cela renvoie l'un des[**Type de propriété**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType)valeurs d'énumération.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Ajout ou suppression de propriétés de document personnalisées**

Comme nous l'avons décrit précédemment au début de cette rubrique, les développeurs ne peuvent pas ajouter ou supprimer des propriétés intégrées car ces propriétés sont définies par le système, mais il est possible d'ajouter ou de supprimer des propriétés personnalisées car elles sont définies par l'utilisateur.

### **Ajout de propriétés personnalisées**

 Aspose.Cells Les API ont exposé le[**ajouter**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) ) méthode pour la[**CustomDocumentPropertyCollectionCustomDocumentPropertyCollectionCustomDocumentPropertyCollectionCustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) class afin d'ajouter des propriétés personnalisées à la collection. La[**ajouter**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) ) ajoute la propriété au fichier Excel et renvoie une référence pour la nouvelle propriété de document en tant que[**PropriétéDocument**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)objet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **Configuration de la propriété personnalisée "Lien vers le contenu"**

 Pour créer une propriété personnalisée liée au contenu d'une plage donnée, appelez le[**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String) ) méthode et transmettez le nom et la source de la propriété. Vous pouvez vérifier si une propriété est configurée comme étant liée au contenu à l'aide de la[**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent) propriété. De plus, il est également possible d'obtenir la plage source à l'aide de la[**La source**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) propriété de la[**PropriétéDocument**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)classer.

 Nous utilisons un simple fichier Excel modèle Microsoft dans l'exemple. Le classeur a une plage nommée définie étiquetée**MaPlage** qui fait référence à une valeur de cellule.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Suppression des propriétés personnalisées**

 Pour supprimer les propriétés personnalisées à l'aide de Aspose.Cells, appelez le[**DocumentPropertyCollection.removeDocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String)) et transmettez le nom de la propriété de document à supprimer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}

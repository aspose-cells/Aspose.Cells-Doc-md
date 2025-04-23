---
title: Gestion des propriétés de document
type: docs
weight: 10
url: /fr/java/managing-document-properties/
---

## **Introduction**

Microsoft Excel permet d'ajouter des propriétés aux fichiers de feuille de calcul. Ces propriétés de document fournissent des informations utiles et sont divisées en 2 catégories comme détaillé ci-dessous.

- Propriétés système définies (intégrées) : Les propriétés intégrées contiennent des informations générales sur le document telles que le titre du document, le nom de l'auteur, les statistiques du document, etc.
- Propriétés utilisateur définies (personnalisées) : Propriétés personnalisées définies par l'utilisateur final sous forme de paire nom-valeur.

{{% alert color="primary" %}}

Le point le plus important à savoir sur les propriétés prédéfinies et personnalisées est que les propriétés prédéfinies peuvent être consultées et modifiées, mais ne peuvent pas être créées ou supprimées, cependant, les propriétés de document personnalisées peuvent être créées et gérées.

{{% /alert %}}

## **Gestion des propriétés de document avec Microsoft Excel**

Microsoft Excel permet de gérer les propriétés de document des fichiers Excel de manière WYSIWYG. Veuillez suivre les étapes ci-dessous pour ouvrir la boîte de dialogue **Propriétés** dans Excel 2016.

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

## **Travailler avec les propriétés de document en utilisant Aspose.Cells**

Les développeurs peuvent gérer dynamiquement les propriétés de document à l'aide des API Aspose.Cells. Cette fonctionnalité aide les développeurs à stocker des informations utiles avec le fichier, telles que la date de réception du fichier, le traitement, l'horodatage, etc.

{{% alert color="primary" %}}

Aspose.Cells for Java écrit directement les informations sur l'API et le numéro de version dans les documents de sortie. Par exemple, lors du rendu du Document au format PDF, Aspose.Cells for Java renseigne le champ **Application** avec la valeur 'Aspose.Cells' et le champ **Producteur PDF** avec la valeur, par exemple 'Aspose.Cells for Java v17.9'.

Veuillez noter que vous ne pouvez pas demander à Aspose.Cells for Java de modifier ou de supprimer ces informations des documents de sortie.

{{% /alert %}}

### **Accès aux propriétés du document**

Les API Aspose.Cells prennent en charge les deux types de propriétés de document, intégrées et personnalisées. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) d'Aspose.Cells représente un fichier Excel et, comme un fichier Excel, la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) peut contenir plusieurs feuilles de calcul, chacune représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet), tandis que la collection de feuilles de calcul est représentée par la classe [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection).

Utilisez [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) pour accéder aux propriétés de document du fichier comme décrit ci-dessous.

- Pour accéder aux propriétés de document intégrées, utilisez [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
- Pour accéder aux propriétés de document personnalisées, utilisez [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

À la fois [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) et [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) renvoient une instance de [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection). Cette collection contient des objets [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty), chacun représentant une seule propriété de document intégrée ou personnalisée.

Il appartient à l'exigence de l'application de savoir comment accéder à une propriété, c'est-à-dire; en utilisant l'index ou le nom de la propriété de [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) comme démontré dans l'exemple ci-dessous.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

La classe [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) permet de récupérer le nom, la valeur et le type de la propriété du document:

- Pour obtenir le nom de la propriété, utilisez [**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
- Pour obtenir la valeur de la propriété, utilisez [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value) renvoie la valeur en tant qu'objet.
- Pour obtenir le type de propriété, utilisez [**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type). Cela renvoie l'une des valeurs d'énumération [**PropertyType**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Ajout ou suppression de propriétés de document personnalisées**

Comme nous l'avons décrit précédemment au début de ce sujet, les développeurs ne peuvent pas ajouter ou supprimer des propriétés intégrées car ces propriétés sont système-définies, mais il est possible d'ajouter ou de supprimer des propriétés personnalisées car celles-ci sont définies par l'utilisateur.

### **Ajout de propriétés personnalisées**

Les API Aspose.Cells ont exposé la méthode [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add-java.lang.String-boolean-) pour la classe [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) afin d'ajouter des propriétés personnalisées à la collection. La méthode [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add-java.lang.String-boolean-) ajoute la propriété au fichier Excel et renvoie une référence pour la nouvelle propriété de document en tant qu'objet [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **Configuration de la propriété personnalisée 'Lien vers le contenu'**

Pour créer une propriété personnalisée liée au contenu d'une plage donnée, appelez la méthode [**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent-java.lang.String-java.lang.String-) et passez le nom de la propriété et la source. Vous pouvez vérifier si une propriété est configurée comme étant liée au contenu en utilisant la propriété [**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent). De plus, il est également possible d'obtenir la plage source en utilisant la propriété [**Source**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) de la classe [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty).

Nous utilisons un fichier modèle Microsoft Excel simple dans l'exemple. Le classeur a une plage nommée définie étiquetée **MyRange** qui fait référence à une valeur de cellule.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Suppression de propriétés personnalisées**

Pour supprimer des propriétés personnalisées à l'aide d'Aspose.Cells, appelez la méthode [**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove-java.lang.String-) et transmettez le nom de la propriété du document à supprimer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
{{< app/cells/assistant language="java" >}}

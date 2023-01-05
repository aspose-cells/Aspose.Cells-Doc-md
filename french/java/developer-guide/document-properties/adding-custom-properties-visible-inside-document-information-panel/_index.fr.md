---
title: Ajout de propriétés personnalisées visibles dans le panneau Informations sur le document
type: docs
weight: 500
url: /fr/java/adding-custom-properties-visible-inside-document-information-panel/
---
{{% alert color="primary" %}}

Aspose.Cells peut être utilisé pour ajouter des propriétés personnalisées à l'intérieur de l'objet classeur qui sont visibles dans le panneau Informations sur le document. Vous pouvez ouvrir le panneau d'informations sur le document dans Microsoft Excel à l'aide des commandes de menu Fichier > Infos > Propriétés > Afficher le panneau de document.

 Veuillez utiliser[**Classeur.getContentTypeProperties().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add(java.lang.Object)) pour ajouter une propriété personnalisée qui sera visible dans le panneau Informations sur le document

{{% /alert %}}

## **Exemple**

L'exemple de code suivant ajoute deux propriétés personnalisées. La première propriété est sans aucun type et la deuxième propriété a un type comme DateTime. Une fois que vous ouvrirez le fichier Excel de sortie généré par ce code, vous verrez ces deux propriétés dans le panneau d'informations sur le document.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **Article associé**

{{% alert color="primary" %}}

- [Utilisation de parties XML personnalisées dans Aspose.Cells](/cells/fr/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}

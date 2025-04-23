---
title: Ajout de propriétés personnalisées visibles dans le volet Informations sur le document
type: docs
weight: 500
url: /fr/java/adding-custom-properties-visible-inside-document-information-panel/
---

{{% alert color="primary" %}}

Aspose.Cells peut être utilisé pour ajouter des propriétés personnalisées à l'intérieur de l'objet classeur qui sont visibles dans le volet Informations sur le document. Vous pouvez ouvrir le volet Informations sur le document dans Microsoft Excel en utilisant les commandes du menu Fichier > Infos > Propriétés > Afficher le volet Document.

Veuillez utiliser la méthode [**Workbook.getContentTypeProperties().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-) pour ajouter une propriété personnalisée qui sera visible dans le volet Informations sur le document

{{% /alert %}}

## **Exemple**

Le code d'exemple suivant ajoute deux propriétés personnalisées. La première propriété n'a aucun type et la deuxième propriété a un type DateTime. Une fois que vous ouvrirez le fichier Excel généré par ce code, vous verrez ces deux propriétés dans le volet Informations sur le document.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **Article connexe**

{{% alert color="primary" %}}

- [Utilisation de pièces XML personnalisées dans Aspose.Cells](/cells/fr/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

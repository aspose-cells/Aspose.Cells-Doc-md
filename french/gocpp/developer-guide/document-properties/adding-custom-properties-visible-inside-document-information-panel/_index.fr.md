---
title: Ajout de propriétés personnalisées visibles dans le panneau d information du document avec Golang via C++
linktitle: Ajout de propriétés personnalisées visibles dans le volet Informations sur le document
type: docs
weight: 300
url: /fr/go-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Apprenez comment ajouter des propriétés personnalisées visibles dans le panneau d informations du document en utilisant Aspose.Cells avec Golang via C++.
---

## **Ajout de propriétés personnalisées visibles dans le volet Informations sur le document**

Aspose.Cells peut être utilisé pour ajouter des propriétés personnalisées à l'intérieur de l'objet classeur qui sont visibles dans le volet Informations sur le document. Vous pouvez ouvrir le volet Informations sur le document dans Microsoft Excel en utilisant les commandes du menu Fichier > Infos > Propriétés > Afficher le volet Document.

Veuillez utiliser la méthode [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) pour ajouter une propriété personnalisée qui sera visible dans le Panneau d'informations sur le document.

Le code d'exemple suivant ajoute deux propriétés personnalisées. La première propriété n'a pas de type, et la seconde a un type DateTime. Une fois que vous ouvrez le fichier Excel généré par ce code, vous verrez ces deux propriétés dans le Panneau d'informations sur le document.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingCustomPropertiesVisibleInsideDocumentInformationPanel.go" >}}
### **Article connexe**

{{% alert color="primary" %}}

- [Utiliser des parties XML personnalisées dans Aspose.Cells](/cells/fr/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}

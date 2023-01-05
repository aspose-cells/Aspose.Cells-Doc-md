---
title: Ajouter une référence de bibliothèque au projet VBA dans le classeur
type: docs
weight: 10
url: /fr/java/add-a-library-reference-to-vba-project-in-workbook/
---
{{% alert color="primary" %}}

 Dans Microsoft Excel, vous pouvez ajouter une référence de bibliothèque au projet VBA en cliquant sur le**Outils > Références...** manuellement. Il ouvrira la boîte de dialogue suivante qui vous aidera à sélectionner parmi les références existantes ou à parcourir vous-même votre bibliothèque.

![tâche : image_autre_texte](add-a-library-reference-to-vba-project-in-workbook_1.png)

 Mais parfois, vous devez ajouter ou enregistrer la référence de bibliothèque au projet VBA via le code. Vous pouvez le faire en utilisant Aspose.Cells[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) méthode.

{{% /alert %}}

## **Ajouter une référence de bibliothèque au projet VBA dans le classeur**

 L'exemple de code suivant ajoute ou enregistre deux références de bibliothèque au projet VBA du classeur à l'aide[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) méthode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}

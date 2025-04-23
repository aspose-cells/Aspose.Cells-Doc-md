---
title: Ajoutez une référence de bibliothèque au projet VBA dans le classeur
type: docs
weight: 10
url: /fr/java/add-a-library-reference-to-vba-project-in-workbook/
description: Apprenez comment ajouter une référence de bibliothèque au projet VBA dans le classeur via l API Aspose.Cells for Java.
keywords: Comment ajouter une référence de bibliothèque au projet VBA dans le classeur en Java, insérer une référence de bibliothèque au projet VBA dans le classeur en utilisant Java, définir une référence de bibliothèque Java au projet VBA dans le classeur. 
---

{{% alert color="primary" %}}

Dans Microsoft Excel, vous pouvez ajouter une référence de bibliothèque au projet VBA en cliquant sur **Outils > Références...** manuellement. Cela ouvrira la boîte de dialogue suivante qui vous aidera à sélectionner parmi les références existantes ou à parcourir votre bibliothèque vous-même.

![todo:image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

Mais parfois, vous devez ajouter ou enregistrer la référence de bibliothèque dans le projet VBA via le code. Vous pouvez le faire en utilisant la méthode [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference-java.lang.String-java.lang.String-) d'Aspose.Cells.

{{% /alert %}}

## **Comment ajouter une référence de bibliothèque au projet VBA dans le classeur**

L'exemple de code suivant ajoute ou enregistre deux références de bibliothèque dans le projet VBA du classeur en utilisant la méthode [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference-java.lang.String-java.lang.String-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
{{< app/cells/assistant language="java" >}}

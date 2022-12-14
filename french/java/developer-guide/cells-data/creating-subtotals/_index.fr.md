---
title: Création de sous-totaux
type: docs
weight: 50
url: /fr/java/creating-subtotals/
---
{{% alert color="primary" %}}

Vous pouvez créer automatiquement des sous-totaux pour toutes les valeurs récurrentes dans une feuille de calcul. Aspose.Cells fournit des fonctionnalités API qui vous aident à ajouter des sous-totaux aux feuilles de calcul par programmation.

{{% /alert %}}

## **Utilisation d'Excel Microsoft**

Pour créer des sous-totaux dans Microsoft Excel :

1. Créez une liste de données simple dans la première feuille de calcul du classeur (comme illustré dans la figure ci-dessous) et enregistrez le fichier sous Book1.xls.
1. Sélectionnez n'importe quelle cellule dans votre liste.
1.  Du**Données** menu, sélectionnez**Sous-totaux**.
 La boîte de dialogue Sous-totaux s'affiche. Définissez la fonction à utiliser et où placer les sous-totaux.

   **Sélection d'une plage de données pour ajouter des sous-totaux**

![tâche : image_autre_texte](creating-subtotals_1.png)

**La boîte de dialogue Sous-total** 

![tâche : image_autre_texte](creating-subtotals_2.png)

## **En utilisant Aspose.Cells API**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classer. La classe fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul et d'autres objets. Chaque feuille de travail se compose d'un[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) le recueil. Pour créer des sous-totaux dans une feuille de calcul, utilisez la[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)méthode de sous-total de la classe. Fournissez des valeurs appropriées pour les paramètres de la méthode afin d'obtenir le résultat souhaité.

L'exemple ci-dessous montre comment créer des sous-totaux dans la première feuille de calcul du fichier de modèle (Book1.xls) en utilisant Aspose.Cells API.

Lorsque le code est exécuté, une feuille de calcul avec des sous-totaux est créée.

**Application de sous-totaux** 

![tâche : image_autre_texte](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}

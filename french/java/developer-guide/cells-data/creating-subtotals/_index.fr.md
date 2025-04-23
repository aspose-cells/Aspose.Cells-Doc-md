---
title: Création de sous totaux
type: docs
weight: 50
url: /fr/java/creating-subtotals/
---

{{% alert color="primary" %}}

Vous pouvez créer automatiquement des sous-totaux pour toutes les valeurs répétées dans une feuille de calcul. Aspose.Cells propose des fonctionnalités d'API qui vous aident à ajouter des sous-totaux aux feuilles de calcul de manière programmatique.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Pour créer des sous-totaux dans Microsoft Excel :

1. Créez une liste de données simples dans la première feuille de calcul du classeur (comme indiqué dans la figure ci-dessous) et enregistrez le fichier sous le nom de Book1.xls.
1. Sélectionnez une cellule quelconque dans votre liste.
1. Dans le menu **Données**, sélectionnez **Sous-totaux**.
   La boîte de dialogue Sous-totaux s'affiche. Définissez la fonction à utiliser et l'endroit où placer les sous-totaux.

   **Sélection d'une plage de données pour ajouter des sous-totaux**

![todo:image_alt_text](creating-subtotals_1.png)

**La boîte de dialogue Sous-total** 

![todo:image_alt_text](creating-subtotals_2.png)

## **Utilisation de l'API Aspose.Cells**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul du fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul et d'autres objets. Chaque feuille de calcul se compose d'une collection [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Pour créer des sous-totaux dans une feuille de calcul, utilisez la méthode de sous-total de la classe [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Fournissez des valeurs appropriées pour les paramètres de la méthode afin d'obtenir le résultat souhaité.

L'exemple ci-dessous montre comment créer des sous-totaux dans la première feuille de calcul du fichier modèle (Book1.xls) en utilisant l'API Aspose.Cells.

Lorsque le code est exécuté, une feuille de calcul avec des sous-totaux est créée.

**Application des sous-totaux** 

![todo:image_alt_text](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
{{< app/cells/assistant language="java" >}}

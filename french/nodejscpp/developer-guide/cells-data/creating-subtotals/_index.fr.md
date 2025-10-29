---
title: Création de sous totaux
type: docs
weight: 800
url: /fr/nodejs-cpp/creating-subtotals/
description: Découvrez comment créer des sous totaux pour toutes les valeurs répétées dans une feuille de calcul en utilisant l API Aspose.Cells for Node.js via C++.
keywords: Appliquez des sous totaux, définissez des sous totaux, ajoutez des sous totaux, créez des sous totaux, comment ajouter des sous totaux à une feuille de calcul 
---

{{% alert color="primary" %}}

Vous pouvez automatiquement créer des sous-totaux pour toutes les valeurs répétées dans une feuille de calcul. L'API Aspose.Cells for Node.js via C++ propose des fonctionnalités d'API qui vous aident à ajouter des sous-totaux aux feuilles de calcul de manière programmatique.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Pour ajouter des sous-totaux dans Microsoft Excel :

1. Créez une liste de données simples dans la première feuille de calcul du classeur (comme indiqué dans la figure ci-dessous) et enregistrez le fichier sous le nom de Book1.xls.
1. Sélectionnez une cellule quelconque dans votre liste.
1. Dans le menu **Données**, sélectionnez **Sous-totaux**. La boîte de dialogue Sous-totaux s'affichera. Définissez la fonction à utiliser et l'emplacement des sous-totaux.

## **En utilisant l'API Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d’accéder à chaque feuille de calcul du fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe fournit une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul et d'autres objets. Chaque feuille de calcul se compose d'une collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Pour ajouter des sous-totaux à une feuille de calcul, utilisez la méthode [**subtotal**](https://reference.aspose.com/cells/nodejs-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) de la classe [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Fournissez des valeurs de paramètre à la méthode pour spécifier comment le sous-total doit être calculé et placé.

Dans les exemples ci-dessous, nous avons ajouté des sous-totaux à la première feuille du fichier [modèle](book1.xlsx) en utilisant l'API Aspose.Cells for Node.js via C++. Lors de l'exécution du code, une feuille avec des sous-totaux est créée.

Les extraits de code suivants montrent comment ajouter des sous-totaux à une feuille de calcul avec Aspose.Cells for Node.js via C++.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CreatingSubtotals-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}

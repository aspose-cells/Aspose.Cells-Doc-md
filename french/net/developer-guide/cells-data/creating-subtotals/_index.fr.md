---
title: Création de sous totaux
type: docs
weight: 800
url: /fr/net/creating-subtotals/
description: Apprenez à créer des sous totaux pour toutes les valeurs répétées dans une feuille de calcul en utilisant l API Aspose.Cells for .NET.
keywords: Appliquez des sous totaux, définissez des sous totaux, ajoutez des sous totaux, créez des sous totaux, comment ajouter des sous totaux à une feuille de calcul 
---

{{% alert color="primary" %}}

Vous pouvez créer automatiquement des sous-totaux pour toutes les valeurs répétées dans une feuille de calcul. Aspose.Cells offre des fonctionnalités API qui vous aident à ajouter des sous-totaux aux feuilles de calcul de manière programmée.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Pour ajouter des sous-totaux dans Microsoft Excel :

1. Créez une liste de données simples dans la première feuille de calcul du classeur (comme indiqué dans la figure ci-dessous) et enregistrez le fichier sous le nom de Book1.xls.
1. Sélectionnez une cellule quelconque dans votre liste.
1. Dans le menu **Données**, sélectionnez **Sous-totaux**. La boîte de dialogue Sous-totaux s'affichera. Définissez la fonction à utiliser et l'emplacement des sous-totaux.

## **Utilisation de l'API Aspose.Cells**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul du fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe fournit une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul et d'autres objets. Chaque feuille de calcul se compose d'une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Pour ajouter des sous-totaux à une feuille de calcul, utilisez la méthode [**Subtotal**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) de la classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Fournissez des valeurs de paramètre à la méthode pour spécifier comment le sous-total doit être calculé et placé.

Dans les exemples ci-dessous, nous avons ajouté des sous-totaux à la première feuille de calcul du fichier modèle (Book1.xls) en utilisant l'API Aspose.Cells. Lorsque le code est exécuté, une feuille de calcul avec des sous-totaux est créée.

Les extraits de code ci-dessous montrent comment ajouter des sous-totaux à une feuille de calcul avec Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **Sujets avancés**
- [Application de sous-total et changement de direction des lignes de résumé en dessous des détails](/cells/fr/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)

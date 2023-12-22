---
title: Création de sous-totaux
type: docs
weight: 800
url: /fr/net/creating-subtotals/
description: Découvrez comment créer des sous-totaux pour toutes les valeurs répétitives dans une feuille de calcul en utilisant le Aspose.Cells for .NET API.
keywords: Apply Subtotals, Set Subtotals, Add subtotals, Create Subtotals, How to add subtotals to a worksheet 
---
{{% alert color="primary" %}}

Vous pouvez créer automatiquement des sous-totaux pour toutes les valeurs répétitives dans une feuille de calcul. Aspose.Cells fournit des fonctionnalités API qui vous aident à ajouter des sous-totaux aux feuilles de calcul par programmation.

{{% /alert %}}

##  **Utilisation d'Excel Microsoft**

Pour ajouter des sous-totaux dans Excel Microsoft :

1. Créez une liste de données simple dans la première feuille de calcul du classeur (comme indiqué dans la figure ci-dessous) et enregistrez le fichier sous Book1.xls.
1. Sélectionnez n’importe quelle cellule de votre liste.
1.  Du**Données** menu, sélectionnez *Sous-totaux**. La boîte de dialogue Sous-totaux s'affichera. Définissez quelle fonction utiliser et où placer les sous-totaux.

##  **En utilisant le Aspose.Cells API**

 Aspose.Cells propose un cours,[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , cela représente un fichier Excel Microsoft. Le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d’accéder à chaque feuille de calcul du fichier Excel.

Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul et autres objets. Chaque feuille de travail se compose d'un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection. Pour ajouter des sous-totaux à une feuille de calcul, utilisez l'outil[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)classe'[**Total**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)méthode. Fournissez des valeurs de paramètre à la méthode pour spécifier comment le sous-total doit être calculé et placé.

Dans les exemples ci-dessous, nous avons ajouté des sous-totaux à la première feuille de calcul du fichier modèle (Book1.xls) à l'aide du Aspose.Cells API. Lorsque le code est exécuté, une feuille de calcul avec des sous-totaux est créée.

Les extraits de code qui suivent montrent comment ajouter des sous-totaux à une feuille de calcul avec Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

##  **Sujets avancés**
- [Application du sous-total et modification de la direction des lignes récapitulatives du plan sous les détails](/cells/fr/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)

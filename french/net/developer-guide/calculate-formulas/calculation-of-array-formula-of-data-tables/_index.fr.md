---
title: Calcul de la formule matricielle des tableaux de données
description: Comment utiliser la bibliothèque Aspose.Cells pour calculer des formules matricielles pour un tableau de données dans Excel Microsoft. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser la méthode fournie par Aspose.Cells pour calculer la formule matricielle du tableau de données et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, data tables, array formulas, calculations
type: docs
weight: 70
url: /fr/net/calculation-of-array-formula-of-data-tables/
---
{{% alert color="primary" %}}

Vous pouvez créer un tableau de données dans Microsoft Excel en utilisant Données > Analyse de simulation > Tableau de données.... Aspose.Cells vous permet désormais de calculer la formule matricielle d'un tableau de données. Veuillez utiliser[**Classeur.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) comme d'habitude pour calculer tout type de formules.

{{% /alert %}}

Dans l'exemple de code suivant, nous avons utilisé le[fichier Excel source](5115535.xlsx) . Si vous modifiez la valeur de la cellule B1 à 100, les valeurs du tableau de données qui sont remplies de couleur jaune deviendront 120, comme le montrent les images suivantes. L'exemple de code génère le[sortie PDF](5115538.pdf).

![tâche : image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![tâche : image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

 Voici l'exemple de code utilisé pour générer le[sortie PDF](5115538.pdf) du[fichier Excel source](5115535.xlsx). Veuillez lire les commentaires pour plus d'informations.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-CalculationOfArrayFormula-CalculateArrayFormula.cs" >}}

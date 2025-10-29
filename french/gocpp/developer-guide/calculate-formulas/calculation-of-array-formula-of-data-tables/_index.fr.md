---
title: Calcul de la formule de tableau pour les tables de données avec Golang via C++
linktitle: Calcul de la formule de tableau de données
description: Comment utiliser la bibliothèque Aspose.Cells pour calculer les formules de tableau pour une table de données dans Microsoft Excel avec Golang via C++. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser la méthode fournie par Aspose.Cells pour calculer la formule de tableau de la table de données et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, tableaux de données, formules matricielles, calculs, C++
type: docs
weight: 70
url: /fr/go-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Vous pouvez créer un tableau de données dans Microsoft Excel en utilisant Données > Analyse de scénarios > Table de données... Aspose.Cells vous permet maintenant de calculer la formule de tableau de données. Veuillez utiliser [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) comme d'habitude pour calculer n'importe quel type de formules.

{{% /alert %}}

Dans le code d'exemple suivant, nous avons utilisé le [fichier Excel source](5115535.xlsx). Si vous changez la valeur de la cellule B1 à 100, les valeurs du tableau de données qui sont remplies de couleur jaune deviendront 120 comme indiqué dans les images suivantes. Le code d'exemple génère le [PDF de sortie](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Voici le code d'exemple utilisé pour générer le [PDF de sortie](5115538.pdf) à partir du [fichier Excel source](5115535.xlsx). Veuillez lire les commentaires pour plus d'informations.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculationOfArrayFormulaOfDataTables.go" >}}

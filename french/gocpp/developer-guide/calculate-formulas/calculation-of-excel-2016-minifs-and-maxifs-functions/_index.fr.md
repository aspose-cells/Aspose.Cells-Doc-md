---
title: Calcul des fonctions MINIFS et MAXIFS d Excel 2016 avec Golang via C++
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour calculer les fonctions MINIFS et MAXIFS dans Microsoft Excel 2016 en utilisant C++.
keywords: Aspose.Cells, Excel, 2016, fonction MINIFS, fonction MAXIFS, calcul
type: docs
weight: 300
url: /fr/go-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Scénarios d'utilisation possibles**
Microsoft Excel 2016 prend en charge les fonctions MINIFS et MAXIFS. Ces fonctions ne sont pas supportées dans Excel 2013 ou versions antérieures. Aspose.Cells prend également en charge le calcul de ces fonctions. La capture d'écran suivante illustre l'utilisation de ces fonctions. Veuillez lire les commentaires en rouge dans la capture pour savoir comment ces fonctions fonctionnent.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Calcul des fonctions MINIFS et MAXIFS d'Excel 2016**
Le code d'exemple suivant charge le [fichier Excel d'exemple](5115149.xlsx) et appelle la méthode [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) pour effectuer le calcul de la formule via Aspose.Cells, puis enregistre les résultats dans le [PDF de sortie](5115154.pdf).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculationOfExcel2016MinifsAndMaxifsFunctions.go" >}}

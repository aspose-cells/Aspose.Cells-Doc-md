---
title: Utilisation de la fonction FormulaText dans Aspose.Cells avec Golang via C++
linktitle: Utiliser la fonction FormulaText
description: Cet article présente comment utiliser la fonction FormulaText dans la bibliothèque Aspose.Cells pour traiter les formules dans Microsoft Excel. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser la méthode fournie par Aspose.Cells pour obtenir et définir le texte de la formule de la cellule et obtenir le résultat. Enfin, nous sauvegardons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, fonctions FormulaText
type: docs
weight: 60
url: /fr/go-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText est une fonction d'Excel 2013 et ultérieure. Elle n'est pas prise en charge par les versions précédentes comme Excel 2010 ou 2007, etc. Comme son nom l'indique, elle imprime le texte de la formule qui est présente dans une cellule donnée. Cet article vous montrera comment faire usage de cette fonction en utilisant Aspose.Cells.

{{% /alert %}} 

Le code d'exemple suivant montre l'utilisation de FormulaText avec Aspose.Cells. Le code écrit d'abord une formule dans la cellule A1, puis imprime le texte de la formule en utilisant FormulaText dans la cellule A2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UsingFormulatextFunctionInAsposeCells.go" >}}
## **Sortie console**
Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}

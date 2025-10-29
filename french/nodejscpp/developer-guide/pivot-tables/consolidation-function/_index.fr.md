---
title: Fonction de consolidation
type: docs
weight: 20
url: /fr/nodejs-cpp/consolidation-function/
description: Comment appliquer ConsolidationFunction aux champs de données du tableau croisé dynamique avec Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, bibliothèque Excel Node.js, ConsolidationFunction aux champs de données du tableau croisé dynamique en utilisant la bibliothèque Excel Aspose.Cells for Node.js via C++.
---

## **Fonction de consolidation**

Aspose.Cells for Node.js via C++ peut être utilisé pour appliquer la ConsolidationFunction aux champs de données (ou champs de valeur) du tableau croisé dynamique. Dans Microsoft Excel, vous pouvez cliquer avec le bouton droit sur le champ de valeur puis sélectionner **Paramètres du champ de valeur...** et ensuite choisir l'onglet **Synthèse des valeurs par**. À partir de là, vous pouvez choisir n'importe quelle fonction de consolidation comme Somme, Compte, Moyenne, Max, Min, Produit, Compte distinct, etc.

Aspose.Cells for Node.js via C++ fournit une énumération [**ConsolidationFunction**](https://reference.aspose.com/cells/nodejs-cpp/consolidationfunction/) pour supporter les fonctions de consolidation suivantes.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **Comment appliquer la ConsolidationFunction aux champs de données du tableau croisé dynamique en utilisant Aspose.Cells for Node.js via C++**

Le code suivant applique la fonction de consolidation **Moyenne** au premier champ de données (ou champ de valeur) et la fonction de consolidation **Nombre distinct** au deuxième champ de données (ou champ de valeur).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ConsolidationFunctions-1.js" >}}

{{% alert color="primary" %}}

La fonction de consolidation DISTINCT_COUNT est prise en charge uniquement par Microsoft Excel 2013.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}

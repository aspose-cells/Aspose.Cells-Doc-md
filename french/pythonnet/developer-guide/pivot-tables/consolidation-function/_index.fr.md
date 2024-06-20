---
title: Fonction de consolidation
type: docs
weight: 20
url: /fr/python-net/consolidation-function/
description: Comment appliquer la fonction de consolidation aux champs de données du tableau croisé dynamique avec Aspose.Cells pour Python via .NET.
keywords: Aspose.Cells for Python Excel, bibliothèque Python Excel, fonction de consolidation aux champs de données du tableau croisé dynamique en utilisant la bibliothèque Excel Aspose.Cells pour Python.
---

## **Fonction de consolidation**

Aspose.Cells for Python via .NET peut être utilisé pour appliquer la fonction de consolidation aux champs de données (ou champs de valeur) du tableau croisé dynamique. Dans Microsoft Excel, vous pouvez cliquer avec le bouton droit sur le champ de valeur, puis sélectionner l'option **Paramètres Champ de valeur...** et ensuite sélectionner l'onglet **Résumer les valeurs par**. À partir de là, vous pouvez sélectionner n'importe quelle fonction de consolidation de votre choix comme Somme, Compter, Moyenne, Max, Min, Produit, Compte distinct, etc.

Aspose.Cells for Python via .NET fournit une énumération [**ConsolidationFunction**](https://reference.aspose.com/cells/python-net/aspose.cells/consolidationfunction/) pour prendre en charge les fonctions de consolidation suivantes.

- ConsolidationFunction.AVERAGE
- ConsolidationFunction.COUNT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.DISTINCT_COUNT
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.SUM
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP

## **Comment appliquer la fonction de consolidation aux champs de données du tableau croisé dynamique à l'aide de la bibliothèque Excel Aspose.Cells pour Python**

Le code suivant applique la fonction de consolidation **AVERAGE** au premier champ de données (ou champ de valeur) et la fonction de consolidation **DISTINCT_COUNT** au deuxième champ de données (ou champ de valeur).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ConsolidationFunctions-1.py" >}}

{{% alert color="primary" %}}

La fonction de consolidation DISTINCT_COUNT est prise en charge uniquement par Microsoft Excel 2013.

{{% /alert %}}

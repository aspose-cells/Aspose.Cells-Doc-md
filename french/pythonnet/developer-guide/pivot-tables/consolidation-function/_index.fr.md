---
title: Fonction de consolidation
type: docs
weight: 20
url: /fr/python-net/consolidation-function/
description: Comment appliquer ConsolidationFunction aux champs de données du tableau croisé dynamique avec Aspose.Cells for Python via .NET.
keywords: ConsolidationFunction to Data Fields of Pivot Table.
---
##  **Fonction de consolidation**

 Aspose.Cells for Python via .NET peut être utilisé pour appliquer ConsolidationFunction aux champs de données (ou champs de valeur) du tableau croisé dynamique. Dans Excel Microsoft, vous pouvez cliquer avec le bouton droit sur le champ de valeur, puis sélectionner**Paramètres du champ de valeur...** puis sélectionnez l'onglet *Résumer les valeurs par**. À partir de là, vous pouvez sélectionner n'importe quelle fonction de consolidation de votre choix, comme Somme, Nombre, Moyenne, Max, Min, Produit, Nombre distinct, etc.

 Aspose.Cells for Python via .NET fournit[**Fonction de consolidation**](https://reference.aspose.com/cells/python-net/aspose.cells/consolidationfunction/) énumération pour prendre en charge les fonctions de consolidation suivantes.

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

###  **Application de ConsolidationFunction aux champs de données du tableau croisé dynamique**

 Le code suivant s'applique**AVERAGE** fonction de consolidation au premier champ de données (ou champ de valeur) et**DISTINCT_COUNT** fonction de consolidation au deuxième champ de données (ou champ de valeur).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ConsolidationFunctions-1.py" >}}

{{% alert color="primary" %}}

La fonction de consolidation DISTINCT_COUNT est prise en charge par Microsoft Excel 2013 uniquement.

{{% /alert %}}

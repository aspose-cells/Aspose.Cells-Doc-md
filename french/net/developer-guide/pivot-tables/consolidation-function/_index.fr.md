---
title: Fonction Consolidation
type: docs
weight: 20
url: /fr/net/consolidation-function/
---
## **Fonction de consolidation**

 Aspose.Cells peut être utilisé pour appliquer ConsolidationFunction aux champs de données (ou champs de valeur) du tableau croisé dynamique. Dans Microsoft Excel, vous pouvez cliquer avec le bouton droit sur le champ de valeur, puis sélectionner**Paramètres du champ de valeur...** l'option puis sélectionnez l'onglet**Résumer les valeurs par**. À partir de là, vous pouvez sélectionner n'importe quelle ConsolidationFunction de votre choix comme Sum, Count, Average, Max, Min, Product, Distinct Count, etc.

 Aspose.Cells fournit[**Fonction de consolidation**](https://reference.aspose.com/cells/net/aspose.cells/consolidationfunction) énumération pour prendre en charge les fonctions de consolidation suivantes.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCountConsolidationFunction.DistinctCount
- ConsolidationFunction.MaxConsolidationFunction.Max
- ConsolidationFunction.MinConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.SumConsolidationFunction.Sum
- ConsolidationFunction.VarConsolidationFunction.Var
- ConsolidationFunction.VarpConsolidationFunction.Varp

### **Application de ConsolidationFunction aux champs de données du tableau croisé dynamique**

 Le code suivant s'applique**Moyenne** fonction de consolidation au premier champ de données (ou champ de valeur) et**DistinctCount** fonction de consolidation au deuxième champ de données (ou champ de valeur).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}

La fonction de consolidation DistinctCount est prise en charge par Microsoft Excel 2013 uniquement.

{{% /alert %}}

---
title: Fonction de consolidation
type: docs
weight: 20
url: /fr/net/consolidation-function/
---

## **Fonction de consolidation**

Aspose.Cells peut être utilisé pour appliquer la fonction de consolidation aux champs de données (ou aux champs de valeur) du tableau croisé dynamique. Dans Microsoft Excel, vous pouvez cliquer avec le bouton droit sur le champ de valeur, puis sélectionner l'option **Paramètres du champ de valeur...** et ensuite sélectionner l'onglet **Recapituler les valeurs par**. À partir de là, vous pouvez sélectionner n'importe quelle fonction de consolidation de votre choix comme Somme, Nombre, Moyenne, Max, Min, Produit, Nombre distinct, etc.

Aspose.Cells fournit une énumération [**ConsolidationFunction**](https://reference.aspose.com/cells/net/aspose.cells/consolidationfunction) pour prendre en charge les fonctions de consolidation suivantes.

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

### **Application de la fonction de consolidation aux champs de données d'un tableau croisé dynamique**

Le code suivant applique la fonction de consolidation **Moyenne** au premier champ de données (ou champ de valeur) et la fonction de consolidation **Nombre distinct** au deuxième champ de données (ou champ de valeur).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}

La fonction de consolidation ComptageDistinct est prise en charge uniquement par Microsoft Excel 2013.

{{% /alert %}}

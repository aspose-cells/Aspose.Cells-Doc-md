---
title: Fonction Consolidation
type: docs
weight: 20
url: /fr/java/consolidation-function/
description: Appliquez ConsolidationFunction aux champs de données du tableau croisé dynamique.
---
## **Fonction de consolidation**

 Aspose.Cells peut être utilisé pour appliquer ConsolidationFunction aux champs de données (ou champs de valeur) du tableau croisé dynamique. Dans Microsoft Excel, vous pouvez cliquer avec le bouton droit sur le champ de valeur, puis sélectionner**Paramètres du champ de valeur...** l'option puis sélectionnez l'onglet**Résumer les valeurs par**. À partir de là, vous pouvez sélectionner n'importe quelle ConsolidationFunction de votre choix comme Sum, Count, Average, Max, Min, Product, Distinct Count, etc.

 Aspose.Cells fournit[**Fonction de consolidation**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) énumération pour prendre en charge les fonctions de consolidation suivantes.

- ConsolidationFunction.SUMConsolidationFunction.SUM
- ConsolidationFunction.COUNT
- ConsolidationFunction.AVERAGE
- ConsolidationFunction.MAXConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- Fonction de consolidation.COUNT_NUMS
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.VARConsolidationFunction.VAR
- ConsolidationFunction.VARP
- Fonction de consolidation.DISTINCT_COUNT

### **Application de ConsolidationFunction aux champs de données du tableau croisé dynamique**

 Le code suivant s'applique**MOYEN** fonction de consolidation au premier champ de données (ou champ de valeur) et**STD_DEV** fonction de consolidation au deuxième champ de données (ou champ de valeur).

Un exemple de fichier source et de fichiers de sortie peut être téléchargé ici pour tester l'exemple de code :

[Fichier Excel source](source.xlsx)

[Fichier Excel de sortie](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

La fonction de consolidation DistinctCount est prise en charge par Microsoft Excel 2013 uniquement.

{{% /alert %}}


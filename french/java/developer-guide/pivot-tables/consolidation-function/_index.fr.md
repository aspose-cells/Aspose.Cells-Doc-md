---
title: Fonction de consolidation
type: docs
weight: 20
url: /fr/java/consolidation-function/
description: Appliquer la fonction de consolidation aux champs de données du tableau croisé dynamique.
---

## **Fonction de consolidation**

Aspose.Cells peut être utilisé pour appliquer la fonction de consolidation aux champs de données (ou aux champs de valeur) du tableau croisé dynamique. Dans Microsoft Excel, vous pouvez cliquer avec le bouton droit sur le champ de valeur, puis sélectionner l'option **Paramètres du champ de valeur...** et ensuite sélectionner l'onglet **Recapituler les valeurs par**. À partir de là, vous pouvez sélectionner n'importe quelle fonction de consolidation de votre choix comme Somme, Nombre, Moyenne, Max, Min, Produit, Nombre distinct, etc.

Aspose.Cells fournit une énumération [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) pour prendre en charge les fonctions de consolidation suivantes.

- ConsolidationFunction.SUM
- ConsolidationFunction.COUNT
- ConsolidationFunction.AVERAGE
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP
- ConsolidationFunction.DISTINCT_COUNT

### **Application de la fonction de consolidation aux champs de données d'un tableau croisé dynamique**

Le code suivant applique la fonction de consolidation **MOYENNE** au premier champ de données (ou champ de valeur) et la fonction de consolidation **ÉCARTYPE** au deuxième champ de données (ou champ de valeur).

Le fichier source d'exemple et les fichiers de sortie peuvent être téléchargés ici pour tester le code d'exemple :

[Fichier Excel source](source.xlsx)

[Fichier Excel de sortie](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

La fonction de consolidation ComptageDistinct est prise en charge uniquement par Microsoft Excel 2013.

{{% /alert %}}

{{< app/cells/assistant language="java" >}}

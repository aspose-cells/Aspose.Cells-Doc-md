---
title: Formatage du tableau croisé dynamique
type: docs
weight: 60
url: /fr/java/formatting-pivot-table/
---
## **Apparence du tableau croisé dynamique**

[Comment créer un tableau croisé dynamique](/cells/fr/java/create-pivot-table/) montré comment créer un tableau croisé dynamique simple. Cet article va plus loin et explique comment personnaliser l'apparence d'un tableau croisé dynamique en définissant des propriétés.

### **Définition des options de format de tableau croisé dynamique**

 Le[**Tableau croisé dynamique**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) La classe vous permet de définir diverses options de formatage pour un tableau croisé dynamique.

#### **Définition des types AutoFormat et PivotTableStyle**

 L'exemple de code qui suit illustre comment définir le type de format automatique et le type de style de tableau croisé dynamique à l'aide de la propriété[**TypeFormatAuto**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) et[**Type de style de tableau croisé dynamique**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType) Propriétés.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Définition des options de format**

L'exemple de code qui suit illustre comment définir un certain nombre d'options de mise en forme pour un rapport de tableau croisé dynamique, y compris l'ajout de totaux généraux pour les lignes et les colonnes.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **Définition des options de format des champs croisés dynamiques**

En plus de contrôler la mise en forme du tableau croisé dynamique global, Aspose.Cells for Java permet un contrôle précis de la mise en forme des champs de ligne, des champs de colonne et des champs de page.

#### **Définition du format des champs de ligne, de colonne et de page**

L'exemple de code qui suit montre comment accéder aux champs de ligne, accéder à une ligne particulière, définir des sous-totaux, appliquer un tri automatique et utiliser l'option autoShow.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Définition du format des champs de données**

Les lignes de code suivantes illustrent la mise en forme des champs de données.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Modifier le style rapide d'un tableau croisé dynamique**

Les exemples de code qui suivent montrent comment modifier le style rapide appliqué à un tableau croisé dynamique.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Effacement des champs de pivot**

[**PivotFieldCollectionPivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) a une méthode nommée[**dégager()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear()qui efface les champs de pivot. Utilisez-le pour effacer les champs de pivot dans tous les domaines, par exemple, page, colonne, ligne ou données.
L'exemple de code ci-dessous montre comment effacer tous les champs de pivot dans la zone de données.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Fonction Consolidation**

### **Application de ConsolidationFunction aux champs de données du tableau croisé dynamique**

 Aspose.Cells peut être utilisé pour appliquer ConsolidationFunction aux champs de données (ou champs de valeur) du tableau croisé dynamique. Dans Microsoft Excel, vous pouvez cliquer avec le bouton droit sur le champ de valeur, puis sélectionner**Paramètres du champ de valeur...** l'option puis sélectionnez l'onglet**Résumer les valeurs par**. À partir de là, vous pouvez sélectionner n'importe quelle fonction de consolidation de votre choix comme la somme, le nombre, la moyenne, le maximum, le minimum, le produit, le nombre distinct, etc.

 Aspose.Cells fournit[**Fonction de consolidation**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) énumération pour prendre en charge les fonctions de consolidation suivantes.

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**Fonction de consolidation.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**Fonction de consolidation.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**ConsolidationFunction.MAXConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**ConsolidationFunction.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**ConsolidationFunction.SUMConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VARConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

 Le code suivant s'applique**Moyenne** fonction de consolidation au premier champ de données (ou champ de valeur) et**DistinctCount** fonction de consolidation au deuxième champ de données (ou champ de valeur).

{{% alert color="primary" %}}

La fonction de consolidation DistinctCount est prise en charge par Microsoft Excel 2013 uniquement.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}

---
title: Formatage du tableau croisé dynamique
type: docs
weight: 60
url: /fr/java/formatting-pivot-table/
---

## **Apparence du tableau croisé dynamique**

[Comment créer un tableau croisé dynamique](/cells/fr/java/create-pivot-table/) a montré comment créer un tableau croisé dynamique simple. Cet article va plus loin et discute de la personnalisation de l'apparence d'un tableau croisé dynamique en définissant des propriétés.

### **Configurer les options de formatage du tableau croisé dynamique**

La classe [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) vous permet de définir diverses options de formatage pour un tableau croisé dynamique.

#### **Définition des types de mise en forme automatique et de style de tableau croisé dynamique**

L'exemple de code suivant illustre comment définir le type de mise en forme automatique et le type de style de tableau croisé dynamique en utilisant les propriétés [**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) et [**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Paramétrage des options de formatage**

L'exemple de code suivant illustre comment définir un certain nombre d'options de formatage pour un rapport de tableau croisé dynamique, y compris l'ajout de totaux généraux pour les lignes et les colonnes.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **Configurer les options de formatage des champs de tableau croisé dynamique**

En plus de contrôler le formatage du tableau croisé dynamique global, Aspose.Cells for Java permet un contrôle précis du formatage des champs de ligne, des champs de colonne et des champs de page.

#### **Format des Champs de Ligne, Colonne et Page**

L'exemple de code suivant montre comment accéder aux champs de ligne, accéder à une ligne particulière, définir des sous-totaux, appliquer un tri automatique et utiliser l'option autoShow.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Formatage des Champs de Données**

Les lignes de code suivantes illustrent comment formater les champs de données.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Modifier le Style Rapide d'un Tableau Croisé Dynamique**

Les exemples de code suivants montrent comment modifier le style rapide appliqué à un tableau croisé dynamique.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Effacement des Champs de Tableau Croisé Dynamique**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) a une méthode nommée [**clear()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear--) qui efface les champs de tableau croisé dynamique. Utilisez-la pour effacer les champs de tableau croisé dynamique dans toutes les zones, par exemple, page, colonne, ligne ou données.
L'exemple de code ci-dessous montre comment effacer tous les champs de tableau croisé dynamique dans la zone de données.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Fonction de consolidation**

### **Application de la fonction de consolidation aux champs de données d'un tableau croisé dynamique**

Aspose.Cells peut être utilisé pour appliquer la fonction de consolidation aux champs de données (ou aux champs de valeur) du tableau croisé dynamique. Dans Microsoft Excel, vous pouvez cliquer avec le bouton droit sur le champ de valeur, puis sélectionner l'option **Paramètres du champ de valeur...** et ensuite sélectionner l'onglet **Résumer les valeurs par**. À partir de là, vous pouvez sélectionner n'importe quelle fonction de consolidation de votre choix, comme Somme, Compte, Moyenne, Max, Min, Produit, Comptage distinct, etc.

Aspose.Cells fournit une énumération [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) pour prendre en charge les fonctions de consolidation suivantes.

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**ConsolidationFunction.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT-NUMS)
- [**ConsolidationFunction.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT-COUNT)
- [**ConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**ConsolidationFunction.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD-DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD-DEVP)
- [**ConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

Le code suivant applique la fonction de consolidation **Moyenne** au premier champ de données (ou champ de valeur) et la fonction de consolidation **ComptageDistinct** au deuxième champ de données (ou champ de valeur).

{{% alert color="primary" %}}

La fonction de consolidation ComptageDistinct est prise en charge uniquement par Microsoft Excel 2013.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
{{< app/cells/assistant language="java" >}}

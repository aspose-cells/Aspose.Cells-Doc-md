---
title: Formatage du tableau croisé dynamique
type: docs
weight: 10
url: /fr/net/formatting-pivot-table/
---

## **Apparence du tableau croisé dynamique**

Comment créer un tableau croisé dynamique explique comment créer un tableau croisé dynamique simple. Cet article décrit comment personnaliser l'apparence d'un tableau croisé dynamique en définissant diverses propriétés :

- Options de formatage du tableau croisé dynamique
- Options de formatage des champs de tableau croisé dynamique
- Options de formatage des champs de données

### **Configurer les options de formatage du tableau croisé dynamique**

La classe [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) contrôle le tableau croisé dynamique global et peut être formatée de plusieurs manières.

#### **Définition du type AutoFormat**

Microsoft Excel propose un certain nombre de formats prédéfinis pour les rapports. Aspose.Cells prend également en charge ces options de formatage. Pour y accéder :

1. Définissez [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) sur **true**.
1. Attribuer une option de mise en forme de l'énumération [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **Paramétrage des options de formatage**

L'exemple de code ci-dessous montre comment formater le tableau croisé dynamique pour afficher les totaux généraux pour les lignes et les colonnes, et comment définir l'ordre des champs du rapport. Il montre également comment définir une chaîne personnalisée pour les valeurs nulles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **Aspect et sensation du formatage manuel**

Pour formater manuellement l'apparence du rapport de tableau croisé dynamique, au lieu d'utiliser des formats de rapport prédéfinis, utilisez les méthodes [**PivotTable.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) et [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall). Créez un objet de style pour votre formatage souhaité, par exemple :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **Options de formatage de champ de tableau croisé dynamique**

La classe [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) représente un champ dans une table de données et peut être formatée de plusieurs manières. L'exemple de code ci-dessous montre comment :

- Accéder aux champs de lignes.
- Définir les sous-totaux.
- Définir l'autotri.
- Définir l'auto-affichage.

#### **Formatage des champs de ligne/colonne/page**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **Formatage des champs de données**

L'exemple de code ci-dessous montre comment définir les formats d'affichage et de nombres pour les champs de données.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **Effacement des Champs de Tableau Croisé Dynamique**

La classe [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) possède une méthode nommée [**Clear()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear) qui vous permet d'effacer les champs de table de données. Utilisez-la lorsque vous voulez effacer tous les champs de table de données dans les zones, par exemple, les pages, les colonnes, les lignes ou les données.
L'exemple de code ci-dessous montre comment effacer tous les champs de table de données dans une zone de données.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

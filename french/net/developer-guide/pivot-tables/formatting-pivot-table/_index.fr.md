---
title: Formatage du tableau croisé dynamique
type: docs
weight: 10
url: /fr/net/formatting-pivot-table/
---
## **Apparence du tableau croisé dynamique**

Comment créer un tableau croisé dynamique explique comment créer un tableau croisé dynamique simple. Cet article explique comment personnaliser l'apparence d'un tableau croisé dynamique en définissant diverses propriétés :

- Options de format de tableau croisé dynamique
- Options de format des champs croisés dynamiques
- Options de format de champ de données

### **Définition des options de format de tableau croisé dynamique**

 La[**Tableau croisé dynamique**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)La classe contrôle le tableau croisé dynamique global et peut être formatée de plusieurs façons.

#### **Définition du type de format automatique**

Microsoft Excel propose un certain nombre de formats de rapport prédéfinis différents. Aspose.Cells prend également en charge ces options de formatage. Pour y accéder :

1.  Régler[**PivotTable.IsAutoFormatPivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) à**vrai**.
1.  Attribuez une option de formatage à partir du[**PivotTableAutoFormatTypePivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype)énumération.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **Définition des options de format**

L'exemple de code ci-dessous montre comment formater le tableau croisé dynamique pour afficher les totaux généraux pour les lignes et les colonnes, et comment définir l'ordre des champs du rapport. Il montre également comment définir une chaîne client pour les valeurs nulles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **Mise en forme manuelle de l'aspect et de la convivialité**

 Pour formater manuellement l'apparence du rapport de tableau croisé dynamique, au lieu d'utiliser des formats de rapport prédéfinis, utilisez le[**Tableau croisé dynamique.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) et[**Tableau croisé dynamique.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall)méthodes. Créez un objet de style pour la mise en forme souhaitée, par exemple :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **Définition des options de format de champ croisé dynamique**

 La[**Champ Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)La classe représente un champ dans un tableau croisé dynamique et peut être formatée de plusieurs façons. L'exemple de code ci-dessous montre comment :

- Accéder aux champs de ligne.
- Définition des sous-totaux.
- Réglage du tri automatique.
- Réglage de l'affichage automatique.

#### **Définition du format des champs de ligne/colonne/page**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **Définition du format des champs de données**

L'exemple de code ci-dessous montre comment définir les formats d'affichage et le format numérique pour les champs de données.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **Effacement des champs de pivot**

 La[**PivotFieldCollectionPivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) a une méthode nommée[**Dégager()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear)qui vous permet d'effacer les champs de pivot. Utilisez-le lorsque vous souhaitez effacer tous les champs de pivot dans les zones, par exemple, page, colonne, ligne ou données.
L'exemple de code ci-dessous montre comment effacer tous les champs de pivot dans une zone de données.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}

---
title: Formatage du tableau croisé dynamique
type: docs
weight: 10
url: /fr/net/formatting-pivot-table/
description: Comment formater un tableau croisé dynamique avec Aspose.Cells for Python via .NET.
keywords: Format pivot table.
---
##  **Apparence du tableau croisé dynamique**

Comment créer un tableau croisé dynamique explique comment créer un tableau croisé dynamique simple. Cet article explique comment personnaliser l'apparence d'un tableau croisé dynamique en définissant diverses propriétés :

- Options de format de tableau croisé dynamique
- Options de format des champs croisés dynamiques
- Options de format de champ de données

###  **Définition des options de format de tableau croisé dynamique**

 Le[**Tableau croisé dynamique**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)La classe contrôle le tableau croisé dynamique global et peut être formatée de plusieurs manières.

####  **Définition du type de formatage automatique**

Microsoft Excel propose un certain nombre de formats de rapport prédéfinis. Aspose.Cells for Python via .NET prennent également en charge ces options de formatage. Pour y accéder :

1.  Ensemble[**Tableau croisé dynamique.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/)à *vrai**.
1.  Attribuez une option de formatage à partir du[**Type de format automatique de tableau croisé dynamique**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/)énumération.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

####  **Définition des options de format**

L'exemple de code ci-dessous montre comment formater le tableau croisé dynamique pour afficher les totaux généraux des lignes et des colonnes, et comment définir l'ordre des champs du rapport. Il montre également comment définir une chaîne client pour les valeurs nulles.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

####  **Formatage manuel de l'apparence et de la convivialité**

Pour formater manuellement l'apparence du rapport de tableau croisé dynamique, au lieu d'utiliser des formats de rapport prédéfinis, utilisez l'option[**Tableau croisé dynamique.format_all(style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) et[**PivotTable.format (ligne, colonne, style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/)méthodes. Créez un objet de style pour le formatage souhaité, par exemple :

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

###  **Définition des options de format de champ pivot**

 Le[**Champ Pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)La classe représente un champ dans un tableau croisé dynamique et peut être formatée de plusieurs manières. L'exemple de code ci-dessous montre comment :

- Accédez aux champs de ligne.
- Définition des sous-totaux.
- Définition du tri automatique.
- Configuration de l'affichage automatique.

####  **Définition du format des champs de ligne/colonne/page**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

###  **Définition du format des champs de données**

L'exemple de code ci-dessous montre comment définir les formats d'affichage et le format numérique pour les champs de données.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

###  **Effacement des champs pivots**

 Le[**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) a une méthode nommée[**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#)qui vous permet d'effacer les champs pivots. Utilisez-le lorsque vous souhaitez effacer tous les champs pivots dans les zones, par exemple page, colonne, ligne ou données.
L'exemple de code ci-dessous montre comment effacer tous les champs pivots dans une zone de données.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}

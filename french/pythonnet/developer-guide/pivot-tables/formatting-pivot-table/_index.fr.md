---
title: Formatage du tableau croisé dynamique
type: docs
weight: 10
url: /fr/python-net/formatting-pivot-table/
description: Comment formater un tableau croisé dynamique avec Aspose.Cells pour Python via .NET.
keywords: Formater un tableau croisé dynamique.
---

## **Apparence du tableau croisé dynamique**

Comment créer un tableau croisé dynamique explique comment créer un tableau croisé dynamique simple. Cet article décrit comment personnaliser l'apparence d'un tableau croisé dynamique en définissant diverses propriétés :

- Options de formatage du tableau croisé dynamique
- Options de formatage des champs de tableau croisé dynamique
- Options de formatage des champs de données

### **Comment définir les options de formatage du tableau croisé dynamique**

La classe [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) contrôle le tableau croisé dynamique global et peut être formatée de plusieurs manières.

#### **Comment définir le type de mise en forme automatique**

Microsoft Excel propose différents formats de rapport prédéfinis. Aspose.Cells for Python via .NET prend également en charge ces options de mise en forme. Pour y accéder :

1. Définissez [**PivotTable.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/) sur **true**.
1. Attribuer une option de mise en forme de l'énumération [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

#### **Comment définir les options de mise en forme**

L'exemple de code ci-dessous montre comment formater le tableau croisé dynamique pour afficher les totaux généraux pour les lignes et les colonnes, et comment définir l'ordre des champs du rapport. Il montre également comment définir une chaîne personnalisée pour les valeurs nulles.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

#### **Aspect et sensation du formatage manuel**

Pour formater manuellement l'aspect du rapport de table de données, au lieu d'utiliser des formats de rapport prédéfinis, utilisez les méthodes [**PivotTable.format_all(style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) et [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/). Créez un objet de style pour le format souhaité, par exemple :

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

### **Comment définir les options de format de champ de table de données**

La classe [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) représente un champ dans une table de données et peut être formatée de plusieurs manières. L'exemple de code ci-dessous montre comment :

- Accéder aux champs de lignes.
- Définir les sous-totaux.
- Définir l'autotri.
- Définir l'auto-affichage.

#### **Comment définir le format des champs de lignes/colonnes/page**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

### **Comment définir le format des champs de données**

L'exemple de code ci-dessous montre comment définir les formats d'affichage et de nombres pour les champs de données.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

### **Comment effacer les champs de table de données**

La classe [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) possède une méthode nommée [**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#) qui vous permet d'effacer les champs de table de données. Utilisez-la lorsque vous voulez effacer tous les champs de table de données dans les zones, par exemple, les pages, les colonnes, les lignes ou les données.
L'exemple de code ci-dessous montre comment effacer tous les champs de table de données dans une zone de données.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}

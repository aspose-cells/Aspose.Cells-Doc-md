---
title: Formatage du tableau croisé dynamique
type: docs
weight: 10
url: /fr/nodejs-cpp/formatting-pivot-table/
description: Comment formater le tableau croisé dynamique avec Aspose.Cells for Node.js via C++.
keywords: Formater un tableau croisé dynamique.
---

## **Apparence du tableau croisé dynamique**

Comment créer un tableau croisé dynamique explique comment créer un tableau croisé dynamique simple. Cet article décrit comment personnaliser l'apparence d'un tableau croisé dynamique en définissant diverses propriétés :

- Options de formatage du tableau croisé dynamique
- Options de formatage des champs de tableau croisé dynamique
- Options de formatage des champs de données

### **Comment définir les options de formatage du tableau croisé dynamique**

La classe [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/) contrôle le tableau croisé dynamique global et peut être formatée de plusieurs manières.

#### **Comment définir le type de mise en forme automatique**

Microsoft Excel offre plusieurs formats de rapports pré-configurés. Aspose.Cells for Node.js via C++ prend également en charge ces options de mise en forme. Pour y accéder :

1. Définissez [**PivotTable.setIsAutoFormat(value)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsAutoFormat-boolean-) sur **true**.
1. Attribuer une option de mise en forme de l'énumération [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/nodejs-cpp/pivottableautoformattype/).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingAutoFormat-1.js" >}}

#### **Comment définir les options de mise en forme**

L'exemple de code ci-dessous montre comment formater le tableau croisé dynamique pour afficher les totaux généraux pour les lignes et les colonnes, et comment définir l'ordre des champs du rapport. Il montre également comment définir une chaîne personnalisée pour les valeurs nulles.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingFormatOptions-1.js" >}}

#### **Aspect et sensation du formatage manuel**

Pour formater manuellement l'aspect du rapport de table de données, au lieu d'utiliser des formats de rapport prédéfinis, utilisez les méthodes [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) et [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-). Créez un objet de style pour le format souhaité, par exemple :

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FormattingLook-1.js" >}}

### **Comment définir les options de format de champ de table de données**

La classe [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/) représente un champ dans une table de données et peut être formatée de plusieurs manières. L'exemple de code ci-dessous montre comment :

- Accéder aux champs de lignes.
- Définir les sous-totaux.
- Définir l'autotri.
- Définir l'auto-affichage.

#### **Comment définir le format des champs de lignes/colonnes/page**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingPageFieldFormat-1.js" >}}

### **Comment définir le format des champs de données**

L'exemple de code ci-dessous montre comment définir les formats d'affichage et de nombres pour les champs de données.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingDataFieldFormat-1.js" >}}

### **Comment effacer les champs de table de données**

La classe [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/) possède une méthode nommée [**clear()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/#clear--) qui vous permet d'effacer les champs de table de données. Utilisez-la lorsque vous voulez effacer tous les champs de table de données dans les zones, par exemple, les pages, les colonnes, les lignes ou les données.
L'exemple de code ci-dessous montre comment effacer tous les champs de table de données dans une zone de données.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ClearPivotFields-1.js" >}}

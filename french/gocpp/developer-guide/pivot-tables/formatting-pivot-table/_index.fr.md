---
title: Mise en forme du tableau croisé dynamique avec Golang via C++
linktitle: Formatage du tableau croisé dynamique
type: docs
weight: 10
url: /fr/go-cpp/formatting-pivot-table/
description: Apprenez comment personnaliser l’apparence des tableaux croisés dynamiques en utilisant Aspose.Cells for C++.
---

## **Apparence du tableau croisé dynamique**

Comment créer un tableau croisé dynamique explique comment créer un tableau croisé dynamique simple. Cet article décrit comment personnaliser l'apparence d'un tableau croisé dynamique en définissant diverses propriétés :

- Options de formatage du tableau croisé dynamique
- Options de formatage des champs de tableau croisé dynamique
- Options de formatage des champs de données

### **Configurer les options de formatage du tableau croisé dynamique**

La classe [**PivotTable**](https://reference.aspose.com/cells/go-cpp/pivottable/) contrôle le tableau croisé dynamique global et peut être formatée de plusieurs manières.

#### **Définition du type AutoFormat**

Microsoft Excel propose plusieurs formats de rapport prédéfinis. Aspose.Cells prend également en charge ces options de mise en forme. Pour y accéder :

1. Définissez [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/go-cpp/pivottable/isautoformat/) sur **true**.
1. Attribuer une option de mise en forme de l'énumération [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/go-cpp/pivottableautoformattype/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable.go" >}}
#### **Paramétrage des options de formatage**

Le code ci-dessous montre comment formater le tableau croisé dynamique pour afficher les totaux généraux pour les lignes et les colonnes, et comment définir l’ordre des champs du rapport. Il montre aussi comment définir une chaîne personnalisée pour les valeurs nulles.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-1.go" >}}
#### **Aspect et sensation du formatage manuel**

Pour formater manuellement l’apparence du rapport du tableau croisé dynamique sans utiliser les formats de rapport prédéfinis, utilisez les méthodes [**PivotTable.Format()**](https://reference.aspose.com/cells/go-cpp/pivottable/format_pivotarea_style/) et [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/). Créez un objet style avec le format souhaité, par exemple :

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-2.go" >}}
### **Options de formatage de champ de tableau croisé dynamique**

La classe [**PivotField**](https://reference.aspose.com/cells/go-cpp/pivotfield/) représente un champ dans une table de données et peut être formatée de plusieurs manières. L'exemple de code ci-dessous montre comment :

- Accéder aux champs de lignes.
- Définir les sous-totaux.
- Définir l'autotri.
- Définir l'auto-affichage.

#### **Formatage des champs de ligne/colonne/page**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-3.go" >}}
### **Formatage des Champs de Données**

L'exemple de code ci-dessous montre comment définir les formats d'affichage et de nombres pour les champs de données.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-4.go" >}}
### **Effacement des Champs de Tableau Croisé Dynamique**

La classe [**PivotFieldCollection**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/) possède une méthode nommée [**Clear()**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/clear/) qui vous permet d'effacer les champs de table de données. Utilisez-la lorsque vous voulez effacer tous les champs de table de données dans les zones, par exemple, les pages, les colonnes, les lignes ou les données.
L'exemple de code ci-dessous montre comment effacer tous les champs de table de données dans une zone de données.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-5.go" >}}

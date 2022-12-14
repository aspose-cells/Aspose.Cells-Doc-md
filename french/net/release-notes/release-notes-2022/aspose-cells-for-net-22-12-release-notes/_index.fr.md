---
title: Aspose.Cells for .NET 22.12 Notes de mise à jour
type: docs
weight: 1
url: /fr/net/aspose-cells-for-net-22-12-release-notes/
---
{{% alert color="primary" %}}

 Cette page contient des notes de version pour[Aspose.Cells for .NET 22.12](https://www.nuget.org/packages/Aspose.Cells/22.12.0).

{{% /alert %}}

|**Clé**|**Sommaire**|**Catégorie**|
|:- |:- |:- |
|CELLSNET-42315|Prise en charge des fichiers crtx - application de modèles de graphiques personnalisés|
|CELLSNET-47895|Les images sont déformées dans le rendu Excel vers PDF/HTML|
|CELLSNET-47946|L'effet de rotation de l'image ne s'affiche pas correctement en pdf/html|
|CELLSNET-47947|L'effet de rotation de la boîte rectangulaire dans le groupe graphique ne s'affiche pas correctement en pdf/html|
|CELLSNET-52126|Certaines formes sont modifiées après la conversion du fichier Excel en PDF|
|CELLSNET-52197|Boîtes modifiées lors de la conversion d'un document XLSX en PDF|
|CELLSNET-52330|Les formes de dessin ne sont pas bien rendues en HTML|
|CELLSNET-50042| Le nom défini est modifié après ré-enregistrement|
|CELLSNET-52270|La fonction YEARFRAC n'est pas calculée correctement|
|CELLSNET-52305|MMULT avec OFFSET n'est pas calculé correctement|
|CELLSNET-52307|La formule du lien brisé renvoie 0 au lieu de #REF !|
|CELLSNET-52325| Workbook.CalculateFormula se bloque dans certaines circonstances|
|CELLSNET-52387|Cell les références aux tables entraînent des erreurs #REF après la suppression des colonnes|
|CELLSNET-52290|L'axe des graphiques n'est pas capturé correctement|
|CELLSNET-52301|Graphique XLSX vers image : les barres de graphique combinées personnalisées ne sont pas rendues correctement|
|CELLSNET-52336|L'histogramme n'est pas rendu correctement dans la conversion XLSX vers HTML/PDF|
|CELLSNET-52292|Le texte s'affiche sur la mauvaise page dans le PDF de sortie - Conversion d'Excel en PDF|
|CELLSNET-52367|AutofitRows entraîne un texte tronqué dans la sortie de conversion PDF|
|CELLSNET-52242|La hiérarchie parent-enfant est incorrecte lors de la conversion d'Excel en JSON et vice versa|
|CELLSNET-52281|L'en-tête Json ne peut pas être ignoré|
|CELLSNET-52289|Le format numérique est perdu lors de la conversion de HTML en Excel|
|CELLSNET-52298|L'option Tri automatique est activée pour le champ pivot lors de la ré-enregistrement de XLSX|
|CELLSNET-52299| L'attribut HasRevisions est incorrect après l'enregistrement d'un classeur|
|CELLSNET-52332|Les nombres sont affichés sous forme de '#' ou de nombre scientifique lors de la conversion en html|
|CELLSNET-52338| Le HTML de sortie est non déterministe|
|CELLSNET-52344|Les hyperliens sont manquants dans la conversion HTML vers JSON|

## **Public API et modifications incompatibles avec les versions antérieures**

Voici une liste de toutes les modifications apportées au public API, telles que les membres ajoutés, renommés, supprimés ou obsolètes, ainsi que toute modification non rétrocompatible apportée à Aspose.Cells for .NET. Si vous avez des inquiétudes concernant l'un des changements répertoriés, veuillez le signaler sur le forum d'assistance Aspose.Cells.

### **Ajoute l'énumération JsonExportHyperlinkType**

Représente le type d'exportation de lien hypertexte vers des fichiers JSON.

### **Ajoute JsonUtility.ExportRangeToJson(Range, JsonSaveOptions) et rend obsolète la méthode ExportRangeToJson(Range, ExportRangeToJsonOptions)**

Utilisez plutôt JsonUtility.ExportRangeToJson(Range, JsonSaveOptions).

### **Ajoute la propriété PivotTable.DataFieldHeaderName**

Obtient et définit le nom de l'en-tête de champ de la zone de valeur dans le tableau croisé dynamique.

### **Ajoute la méthode de remplacement Range.SetStyle(Style,System.Boolean)**

N'écraser que la mise en forme qui est explicitement définie lorsque l'indicateur est défini

### **Ajoute la propriété PivotField.NonAutoSortDefault**

Indique si une opération de tri qui sera appliquée à ce champ pivot est une opération de tri automatique ou un simple tri de données.

### **Ajoute la méthode GlobalizationSettings.GetDataFieldHeaderNameOfPivotTable()**

Obtient le nom local de l'en-tête de champ de la zone de valeur dans le tableau croisé dynamique.

### **Ajoute la propriété Chart.PlotVisibleCellsOnly et rend obsolète la propriété Chart.PlotVisibleCells.**

Utilisez plutôt la propriété Chart.PlotVisibleCellsOnly.

### **Ajoute la propriété JsonSaveOptions.ExportEmptyCells.**

Indique si les cellules vides sont exportées comme nulles.

### **Ajoute la propriété JsonSaveOptions.ExportHyperlinkType.**

Représente le type de lien hypertexte d'exportation vers json.

### **Ajoute la propriété JsonSaveOptions.ExportNestedStructure.**

Exporté en tant que structure Json de hiérarchie parent-enfant.

### **Ajoute la propriété JsonSaveOptions.SkipEmptyRows.**

Indique si les lignes vides sont ignorées.

### **Supprime la méthode obsolète SheetRender.GetPageSize(System.Int32)**

Utilisez plutôt SheetRender.GetPageSizeInch(System.Int32).

### **Supprime la méthode obsolète WorkbookRender.GetPageSize(System.Int32)**

Utilisez plutôt WorkbookRender.GetPageSizeInch(System.Int32).

### **Supprime les énumérations AutoShapeType.TextWave3 et AutoShapeType.TextWave4 obsolètes**

Utilisez UseAutoShape.TextDoubleWave1 et UseAutoShape.TextDoubleWave2 à la place.

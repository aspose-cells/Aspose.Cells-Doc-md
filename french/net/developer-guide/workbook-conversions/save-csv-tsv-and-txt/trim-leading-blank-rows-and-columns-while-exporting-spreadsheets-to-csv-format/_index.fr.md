---
title: Coupez les premières lignes et colonnes vides lors de l'exportation des feuilles de calcul au format CSV
type: docs
weight: 100
url: /fr/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---
## **Scénarios d'utilisation possibles**

Parfois, votre fichier Excel ou CSV comporte des colonnes ou des lignes vides. Par exemple, considérons cette ligne

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

Ici, les trois premières cellules ou colonnes sont vides. Lorsque vous ouvrez un tel fichier CSV dans Microsoft Excel, puis Microsoft Excel ignore ces premières lignes et colonnes vides.

 Par défaut, Aspose.Cells ne supprime pas les premières colonnes et lignes vides lors de l'enregistrement, mais si vous souhaitez les supprimer comme le fait Microsoft Excel, alors Aspose.Cells fournit**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** la propriété. Veuillez le régler sur**vrai**puis toutes les premières lignes et colonnes vides seront supprimées lors de l'enregistrement.

{{% alert color="primary" %}}

 Avant la publication de Aspose.Cells for .NET 20.4, la valeur par défaut de**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** a été**faux** . Depuis la version 20.4, la valeur par défaut de**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** est**vrai.**

{{% /alert %}}

## **Coupez les premières lignes et colonnes vides lors de l'exportation des feuilles de calcul au format CSV**

 L'exemple de code suivant charge le[fichier excel source](sampleTrimBlankColumns.xlsx) qui a deux premières colonnes vides. Il enregistre d'abord le fichier Excel au format CSV sans aucune modification, puis il définit**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** propriété à**vrai** et l'enregistre à nouveau. La capture d'écran montre le[fichier excel source](sampleTrimBlankColumns.xlsx), [fichier de sortie CSV sans rognage](outputWithoutTrimBlankColumns.csv), et le[fichier de sortie CSV avec rognage](outputTrimBlankColumns.csv).

![tâche : image_autre_texte](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}

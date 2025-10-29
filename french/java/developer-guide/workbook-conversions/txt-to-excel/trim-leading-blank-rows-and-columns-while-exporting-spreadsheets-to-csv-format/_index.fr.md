---
title: Supprimer les lignes et colonnes vides initiales lors de l exportation de feuilles de calcul au format CSV
type: docs
weight: 50
url: /fr/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **Scénarios d'utilisation possibles**

Parfois, votre fichier Excel ou CSV contient des colonnes ou des lignes vides initiales. Par exemple, considérez cette ligne

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Ici, les trois premières cellules ou colonnes sont vides. Lorsque vous ouvrez un tel fichier CSV dans Microsoft Excel, Microsoft Excel ignore ces lignes et colonnes vides initiales.

Par défaut, Aspose.Cells ne supprime pas les colonnes et lignes vides de tête lors de l'enregistrement, mais si vous souhaitez les supprimer comme le fait Microsoft Excel, alors Aspose.Cells fournit la propriété [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn). Veuillez la définir sur **true** et ensuite toutes les colonnes et lignes vides de tête seront supprimées lors de l'enregistrement.

{{% alert color="primary" %}}

Avant la sortie de Aspose.Cells for Java 20.4, la valeur par défaut de [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) était **fausse**. Depuis la version 20.4, la valeur par défaut de [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) est **vraie.**

{{% /alert %}}

## **Supprimer les lignes et colonnes vides en tête lors de l'exportation de feuilles de calcul au format CSV**

Le code d'exemple suivant charge le fichier Excel source qui comporte deux colonnes vides de tête. Il enregistre d'abord le fichier Excel au format CSV sans apporter de modifications, puis il définit la propriété [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) sur **true** et l'enregistre à nouveau. La capture d'écran montre le [fichier Excel source](sampleTrimBlankColumns.xlsx), [fichier CSV de sortie sans élagage des colonnes vides](outputWithoutTrimBlankColumns.csv) et le [fichier CSV de sortie avec élagage](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
{{< app/cells/assistant language="java" >}}

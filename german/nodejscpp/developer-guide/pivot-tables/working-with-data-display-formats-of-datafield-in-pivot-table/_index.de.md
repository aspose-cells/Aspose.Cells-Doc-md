---
title: Arbeiten mit Datenanzeigeformaten von DataField im Pivot Table
type: docs
weight: 140
url: /de/nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ unterstützt alle Datenanzeigeformate von DataField.

{{% /alert %}}

## **"Rang Kleinste bis Größte" und "Rang Größte bis Kleinste" Anzeigeformat-Option**

Aspose.Cells bietet die Möglichkeit, die Anzeigeformatoption für Pivot-Felder festzulegen. Hierfür stellt die API die Eigenschaft [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-) bereit. Um von größtem nach kleinstem Rang zu ordnen, können Sie die [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-) Eigenschaft auf [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/nodejs-cpp/pivotfielddatadisplayformat/) setzen. Der folgende Codeausschnitt zeigt das Festlegen der Anzeigeformatoptionen.

Die Beispielsquell- und Ausgabedateien können hier für das Testen des Beispielcodes heruntergeladen werden:

[Quell-Excel-Datei](101089332.xlsx)

[Ausgabe-Excel-Datei](101089333.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTableDataDisplayFormatRanking-1.js" >}}


---
title: Enregistrer les feuilles de calcul spécifiées au PDF
type: docs
weight: 140
url: /fr/net/save-specified-worksheets-to-pdf/
---
 Par défaut, Aspose.Cells enregistre tout**visible** feuilles de calcul dans un classeur en fichier pdf. Avec**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** option, vous pouvez enregistrer des feuilles de calcul spécifiées dans un fichier pdf. par exemple, vous pouvez enregistrer la feuille de calcul active au format pdf, enregistrer toutes les feuilles de calcul (feuilles de calcul visibles et masquées) au format pdf, enregistrer plusieurs feuilles de calcul personnalisées au format pdf.

##  **Enregistrer la feuille de calcul active au PDF**

 Si vous souhaitez uniquement exporter la feuille active au format pdf, vous pouvez y parvenir en passant**[`SheetSet.Active`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/)** pour**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** option.

 La fiche `Sheet2` est la fiche active du fichier source[sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

##  **Enregistrer toutes les feuilles de calcul au PDF**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/)** indique les feuilles visibles dans un classeur, et**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)** indique toutes les feuilles, y compris les feuilles visibles et les feuilles masquées/invisibles dans un classeur. Si vous souhaitez exporter toutes les feuilles au format pdf, vous pouvez simplement passer**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)** pour**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** option.

 Le fichier source[sheetset-example.xlsx](sheetset-example.xlsx) contient les quatre feuilles avec feuille cachée `Sheet3`.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

##  **Enregistrer les feuilles de calcul spécifiées au PDF**
 Si vous souhaitez exporter plusieurs feuilles souhaitées/personnalisées au format pdf, vous pouvez y parvenir en transmettant plusieurs index de feuille à**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** option.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

Si votre feuille de calcul contient des formules, il est préférable d'appeler le [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le fichier PDF.

{{% /alert %}}

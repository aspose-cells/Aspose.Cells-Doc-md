---
title: Enregistrer des feuilles de calcul spécifiées en PDF
type: docs
weight: 140
url: /fr/net/save-specified-worksheets-to-pdf/
---

Par défaut, Aspose.Cells enregistre toutes les feuilles de calcul **visibles** dans un classeur au format PDF. Avec l'option [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/), vous pouvez enregistrer des feuilles de calcul spécifiées au format PDF. Par exemple, vous pouvez enregistrer la feuille active au format PDF, enregistrer toutes les feuilles de calcul (à la fois les feuilles visibles et cachées) au format PDF, enregistrer des feuilles de calcul multiples personnalisées au format PDF.

## **Enregistrer la feuille de calcul active en PDF**

Si vous voulez exporter uniquement la feuille active en pdf, vous pouvez y parvenir en passant [**SheetSet.Active**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/) à l'option [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/).

La feuille `Sheet2` est la feuille active du fichier source [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

## **Enregistrer toutes les feuilles de calcul en PDF**

[**SheetSet.Visible**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/) indique les feuilles visibles dans un classeur, et [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) indique toutes les feuilles, y compris les feuilles visibles et masquées/invisibles dans un classeur. Si vous voulez exporter toutes les feuilles en pdf, vous pouvez simplement passer [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) à l'option [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/).

Le fichier source [sheetset-example.xlsx](sheetset-example.xlsx) contient les quatre feuilles avec la feuille cachée `Sheet3`.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

## **Enregistrer des feuilles de calcul spécifiées au format PDF**
Si vous souhaitez exporter des feuilles multiples désirées/personnalisées en pdf, vous pouvez y parvenir en passant les indices de feuille multiples à l'option [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

## **Réorganiser les feuilles de calcul en PDF**

Si vous souhaitez réorganiser les feuilles (par exemple, en ordre inverse) en PDF sans modifier le fichier source, vous pouvez le faire en passant les indices des feuilles réarrangées à l'option [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ReorderSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

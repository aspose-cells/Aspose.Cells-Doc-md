---
title: Enregistrer les feuilles de calcul spécifiées au PDF
type: docs
weight: 140
url: /fr/python-net/save-specified-worksheets-to-pdf/
description: Découvrez comment enregistrer les feuilles de calcul spécifiées au PDF avec Aspose.Cells for Python via .NET API.
keywords: Python Save Active Worksheet to PDF, Save All Worksheets to PDF, Save Specified Worksheets to PDF
---
 Par défaut, Aspose.Cells for Python via .NET enregistre tout**visible** feuilles de calcul dans un classeur en fichier pdf. Avec**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** option, vous pouvez enregistrer les feuilles de calcul spécifiées dans un fichier pdf. Par exemple, vous pouvez enregistrer une feuille de calcul active au format PDF, enregistrer toutes les feuilles de calcul (feuilles de calcul visibles et masquées) au format PDF, enregistrer plusieurs feuilles de calcul personnalisées au format PDF.

##  **Enregistrer la feuille de travail active au PDF**

Si vous souhaitez exporter uniquement la feuille active au format PDF, vous pouvez y parvenir en passant**[`SheetSet.active`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/)** à**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** option.

 La feuille `Sheet2` est la feuille active du fichier source[exemple-ensemble de feuilles.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

##  **Enregistrez toutes les feuilles de travail au PDF**

**[`SheetSet.visible`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/)** indique les feuilles visibles dans un classeur, et**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** indique toutes les feuilles, y compris les feuilles visibles et les feuilles masquées/invisibles dans un classeur. Si vous souhaitez exporter toutes les feuilles au format PDF, vous pouvez simplement passer**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** à**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** option.

 Le fichier source[exemple-ensemble de feuilles.xlsx](sheetset-example.xlsx) contient les quatre feuilles avec la feuille cachée `Sheet3`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

##  **Enregistrer les feuilles de calcul spécifiées au PDF**
 Si vous souhaitez exporter plusieurs feuilles souhaitées/personnalisées au format PDF, vous pouvez y parvenir en transmettant plusieurs index de feuille à**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** option.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

 Si votre feuille de calcul contient des formules, il est préférable d'appeler[**Classeur.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}

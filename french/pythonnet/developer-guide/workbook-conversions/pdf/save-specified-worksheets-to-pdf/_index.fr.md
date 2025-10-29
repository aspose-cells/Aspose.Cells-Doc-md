---
title: Enregistrer des feuilles de calcul spécifiées en PDF
type: docs
weight: 140
url: /fr/python-net/save-specified-worksheets-to-pdf/
description: Apprenez comment enregistrer des feuilles de calcul spécifiées en PDF avec l API Aspose.Cells pour Python via .NET.
keywords: Enregistrer la feuille de calcul active en PDF, enregistrer toutes les feuilles de calcul en PDF, enregistrer des feuilles de calcul spécifiques en PDF
---

Par défaut, Aspose.Cells pour Python via .NET enregistre toutes les feuilles de calcul **visibles** dans un classeur au format pdf. Avec l'option [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/), vous pouvez enregistrer des feuilles de calcul spécifiées dans un fichier pdf, par exemple, vous pouvez enregistrer la feuille de calcul active en pdf, enregistrer toutes les feuilles de calcul (à la fois visibles et masquées) en pdf, enregistrer plusieurs feuilles de calcul personnalisées en pdf.

## **Enregistrer la feuille de calcul active en PDF**

Si vous voulez exporter uniquement la feuille active en pdf, vous pouvez y parvenir en passant [**SheetSet.active**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/) à l'option [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/).

La feuille `Sheet2` est la feuille active du fichier source [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

## **Enregistrer toutes les feuilles de calcul en PDF**

[**SheetSet.visible**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/) indique les feuilles visibles dans un classeur, et [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) indique toutes les feuilles, y compris les feuilles visibles et masquées/invisibles dans un classeur. Si vous voulez exporter toutes les feuilles en pdf, vous pouvez simplement passer [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) à l'option [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/).

Le fichier source [sheetset-example.xlsx](sheetset-example.xlsx) contient les quatre feuilles avec la feuille cachée `Sheet3`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

## **Enregistrer des feuilles de calcul spécifiées au format PDF**
Si vous souhaitez exporter des feuilles multiples désirées/personnalisées en pdf, vous pouvez y parvenir en passant les indices de feuille multiples à l'option [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}

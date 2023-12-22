---
title: Évitez les pages vierges dans la sortie PDF lorsqu'il n'y a rien à imprimer
type: docs
weight: 30
url: /fr/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Découvrez comment éviter une page vierge dans la sortie PDF lorsqu'il n'y a rien à imprimer avec Aspose.Cells for Python via .NET API.
keywords: Python Avoid Blank Page in Output PDF when there is Nothing to Print
---
##  **Scénarios d'utilisation possibles**

Lorsque le fichier Excel est vide et que l'utilisateur l'enregistre sous PDF en utilisant Aspose.Cells for Python via .NET, une page vierge apparaît dans la sortie PDF. Parfois, ce comportement par défaut n'est pas souhaitable. Aspose.Cells for Python via .NET fournit le[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)propriété pour traiter ce problème. Si vous le définissez sur *false**, alors[**CellulesException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)se produira chaque fois qu'il n'y aura rien à imprimer dans la sortie PDF.

##  **Évitez les pages vierges dans la sortie PDF lorsqu'il n'y a rien à imprimer**

L'exemple de code suivant crée un classeur vide, puis l'enregistre sous le nom PDF après avoir défini le[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)propriété comme *faux**. Puisqu'il n'y a rien à imprimer dans la sortie PDF, le[**CellulesException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)se produit comme indiqué ci-dessous.

##  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

##  **Exception**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}

---
title: Éviter une page vierge dans le PDF de sortie lorsqu il n y a rien à imprimer
type: docs
weight: 30
url: /fr/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Apprenez comment éviter une page blanche dans le PDF de sortie lorsqu il n y a rien à imprimer avec Aspose.Cells pour l API Python via .NET.
keywords: Éviter la page blanche dans le PDF de sortie lorsqu il n y a rien à imprimer en Python
---

## **Scénarios d'utilisation possibles**

Lorsque le fichier Excel est vide et que l'utilisateur le sauvegarde en PDF à l'aide d'Aspose.Cells pour l'API Python via .NET, il affiche une page blanche dans le PDF de sortie. Parfois, ce comportement par défaut est indésirable. Aspose.Cells pour l'API Python via .NET fournit la propriété [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) pour gérer ce problème. Si vous le définissez sur **false**, alors [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) se produira chaque fois qu'il n'y aura rien à imprimer dans le PDF de sortie.

## **Éviter la page blanche dans le PDF final lorsqu'il n'y a rien à imprimer**

Le code d'exemple suivant crée un classeur vide, puis le sauve sous forme de PDF après avoir défini la propriété [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) sur **false**. Comme il n'y a rien à imprimer dans le PDF de sortie, [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) se produit comme indiqué ci-dessous.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

## **Exception**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}

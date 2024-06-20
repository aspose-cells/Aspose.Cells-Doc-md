---
title: Verificare se il foglio di lavoro è un foglio di dialogo
type: docs
weight: 70
url: /it/python-java/find-if-the-worksheet-is-dialog-sheet/
---

## **Possibili Scenari di Utilizzo**
Dialog Sheet è un vecchio formato del foglio che contiene una finestra di dialogo. Tale foglio potrebbe essere inserito da una versione più vecchia di Microsoft Excel ad esempio 2003 come mostrato in questa schermata. Può anche essere inserito con VBA in versioni più recenti ad esempio Microsoft Excel 2016.

![todo:image_alt_text](DialogSheet.png)
## **Trova se il foglio di lavoro è un foglio di dialogo**
Aspose.Cells for Python via Java ti offre la possibilità di verificare se il foglio di lavoro è un foglio di dialogo. A questo scopo, fornisce la proprietà [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type). Se [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type) restituisce il valore di enumerazione [SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG), significa che stai lavorando con un foglio di dialogo.

Il seguente frammento di codice mostra come verificare un foglio di dialogo. L'output della console generato dal codice è fornito di seguito a titolo di riferimento.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **Output della console**
{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}

---
title: Verificare se il foglio di lavoro è un foglio di dialogo
type: docs
weight: 90
url: /it/net/find-if-the-worksheet-is-dialog-sheet/
description: Il foglio di dialogo è un vecchio formato di foglio. Questo articolo fornisce istruzioni e codice di esempio per determinare in modo programmato se un foglio di lavoro di Excel è un foglio di dialogo utilizzando l API C# o la libreria .NET.
keywords: trova excel worksheet dialog type c#, dialog worksheet c#
---

## **Possibili Scenari di Utilizzo**

Il foglio di dialogo è un vecchio formato di foglio che contiene una finestra di dialogo. Tale foglio potrebbe essere stato inserito da una versione precedente di Microsoft Excel, ad esempio la versione 2003 come mostrato in questa schermata. Può anche essere inserito con VBA nelle nuove versioni, ad esempio Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

È possibile verificare se il foglio è un foglio di dialogo o un altro tipo di foglio con la proprietà [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type) fornita da Aspose.Cells. Se restituisce il valore di enumerazione [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), significa che si tratta di un foglio di dialogo.

## **Trova se il foglio di lavoro è un foglio di dialogo**

Il seguente codice di esempio carica il [file Excel di esempio](64716820.xlsx) che contiene un foglio di dialogo. Controlla la proprietà [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type), la confronta con [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) e quindi stampa il messaggio. Si prega di vedere l'output della console del codice di esempio qui sotto per ulteriori informazioni.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **Output della console**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}

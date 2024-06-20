---
title: Verificare se il foglio di lavoro è un foglio di dialogo
type: docs
weight: 100
url: /it/java/find-if-the-worksheet-is-dialog-sheet/
---

## **Possibili Scenari di Utilizzo**

Dialog Sheet è un vecchio formato del foglio che contiene una finestra di dialogo. Tale foglio potrebbe essere inserito da una versione più vecchia di Microsoft Excel ad esempio 2003 come mostrato in questa schermata. Può anche essere inserito con VBA in versioni più recenti ad esempio Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

È possibile verificare se il foglio è un foglio di dialogo o un altro tipo di foglio con la proprietà [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) fornita da Aspose.Cells. Se restituisce il valore di enumerazione [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG), significa che si sta trattando di un foglio di dialogo.

## **Trova se il foglio di lavoro è un foglio di dialogo**

Il seguente codice di esempio carica il [file Excel di esempio](64716841.xlsx) che contiene un foglio di dialogo. Controlla la proprietà [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) la confronta con [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG) e quindi stampa il messaggio. Si prega di consultare l'output della console del codice di esempio qui sotto per ulteriori informazioni.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Output della console**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}

---
title: Trova se il foglio di lavoro è Foglio di dialogo
type: docs
weight: 100
url: /it/java/find-if-the-worksheet-is-dialog-sheet/
---
## **Possibili scenari di utilizzo**

Foglio di dialogo è un vecchio formato del foglio che contiene una finestra di dialogo. Tale foglio potrebbe essere inserito da una versione precedente di Microsoft Excel, ad esempio 2003, come mostrato in questa schermata. Può anche essere inserito con VBA nelle versioni più recenti, ad esempio Microsoft Excel 2016.

![cose da fare:immagine_alt_testo](find-if-the-worksheet-is-dialog-sheet_1.png)

Puoi scoprire se il foglio è un foglio di dialogo o qualche altro tipo di foglio con[**Foglio.Tipo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)proprietà fornita da Aspose.Cells. Se restituisce il valore di enumerazione[**TipoFoglio.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG), quindi significa che hai a che fare con un foglio di dialogo.

## **Trova se il foglio di lavoro è Foglio di dialogo**

Il codice di esempio seguente carica il file[esempio di file Excel](64716841.xlsx)che contiene un foglio di dialogo. Controlla il[**Foglio.Tipo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)proprietà lo confronta con[**TipoFoglio.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)e poi stampa il messaggio. Si prega di consultare l'output della console del codice di esempio fornito di seguito per ulteriore assistenza.

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Uscita console**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}

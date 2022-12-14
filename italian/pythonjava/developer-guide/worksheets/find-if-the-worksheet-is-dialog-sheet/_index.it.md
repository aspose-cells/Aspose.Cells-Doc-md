---
title: Trova se il foglio di lavoro è Foglio di dialogo
type: docs
weight: 70
url: /it/python-java/find-if-the-worksheet-is-dialog-sheet/
---
## **Possibili scenari di utilizzo**
Foglio di dialogo è un vecchio formato del foglio che contiene una finestra di dialogo. Tale foglio potrebbe essere inserito da una versione precedente di Excel Microsoft, ad esempio 2003, come mostrato in questa schermata. Può anche essere inserito con VBA nelle versioni più recenti, ad esempio Microsoft Excel 2016.

![cose da fare:immagine_alt_testo](DialogSheet.png)
## **Trova se il foglio di lavoro è Foglio di dialogo**
Aspose.Cells per Python tramite Java offre la possibilità di verificare se il foglio di lavoro è un foglio di dialogo. Per questo, fornisce il[Foglio.Tipo](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)proprietà. Se[Foglio.Tipo](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)restituisce il valore di enumerazione[TipoFoglio.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG), quindi significa che hai a che fare con un foglio di dialogo.

Il seguente frammento di codice mostra come verificare la presenza di un foglio di dialogo. L'output della console generato dal codice è riportato di seguito per riferimento.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **Uscita console**
Il foglio di lavoro è un foglio di dialogo.

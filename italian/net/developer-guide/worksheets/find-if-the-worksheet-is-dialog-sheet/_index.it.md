---
title: Trova se il foglio di lavoro è Foglio di dialogo
type: docs
weight: 90
url: /it/net/find-if-the-worksheet-is-dialog-sheet/
description: Foglio di dialogo è un vecchio formato di foglio. In questo articolo vengono fornite istruzioni e codice di esempio per determinare a livello di codice se un foglio di lavoro di Excel è un foglio di dialogo utilizzando la libreria C# API o .NET.
keywords: find excel worksheet dialog type c#, worksheet dialog c#
---
##  **Possibili scenari di utilizzo**

Foglio di dialogo è un vecchio formato di foglio che contiene una finestra di dialogo. Tale foglio potrebbe essere inserito da una versione precedente di Excel Microsoft es. 2003 come mostrato in questa schermata. Può anche essere inserito con VBA nelle versioni più recenti, ad esempio Microsoft Excel 2016.

![cose da fare:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Puoi scoprire se il foglio è un foglio di dialogo o qualche altro tipo di foglio con[**Foglio.Tipo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)proprietà fornita da Aspose.Cells. Se restituisce il valore di enumerazione[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), quindi significa che hai a che fare con il foglio di dialogo.

##  **Trova se il foglio di lavoro è Foglio di dialogo**

 Il codice di esempio seguente carica il file[esempio di file Excel](64716820.xlsx) che contiene un foglio di dialogo. Controlla il[**Foglio.Tipo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)proprietà lo confronta con[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) e poi stampa il messaggio. Si prega di consultare l'output della console del codice di esempio fornito di seguito per ulteriore assistenza.

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

##  **Uscita console**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}

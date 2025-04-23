---
title: Verificare se il foglio di lavoro è un foglio di dialogo
type: docs
weight: 90
url: /it/python-net/find-if-the-worksheet-is-dialog-sheet/
description: Il foglio di dialogo è un vecchio formato di foglio. Questo articolo fornisce istruzioni e codice di esempio per determinare programmaticamente se un foglio di lavoro Excel è un Foglio di Dialogo usando la libreria Aspose.Cells for Python via .NET.
keywords: Libreria Python per Excel, tipo di dialogo per trovare il foglio di lavoro Excel in Python, dialogo del foglio di lavoro in python.
---

## **Possibili Scenari di Utilizzo**

Il foglio di dialogo è un vecchio formato di foglio che contiene una finestra di dialogo. Tale foglio potrebbe essere stato inserito da una versione precedente di Microsoft Excel, ad esempio la versione 2003 come mostrato in questa schermata. Può anche essere inserito con VBA nelle nuove versioni, ad esempio Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Puoi verificare se il foglio è un foglio di dialogo o di altro tipo con la proprietà [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/) fornita da Aspose.Cells per Python via .NET. Se restituisce il valore di enumerazione [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/), significa che stai lavorando con un foglio di dialogo.

## **Trova se il foglio di lavoro è un foglio di dialogo**

Il seguente codice di esempio carica il [file Excel di esempio](64716820.xlsx) che contiene un foglio di dialogo. Controlla la proprietà [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/), la confronta con [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/) e quindi stampa il messaggio. Si prega di vedere l'output della console del codice di esempio qui sotto per ulteriori informazioni.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}

## **Output della console**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}

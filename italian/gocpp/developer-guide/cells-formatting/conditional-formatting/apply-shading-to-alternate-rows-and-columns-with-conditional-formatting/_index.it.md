---
title: Applica la sfumatura alle righe e alle colonne alternate con formattazione condizionale con Golang tramite C++
linktitle: Applicare tonalità alternate alle righe e alle colonne
description: Come usare la libreria Aspose.Cells in C++ per applicare ombreggiature di formattazione condizionale alle righe e alle colonne alternate. Modificando questi criteri, hai un maggiore controllo sull aspetto delle celle.
keywords: Aspose.Cells, Formattazione Condizionale, C++, Righe Alternate, Colonne Alternate, Ombreggiature
type: docs
weight: 30
url: /it/go-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Le API di Aspose.Cells forniscono i mezzi per aggiungere e manipolare regole di formattazione condizionale per l'oggetto [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/). Queste regole possono essere personalizzate in diversi modi per ottenere la formattazione desiderata in base a condizioni o regole. Questo articolo dimostrerà l'uso delle API Aspose.Cells for C++ per applicare ombreggiature a righe e colonne alternate con l'aiuto di regole di formattazione condizionale e funzioni integrate di Excel.

{{% /alert %}}

Questo articolo fa uso di funzioni integrate di Excel come ROW, COLUMN e MOD. Ecco alcuni dettagli di queste funzioni per una migliore comprensione dello snippet di codice fornito in seguito.

- La funzione **ROW()** restituisce il numero di riga di un riferimento di cella. Se il parametro di riferimento viene omesso, si assume che il riferimento sia l'indirizzo della cella in cui è stata inserita la funzione ROW.
- La funzione **COLUMN()** restituisce il numero di colonna di un riferimento di cella. Se il parametro di riferimento viene omesso, si assume che il riferimento sia l'indirizzo della cella in cui è stata inserita la funzione COLUMN.
- La funzione **MOD()** restituisce il resto dopo che un numero è diviso per un divisore, dove il primo parametro della funzione è il valore numerico di cui si desidera trovare il resto e il secondo parametro è il numero utilizzato per dividere il parametro del numero. Se il divisore è 0, restituirà l'errore #DIV/0!.

Iniziamo a scrivere del codice per raggiungere questo obiettivo con l'uso delle API Aspose.Cells for C++.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyShadingToAlternateRowsAndColumnsWithConditionalFormatting.go" >}}
Il seguente screenshot mostra il foglio elettronico caricato nell'applicazione Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Per applicare l'ombreggiatura alle colonne alternative, tutto ciò che devi fare è modificare la formula **=MOD(FILA(),2)=0** in **=MOD(COLONNA(),2)=0**, cioè; invece di ottenere l'indice di riga, modifica la formula per recuperare l'indice di colonna. 
Il foglio elettronico risultante, in questo caso, avrà questo aspetto.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |

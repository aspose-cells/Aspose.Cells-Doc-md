---
title: Applicare una sfumatura alle righe e alle colonne alternate con la formattazione condizionale
linktitle: Applicare una sfumatura alle righe e alle colonne alternate con la formattazione condizionale
description: Come usare la libreria Aspose.Cells in Node.js tramite C++ per applicare ombre di formattazione condizionale per righe e colonne alternate. Regolando questi criteri, hai più controllo sull aspetto delle celle.
keywords: Aspose.Cells, Formattazione condizionale, Node.js tramite C++, Righe alternate, Colonne alternate, Ombre
type: docs
weight: 30
url: /it/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Le API di Aspose.Cells forniscono i mezzi per aggiungere e manipolare regole di formattazione condizionale per l'oggetto [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Queste regole possono essere adattate in vari modi per ottenere la formattazione desiderata in base alle condizioni o alle regole. Questo articolo dimostrerà l'uso delle API Aspose.Cells for Node.js via C++ per applicare ombreggiature alle righe e colonne alternate con l'aiuto di regole di formattazione condizionale e funzioni integrate di Excel.

{{% /alert %}}

Questo articolo fa uso di funzioni integrate di Excel come ROW, COLUMN e MOD. Ecco alcuni dettagli di queste funzioni per una migliore comprensione dello snippet di codice fornito in seguito.

- La funzione **ROW()** restituisce il numero di riga di un riferimento di cella. Se si omette il parametro reference, si assume che il riferimento sia l'indirizzo della cella in cui è stato inserito il funzione ROW.
- La funzione **COLUMN()** restituisce il numero di colonna di un riferimento di cella. Se si omette il parametro reference, si assume che il riferimento sia l'indirizzo della cella in cui è stato inserito il funzione COLUMN.
- La funzione **MOD()** restituisce il resto dopo che un numero è diviso per un divisore, dove il primo parametro della funzione è il valore numerico di cui si desidera trovare il resto e il secondo parametro è il numero utilizzato per dividere il parametro del numero. Se il divisore è 0, restituirà l'errore #DIV/0!.

Iniziamo a scrivere del codice per raggiungere questo obiettivo con l'aiuto dell'API Aspose.Cells for Node.js via C++.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyShadingToAlternateRowsAndColumns.js" >}}


Il seguente screenshot mostra il foglio elettronico caricato nell'applicazione Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Per applicare l'ombreggiatura alle colonne alternative, tutto ciò che devi fare è modificare la formula **=MOD(FILA(),2)=0** in **=MOD(COLONNA(),2)=0**, cioè; invece di ottenere l'indice di riga, modifica la formula per recuperare l'indice di colonna.  
Il foglio elettronico risultante, in questo caso, avrà questo aspetto.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |

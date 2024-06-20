---
title: Applicare una sfumatura alle righe e alle colonne alternate con la formattazione condizionale
type: docs
weight: 10
url: /it/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}} 

Le API di Aspose.Cells forniscono i mezzi per aggiungere e manipolare regole di formattazione condizionale per l'oggetto [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Queste regole possono essere personalizzate in vari modi per ottenere la formattazione desiderata in base a condizioni o regole. Questo articolo mostrerà l'uso dell'API Aspose.Cells for Java per applicare sfumature alle righe e alle colonne alternative con l'ausilio di regole di formattazione condizionale e delle funzioni incorporate di Excel.

{{% /alert %}} 
## **Applica Sfumature alle Righe e alle Colonne Alternative utilizzando la Formattazione Condizionale**
Questo articolo fa uso di funzioni incorporate di Excel come ROW, COLUMN & MOD. Ecco alcuni dettagli su queste funzioni per una migliore comprensione del frammento di codice fornito sopra.

- La funzione **ROW()** restituisce il numero di riga di un riferimento di cella. Se il riferimento viene omesso, si assume che il riferimento sia l'indirizzo della cella in cui è stata inserita la funzione ROW.
- La funzione **COLUMN()** restituisce il numero di colonna di un riferimento di cella. Se il riferimento viene omesso, si assume che il riferimento sia l'indirizzo della cella in cui è stata inserita la funzione COLUMN.
- La funzione **MOD()** restituisce il resto dopo che un numero è diviso per un divisore, dove il primo parametro della funzione è il valore numerico di cui si desidera trovare il resto e il secondo parametro è il numero utilizzato per dividere il parametro del numero. Se il divisore è 0, restituirà l'errore #DIV/0!.

Iniziamo a scrivere del codice per raggiungere l'obiettivo con l'aiuto dell'API Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



Il seguente screenshot mostra il foglio elettronico caricato nell'applicazione Excel.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

Per applicare l'ombreggiatura alle colonne alternative, tutto ciò che devi fare è modificare la formula **=MOD(FILA(),2)=0** in **=MOD(COLONNA(),2)=0**, cioè; invece di ottenere l'indice di riga, modifica la formula per recuperare l'indice di colonna. 
Il foglio di calcolo risultante, in questo caso, avrà un aspetto simile all'immagine seguente.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)

---
title: Conversione tra nome cella e indice riga/colonna
linktitle: Cell Conversione Nome e Indice
type: docs
weight: 5
url: /it/java/names-and-indices/
---
## **Ottieni il nome Cell dagli indici di riga e colonna**
È possibile trovare il nome di una cella dato l'indice di riga e colonna. Questo articolo spiega come.

 Aspose.Cells fornisce il[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) che consente agli sviluppatori di ottenere il nome di una cella se forniscono l'indice di riga e colonna.

{{% alert color="primary" %}} 

A differenza di Microsoft Excel, dove gli indici di riga e colonna iniziano da 1, Aspose.Cells inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

 Il seguente codice di esempio illustra come utilizzare[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) per accedere al nome della cella specificato in un indice di riga e colonna noto. Il codice genera il seguente output.



Cell Nome in [0, 0]: A1

Cell Nome in [4, 0]: A5

Cell Nome in [0, 4]: E1

Cell Nome al [2, 2]: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **Ottieni gli indici di riga e colonna dal nome Cell**
È possibile trovare un indice di riga e colonna della cella dal suo nome. Questo articolo spiega come.

 Aspose.Cells fornisce il[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) che consente agli sviluppatori di ottenere un indice di riga e colonna dal nome della cella.

{{% alert color="primary" %}} 

A differenza di Microsoft Excel, dove gli indici di riga e colonna iniziano da 1, Aspose.Cells inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

 Il seguente codice di esempio illustra come utilizzare[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) per ottenere l'indice di riga e colonna dal nome della cella. Il codice genera il seguente output.



Indice Righe di Cell C6: 5

Indice colonna Cell C6: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **Crea nomi di fogli sicuri**
 volte è necessario assegnare il nome del foglio in fase di esecuzione. In questo scenario, potrebbero esserci nomi di fogli che potrebbero contenere alcuni caratteri aggiuntivi come<>+(?". È necessario sostituire qualsiasi carattere di questo tipo, che non è consentito come nome di un foglio, con un carattere preimpostato fornito dall'utente. Allo stesso modo, la lunghezza può aumentare fino a più di 31 caratteri che devono essere troncati. Apache POI fornisce alcune funzionalità per la creazione di nomi sicuri, quindi funzionalità simili sono fornite da Aspose.Cells per gestire tutti questi problemi.Il seguente codice di esempio dimostra questa funzionalità:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Uscita console**

questo è il nome che è cre

` `<> + (agg.Privato _ "Privato"

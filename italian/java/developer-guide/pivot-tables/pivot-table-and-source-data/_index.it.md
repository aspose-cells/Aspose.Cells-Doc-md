---
title: Tabella pivot e dati di origine
type: docs
weight: 110
url: /it/java/pivot-table-and-source-data/
---
## **Dati di origine della tabella pivot**
Ci sono momenti in cui si desidera creare report di Microsoft Excel con tabelle pivot che prendono dati da diverse origini dati (come un database) che non sono note in fase di progettazione. Questo articolo fornisce un approccio per modificare dinamicamente l'origine dati di una tabella pivot.
## **Modifica dei dati di origine di una tabella pivot**
1. Creazione di un nuovo modello di designer.
1. Crea un nuovo file modello di designer come nello screenshot qui sotto.
 1. Quindi definire un intervallo denominato,**Fonte di dati** , che si riferisce a questo intervallo di celle.

      **Creazione di un modello di progettazione e definizione di un intervallo denominato, DataSource** 

![cose da fare:immagine_alt_testo](pivot-table-and-source-data_1.png)

1. Creazione di una tabella pivot basata su questo intervallo denominato.
 1. In Microsoft Excel, scegli**Dati** , poi**Tabella pivot** e**Rapporto grafico pivot**.
 1. Crea una tabella pivot basata sull'intervallo denominato creato nel primo passaggio.

      **Creazione di una tabella pivot basata sull'intervallo denominato, DataSource** 

![cose da fare:immagine_alt_testo](pivot-table-and-source-data_2.png)

1.  Trascina il campo corrispondente sulla riga e colonna della tabella pivot, quindi crea la tabella pivot risultante come nello screenshot qui sotto.

   **Creazione di una tabella pivot basata su un campo corrispondente** 

![cose da fare:immagine_alt_testo](pivot-table-and-source-data_3.png)

1.  Fai clic con il pulsante destro del mouse sulla tabella pivot e seleziona**Opzioni tabella**.
 1. Controlla**Aggiorna all'apertura** in**Opzioni dati** impostazioni.

      **Impostazione delle opzioni della tabella pivot** 

![cose da fare:immagine_alt_testo](pivot-table-and-source-data_4.png)



Ora puoi salvare questo file come file modello del designer.

1. Popolamento di nuovi dati e modifica dei dati di origine di una tabella pivot.
1. Una volta creato il modello di progettazione, utilizzare il codice seguente per modificare i dati di origine della tabella pivot.

L'esecuzione del codice di esempio seguente modifica i dati di origine della tabella pivot e la tabella pivot avrà l'aspetto di quella sottostante.

**Tabella pivot modificata dinamicamente** 

![cose da fare:immagine_alt_testo](pivot-table-and-source-data_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ChangeSourceData-ChangeSourceData.java" >}}

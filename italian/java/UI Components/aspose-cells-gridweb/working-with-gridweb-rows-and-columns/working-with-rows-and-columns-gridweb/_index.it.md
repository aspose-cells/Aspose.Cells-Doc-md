---
title: Lavorare con righe e colonne GridWeb
type: docs
weight: 20
url: /it/java/working-with-rows-and-columns-gridweb/
---
## **Inserimento di righe e colonne**
Questo argomento spiega come inserire nuove righe e colonne in un foglio di lavoro usando Aspose.Cells.GridWeb API. Righe o colonne possono essere inserite in qualsiasi posizione nel foglio di lavoro.
### **Inserimento di righe**
Per inserire una riga in qualsiasi posizione in un foglio di lavoro:

1. Aggiungere il controllo Aspose.Cells.GridWeb al Web Form o alla pagina.
1. Accedi al foglio di lavoro a cui stai aggiungendo righe.
1. Inserire una riga specificando un indice di riga in cui verrà inserita la riga.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **Inserimento di colonne**
Per inserire una colonna in qualsiasi posizione in un foglio di lavoro:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un Web Form oa una pagina.
1. Accedi al foglio di lavoro a cui stai aggiungendo colonne.
1. Inserire una colonna specificando l'indice di colonna in cui verrà inserita la colonna.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

È inoltre possibile utilizzare i metodi insertRows()/insertColumns() per inserire più righe/colonne nei fogli di lavoro di conseguenza.

{{% /alert %}} 
## **Eliminazione di righe e colonne**
Questo argomento illustra come eliminare righe e colonne da un foglio di lavoro utilizzando Aspose.Cells.GridWeb API. Con l'aiuto di questa funzionalità, gli sviluppatori possono eliminare righe o colonne in fase di esecuzione.
### **Eliminazione di righe**
Per eliminare una riga dal foglio di lavoro:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un Web Form oa una pagina.
1. Accedi al foglio di lavoro da cui vuoi eliminare le righe.
1. Elimina una riga dal foglio di lavoro specificandone l'indice di riga.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **Eliminazione di colonne**
Per eliminare una colonna dal foglio di lavoro:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un Web Form oa una pagina.
1. Accedi al foglio di lavoro da cui vuoi eliminare le colonne.
1. Elimina una colonna dal foglio di lavoro specificandone l'indice di colonna.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **Impostazione dell'altezza della riga e della larghezza della colonna**
A volte i valori delle celle sono più larghi della cella in cui si trovano o si trovano su più righe. Tali valori non sono completamente visibili agli utenti a meno che non modifichino l'altezza e la larghezza di righe e colonne. Aspose.Cells.GridWeb supporta completamente l'impostazione dell'altezza delle righe e della larghezza delle colonne. Questo argomento discute queste funzionalità in dettaglio con l'aiuto di esempi.
### **Lavorare con l'altezza delle righe e la larghezza delle colonne**
#### **Impostazione dell'altezza della riga**
Per impostare l'altezza di una riga:

1. Aggiungere il controllo Aspose.Cells.GridWeb alla pagina Web Form/.
1. Accedi alla raccolta GridCells del foglio di lavoro.
1. Imposta l'altezza di tutte le celle in qualsiasi riga specificata.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb accetta misure di altezza di riga e larghezza di colonna in punti, pollici, pixel, ecc.

{{% /alert %}} 

**Output: l'altezza della prima riga è stata impostata a 50 punti** 

![cose da fare:immagine_alt_testo](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **Impostazione della larghezza della colonna**
Per impostare la larghezza di una colonna:

1. Aggiungere il controllo Aspose.Cells.GridWeb alla pagina Web Form/.
1. Accedi alla raccolta GridCells del foglio di lavoro.
1. Imposta la larghezza di tutte le celle in qualsiasi colonna specificata.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **Personalizzazione delle intestazioni di righe e colonne**
Come Microsoft Excel, Aspose.Cells.GridWeb utilizza anche intestazioni o didascalie standard per righe (numeri come 1, 2, 3 e così via) e colonne (alfabetiche come A, B, C e così via). Aspose.Cells.GridWeb permette anche di personalizzare le didascalie. Questo argomento illustra la personalizzazione delle intestazioni di riga e colonna in fase di esecuzione utilizzando Aspose.Cells.GridWeb API.
### **Personalizzazione dell'intestazione di riga**
Per personalizzare l'intestazione o la didascalia di una riga:

1. Aggiungere il controllo Aspose.Cells.GridWeb a una pagina Web Form/.
1. Accedi al foglio di lavoro in GridWorksheetCollection.
1. Imposta la didascalia di qualsiasi riga specificata.

**Le intestazioni delle righe 1 e 2 sono state personalizzate** 

![cose da fare:immagine_alt_testo](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **Personalizzazione dell'intestazione di colonna**
Per personalizzare l'intestazione o la didascalia di una colonna:

1. Aggiungere il controllo Aspose.Cells.GridWeb a una pagina Web Form/.
1. Accedi al foglio di lavoro in GridWorksheetCollection.
1. Imposta la didascalia di qualsiasi colonna specificata.

**Le intestazioni delle colonne 1 e 2 sono state personalizzate** 

![cose da fare:immagine_alt_testo](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **Blocca e sblocca righe e colonne**
Questo argomento spiega come bloccare e sbloccare righe e colonne. Il blocco di colonne o righe consente agli utenti di mantenere visibili le intestazioni di colonna o i titoli di riga mentre scorrono verso altre parti del foglio di lavoro. Questa funzione è molto utile quando si lavora con fogli di lavoro che contengono grandi volumi di dati. Quando gli utenti scorrono solo i dati vengono fatti scorrere verso il basso e le intestazioni rimangono al loro posto, rendendo la data più facile da leggere. La funzione Blocca riquadri è supportata solo in Internet Explorer 6.0 o versioni successive.
### **Congelamento di righe e colonne**
Per bloccare un numero specifico di righe e colonne:

1. Aggiungere il controllo Aspose.Cells.GridWeb a una pagina Web Form/.
1. Accedi a un foglio di lavoro.
1. Blocca un numero di righe e colonne.

{{% alert color="primary" %}} 

 È anche possibile bloccare un numero specifico di righe e colonne utilizzando l'interfaccia. Fare clic con il pulsante destro del mouse su una cella in cui si desidera bloccare righe e colonne e selezionare**Congelare** dalla lista.

{{% /alert %}} 

**Righe e colonne in uno stato bloccato** 

![cose da fare:immagine_alt_testo](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **Sblocco di righe e colonne**
Per sbloccare righe e colonne:

1. Aggiungere il controllo Aspose.Cells.GridWeb a una pagina Web Form/.
1. Accedi a un foglio di lavoro.
1. Sblocca righe e colonne.

**Foglio di lavoro dopo essere stato sbloccato** 

![cose da fare:immagine_alt_testo](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **Protezione di righe e colonne**
In questo argomento vengono illustrate alcune tecniche per proteggere le celle in righe e colonne da qualsiasi tipo di azione eseguita dagli utenti finali. Gli sviluppatori possono implementare questa protezione utilizzando due tecniche: rendendo le celle in righe e colonne di sola lettura o limitando le opzioni del menu contestuale di GridWeb.
### **Limitazione delle opzioni del menu contestuale**
GridWeb fornisce un menu di scelta rapida che gli utenti finali possono utilizzare per eseguire operazioni sul controllo. Il menu offre molte opzioni per manipolare celle, righe e colonne.

**Opzioni contestuali complete** 

![cose da fare:immagine_alt_testo](working-with-rows-and-columns-gridweb_6.png)

È possibile limitare qualsiasi tipo di operazione lato client su righe e colonne restringendo le opzioni disponibili nel menu contestuale. Può essere eseguito impostando gli attributi EnableClientColumnOperations e EnableClientRowOperations del controllo GridWeb su false. È inoltre possibile impedire agli utenti di bloccare righe e colonne impostando l'attributo EnableClientFreeze del controllo GridWeb su false.

**Menu contestuale dopo aver limitato le opzioni di riga e colonna** 

![cose da fare:immagine_alt_testo](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}

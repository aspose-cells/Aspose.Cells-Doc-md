---
title: Lavorare con Righe e Colonne GridWeb
type: docs
weight: 20
url: /it/java/working-with-rows-and-columns-gridweb/
---

## **Inserimento Righe e Colonne**
Questo argomento spiega come inserire nuove righe e colonne in un foglio di lavoro utilizzando l'API di Aspose.Cells.GridWeb. Le righe o colonne possono essere inserite in qualsiasi posizione nel foglio di lavoro.
### **Inserimento Righe**
Per inserire una riga in qualsiasi posizione in un foglio di lavoro:

1. Aggiungi il controllo Aspose.Cells.GridWeb al modulo web o pagina.
1. Accedi al foglio di lavoro a cui stai aggiungendo righe.
1. Inserisci una riga specificando un indice di riga in cui la riga deve essere inserita.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **Inserimento di colonne**
Per inserire una colonna in qualsiasi posizione in un foglio di lavoro:

1. Aggiungi il controllo Aspose.Cells.GridWeb a un modulo web o pagina.
1. Accedi al foglio di lavoro a cui stai aggiungendo colonne.
1. Inserisci una colonna specificando l'indice di colonna in cui la colonna deve essere inserita.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

È anche possibile utilizzare i metodi insertRows()/insertColumns() per inserire più righe/colonne nei fogli di lavoro di conseguenza.

{{% /alert %}} 
## **Eliminazione di righe e colonne**
Questo argomento dimostra come eliminare righe e colonne da un foglio di lavoro utilizzando l'API Aspose.Cells.GridWeb. Con l'aiuto di questa funzionalità, gli sviluppatori possono eliminare righe o colonne durante l'esecuzione.
### **Eliminazione delle righe**
Per eliminare una riga dal tuo foglio di lavoro:

1. Aggiungi il controllo Aspose.Cells.GridWeb a un modulo web o pagina.
1. Accedi al foglio di lavoro da cui vuoi eliminare le righe.
1. Elimina una riga dal foglio di lavoro specificando il suo indice di riga.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **Eliminazione di colonne**
Per eliminare una colonna dal tuo foglio di lavoro:

1. Aggiungi il controllo Aspose.Cells.GridWeb a un modulo web o pagina.
1. Accedi al foglio di lavoro da cui vuoi eliminare colonne.
1. Elimina una colonna dal foglio di lavoro specificando il suo indice di colonna.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **Impostazione dell'altezza della riga e della larghezza della colonna**
A volte i valori delle celle sono più larghi della cella in cui si trovano o sono su diverse righe. Tali valori non sono completamente visibili agli utenti a meno che non cambino l'altezza e la larghezza delle righe e delle colonne. Aspose.Cells.GridWeb supporta pienamente l'impostazione dell'altezza delle righe e della larghezza delle colonne. Questo argomento discute in dettaglio queste funzionalità con l'aiuto di esempi.
### **Lavorare con altezze delle righe e larghezze delle colonne**
#### **Impostazione dell'altezza della riga**
Per impostare l'altezza di una riga:

1. Aggiungi il controllo Aspose.Cells.GridWeb al tuo modulo / pagina Web.
1. Accedi alla collezione GridCells del foglio di lavoro.
1. Imposta l'altezza di tutte le celle in una qualsiasi riga specificata.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb accetta misurazioni dell'altezza della riga e della larghezza della colonna in punti, pollici, pixel, ecc.

{{% /alert %}} 

**Output: l'altezza della 1a riga è stata impostata a 50 punti** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **Impostazione della larghezza della colonna**
Per impostare la larghezza di una colonna:

1. Aggiungi il controllo Aspose.Cells.GridWeb al tuo modulo / pagina Web.
1. Accedi alla collezione GridCells del foglio di lavoro.
1. Imposta la larghezza di tutte le celle in una qualsiasi colonna specificata.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **Personalizzazione degli intestazioni di riga e colonna**
Come Microsoft Excel, Aspose.Cells.GridWeb utilizza anche intestazioni standard o didascalie per le righe (numeri come 1, 2, 3 e così via) e colonne (alfabetici come A, B, C e così via). Aspose.Cells.GridWeb consente anche di personalizzare le didascalie. Questo argomento discute la personalizzazione delle intestazioni di riga e colonna in fase di esecuzione utilizzando l'API Aspose.Cells.GridWeb.
### **Personalizzazione dell'intestazione di riga**
Per personalizzare l'intestazione o la didascalia di una riga:

1. Aggiungi il controllo Aspose.Cells.GridWeb a una Form/ pagina Web.
1. Accedi al foglio di lavoro nella raccolta GridWorksheet.
1. Imposta la didascalia di una riga specifica.

**Le intestazioni della riga 1 e 2 sono state personalizzate** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **Personalizzazione dell'intestazione della colonna**
Per personalizzare l'intestazione o la didascalia di una colonna:

1. Aggiungi il controllo Aspose.Cells.GridWeb a una Form/ pagina Web.
1. Accedi al foglio di lavoro nella raccolta GridWorksheet.
1. Imposta la didascalia di una colonna specifica.

**Le intestazioni della colonna 1 e 2 sono state personalizzate** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **Congela e Scongela Righe e Colonne**
Questo argomento spiega come congelare e scongelare righe e colonne. Congelare colonne o righe consente agli utenti di mantenere visibili gli intestazioni delle colonne o i titoli delle righe mentre scorrono verso altre parti del foglio di lavoro. Questa funzionalità è molto utile quando si lavora con fogli contenenti grandi volumi di dati. Durante lo scorrimento, solo i dati vengono spostati verso il basso e le intestazioni rimangono al loro posto, facilitando la lettura dei dati. La funzione di blocco riquadri è supportata solo in Internet Explorer 6.0 o versioni successive.
### **Congelare Righe e Colonne**
Per congelare un numero specifico di righe e colonne:

1. Aggiungi il controllo Aspose.Cells.GridWeb a una Form/ pagina Web.
1. Accedi a un foglio di lavoro.
1. Congelare un numero di righe e colonne.

{{% alert color="primary" %}} 

È anche possibile congelare un numero specifico di righe e colonne utilizzando l'interfaccia. Fare clic con il pulsante destro del mouse su una cella dove si desidera congelare righe e colonne e selezionare **Congela** dalla lista.

{{% /alert %}} 

**Righe e colonne in stato bloccato** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **Scongelare Righe e Colonne**
Per scongelare righe e colonne:

1. Aggiungi il controllo Aspose.Cells.GridWeb a una Form/ pagina Web.
1. Accedi a un foglio di lavoro.
1. Rimuovere il blocco delle righe e delle colonne.

**Foglio di lavoro dopo aver rimosso il blocco** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **Protezione delle righe e delle colonne**
Questo argomento discute alcune tecniche per proteggere le celle nelle righe e nelle colonne da qualsiasi tipo di azione eseguita dagli utenti finali. Gli sviluppatori possono implementare questa protezione utilizzando due tecniche: rendendo le celle nelle righe e nelle colonne di sola lettura, o limitando le opzioni del menu contestuale di GridWeb.
### **Limitazione delle opzioni del menu contestuale**
GridWeb fornisce un menu contestuale che gli utenti finali possono utilizzare per eseguire operazioni sul controllo. Il menu offre molte opzioni per manipolare celle, righe e colonne.

**Opzioni contestuali complete** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

E' possibile limitare qualsiasi tipo di operazione lato client su righe e colonne limitando le opzioni disponibili nel menu contestuale. E' possibile impedire agli utenti di bloccare le righe e le colonne impostando l'attributo EnableClientFreeze del controllo GridWeb su falso.

**Menu contestuale dopo aver limitato le opzioni di riga e colonna** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}

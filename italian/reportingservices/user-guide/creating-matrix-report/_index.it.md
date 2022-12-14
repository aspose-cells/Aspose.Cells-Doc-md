---
title: Creazione rapporto matrice
type: docs
weight: 10
url: /it/reportingservices/creating-matrix-report/
---
{{% alert color="primary" %}} 

 Aspose.Cells per Reporting Services consente di progettare una matrice in Microsoft Excel.

{{% /alert %}} 
### **Modello di matrice**
In un modello di report Aspose.Cells, una matrice è composta da angoli, gruppi di righe, gruppi di colonne e porzioni di dati. Di seguito è mostrata una matrice di esempio.

**Una matrice campione** 

![cose da fare:immagine_alt_testo](creating-matrix-report_1.png)

- **Angolo della matrice**situato nell'angolo in alto a sinistra o nell'angolo in alto a destra per i layout da destra a sinistra (RTL). Quest'area viene creata automaticamente quando si aggiungono gruppi di righe e gruppi di colonne a un'area dati matrice. In quest'area è possibile unire celle elemento del report casella di testo incorporata.
- **Area dei gruppi di colonne della matrice**: situato nell'angolo in alto a destra (angolo in alto a sinistra per il layout RTL). Quest'area viene creata automaticamente quando si aggiunge un gruppo di colonne. Le celle in quest'area rappresentano i membri della gerarchia dei gruppi di colonne e visualizzano i valori di istanza del gruppo di colonne. Nella figura, le celle che visualizzano OrderYear sono un gruppo di colonne nidificato e la cella che visualizza OrderQtr è un gruppo di colonne adiacente.
- **Area dei gruppi di righe della matrice**: situato nell'angolo in basso a sinistra (in basso a destra per il layout RTL). Quest'area viene creata automaticamente quando si aggiunge un gruppo di righe. Le celle in quest'area rappresentano i membri della gerarchia dei gruppi di righe e visualizzano i valori di istanza del gruppo di righe. Nella figura, queste celle sono gruppi di righe annidati.
- **Area dei dati della matrice**: situato nell'angolo in basso a destra (in basso a sinistra per il layout RTL). I dati della matrice visualizzano i dettagli ei dati raggruppati. In questo esempio vengono utilizzati solo dati aggregati. Per impostazione predefinita, le celle in una riga o colonna di gruppo che contengono espressioni semplici che non includono una funzione di aggregazione restituiscono il primo valore nel gruppo. Nella figura, le celle visualizzano i totali aggregati per i totali di riga per tutti gli ordini cliente.
#### **Creazione di un modello di matrice**
 Prima di creare un report matrice, creare le origini dati, i set di dati e i parametri del report (facoltativo). (Seguire le istruzioni in[Origini dati e query](/cells/it/reportingservices/data-sources-and-queries/) se hai bisogno di assistenza.) Nell'esempio viene utilizzato il database di esempio AdventureWorks fornito con SQL Server Reporting Services 2008.

Per creare una nuova matrice:

1. Apri Microsoft Excel.
1.  Clic**Apri rapporto** per aprire un file RDL Report che contiene le origini dati, i set di dati e i parametri del report creati in precedenza.
Una volta che il file è stato aperto correttamente, tutte le sue informazioni sono disponibili per l'uso, ad esempio, i suoi set di dati sono elencati nel file**Set di dati** elenco.
1.  Aprire un foglio di lavoro Excel Microsoft e selezionare un set di dati.

![cose da fare:immagine_alt_testo](creating-matrix-report_2.png)




1.  Impostare gruppi di righe e gruppi di colonne tramite**Imposta gruppo**. 

![cose da fare:immagine_alt_testo](creating-matrix-report_3.png)




1. Unisci le celle per impostare l'angolo della matrice.

![cose da fare:immagine_alt_testo](creating-matrix-report_4.png)




1.  Imposta l'angolo della matrice inserendo una formula.

![cose da fare:immagine_alt_testo](creating-matrix-report_5.png)




![cose da fare:immagine_alt_testo](creating-matrix-report_6.png)




1.  Clic**Imposta attributo** per impostare l'attributo della matrice.

![cose da fare:immagine_alt_testo](creating-matrix-report_7.png)



Consiste di nome, intervallo, gruppo e ordine.

1. Facendo clic su Modifica attributo vengono controllati e modificati tutti gli attributi della matrice del foglio di lavoro corrente.

![cose da fare:immagine_alt_testo](creating-matrix-report_8.png)




1. Salva, pubblica e rivedi il rapporto.

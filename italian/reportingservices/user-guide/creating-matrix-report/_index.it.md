---
title: Creazione di un Report Matrice
type: docs
weight: 10
url: /it/reportingservices/creating-matrix-report/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services consente di progettare una matrice in Microsoft Excel. 

{{% /alert %}} 
### **Modello a matrice**
In un modello di rapporto Aspose.Cells, una matrice consiste di angolo, gruppi di righe, gruppi di colonne e porzioni di dati. Di seguito è mostrata un esempio di matrice.

**Un esempio di matrice** 

![todo:image_alt_text](creating-matrix-report_1.png)

- **Angolo della matrice**: situato nell'angolo in alto a sinistra o in alto a destra per layout da destra a sinistra (RTL). Questa area viene creata automaticamente quando si aggiungono sia gruppi di righe che gruppi di colonne a una regione dati della matrice. In questa area, è possibile unire le celle incorporate nell'elemento di report a casella di testo.
- **Area gruppi di colonne della matrice**: situata nell'angolo in alto a destra (in alto a sinistra per il layout RTL). Quest'area viene creata automaticamente quando si aggiunge un gruppo di colonne. Le celle in questa area rappresentano membri della gerarchia dei gruppi di colonne e mostrano i valori dell'istanza del gruppo di colonne. Nella figura, le celle che mostrano l'anno dell'ordine sono un gruppo di colonne nidificato e la cella che mostra il trimestre dell'ordine è un gruppo di colonne adiacente.
- **Area gruppi di righe della matrice**: situata nell'angolo in basso a sinistra (in basso a destra per il layout RTL). Quest'area viene creata automaticamente quando si aggiunge un gruppo di righe. Le celle in questa area rappresentano membri della gerarchia dei gruppi di righe e mostrano i valori dell'istanza del gruppo di righe. Nella figura, queste celle sono gruppi di righe nidificati.
- **Area dati della matrice**: situata nell'angolo in basso a destra (in basso a sinistra per il layout RTL). I dati della matrice mostrano dettagli e dati raggruppati. In questo esempio, vengono utilizzati solo dati aggregati. Per impostazione predefinita, le celle in un gruppo di righe o colonne che contengono espressioni semplici che non includono una funzione di aggregazione, valutano al primo valore nel gruppo. Nella figura, le celle mostrano i totali aggregati per i totali delle linee di tutti gli ordini di vendita.
#### **Creazione di un modello di matrice**
Prima di creare un rapporto a matrice, creare le origini dati, i set di dati e i parametri di report (opzionale). (Seguire le istruzioni in [Origini dati e query](/cells/it/reportingservices/data-sources-and-queries/) se si ha bisogno di assistenza.) Nell'esempio, viene utilizzato il database di esempio AdventureWorks fornito con SQL Server Reporting Services 2008.

Per creare una nuova matrice:

1. Aprire Microsoft Excel.
1. Fare clic su **Apri rapporto** per aprire un file di rapporto RDL che contiene le origini dati, i set di dati e i parametri di report creati in anticipo.
   Una volta che il file è stato aperto con successo, tutte le sue informazioni sono disponibili per l'uso, ad esempio, i suoi set di dati sono elencati nell'elenco **Set di dati**.
1. Aprire un foglio di lavoro di Microsoft Excel e selezionare un set di dati. 

![todo:image_alt_text](creating-matrix-report_2.png)




1. Impostare gruppi di righe e gruppi di colonne tramite **Imposta gruppo**. 

![todo:image_alt_text](creating-matrix-report_3.png)




1. Unire le celle per impostare l'angolo della matrice.

![todo:image_alt_text](creating-matrix-report_4.png)




1. Impostare l'angolo della matrice tramite l'inserimento di una formula. 

![todo:image_alt_text](creating-matrix-report_5.png)




![todo:image_alt_text](creating-matrix-report_6.png)




1. Fare clic su **Imposta attributo** per impostare l'attributo della matrice. 

![todo:image_alt_text](creating-matrix-report_7.png)



È composto da nome, intervallo, gruppo e ordine.

1. Facendo clic su modifica attributo, si controlla e si modificano tutti gli attributi della matrice del foglio di lavoro corrente.

![todo:image_alt_text](creating-matrix-report_8.png)




1. Salvare, pubblicare e rivedere il report.

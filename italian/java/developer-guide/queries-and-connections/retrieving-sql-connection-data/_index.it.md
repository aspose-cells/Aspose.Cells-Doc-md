---
title: Recupero dei dati di connessione SQL
type: docs
weight: 20
url: /it/java/retrieving-sql-connection-data/
---
{{% alert color="primary" %}} 

 Aspose.Cells può aiutarti a recuperare i dati di connessione SQL. Ciò include tutti i dati necessari per stabilire una connessione al server SQL, ad esempio,**URL del server**, **nome utente**, **nome della tabella**, **query SQL completa**, **tipo di interrogazione**, **posizione del tavolo** , e**nome dell'intervallo denominato** ad esso associato.

{{% /alert %}} 

In Microsoft Excel, connettiti a un database tramite:

1.  Facendo clic sul**Dati** menù e selezione**Da altre fonti** seguito da**Da SQLServer**.
1.  Quindi seleziona**Dati** seguito da**Connessioni**.
1. Utilizzare la procedura guidata Connessioni per connettersi al database e creare una query del database.

**Visualizzazione dell'opzione di connessione SQL in Microsoft Excel** 

![cose da fare:immagine_alt_testo](retrieving-sql-connection-data_1.png)

Aspose.Cells fornisce il metodo Workbook.getDataConnections() per recuperare le connessioni esterne. Restituisce una raccolta di oggetti ExternalConnection nella cartella di lavoro.

Se l'oggetto ExternalConnection contiene dati di connessione SQL, può essere trasformato in un oggetto DBConnection e le sue proprietà utilizzate per recuperare il comando del database, il tipo di comando, la descrizione della connessione, le informazioni sulla connessione, le credenziali e così via.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}







---
title: Recupero dei dati di connessione SQL
type: docs
weight: 10
url: /it/net/retrieving-sql-connection-data/
---
{{% alert color="primary" %}}

 Aspose.Cells può aiutarti a recuperare i dati di connessione SQL. Ciò include tutti i dati necessari per stabilire una connessione al server SQL, ad esempio,**URL del server**, **nome utente**, **nome della tabella**, **query SQL completa**, **tipo di interrogazione**, **posizione del tavolo** , e**nome dell'intervallo denominato** ad esso associato.

{{% /alert %}}

In Microsoft Excel, connettiti a un database tramite:

1.  Facendo clic sul**Dati** menù e selezione**Da altre fonti** seguito da**Da SQLServer**.
1.  Quindi seleziona**Dati** seguito da**Connessioni**.
1. Utilizzare la procedura guidata Connessioni per connettersi al database e creare una query del database.

Aspose.Cells fornisce la proprietà Workbook.DataConnections per il recupero delle connessioni esterne. Restituisce una raccolta di oggetti ExternalConnection nella cartella di lavoro.

Se l'oggetto ExternalConnection contiene dati di connessione SQL, può essere di tipo casta in un oggetto DBConnection e le relative proprietà possono essere utilizzate per recuperare il comando del database, il tipo di comando, la descrizione della connessione, le informazioni sulla connessione, le credenziali e così via.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}

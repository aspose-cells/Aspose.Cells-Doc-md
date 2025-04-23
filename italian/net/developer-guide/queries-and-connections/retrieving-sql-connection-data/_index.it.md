---
title: Recupero dei Dati di Connessione SQL
type: docs
weight: 10
url: /it/net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells può aiutarti a recuperare i dati di connessione SQL. Ciò include tutti i dati necessari per stabilire una connessione con il server SQL, ad esempio, **URL server**, **nome utente**, **nome tabella**, **query SQL completa**, **tipo di query**, **posizione della tabella**, e **nome dell'intervallo con nome** ad esso associato.

{{% /alert %}}

In Microsoft Excel, connettersi a un database tramite:

1. Cliccando sul menu **Dati** e selezionando **Da Altre Origini** seguito da **Da Server SQL**.
1. Poi selezionare **Dati** seguito da **Connessioni**.
1. Utilizzare la procedura guidata di connessione per collegarsi al database e creare una query del database.

Aspose.Cells fornisce la proprietà Workbook.DataConnections per il recupero delle connessioni esterne. Restituisce una raccolta di oggetti ExternalConnection nel documento di lavoro.

Se l'oggetto ExternalConnection contiene dati di connessione SQL, può essere convertito tramite casting in un oggetto DBConnection e le sue proprietà possono essere utilizzate per recuperare il comando del database, il tipo di comando, la descrizione della connessione, le informazioni di connessione, le credenziali, e così via.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

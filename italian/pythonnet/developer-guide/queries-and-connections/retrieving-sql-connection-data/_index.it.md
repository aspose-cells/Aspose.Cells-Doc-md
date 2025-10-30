---
title: Recupero dei Dati di Connessione SQL
type: docs
weight: 10
url: /it/python-net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET può aiutarti a recuperare i dati di connessione SQL. Questo include tutti i dati necessari per stabilire una connessione al server SQL, ad esempio, **URL del server**, **nome utente**, **nome tabella**, ** query SQL completa**, **tipo di query**, **posizione della tabella** e **nome dell'intervallo nominato** associato.

{{% /alert %}}

In Microsoft Excel, connettersi a un database tramite:

1. Cliccando sul menu **Dati** e selezionando **Da Altre Origini** seguito da **Da Server SQL**.
1. Poi selezionare **Dati** seguito da **Connessioni**.
1. Utilizzare la procedura guidata di connessione per collegarsi al database e creare una query del database.

Aspose.Cells per Python via .NET fornisce la proprietà Workbook.DataConnections per recuperare le connessioni esterne. Restituisce una collezione di oggetti ExternalConnection nel workbook.

Se l'oggetto ExternalConnection contiene dati di connessione SQL, può essere convertito tramite casting in un oggetto DBConnection e le sue proprietà possono essere utilizzate per recuperare il comando del database, il tipo di comando, la descrizione della connessione, le informazioni di connessione, le credenziali, e così via.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-RetrievingSQLConnectionData-1.py" >}}

{{< app/cells/assistant language="python-net" >}}

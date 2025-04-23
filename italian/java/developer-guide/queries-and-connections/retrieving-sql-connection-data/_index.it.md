---
title: Recupero dei Dati di Connessione SQL
type: docs
weight: 20
url: /it/java/retrieving-sql-connection-data/
---

{{% alert color="primary" %}} 

Aspose.Cells può aiutarti a recuperare i dati della connessione SQL. Questo include tutti i dati necessari per stabilire una connessione con il server SQL, ad esempio, **URL del server**, **nome utente**, **nome tabella**, **query SQL completa**, **tipo di query**, **posizione della tabella**, e **nome del riferimento denominato** associato ad esso.

{{% /alert %}} 

In Microsoft Excel, connettersi a un database tramite:

1. Cliccando sul menu **Dati** e selezionando **Da Altre Origini** seguito da **Da Server SQL**.
1. Poi selezionare **Dati** seguito da **Connessioni**.
1. Utilizzare la procedura guidata di connessione per collegarsi al database e creare una query del database.

**Mostrare l'opzione di connessione SQL in Microsoft Excel** 

![todo:image_alt_text](retrieving-sql-connection-data_1.png)

Aspose.Cells fornisce il metodo Workbook.getDataConnections() per il recupero delle connessioni esterne. Restituisce una raccolta di oggetti ExternalConnection nel workbook.

Se l'oggetto ExternalConnection contiene dati di connessione SQL, può essere iniettato nel tipo DBConnection le sue proprietà utilizzate per recuperare il comando del database, il tipo di comando, la descrizione della connessione, le informazioni sulla connessione, le credenziali, e così via.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}






{{< app/cells/assistant language="java" >}}

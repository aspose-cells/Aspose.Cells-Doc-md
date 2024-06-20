---
title: SQL Verbindungsdaten abrufen
type: docs
weight: 10
url: /de/net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells kann Ihnen helfen, SQL-Verbindungsdaten abzurufen. Dazu gehören alle Daten, die zum Herstellen einer Verbindung zum SQL-Server erforderlich sind, z. B. **Server-URL**, **Benutzername**, **Tabellenname**, **vollständige SQL-Abfrage**, **Abfragetyp**, **Speicherort der Tabelle** und **Name des benannten Bereichs**, der damit verbunden ist.

{{% /alert %}}

In Microsoft Excel eine Datenbankverbindung herstellen, indem Sie:

1. Zum **Daten**-Menü gehen und **Aus anderen Quellen** gefolgt von **Vom SQL Server** auswählen.
1. Dann **Daten** gefolgt von **Verbindungen** auswählen.
1. Verwenden Sie den Verbindungs-Assistenten, um eine Verbindung zur Datenbank herzustellen und eine Datenbankabfrage zu erstellen.

Aspose.Cells stellt die Eigenschaft Workbook.DataConnections zum Abrufen externer Verbindungen bereit. Es gibt eine Sammlung von ExternalConnection-Objekten in der Arbeitsmappe zurück.

Wenn das ExternalConnection-Objekt SQL-Verbindungsdaten enthält, kann es in ein DBConnection-Objekt umgewandelt und seine Eigenschaften zur Abrufung von Datenbankbefehl, Befehlstyp, Verbindungsinformationen, Anmeldeinformationen usw. verwendet werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}

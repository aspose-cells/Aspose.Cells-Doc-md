---
title: Abrufen von SQL-Verbindungsdaten
type: docs
weight: 10
url: /de/net/retrieving-sql-connection-data/
---
{{% alert color="primary" %}}

 Aspose.Cells kann Ihnen beim Abrufen von SQL-Verbindungsdaten helfen. Dazu gehören alle Daten, die für eine Verbindung zum SQL-Server benötigt werden, z. B.**Server-URL**, **Nutzername**, **Tabellenname**, **vollständige SQL-Abfrage**, **Abfragetyp**, **Standort des Tisches** , und**Name des benannten Bereichs** mit ihr verbundenen.

{{% /alert %}}

Stellen Sie in Microsoft Excel eine Verbindung zu einer Datenbank her, indem Sie:

1.  Klicken Sie auf die**Daten** Menü und Auswahl**Aus anderen Quellen** gefolgt von**Von SQL-Server**.
1.  Wählen Sie dann aus**Daten** gefolgt von**Verbindungen**.
1. Verwenden Sie den Verbindungsassistenten, um eine Verbindung zur Datenbank herzustellen und eine Datenbankabfrage zu erstellen.

Aspose.Cells stellt die Workbook.DataConnections-Eigenschaft zum Abrufen externer Verbindungen bereit. Es gibt eine Sammlung von ExternalConnection-Objekten in der Arbeitsmappe zurück.

Wenn das ExternalConnection-Objekt SQL-Verbindungsdaten enthält, kann es in ein DBConnection-Objekt umgewandelt werden, und seine Eigenschaften können verwendet werden, um Datenbankbefehle, Befehlstypen, Verbindungsbeschreibungen, Verbindungsinformationen, Berechtigungsnachweise usw. abzurufen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}

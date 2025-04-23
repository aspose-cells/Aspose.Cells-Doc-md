---
title: SQL Verbindungsdaten abrufen
type: docs
weight: 10
url: /de/python-net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET kann Ihnen helfen, SQL-Verbindungsdaten abzurufen. Dazu gehören alle erforderlichen Daten, um eine Verbindung zum SQL-Server herzustellen, z.B. **Server-URL**, **Benutzername**, **Tabellenname**, **vollständige SQL-Abfrage**, **Abfragetyp**, **Ort der Tabelle** und **Name des zugehörigen Bereichs**.

{{% /alert %}}

In Microsoft Excel eine Datenbankverbindung herstellen, indem Sie:

1. Zum **Daten**-Menü gehen und **Aus anderen Quellen** gefolgt von **Vom SQL Server** auswählen.
1. Dann **Daten** gefolgt von **Verbindungen** auswählen.
1. Verwenden Sie den Verbindungs-Assistenten, um eine Verbindung zur Datenbank herzustellen und eine Datenbankabfrage zu erstellen.

Aspose.Cells für Python via .NET bietet die Eigenschaft Workbook.DataConnections zum Abrufen externer Verbindungen. Sie gibt eine Sammlung von ExternalConnection-Objekten im Arbeitsbuch zurück.

Wenn das ExternalConnection-Objekt SQL-Verbindungsdaten enthält, kann es in ein DBConnection-Objekt umgewandelt und seine Eigenschaften zur Abrufung von Datenbankbefehl, Befehlstyp, Verbindungsinformationen, Anmeldeinformationen usw. verwendet werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-RetrievingSQLConnectionData-1.py" >}}


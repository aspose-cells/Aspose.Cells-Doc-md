---
title: SQL Verbindungsdaten abrufen
type: docs
weight: 20
url: /de/java/retrieving-sql-connection-data/
---

{{% alert color="primary" %}} 

Mit Aspose.Cells können Sie SQL-Verbindungsdaten abrufen. Dies umfasst alle benötigten Daten, um eine Verbindung zum SQL-Server herzustellen, z. B. **Server-URL**, **Benutzername**, **Tabellenname**, **vollständige SQL-Abfrage**, **Abfragetyp**, **Speicherort der Tabelle** und **Name des benannten Bereichs**, der damit verbunden ist.

{{% /alert %}} 

In Microsoft Excel eine Datenbankverbindung herstellen, indem Sie:

1. Zum **Daten**-Menü gehen und **Aus anderen Quellen** gefolgt von **Vom SQL Server** auswählen.
1. Dann **Daten** gefolgt von **Verbindungen** auswählen.
1. Verwenden Sie den Verbindungs-Assistenten, um eine Verbindung zur Datenbank herzustellen und eine Datenbankabfrage zu erstellen.

**Anzeige der SQL-Verbindungsoption in Microsoft Excel** 

![todo:image_alt_text](retrieving-sql-connection-data_1.png)

Aspose.Cells bietet die Methode Workbook.getDataConnections() zur Abfrage externer Verbindungen. Sie gibt eine Sammlung von ExternalConnection-Objekten in der Arbeitsmappe zurück.

Wenn das ExternalConnection-Objekt SQL-Verbindungsdaten enthält, kann es in ein DBConnection-Objekt umgewandelt werden, dessen Eigenschaften verwendet werden, um Datenbankbefehl, Befehlstyp, Verbindungsbeschreibung, Verbindungsinformationen usw. abzurufen.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}







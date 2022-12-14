---
title: Abrufen von SQL-Verbindungsdaten
type: docs
weight: 20
url: /de/java/retrieving-sql-connection-data/
---
{{% alert color="primary" %}} 

 Aspose.Cells kann Ihnen beim Abrufen von SQL-Verbindungsdaten helfen. Dazu gehören alle Daten, die für eine Verbindung zum SQL-Server erforderlich sind, z. B.**Server-URL**, **Nutzername**, **Tabellenname**, **vollständige SQL-Abfrage**, **Abfragetyp**, **Standort des Tisches** , und**Name des benannten Bereichs** mit ihr verbundenen.

{{% /alert %}} 

Stellen Sie in Microsoft Excel eine Verbindung zu einer Datenbank her, indem Sie:

1.  Klicken Sie auf die**Daten** Menü und Auswahl**Aus anderen Quellen** gefolgt von**Von SQL-Server**.
1.  Wählen Sie dann aus**Daten** gefolgt von**Verbindungen**.
1. Verwenden Sie den Verbindungsassistenten, um eine Verbindung zur Datenbank herzustellen und eine Datenbankabfrage zu erstellen.

**Anzeigen der SQL-Verbindungsoption in Microsoft Excel** 

![todo: Bild_alt_Text](retrieving-sql-connection-data_1.png)

Aspose.Cells stellt die Methode Workbook.getDataConnections() zum Abrufen externer Verbindungen bereit. Es gibt eine Sammlung von ExternalConnection-Objekten in der Arbeitsmappe zurück.

Wenn das ExternalConnection-Objekt SQL-Verbindungsdaten enthält, kann es in ein DBConnection-Objekt umgewandelt werden, dessen Eigenschaften zum Abrufen von Datenbankbefehl, Befehlstyp, Verbindungsbeschreibung, Verbindungsinformationen, Anmeldeinformationen usw. verwendet werden.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}







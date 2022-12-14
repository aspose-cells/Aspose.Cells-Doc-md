---
title: Importieren Sie Daten aus dem ResultSet-Objekt der Access-Datenbank Microsoft in das Arbeitsblatt
type: docs
weight: 200
url: /de/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---
## **Mögliche Nutzungsszenarien**
Aspose.Cells kann Daten aus dem ResultSet-Objekt, das aus jeder Datenbank erstellt werden kann, in Arbeitsblätter importieren. Dieser Artikel erstellt jedoch speziell ein ResultSet-Objekt aus der Access-Datenbank Microsoft. Da der Code für alle Arten von Datenbanken gleich ist, können Sie ihn allgemein verwenden.
## **UCanAccess – Erforderlich, um eine Verbindung zur Microsoft Access-Datenbank herzustellen**
 Bitte herunterladen[UCanAccess](http://ucanaccess.sourceforge.net/site.html). Es enthält die folgenden JAR-Dateien. Fügen Sie alle im Klassenpfad hinzu.

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

Weitere Hilfe finden Sie unter diesem Stack Overflow-Link.

- [Manuelles Hinzufügen der JARs zu Ihrem Projekt](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **Beispiel Microsoft Access 2016-Datenbankdatei, die im Beispielcode verwendet wird**
Das folgende Beispiel Microsoft Access 2016-Datenbankdatei wurde im Beispielcode verwendet. Sie können eine beliebige Datenbankdatei verwenden oder Ihre eigene erstellen.

- [Studenten.accdb](48496712.accdb)

Der folgende Screenshot zeigt die Datenbankdatei beim Öffnen in Microsoft Access 2016.

![todo: Bild_alt_Text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Importieren Sie Daten aus dem ResultSet-Objekt der Access-Datenbank Microsoft in das Arbeitsblatt.**
 Der folgende Beispielcode führt eine SQL-Abfrage aus der Access-Datenbank Microsoft aus und erstellt ein ResultSet-Objekt. Dann importiert es Daten aus dem ResultSet-Objekt in das Arbeitsblatt mit[Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\)) Methode. Beim ersten Mal verwendet es Zeilen- und Spaltenindizes und dann den Zellennamen, um Daten in das Arbeitsblatt zu importieren. Schließlich speichert es die Arbeitsmappe als[Excel-Datei ausgeben](48496713.xlsx). Der Screenshot zeigt die Auswirkung des Beispielcodes auf die ausgegebene Excel-Datei als Referenz.

![todo: Bild_alt_Text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}

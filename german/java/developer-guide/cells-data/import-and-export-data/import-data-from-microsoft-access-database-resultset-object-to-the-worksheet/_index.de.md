---
title: Daten aus dem ResultSet Objekt der Microsoft Access Datenbank in das Arbeitsblatt importieren
type: docs
weight: 200
url: /de/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells kann Daten zu Arbeitsblättern aus dem ResultSet-Objekt importieren, das aus jeder Datenbank erstellt werden kann. Dieser Artikel erstellt jedoch speziell ein ResultSet-Objekt aus der Microsoft Access-Datenbank. Da der Code für alle Arten von Datenbanken gleich ist, können Sie ihn generell verwenden.
## **UCanAccess - Erforderlich, um eine Verbindung zur Microsoft Access-Datenbank herzustellen**
Bitte laden Sie [UCanAccess](http://ucanaccess.sourceforge.net/site.html) herunter. Es enthält die folgenden JAR-Dateien. Fügen Sie alle von ihnen zum Klassenpfad hinzu.

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

Für weitere Hilfe besuchen Sie bitte diesen Stack Overflow-Link.

- [Manuelles Hinzufügen der JAR-Dateien zu Ihrem Projekt](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **Beispieldatei der Microsoft Access 2016-Datenbank, die im Beispielcode verwendet wird**
Die folgende Beispiel-Microsoft Access 2016-Datenbankdatei wurde im Beispielcode verwendet. Sie können eine beliebige Datenbankdatei verwenden oder Ihre eigene erstellen.

- [Students.accdb](48496712.accdb)

Der folgende Screenshot zeigt die Datenbankdatei, wenn sie in Microsoft Access 2016 geöffnet wird.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Daten aus dem ResultSet-Objekt der Microsoft Access-Datenbank in das Arbeitsblatt importieren.**
Der folgende Beispielcode führt eine SQL-Abfrage aus der Microsoft Access-Datenbank aus und erstellt ein ResultSet-Objekt. Dann importiert es Daten aus dem ResultSet-Objekt in das Arbeitsblatt mittels der [Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\))-Methode. Zuerst verwendet es Zeilen- und Spaltenindizes und dann verwendet es Zellennamen, um Daten in das Arbeitsblatt zu importieren. Schließlich speichert es die Arbeitsmappe als [Ausgabedatei Excel](48496713.xlsx). Der Screenshot zeigt die Auswirkung des Beispielcodes auf die Ausgabedatei Excel zur Referenz.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}

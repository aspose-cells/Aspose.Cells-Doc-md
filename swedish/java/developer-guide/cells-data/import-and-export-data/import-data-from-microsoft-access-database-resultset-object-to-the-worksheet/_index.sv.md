---
title: Importera data från Microsoft Access databas ResultSet objekt till kalkylarket
type: docs
weight: 200
url: /sv/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---

## **Möjliga användningsscenario**
Aspose.Cells kan importera data till kalkylark från ResultSet-objekt som kan skapas från valfri databas. Dock skapar denna artikel specifikt ett ResultSet-objekt från Microsoft Access-databasen. Eftersom koden är densamma för alla typer av databaser kan du använda den generellt sett.
## **UCanAccess - Krävs för att ansluta till Microsoft Access Database**
Vänligen ladda ner[UCanAccess](http://ucanaccess.sourceforge.net/site.html). Det inkluderar följande JAR-filer. Lägg till alla i klassvägen.

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

För mer hjälp, besök denna Stack Overflow-länk.

- [Manuell tillägg av JAR till ditt projekt](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **Exempel på Microsoft Access 2016-databasfil som används inne i provkoden**
Följande exempel på Microsoft Access 2016-databasfil användes inuti provkoden. Du kan använda valfri databasfil eller skapa din egen.

- [Students.accdb](48496712.accdb)

Följande skärmbild visar databasfilen när den öppnas i Microsoft Access 2016.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Importera data från Microsoft Access-databas ResultSet-objekt till kalkylarket.**
Följande exempel exekverar en SQL-fråga från Microsoft Access-databasen och skapar ett ResultSet-objekt. Sedan importerar det data från ResultSet-objektet till kalkbladet med hjälp av [Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet-java.sql.ResultSet-int-int-boolean-) metod. Första gången använder det rad- och kolumnindex och sedan använder det cellnamnet för att importera data till kalkbladet. Slutligen sparar det arbetsboken som en [Output Excel Fil](48496713.xlsx). Skärmbilden visar effekten av koden på output-Excelfilen för referens.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}

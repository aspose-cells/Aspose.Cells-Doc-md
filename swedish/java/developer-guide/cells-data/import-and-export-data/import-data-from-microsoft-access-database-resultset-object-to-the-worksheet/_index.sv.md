---
title: Importera data från Microsoft Access Database ResultSet Object till arbetsbladet
type: docs
weight: 200
url: /sv/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---
## **Möjliga användningsscenarier**
Aspose.Cells kan importera data till kalkylblad från ResultSet-objekt som kan skapas från vilken databas som helst. Den här artikeln skapar dock specifikt ett ResultSet-objekt från Microsoft Access Database. Eftersom koden är densamma för alla typer av databaser, så kan du använda den i allmänhet.
## **UCanAccess - Krävs för att ansluta till Microsoft Access Database**
 Vänligen ladda ner[UCanAccess](http://ucanaccess.sourceforge.net/site.html). Den innehåller följande JAR-filer. Lägg till alla i klassvägen.

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

För mer hjälp, besök denna Stack Overflow-länk.

- [Lägga till JAR manuellt i ditt projekt](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **Exempel Microsoft Åtkomst till 2016 databasfil som används i exempelkoden**
Följande exempel Microsoft Access 2016 Database File användes i exempelkoden. Du kan använda vilken databasfil som helst eller skapa din egen.

- [Students.acdb](48496712.accdb)

Följande skärmdump visar databasfilen när den öppnas i Microsoft Access 2016.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Importera data från Microsoft Access Database ResultSet Object till arbetsbladet.**
 Följande exempelkod kör SQL-fråga från Microsoft Access Database och skapar ett ResultSet-objekt. Sedan importerar den data från ResultSet-objektet till kalkylbladet med hjälp av[Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\)) metod. Första gången använder den rad- och kolumnindex och sedan använder den cellnamn för att importera data till kalkylbladet. Slutligen sparar den arbetsboken som en[Utdata Excel-fil](48496713.xlsx). Skärmdumpen visar effekten av exempelkoden på den utgående Excel-filen som referens.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}

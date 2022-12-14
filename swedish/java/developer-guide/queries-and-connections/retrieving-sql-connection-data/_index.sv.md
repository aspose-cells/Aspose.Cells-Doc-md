---
title: Hämta SQL-anslutningsdata
type: docs
weight: 20
url: /sv/java/retrieving-sql-connection-data/
---
{{% alert color="primary" %}} 

 Aspose.Cells kan hjälpa dig att hämta SQL-anslutningsdata. Detta inkluderar all data som krävs för att göra en anslutning till SQL-servern, till exempel,**serverns URL**, **Användarnamn**, **tabellnamn**, **fullständig SQL-fråga**, **frågetyp**, **bordets placering** , och**namnet på det namngivna området** förknippas med det.

{{% /alert %}} 

I Microsoft Excel, anslut till en databas genom att:

1.  Genom att klicka på**Data** menyn och välja**Från andra källor** följd av**Från SQL Server**.
1.  Välj sedan**Data** följd av**Anslutningar**.
1. Använd guiden Anslutningar för att ansluta till databasen och skapa en databasfråga.

**Visar SQL-anslutningsalternativet i Microsoft Excel** 

![todo:image_alt_text](retrieving-sql-connection-data_1.png)

Aspose.Cells tillhandahåller metoden Workbook.getDataConnections() för att hämta externa anslutningar. Den returnerar en samling ExternalConnection-objekt i arbetsboken.

Om ExternalConnection-objektet innehåller SQL-anslutningsdata kan det typ-castas till ett DBConnection-objekt som dess egenskaper används för att hämta databaskommando, kommandotyp, anslutningsbeskrivning, anslutningsinformation, autentiseringsuppgifter och så vidare.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}







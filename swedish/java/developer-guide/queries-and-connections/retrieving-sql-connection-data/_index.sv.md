---
title: Hämta SQL anslutningsdata
type: docs
weight: 20
url: /sv/java/retrieving-sql-connection-data/
---

{{% alert color="primary" %}} 

Aspose.Cells kan hjälpa dig att hämta SQL-anslutningsdata. Detta inkluderar all data som krävs för att ansluta till SQL-servern, t.ex. **server-URL**, **användarnamn**, **tabellnamn**, **fullständig SQL-fråga**, **frågetyp**, **platsen för tabellen** och **namnet på det namngivna området** som är associerat med det.

{{% /alert %}} 

I Microsoft Excel, anslut till en databas genom att:

1. Klicka på menyn **Data** och välj sedan **Från andra källor** följt av **Från SQL Server**.
1. Välj sedan **Data** följt av **Anslutningar**.
1. Använd Anslutningar-guiden för att ansluta till databasen och skapa en databasfråga.

**Visar SQL-anslutningsalternativet i Microsoft Excel** 

![todo:image_alt_text](retrieving-sql-connection-data_1.png)

Aspose.Cells tillhandahåller Workbook.getDataConnections() metoden för att hämta externa anslutningar. Den returnerar en samling ExternalConnection-objekt i arbetsboken.

Om ExternalConnection-objektet innehåller SQL-anslutningsdata kan det typomvandlas till ett DBConnection-objekt och dess egenskaper användas för att hämta databas kommando, kommandotyp, anslutningsbeskrivning, anslutningsinfo, autentisering osv.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}







---
title: Hämta SQL anslutningsdata
type: docs
weight: 10
url: /sv/net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells kan hjälpa dig att hämta SQL-anslutningsdata. Detta inkluderar all data som krävs för att göra en anslutning till SQL-servern, till exempel **server-URL**, **användarnamn**, **tabellnamn**, **full SQL-fråga**, **frågetyp**, **platsen för tabellen**, och **namnet på namngiven omfattning** som är associerat med den.

{{% /alert %}}

I Microsoft Excel, anslut till en databas genom att:

1. Klicka på menyn **Data** och välj sedan **Från andra källor** följt av **Från SQL Server**.
1. Välj sedan **Data** följt av **Anslutningar**.
1. Använd Anslutningar-guiden för att ansluta till databasen och skapa en databasfråga.

Aspose.Cells tillhandahåller egenskapen Workbook.DataConnections för att hämta externa anslutningar. Den returnerar en samling ExternalConnection-objekt i arbetsboken.

Om ExternalConnection-objektet innehåller SQL-anslutningsdata kan det typomvandlas till ett DBConnection-objekt och dess egenskaper kan användas för att hämta databasfråga, frågetyp, anslutningsbeskrivning, anslutningsinformation, referenser och så vidare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}

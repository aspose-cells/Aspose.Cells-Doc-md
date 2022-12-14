---
title: Hämta SQL-anslutningsdata
type: docs
weight: 10
url: /sv/net/retrieving-sql-connection-data/
---
{{% alert color="primary" %}}

 Aspose.Cells kan hjälpa dig att hämta SQL-anslutningsdata. Detta inkluderar all data som krävs för att göra en anslutning till SQL-servern, till exempel,**serverns URL**, **Användarnamn**, **tabellnamn**, **fullständig SQL-fråga**, **frågetyp**, **bordets placering** , och**namnet på det namngivna området** förknippas med det.

{{% /alert %}}

I Microsoft Excel, anslut till en databas genom att:

1.  Genom att klicka på**Data** menyn och välja**Från andra källor** följd av**Från SQL Server**.
1.  Välj sedan**Data** följd av**Anslutningar**.
1. Använd guiden Anslutningar för att ansluta till databasen och skapa en databasfråga.

Aspose.Cells tillhandahåller egenskapen Workbook.DataConnections för att hämta externa anslutningar. Den returnerar en samling ExternalConnection-objekt i arbetsboken.

Om ExternalConnection-objektet innehåller SQL-anslutningsdata kan det vara typ-caste till ett DBConnection-objekt och dess egenskaper kan användas för att hämta databaskommando, kommandotyp, anslutningsbeskrivning, anslutningsinformation, autentiseringsuppgifter och så vidare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}

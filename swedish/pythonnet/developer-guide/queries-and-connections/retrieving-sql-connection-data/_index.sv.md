---
title: Hämta SQL anslutningsdata
type: docs
weight: 10
url: /sv/python-net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET kan hjälpa dig att återföra SQL-anslutningsdata. Detta inkluderar all data som krävs för att skapa en anslutning till SQL-servern, till exempel, **server-URL**, **användarnamn**, **tabellnamn**, **fullständigt SQL-kommando**, **frågetyp**, **plats för tabellen** och **namn på det namngivna området** kopplat till det.

{{% /alert %}}

I Microsoft Excel, anslut till en databas genom att:

1. Klicka på menyn **Data** och välj sedan **Från andra källor** följt av **Från SQL Server**.
1. Välj sedan **Data** följt av **Anslutningar**.
1. Använd Anslutningar-guiden för att ansluta till databasen och skapa en databasfråga.

Aspose.Cells för Python via .NET ger egenskapen Workbook.DataConnections för att hämta externa anslutningar. Den returnerar en samling av ExternalConnection-objekt i arbetsboken.

Om ExternalConnection-objektet innehåller SQL-anslutningsdata kan det typomvandlas till ett DBConnection-objekt och dess egenskaper kan användas för att hämta databasfråga, frågetyp, anslutningsbeskrivning, anslutningsinformation, referenser och så vidare.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-RetrievingSQLConnectionData-1.py" >}}

{{< app/cells/assistant language="python-net" >}}

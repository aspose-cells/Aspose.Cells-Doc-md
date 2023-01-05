---
title: Lägg till eller infoga ett arbetsblad
type: docs
weight: 20
url: /sv/net/add-or-insert-a-worksheet/
---
{{% alert color="primary" %}} 

I det här ämnet kommer vi att diskutera teknikerna för att lägga till eller infoga kalkylblad i en Excel-fil med Aspose.Cells.GridDesktop. Skillnaden mellan att lägga till och infoga kalkylblad är att dessutom läggs ett kalkylblad helt enkelt till i slutet av kalkylbladssamlingen i Excel-filen, men infogning innebär att lägga till ett kalkylblad till en specifik position i kalkylbladssamlingen.

{{% /alert %}} 
## **Lägga till ett arbetsblad**
För att lägga till ett kalkylblad med Aspose.Cells.GridDesktop, följ stegen nedan:

1. Lägg till Aspose.Cells.GridDesktop-kontroll i ett formulär.
1. Anropa kalkylbladssamlingens Lägg till metod i GridDesktop-kontrollen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


Många överbelastade versioner av Add-metoden finns tillgängliga. Med den ovan överbelastade versionen läggs till exempel ett kalkylblad till i Excel-filen med ett standardarknamn. Med andra överbelastade versioner av Add-metoden är det möjligt att definiera namnet som visas nedan i exemplet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **Infoga ett arbetsblad**
För att infoga ett kalkylblad med Aspose.Cells.GridDesktop, följ stegen nedan:

1. Lägg till Aspose.Cells.GridDesktop-kontrollen i ett formulär.
1. Anropa Worksheets-samlingens Insert-metod i GridDesktop-kontrollen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

VIKTIGT: Microsoft Excel (97-2003 XLS) stöder Excel-ark med upp till 65 536 rader och 256 kolumner. Aspose.Cells.GridDesktop följer samma standarder. I Aspose.Cells.GridDesktop-kontrollen kan utvecklare lägga till eller infoga kalkylblad med fler rader och kolumner än standardgränsen, men när de försöker spara Grid-data till en Excel-fil kommer ett undantag att skapas. Det betyder att endast data som finns i de 65 536 raderna och 256 kolumnerna kan sparas i en Excel XLS-fil med Aspose.Cells.GridDesktop, om du använder XLSX (MS Excel 2007/2010) filformat finns det dock ingen sådan begränsning.

{{% /alert %}}

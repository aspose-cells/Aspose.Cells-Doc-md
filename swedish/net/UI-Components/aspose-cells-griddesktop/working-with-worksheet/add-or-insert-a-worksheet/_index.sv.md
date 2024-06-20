---
title: Lägg till eller Infoga ett kalkylblad
type: docs
weight: 20
url: /sv/net/aspose-cells-griddesktop/add-or-insert-a-worksheet/
keywords: GridDesktop, infoga, kalkylblad, infoga kalkylblad
description: Den här artikeln introducerar hur man lägger till eller infogar ett kalkylblad i GridDesktop.
---

{{% alert color="primary" %}} 

I detta ämne kommer vi att diskutera teknikerna för att lägga till eller sätta in arbetsblad i en Excelfil med hjälp av Aspose.Cells.GridDesktop. Skillnaden mellan att lägga till och att sätta in arbetsblad är att förutom att läggas till, så läggs ett arbetsblad helt enkelt till i slutet av arbetsbladssamlingen i Excel-filen medan insättning innebär att lägga till ett arbetsblad på en specifik position i arbetsbladssamlingen.

{{% /alert %}} 
## **Lägga till ett arbetsblad**
För att lägga till ett arbetsblad med Aspose.Cells.GridDesktop, följ stegen nedan:

1. Lägg till Aspose.Cells.GridDesktop-kontrollen på en form.
1. Anropa arbetsbladssamlingens Add-metod i GridDesktop-kontrollen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


Många överbelastade versioner av Add-metoden finns tillgängliga. Genom att använda den ovan överbelastade versionen, till exempel, läggs ett arbetsblad till Excelfilen med ett standardnamn. Genom att använda andra överbelastade versioner av Add-metoden är det möjligt att definiera namnet som visas nedan i exemplet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **Infogning av ett arbetsblad**
För att infoga ett arbetsblad med Aspose.Cells.GridDesktop, följ stegen nedan:

1. Lägg till kontrollen Aspose.Cells.GridDesktop på en formulär.
1. Anropa arbetsbladssamlingens Insert-metod i GridDesktop-kontrollen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

VIKTIGT: Microsoft Excel (97-2003 XLS) stödjer Excelflikar med upp till 65 536 rader och 256 kolumner. Aspose.Cells.GridDesktop följer samma standarder. I Aspose.Cells.GridDesktop-kontrollen kan utvecklare lägga till eller infoga arbetsblad med fler rader och kolumner än standardbegränsningen, men när de försöker spara rutnätsdatan till en Excelfil kommer ett undantag att kastas. Det innebär att endast data som finns i 65 536 rader och 256 kolumner kan sparas i en Excel XLS-fil med hjälp av Aspose.Cells.GridDesktop, om du använder XLSX (MS Excel 2007/2010) filformatet finns det ingen sådan begränsning dock.

{{% /alert %}}

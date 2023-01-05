---
title: Åtkomst till arbetsblad
type: docs
weight: 10
url: /sv/net/accessing-worksheet/
---
{{% alert color="primary" %}} 

Ett kalkylblad är en integrerad del av en Excel-fil. Faktum är att en Excel-fil består av ett eller flera kalkylblad. Varje kalkylblad kan endast bestå av upp till 65 536 rader och 256 kolumner. Det är kalkylbladet som innehåller data i en Excel-fil.

Aspose.Cells.GridDesktop kan skapa och manipulera befintliga och nya Excel-filer så det finns naturligtvis ett sätt att komma åt kalkylblad med Aspose.Cells.GridDesktop. Det här ämnet diskuterar hur.

{{% /alert %}} 
## **Använda kalkylbladsindex**
Utvecklare kan komma åt en instans av vilket kalkylblad som helst genom att använda kalkylbladsindexet för ett önskat kalkylblad som visas nedan i exemplet. Detta tillvägagångssätt är bra för att iterera genom ett antal kalkylblad i en Excel-fil.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Använder kalkylbladsnamn**
Om namnet på kalkylbladet är känt är det möjligt att komma åt ett kalkylblad med dess namn enligt nedan.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Få tillgång till ett aktivt arbetsblad**
Det är möjligt att en Excel-fil kommer att ha mer än ett kalkylblad. Den htat en användare arbetar med kallas det aktiva kalkylbladet. Det är möjligt att komma åt det aktiva arket.

För att komma åt ett aktivt kalkylblad erbjuder Aspose.Cells.GridDesktop två metoder:
### **Använda egenskapen AcriveSheetIndex**
Ett sätt att komma åt ett aktivt kalkylblad med Aspose.Cells.GridDesktop-kontrollen är att använda GridDesktop-kontrollens ActiveSheetIndex-egenskap. Med den här egenskapen är det möjligt att hämta indexet för det aktiva kalkylbladet i Aspose.Cells.GridDesktop-kontrollen. Sedan kan det indexet användas för att komma åt kalkylbladet på ett traditionellt sätt som visas nedan.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **Använda GetActiveWorksheet-metoden**
Den andra metoden är att anropa GridDesktop-kontrollens GetActiveWorksheet-metod. Den här metoden ger en referens till det kalkylblad som för närvarande är aktivt i Aspose.Cells.GridDesktop-kontroll som visas nedan.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}

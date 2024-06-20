---
title: Åtkomst av Kalkylblad
type: docs
weight: 10
url: /sv/net/aspose-cells-griddesktop/access-worksheet/
keywords: GridDesktop, kalkylblad
description: Denna artikel introducerar hur man arbetar med kalkylblad i GridDesktop.
---

{{% alert color="primary" %}} 

Ett kalkylblad är en integrerad del av en Excel-fil. Faktum är att en Excel-fil är sammansatt av ett eller flera kalkylblad. Varje kalkylblad kan bestå av upp till 65 536 rader och endast 256 kolumner. Det är kalkylarket som håller data i en Excel-fil.

Aspose.Cells.GridDesktop kan skapa och manipulera befintliga och nya Excel-filer, så det finns naturligtvis ett sätt att komma åt kalkylblad med hjälp av Aspose.Cells.GridDesktop. Detta ämne diskuterar hur.

{{% /alert %}} 
## **Användning av Arbetsbladsindex**
Utvecklare kan komma åt en instans av ett önskat kalkylblad genom att använda kalkylbladets index som visas nedan i exemplet. Det här tillvägagångssättet är bra för att iterera igenom ett antal kalkylblad i en Excel-fil.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Användning av Arbetsbladsnamn**
Om kalkylbladets namn är känt, är det möjligt att komma åt ett kalkylblad med hjälp av dess namn som visas nedan.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Åtkomst av ett aktivt kalkylblad**
Det är möjligt att en Excel-fil har fler än ett kalkylblad. Det som en användare arbetar på kallas det aktiva kalkylbladet. Det är möjligt att komma åt det aktiva arket.

För att komma åt ett aktivt kalkylblad, erbjuder Aspose.Cells.GridDesktop två tillvägagångssätt:
### **Använda AcriveSheetIndex-egenskapen**
Ett sätt att komma åt ett aktivt kalkylblad med hjälp av styreglen GridDesktops egenskap ActiveSheetIndex är att använda. Med denna egenskap är det möjligt att få indexet för det aktiva kalkylbladet i styregeln GridDesktop. Därefter kan det indexet användas för att komma åt kalkylarket på ett traditionellt sätt som visas nedan.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **Använda GetActiveWorksheet-metoden**
Det andra tillvägagångssättet är att anropa styregeln GridDesktops GetActiveWorksheet-metod. Denna metod ger en referens till det kalkylblad som för närvarande är aktivt i styregeln GridDesktop enligt nedan.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}

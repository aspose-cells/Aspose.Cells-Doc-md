---
title: Använder namngivna intervall
type: docs
weight: 110
url: /sv/net/using-named-ranges/
---
{{% alert color="primary" %}} 

 Normalt använder du etiketterna för kolumner och rader på ett kalkylblad för att referera till cellerna i dessa kolumner och rader. Men du kan skapa beskrivande namn för att representera celler, cellintervall, formler eller konstanta värden. Ordet**namn**kan hänvisa till en teckensträng som representerar en cell, cellintervall, formel eller konstant värde. Använd till exempel lättförståeliga namn, som Produkter, för att referera till svårförståeliga intervall, till exempel Sales!C20:C30 för att representera en cell, cellintervall, formel eller konstant värde. Etiketter kan användas i formler som refererar till data på samma kalkylblad; om du vill representera ett intervall på ett annat kalkylblad kan du använda ett namn.**Namngivna Ranges** är bland de mest kraftfulla funktionerna i Microsoft. Användare kan tilldela ett namn till ett namngivet område så att detta cellområde kan refereras med dess namn i formlerna.**Aspose.Cells.GridDesktop** stöder denna funktion.

{{% /alert %}} 
## **Lägga till/refera till namngivna intervall i formler**
GridDesktop-kontrollen stöder import/export av namngivna intervall i Excel-filerna, den tillhandahåller två klasser (**namn** och**Namnsamling**) för att arbeta med namngivna intervall.

Följande kodavsnitt hjälper dig hur du använder dem.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}

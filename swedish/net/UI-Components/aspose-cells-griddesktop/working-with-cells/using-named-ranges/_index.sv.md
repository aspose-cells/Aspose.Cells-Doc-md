---
title: Använd namngivna områden
type: docs
weight: 110
url: /sv/net/aspose-cells-griddesktop/use-named-ranges/
keywords: GridDesktop,namngivna områden,namn
description: Denna artikel introducerar de namngivna områdena i GridDesktop.
---

{{% alert color="primary" %}} 

Normalt sett använder du kolumn- och radetiketter på ett blad för att hänvisa till cellerna inom de kolumnerna och raderna. Men du kan skapa beskrivande namn för att representera celler, cellintervall, formler eller konstanta värden. Ordet **Namn** kan referera till en sträng av tecken som representerar en cell, cellintervall, formel eller konstant värde. Använd lättförståeliga namn, exempelvis Produkter, för att hänvisa till svåra att förstå intervall, som Försäljning!C20:C30 för att representera en cell, cellintervall, formel eller konstant värde. Etiketter kan användas i formler som hänvisar till data på samma blad; om du vill representera ett intervall på ett annat blad kan du använda ett namn. **Namngivna områden** är bland de mest kraftfulla funktionerna i Microsoft. Användare kan tilldela ett namn till ett namngivet område så att detta cellintervall kan hänvisas till med sitt namn i formlerna. **Aspose.Cells.GridDesktop** stödjer denna funktion.

{{% /alert %}} 
## **Lägga till/hänvisa namngivna områden i formler**
GridDesktop-kontrollen stöder att importera/exportera namngivna områden i Excel-filerna, den ger två klasser (**Namn** och **NamnCollection**) för att arbeta med namngivna områden.

Följande kodsnutt hjälper dig att använda dem.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}

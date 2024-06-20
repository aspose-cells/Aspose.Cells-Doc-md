---
title: Lägga till och referera namngivna områden
type: docs
weight: 120
url: /sv/net/aspose-cells-gridweb/add-and-reference-named-ranges/
keywords: GridWeb,GridName,Names
description: Den här artikeln introducerar hur du arbetar med namngivna områden i GridWeb. 
---

{{% alert color="primary" %}} 

Vanligtvis används kolumn- och radetiketter för att unikt hänvisa till celler. Men du kan skapa beskrivande namn för att representera celler, cellintervall, formler eller konstanta värden. Ordet **Namn** kan till exempel hänvisa till en sträng av tecken som representerar en cell, ett cellintervall, en formel eller ett konstant värde. Använd enkelt förståeliga namn, som Produkter, för att hänvisa till svårförståeliga intervall, som Försäljning!C20:C30. Etiketter kan användas i formler som hänvisar till data på samma arbetsblad. Om du vill representera ett intervall på ett annat arbetsblad kan du använda ett namn. **Namngivna områden** är en av de mest kraftfulla funktionerna i Microsoft Excel. Användare kan tilldela ett namn till ett område och använda det namnet i formler. Aspose.Cells.GridWeb stöder denna funktion.

{{% /alert %}} 
## **Lägga till/hänvisa namngivna områden i formler**
GridWeb-kontrollen tillhandahåller två klasser (GridName och GridNameCollection) för att arbeta med namngivna områden. Följande kodsnutt hjälper dig att förstå hur du skapar det namngivna området och får åtkomst till det i formler.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}

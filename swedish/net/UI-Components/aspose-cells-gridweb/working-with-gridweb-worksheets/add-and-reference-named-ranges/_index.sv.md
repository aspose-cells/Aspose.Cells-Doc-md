---
title: Lägg till och referera till namngivna intervall
type: docs
weight: 120
url: /sv/net/add-and-reference-named-ranges/
---
{{% alert color="primary" %}} 

 Normalt används kolumn- och radetiketter för att unikt referera till celler. Men du kan skapa beskrivande namn för att representera celler, cellintervall, formler eller konstanta värden. Ordet**namn**kan hänvisa till en teckensträng som representerar en cell, cellintervall, formel eller konstant värde. Använd till exempel lättförståeliga namn, som Produkter, för att referera till svårförståeliga intervall, som Sales!C20:C30. Etiketter kan användas i formler som refererar till data på samma kalkylblad; om du vill representera ett intervall på ett annat kalkylblad kan du använda ett namn.**Namngivna intervall** är en av de mest kraftfulla funktionerna i Microsoft Excel. Användare kan tilldela ett namn till ett intervall och använda det namnet i formler. Aspose.Cells.GridWeb stöder den här funktionen.

{{% /alert %}} 
## **Lägga till/refera till namngivna intervall i formler**
GridWeb-kontrollen tillhandahåller två klasser (GridName och GridNameCollection) för att arbeta med namngivna intervall. Följande kodavsnitt hjälper dig att förstå hur du skapar det namngivna intervallet och kommer åt det i formlerna.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}

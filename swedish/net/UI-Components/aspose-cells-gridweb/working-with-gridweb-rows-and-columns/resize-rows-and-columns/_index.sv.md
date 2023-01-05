---
title: Ändra storlek på rader och kolumner
type: docs
weight: 30
url: /sv/net/resize-rows-and-columns/
---
{{% alert color="primary" %}} 

Ibland är cellvärden bredare än cellen de är i, eller finns på flera rader. Sådana värden är inte helt synliga för användare om de inte ändrar höjden och bredden på rader och kolumner. Aspose.Cells.GridWeb stöder fullt ut inställning av radhöjder och kolumnbredd. Det här ämnet diskuterar dessa funktioner i detalj med hjälp av exempel.

{{% /alert %}} 
## **Arbeta med radhöjder och kolumnbredd**
### **Ställa in radhöjd**
Så här ställer du in höjden på en rad:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ditt webbformulär.
1. Gå till kalkylbladets Cells-samling.
1. Ställ in höjden på alla celler i en angiven rad.

{{% alert color="primary" %}} 

SetRowHeight och SetColumnWidth-metoden för Cells-samlingen har också varianter tillgängliga för att ställa in radhöjd och kolumnbreddsmått i tum och pixlar.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetRowHeight.cs" >}}
### **Ställa in kolumnbredd**
Så här ställer du in bredden på en kolumn:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ditt webbformulär.
1. Gå till kalkylbladets Cells-samling.
1. Ställ in bredden på alla celler i en viss kolumn.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetColumnWidth.cs" >}}

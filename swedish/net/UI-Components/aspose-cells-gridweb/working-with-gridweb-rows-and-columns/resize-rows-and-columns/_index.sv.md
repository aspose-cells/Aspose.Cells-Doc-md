---
title: Ändra storlek på rader och kolumner
type: docs
weight: 30
url: /sv/net/aspose-cells-gridweb/resize-rows-and-columns/
keywords: GridWeb,bredd,höjd,radhöjd,kolumnbredd
description: Den här artikeln introducerar hur man ställer in radhöjd och kolumnbredd i GridWeb.
---

{{% alert color="primary" %}} 

Ibland är cellvärden bredare än cellen de är i eller går över flera rader. Sådana värden syns inte helt för användare om de inte ändrar höjden och bredden på rader och kolumner. Aspose.Cells.GridWeb stöder fullt ut att ställa in radhöjder och kolumnbredder. Detta ämne diskuterar dessa funktioner i detalj med hjälp av exempel.

{{% /alert %}} 
## **Arbeta med radhöjder och kolumnbredder**
### **Ange radhöjd**
För att ställa in höjden på en rad:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i ditt webbformulär.
1. Få åtkomst till Cells-samlingen i kalkylarket.
1. Ställ in höjden på alla celler i valfri angiven rad.

{{% alert color="primary" %}} 

SetRowHeight och SetColumnWidth-metoden i Cells-samlingen har också varianter tillgängliga för att ställa in radhöjd och kolumnbredds mätningar i tum och pixlar.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetRowHeight.cs" >}}
### **Ange kolumnbredd**
För att ställa in bredden på en kolumn:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i ditt webbformulär.
1. Få åtkomst till Cells-samlingen i kalkylarket.
1. Ställ in bredden på alla celler i valfri angiven kolumn.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetColumnWidth.cs" >}}

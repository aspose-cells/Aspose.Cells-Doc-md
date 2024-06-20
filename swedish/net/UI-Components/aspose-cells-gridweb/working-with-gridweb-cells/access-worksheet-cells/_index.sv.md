---
title: Åtkomst till arbetsbladscell
type: docs
weight: 10
url: /sv/net/aspose-cells-gridweb/access-worksheet-cell/
keywords: GridWeb,cell,GridCell
description: Den här artikeln introducerar hur man får cellen (GridCell) i GridWeb.
---

{{% alert color="primary" %}} 

Detta ämne diskuterar celler och tittar på Aspose.Cells.GridWeb's mest grundläggande funktion: åtkomst till celler.

{{% /alert %}} 
## **Åtkomst till celler i ett arbetsblad**
Varje arbetsblad innehåller en egenskap med namnet Cells som faktiskt är en samling av GridCell-objekt där ett GridCell-objekt representerar en cell i Aspose.Cells.GridWeb. Det är möjligt att komma åt vilken cell som helst med hjälp av Aspose.Cells.GridWeb. Det finns två föredragna metoder, vilka båda diskuteras nedan.


### **Användning av cellnamn**
Alla celler har ett unikt namn. Till exempel A1, A2, B1, B2 osv. Aspose.Cells.GridWeb tillåter utvecklare att komma åt vilken önskad cell som helst genom att använda cellnamnet. Ange helt enkelt cellnamnet (som en index) till Cells-samlingen av GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


**Observera**

Åtkomst till GridCell med hjälp av cells[cellName] kan använda mer minne. Det kommer alltid att skapa en ny cell (GridCell) objekt oavsett om cellen är null.


### **Använda rad- och kolumnindex**


En cell kan också identifieras med dess plats i form av rad- och kolumnindex. Skicka bara en cells rad- och kolumnindex till Cells-samlingen av GridWorksheet. Detta tillvägagångssätt är snabbare än det ovanstående.

**Bästa praxis**:

om vi vill få cellens värde eller cellstil och inte vill göra uppdateringsoperationen, kan vi använda **CheckCell**-metoden som kommer att returnera null om cellen inte finns. Detta kommer att **spara minne**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   GridCell cell = cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}



**Bästa praxis**:
### Iterera över celler
om vi vill komma åt alla celler i arbetsbladet en efter en, kan vi använda **iterators** för att gå igenom de befintliga cellerna. Detta kommer att **spara minne**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
jämför nedanstående kod som är **dålig**, detta kommer att skapa alla celler oavsett om de är null, vilket kommer att orsaka minnesproblem, så använd inte detta sätt
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r< cells.MaxRow;r++)
 {
     for(int c=0;c< cells.MaxColumn; c++)
     {
         Console.WriteLine(cells[r,c].ToString());
     }
 }
~~~

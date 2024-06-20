---
title: Åtkomst av GridCell i ett arbetsblad
type: docs
weight: 10
url: /sv/net/aspose-cells-griddesktop/access-cell-in-a-worksheet/
keywords: GridDesktop,GridCell,get cell
description: Denna artikel introducerar hur man får cellobjekt (GridCell) i arbetsbladet i GridDesktop.
---

{{% alert color="primary" %}} 

Vi har hittills diskuterat att arbeta med arbetsblad, rader och kolumner men nu är det dags att gå djupare och prata om celler. Så i det här ämnet ska vi börja vår diskussion om celler med en grundläggande funktion för att få åtkomst till celler.

{{% /alert %}} 
## **Åtkomst av cell i ett arbetsblad**
Vi kan få åtkomst till vilken cell som helst i ett arbetsblad med hjälp av Aspose.Cells.GridDesktops API. Det kan finnas tre möjliga sätt att få åtkomst till cellen enligt följande:

- **Använda cellnamn**
- **Använda rad- och kolumnindex**
- **Få fokuserad cell**

Låt oss diskutera ovanstående tre tillvägagångssätt en efter en.
### **Användning av cellnamn**
Alla celler i ett arbetsblad har ett unikt namn. Till exempel A1, A2, B1, B2 etc. Aspose.Cells.GridDesktop tillåter utvecklare att få åtkomst till vilken önskad cell som helst genom att använda dess cellnamn. Det enda vi behöver göra är att helt enkelt skicka cellnamnet (som index) till **Cells**-samlingen på **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}

**Observera**

Åtkomst till GridCell med hjälp av cells[cellName] kan använda mer minne. Det kommer alltid att skapa en ny cell (GridCell) objekt oavsett om cellen är null.

### **Användning av cellens rad- och kolumnindex**

**Bästa praxis**:

om vi vill få cellens värde eller cellstil och inte vill göra uppdateringsoperationen, kan vi använda **CheckCell**-metoden som kommer att returnera null om cellen inte finns. Detta kommer att **spara minne**.
~~~C#
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Åtkomst av en cell med hjälp av dess rad- och kolumnindex
GridCell cell = sheet.Cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~

En cell i ett arbetsblad kan också identifieras med sin plats i termer av dess rad- och kolumnindex. Det enda vi behöver göra är att helt enkelt skicka rad- och kolumnindexen för cellen till **Cells**-samlingen på **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}

**Observera**

Att komma åt gridcellen med cells[rowIndex, columnIndex] kan förbruka mer minne. Det kommer alltid att skapa en ny cell (GridCell)-objekt oavsett om cellen är null eller inte.


### **Få fokuserad cell**
Om du inte vet exakt vilken cell som ska kommas åt, tillåter också Aspose.Cells.GridDesktop dig att komma åt en cell som är i fokus för en användare. Med den här funktionen kan du låta en användare välja vilken cell som helst och sedan komma åt den cellen i bakgrunden. Det kan enkelt uppnås genom att använda **GetFocusedCell**-metoden i **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}

**Bästa praxis**:
### Iterera över celler
om vi vill komma åt alla celler i arbetsbladet en efter en, kan vi använda **iterators** för att gå igenom de befintliga cellerna. Detta kommer att **spara minne**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();

   GridCells cells = sheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
jämför nedanstående kod som är **dålig**, detta kommer att skapa alla celler oavsett om de är null, vilket kommer att orsaka minnesproblem, så använd inte detta sätt
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 for(int r=0;r< sheet.RowsCount;r++)
 {
     for(int c=0;c< sheet.ColumnsCount; c++)
     {
         Console.WriteLine(sheet.Cells[r,c].ToString());
     }
 }
~~~


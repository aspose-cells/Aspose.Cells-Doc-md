---
title: Kopiera ett arbetsblad
type: docs
weight: 50
url: /sv/net/copy-a-worksheet/
---
{{% alert color="primary" %}} 

[Lägg till arbetsblad](/cells/sv/net/add-worksheets/) beskriver hur man lägger till nya kalkylblad till Aspose.Cells.GridWeb. Det är också möjligt att lägga till en kopia (eller replika) av ett annat kalkylblad till Aspose.Cells.GridWeb-kontrollen. Den här funktionen kan vara användbar när identiska eller liknande data i ett kalkylblad också krävs i ett annat kalkylblad. När så är fallet är det lättare att kopiera ett befintligt kalkylblad och lägga till det i Aspose.Cells.GridWeb som ett nytt kalkylblad istället för att skapa det från början.

{{% /alert %}} 
## **Kopiera ett arbetsblad**
### **Använder Sheet index**
Exempelkoden nedan visar hur man lägger till en kopia av ett kalkylblad till GridWeb-kontrollen genom att ange kalkylbladets index i GridWorksheetCollections AddCopy-metod.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **Använder arknamn**
Exempelkoden nedan visar hur man lägger till en kopia av ett kalkylblad till GridWeb-kontrollen genom att ange kalkylbladets namn i GridWorksheetCollections AddCopy-metod.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

 Metoden AddCopy returnerar det nyligen tillagda kalkylbladets index som kan användas för att komma åt kalkylbladsinstansen. För mer information om hur du kommer åt arbetsblad, läs[Få tillgång till arbetsblad](/cells/sv/net/access-worksheets/).

{{% /alert %}}

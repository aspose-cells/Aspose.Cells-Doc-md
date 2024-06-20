---
title: Kopiera ett kalkylblad
type: docs
weight: 50
url: /sv/net/aspose-cells-gridweb/copy-a-worksheet/
keywords: GridWeb, kopiera, GridWorksheet
description: Den här artikeln introducerar hur man kopierar ett kalkylblad (GridWorksheet) i GridWeb.
---

{{% alert color="primary" %}} 

[Lägg till kalkylblad](/cells/sv/net/aspose-cells-gridweb/lagg-till-kalkylblad/) beskriver hur man lägger till nya kalkylblad i Aspose.Cells.GridWeb. Det är också möjligt att lägga till en kopia (eller replika) av ett annat kalkylblad till Aspose.Cells.GridWeb-kontrollen. Den här funktionen kan vara användbar när identiska eller liknande data i ett kalkylblad också krävs i ett annat kalkylblad. När så är fallet är det enklare att kopiera ett befintligt kalkylblad och lägga till det i Aspose.Cells.GridWeb som ett nytt kalkylblad istället för att skapa det från början.

{{% /alert %}} 
## **Kopiera ett kalkylblad**
### **Genom att använda arkindex**
Det här exempelkoden nedan visar hur man lägger till en kopia av ett kalkylblad i GridWeb-kontrollen genom att ange kalkylbladets index i GridWorksheetCollections AddCopy-metod.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **Genom att använda arknamn**
Det här exempelkoden nedan visar hur man lägger till en kopia av ett kalkylblad i GridWeb-kontrollen genom att ange kalkylbladets namn i GridWorksheetCollections AddCopy-metod.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

AddCopy-metoden returnerar det nyss tillagda kalkylbladets index vilket kan användas för att komma åt kalkylbladsinstansen. För mer detaljer om hur man kommer åt kalkylblad, läs [Kom åt kalkylblad](/cells/sv/net/aspose-cells-gridweb/kom-at-kalkylblad/).

{{% /alert %}}

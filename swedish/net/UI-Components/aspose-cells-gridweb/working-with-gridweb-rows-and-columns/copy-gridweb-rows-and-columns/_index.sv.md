---
title: Kopiera GridWeb rader och kolumner
type: docs
weight: 80
url: /sv/net/aspose-cells-gridweb/copy-gridweb-rows-and-columns/
keywords: GridWeb, kopiera
description: Denna artikel beskriver hur man kopierar rader och kolumner i GridWeb.
---

{{% alert color="primary" %}} 

Komponenten Aspose.Cells.GridWeb erbjuder möjligheten att kopiera rad och kolumn med hjälp av GridCells-klassen. Denna artikel demonstrerar användningen av de API: er som tillhandahålls av Aspose.Cells.GridWeb för att kopiera rader och kolumner på GridWeb-gränssnittet. 

Metoderna GridCells.CopyRow, GridCells.CopyColumn, GridCells.CopyRows och GridCells.CopyColumns kommer att kopiera innehållet, stilen och formlerna från källraden och kolumnen till destinationen.

{{% /alert %}} 
## **Kopiera rader och kolumner**
Om du inte redan är bekant med Aspose.Cells.GridWeb-komponenten rekommenderar vi starkt att du kontrollerar [Introduktion till Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/aspose-cells-gridweb/browsers-capabilities/) och detaljerad artikel om [Så här lägger du till Aspose.Cells.GridWeb-komponenten i en webbformsapplikation](https://docs.aspose.com/cells/net/aspose-cells-gridweb/add-gridweb-to-web-form/).
### **Kopiera enstaka rad**
För att hålla exemplet enkelt använder artikeln en befintlig kalkylblad med en rad och en enkel formel som summerar alla värden i raden. Här är hur kalkylbladet visas i gränssnittet Aspose.Cells.GridWeb före kopieringen av raden.

![todo:image_alt_text](copy-gridweb-rows-and-columns_1.png)

Kodexemplet är enkelt som visas nedan. Det används GridCells-objektet för aktivt arbetsblad för att kopiera den första raden till den efterföljande raden.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


Så här ser Aspose.Cells.GridWeb ut efter kopieringsoperationen av raden.

![todo:image_alt_text](copy-gridweb-rows-and-columns_2.png)
### **Kopiera enstaka kolumn**
I det följande exemplet används en befintlig kalkylblad med en kolumn och en enkel formel som summerar alla värden i kolumnen. Så här visas kalkylbladet i gränssnittet Aspose.Cells.GridWeb före kopiering av kolumnen.

![todo:image_alt_text](copy-gridweb-rows-and-columns_3.png)

På samma sätt som det tidigare exemplet, använder följande kodsnutt GridCells-objektet för aktivt arbetsblad för att kopiera den första kolumnen till den efterföljande kolumnen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



Så här ser Aspose.Cells.GridWeb ut efter kopiering av kolumnen.

![todo:image_alt_text](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

Du kan använda metoderna GridCells.CopyRow och GridCells.CopyColumn i en loop för att kopiera källraden och kolumnen till flera rader och kolumner.

{{% /alert %}} 
### **Kopiera flera rader**
Det är också möjligt att kopiera flera rader till en ny destination med metoden GridCells.CopyRows, som tar ett ytterligare parameter av typen int för att ange antalet källrader som ska kopieras.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



Här är hur Aspose.Cells.GridWeb ser ut före och efter kopiering av rader.

![todo:image_alt_text](copy-gridweb-rows-and-columns_5.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_6.png)
### **Kopiera flera kolumner**
GridCells-klassen tillhandahåller också metoden CopyColumns, vilken tar en extra parameter av typ integer för att specificera antalet källekolumner som ska kopieras.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



Här är hur Aspose.Cells.GridWeb ser ut före och efter kopiering av rader.

![todo:image_alt_text](copy-gridweb-rows-and-columns_7.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_8.png)

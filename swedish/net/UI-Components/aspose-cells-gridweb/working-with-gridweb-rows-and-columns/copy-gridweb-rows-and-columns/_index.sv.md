---
title: Kopiera GridWeb rader och kolumner
type: docs
weight: 80
url: /sv/net/copy-gridweb-rows-and-columns/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb-komponenten erbjuder möjligheten att kopiera rader och kolumner medan du använder GridCells-klassen. Den här artikeln visar användningen av API:er som exponeras av Aspose.Cells.GridWeb för att kopiera rader och kolumner i GridWeb-gränssnittet.

Metoderna GridCells.CopyRow, GridCells.CopyColumn, GridCells.CopyRows & GridCells.CopyColumns kopierar innehållet, stilen och formlerna från källraden och kolumnen till destinationen.

{{% /alert %}} 
## **Kopiera rader och kolumner**
 Om du inte redan är bekant med Aspose.Cells.GridWeb-komponenten rekommenderar vi starkt att du kontrollerar[Introduktion till Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/browsers-capabilities/) och detaljerad artikel om[Hur man lägger till Aspose.Cells.GridWeb-komponent i en WebForms-applikation](https://docs.aspose.com/cells/net/add-gridweb-to-web-form/).
### **Kopiera en rad**
För att hålla exemplet enkelt använder artikeln ett befintligt kalkylblad med en rad och en enkel formel som summerar alla värden i raden. Så här visas kalkylarket i Aspose.Cells.GridWeb-gränssnittet innan du kopierar raden.

![todo:image_alt_text](copy-gridweb-rows-and-columns_1.png)

Kodavsnittet är enkelt som visas nedan. Den kommer åt GridCells objekt i aktiv kalkylbladsordning för att göra en kopia av den första raden till den efterföljande raden.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


Så här ser Aspose.Cells.GridWeb ut efter kopieringsradoperation.

![todo:image_alt_text](copy-gridweb-rows-and-columns_2.png)
### **Kopiera en kolumn**
Följande exempel använder ett befintligt kalkylblad med en kolumn och en enkel formel som summerar alla värden i kolumnen. Så här visas kalkylarket i Aspose.Cells.GridWeb-gränssnittet innan du kopierar kolumnen.

![todo:image_alt_text](copy-gridweb-rows-and-columns_3.png)

I likhet med exemplet ovan får följande kodavsnitt åtkomst till GridCells-objektet i aktiv kalkylbladsordning för att göra en kopia av den första kolumnen till den efterföljande kolumnen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



Så här ser Aspose.Cells.GridWeb ut efter kopieringskolumnen.

![todo:image_alt_text](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

Du kan använda metoderna GridCells.CopyRow & GridCells.CopyColumn i loop för att kopiera källraden och kolumnen till flera respektive rader och kolumner.

{{% /alert %}} 
### **Kopiera flera rader**
Det är också möjligt att kopiera flera rader till en ny destination medan du använder metoden GridCells.CopyRows, som kräver en extra parameter av typen heltal för att specificera antalet källrader som ska kopieras.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



Så här ser Aspose.Cells.GridWeb ut före och efter operation av kopieringsrader.

![todo:image_alt_text](copy-gridweb-rows-and-columns_5.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_6.png)
### **Kopiera flera kolumner**
GridCells-klassen tillhandahåller också CopyColumns-metoden, som kräver en extra parameter av typen heltal för att ange antalet källkolumner som ska kopieras.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



Så här ser Aspose.Cells.GridWeb ut före och efter operation av kopieringsrader.

![todo:image_alt_text](copy-gridweb-rows-and-columns_7.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_8.png)

---
title: Pivot tabell och källdata
type: docs
weight: 110
url: /sv/java/pivot-table-and-source-data/
---

## **Pivot-tabellens källdata**
Det finns tillfällen när du vill skapa Microsoft Excel-rapporter med pivot-tabeller som hämtar data från olika datakällor (såsom en databas) som inte är kända vid design-tid. Den här artikeln presenterar ett tillvägagångssätt för dynamiskt att ändra en pivot-tabells datakälla.
## **Ändra en pivot-tabells källdata**
1. Skapa en ny designer-mall.
   1. Skapa en ny designer-mallfil enligt skärmbilden nedan.
   1. Definiera sedan ett namngivet område, **Datakälla**, som hänvisar till detta cellområde. 

      **Skapa en designer-mall & definiera ett namngivet område, Datakälla** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Skapa en pivot-tabell baserad på detta namngivna område.
   1. I Microsoft Excel, välj **Data**, sedan **Pivottabell** och **PivotDiagramrapport**.
   1. Skapa en pivottabell baserad på det namngivna området som skapats i det första steget. 

      **Skapa en pivottabell baserad på det namngivna området, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)

1. Dra det motsvarande fältet till pivottabellraden och kolumnen, skapa sedan den resulterande pivottabellen enligt skärmdumpen nedan. 

   **Skapa en pivottabell baserad på ett motsvarande fält** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)

1. Högerklicka på pivottabellen och välj **Tabelloptioner**.
   1. Markera **Uppdatera vid öppning** i inställningarna för **Dataalternativ**. 

      **Inställning av pivottabellalternativ** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)



Nu kan du spara den här filen som din designer-mallfil.

1. Försörjning av ny data och ändring av källdata för en pivottabell.
   1. När den designer-mall är skapad, använd följande kod för att ändra källan till pivottabellen.

Genom att köra exempelkoden nedan ändras källan till datan för pivottabellen och pivottabellen kommer att se ut som nedan.

**Dynamiskt ändrad pivottabell** 

![todo:image_alt_text](pivot-table-and-source-data_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ChangeSourceData-ChangeSourceData.java" >}}
{{< app/cells/assistant language="java" >}}

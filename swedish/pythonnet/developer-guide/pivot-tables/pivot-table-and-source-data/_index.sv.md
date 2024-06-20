---
title: Pivot tabell och källdata
type: docs
weight: 30
url: /sv/python-net/pivot-table-and-source-data/
description: Den här artikeln visar hur du ändrar källdata för pivottabell med Aspose.Cells för Python via .NET.
keywords: Aspose.Cells för Python Excel, Excel Python bibliotek, Hur man ändrar pivottabellens källdata med hjälp av Aspose.Cells för Python Excel Library.
---

## **Pivot-tabellens källdata**

Det finns tillfällen då du vill skapa Microsoft Excel-rapporter med pivottabeller som hämtar data från olika datakällor (t.ex. en databas) som inte är kända vid design-tid. Denna artikel ger en metod för att dynamiskt ändra en pivot-tabells datakälla.

### **Ändra en pivot-tabells källdata**

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

Genom att köra den här exempelkoden nedan ändras källan till pivottabellen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-ChangeSourceData-1.py" >}}


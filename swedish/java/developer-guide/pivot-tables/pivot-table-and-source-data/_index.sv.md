---
title: Pivottabell och källdata
type: docs
weight: 110
url: /sv/java/pivot-table-and-source-data/
---
## **Pivottabellens källdata**
Det finns tillfällen då du vill skapa Microsoft Excel-rapporter med pivottabeller som tar data från olika datakällor (som en databas) som inte är kända vid designtillfället. Den här artikeln ger en metod för att dynamiskt ändra en pivottabells datakälla.
## **Ändra en pivottabells källdata**
1. Skapa en ny designermall.
1. Skapa en ny designermallfil enligt skärmdumpen nedan.
 1. Definiera sedan ett namngivet intervall,**Datakälla** , som hänvisar till detta cellområde.

      **Skapa en designermall och definiera ett namngivet intervall, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Skapa en pivottabell baserat på detta namngivna intervall.
 1. Välj i Microsoft Excel**Data** , då**Pivottabell** och**Pivotdiagramrapport**.
 1. Skapa en pivottabell baserat på det namngivna intervallet som skapades i det första steget.

      **Skapa en pivottabell baserad på det namngivna intervallet, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)

1.  Dra motsvarande fält för att pivotera tabellens rad och kolumn och skapa sedan den resulterande pivottabellen som i skärmdumpen nedan.

   **Skapa en pivottabell baserat på ett motsvarande fält** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)

1.  Högerklicka på pivottabellen och välj**Tabellalternativ**.
 1. Kontrollera**Uppdatera vid öppen** i**Dataalternativ** inställningar.

      **Ställa in alternativen för pivottabellen** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)



Nu kan du spara den här filen som din designermallfil.

1. Fylla på nya data och ändra källdata för en pivottabell.
1. När designmallen har skapats använder du följande kod för att ändra källdata för pivottabellen.

Genom att köra exempelkoden nedan ändras källdata för pivottabellen och pivottabellen kommer att se ut som den nedan.

**Dynamiskt ändrad pivottabell** 

![todo:image_alt_text](pivot-table-and-source-data_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ChangeSourceData-ChangeSourceData.java" >}}

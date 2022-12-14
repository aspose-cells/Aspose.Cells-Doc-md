---
title: Skapa och formatera tabell
type: docs
weight: 10
url: /sv/cpp/create-and-format-table/
---
## **Skapa bord**
En av fördelarna med kalkylblad är att de låter dig skapa olika typer av listor, till exempel telefonlistor, uppgiftslistor, listor över transaktioner, tillgångar eller skulder. Flera användare kan arbeta tillsammans för att använda, skapa och underhålla olika listor.

Aspose.Cells stöder att skapa och hantera listor.
### **Fördelar med ett listobjekt**
Det finns en hel del fördelar när du konverterar en lista med data till ett faktiskt listobjekt

- Nya rader och kolumner inkluderas automatiskt.
- En total rad längst ner på din lista kan enkelt läggas till för att visa SUMMA, AVERAGE, COUNT, etc.
- Kolumner som läggs till till höger infogas automatiskt i List-objektet.
- Diagram baserade på rader och kolumner utökas automatiskt.
- Namngivna intervall som tilldelats rader och kolumner kommer att utökas automatiskt.
- Listan är skyddad från oavsiktlig radering och radering.
### **Skapa ett listobjekt med hjälp av Microsoft Excel**

|**Väljer dataintervall för att skapa listobjekt**|
|:- |
|![todo:image_alt_text](jHcNq4o.png)|
Detta visar dialogrutan Skapa lista.

|**Dialogrutan Skapa lista**|
|:- |
|![todo:image_alt_text](kJmukRF.png)|
 Implementera List-objektet för data och ange total rad (Välj**Data** , då**Lista** , följd av**Total rad**).

|**Skapa ett listobjekt**|
|:- |
|![todo:image_alt_text](ECSGVdR.png)|
### **Använder Aspose.Cells API**
 Aspose.Cells tillhandahåller en klass[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) som representerar en Microsoft Excel-fil. De[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) klass innehåller en[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass. De[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass tillhandahåller ett brett utbud av metoder för att hantera ett kalkylblad. Att skapa en[IListObject](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object) i ett kalkylblad använder du[GetIListObjects](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4356bc4b8cffee624891f10ea49a4705) insamlingsmetod för[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass. Varje `[IListObject]` är i själva verket ett föremål för[IListObjectCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection) klass, som ytterligare ger[Lägg till](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)metod för att lägga till ett `[IListObject]`-objekt och ange ett cellintervall för listan.

 Enligt det specificerade cellintervallet skapas objektet `[IListObject]` av Aspose.Cells. Använd attribut (t.ex.[ShowTotals](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a9026460927f035f374f5e1ea74e639f2) och[Lista kolumner](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#afeeb7bfabd0971e9fe34a09f0b83ae73)etc.) av klassen `[IListObject]` för att kontrollera listan.

I exemplet nedan har vi skapat samma `[IListObject]` med Aspose.Cells API som vi skapade med Microsoft Excel i avsnittet ovan.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects.cpp" >}}
## **Formatera en tabell**
För att hantera och analysera en grupp relaterade data är det möjligt att förvandla ett cellintervall till ett listobjekt (även känt som en Excel-tabell). En tabell är en serie rader och kolumner som innehåller relaterade data som hanteras oberoende av data i andra rader och kolumner. Som standard har varje kolumn i tabellen filtrering aktiverad i rubrikraden så att du snabbt kan filtrera eller sortera dina listobjektdata. Du kan lägga till en totalrad (en speciell rad i en lista som tillhandahåller ett urval av aggregerade funktioner som är användbara för att arbeta med numerisk data) till listobjektet som tillhandahåller en rullgardinslista med aggregerade funktioner för varje totalradcell. Aspose.Cells ger alternativ för att skapa och hantera listor (eller tabeller).
### **Formatera ett listobjekt**
 Aspose.Cells tillhandahåller en klass[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) som representerar en Microsoft Excel-fil. De[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) klass innehåller en[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass. De[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass tillhandahåller ett brett utbud av metoder för att hantera kalkylblad. Att skapa en*ListObject*i ett kalkylblad, använd `IListObjectCollection`. Varje `[IListObject]` är i själva verket ett objekt i klassen `IListObjectCollection`, vilket ytterligare tillhandahåller[Lägg till](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)metod för att lägga till ett `[IListObject]`-objekt och ange det cellintervall som det ska omfatta. Enligt det specificerade cellområdet, a*ListObject* skapas i kalkylbladet av Aspose.Cells. Använd attribut (t.ex.[TableStyleType](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a5de8b5321b0ccb30dfb09cefe6536462)) av klassen `[IListObject]` för att formatera tabellen för dina krav.

Exemplet nedan lägger till exempeldata i ett kalkylblad, lägger till ett `[IListObject]` och tillämpar standardstilar på det. `[IListObject]` stilar stöds av Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable.cpp" >}}

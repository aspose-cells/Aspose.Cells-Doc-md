---
title: Hur man anpassar bild till cellens bredd och höjd
type: docs
weight: 130
url: /sv/net/how-to-fit-image-to-cell-width-height/
description: Lär dig hur du anpassar bild till cellens bredd med Aspose.Cells.
keywords: Hur man anpassar bild till cellens bredd, anpassa bild till cellens bredd, hur man anpassar bild till cellens bredd och höjd, hur man anpassar bild till cellens höjd.
---


## ** Varför anpassa bild till cellens bredd och höjd**
Att anpassa en bild till ett specifikt cellens bredd och höjd handlar inte bara om estetik. Det handlar i grund och botten om precision, automation och datan organisation.

1. För professionell presentation och läsbarhet: När du bygger en instrumentbräda behöver du ofta ikoner, flaggor eller produktbilder som passar perfekt med datapunterna. En feljusterad bild ser slarvig och oprofessionell ut. Om du utformar en mall för andra att använda (t.ex. en produktkatalog, en personalregister), vill du att bilderna automatiskt ska passa in i de avsedda utrymmena, vilket säkerställer kontinuitet varje gång mallen används. Bilder som överskrider cellerna kan orsaka oväntade sidbrytningar och formateringsproblem vid utskrift. En passande bild beter sig förutsägbart på den utskrivna sidan.

2. För dataorganisation och struktur: Detta är den viktigaste funktionella anledningen. Excel är ett rutnät för data. När en bild "placerad" på rutnätet inte "passas" till en cell, orsakar det problem. Problem med flytande bilder: De flyttar inte med cellerna: Om du sorterar, filtrerar eller infogar/tar bort rader, förblir bilden i sin absoluta position på bladet, helt åtskild från data den ska representera. De ändrar inte storlek med cellerna: Om du ändrar radens höjd eller kolumnens bredd, förblir en flytande bild densamma i storlek, vilket bryter layouten. Fördel med att passa in i en cell: Cells blir "behållare" för bilden: När en bild passar in i en cell bestäms dess position och storlek av cellens rutnätskoordinater. Om du flyttar data (t.ex. sorterar en tabell), flyttar sig bilden med sin motsvarande rad. Det skapar ett sant bild-uppgiftspar: Detta gör att du kan behandla bilden som ett visuellt attribut för datan i den raden, vilket är viktigt för automation.

3. För automatisering och avancerad funktionalitet: Detta är där passning av bilder till celler blir en superkraft. Dittdera bilder dynamiskt: Du kan använda en formel för att hämta en bildväg från en cell och sedan använda ett makro (VBA) för att automatiskt storleksanpassa och infoga bilden i en intilliggande cell. Så skapar du en dynamisk produktkatalog där ändring av ett produkt-ID automatiskt uppdaterar namn, pris och bild. Databasintegration: När du exporterar data eller länkar Excel till en databas gör innehållande bilder i specifika celler hela datasetet, inklusive dess visuella element, mer strukturerat och portabelt.

## **Hur man passar in en bild till cellens bredd och höjd med Excel**
Du kan passa in en bild till cellens bredd och höjd i Excel på följande två sätt.

### **Passa in bild till cellens bredd och höjd med placering i cellen**
Om hur man infogar en bild i en cell i Excel, följ dessa steg:

1. Gå till fliken Infoga och klicka på alternativet Bilder.
2. Välj **Plats i cell**. Välj en av följande källor från rullgardinsmenyn Infoga bild från (**Den här enheten**, **Lagerbilder** och **Onlinebilder**). Den här enheten för att infoga bild från din enhet. Lagerbilder för att infoga bild från lagerbilder. Onlinebilder för att infoga bild från webben.
<br>
<img src="1.png" width=60% />
3. Välj bild och infoga bild i en cell.
<br>
<img src="8.png" width=60% />

### **Passa in bild till cellens bredd och höjd med placering över cellerna**
Om hur man infogar en bild över celler i Excel, följ dessa steg:

1. Gå till fliken Infoga och klicka på alternativet Bilder.
2. Välj **Plats över celler**. Välj en av följande källor från rullgardinsmenyn Infoga bild från (**Den här enheten**, **Lagerbilder** och **Onlinebilder**). Den här enheten för att infoga bild från din enhet. Lagerbilder för att infoga bild från lagerbilder. Onlinebilder för att infoga bild från webben.
<br>
<img src="2.png" width=60% />
3. Välj bild och infoga bild över celler.
<br>
<img src="3.png" width=60% />
4. Justera manuellt bildens bredd och höjd för att matcha cellernas bredd och höjd.
<br>
<img src="6.png" width=60% />

## **Hur man passar in en bild till cellens bredd och höjd med Aspose.Cells**
På grund av variationer i rad- och kolumnbredder beroende på språk och visningsförhållande, kan justering av bildens bredd och höjd leda till små skillnader och ibland inte vara helt konsekvent med cellernas bredd och höjd. Du kan passa in bilden till cellens bredd och höjd med Aspose.Cells på följande två sätt.

### **Hur man passar in en bild till cellens bredd och höjd med placering i cellen**
Infoga bild i cell med hjälp av Aspose.Cells. Se följande exempelkod. Efter att ha utfört exempelkoden infogas en bild i en cell.
1. Skapa en Workbook-objekt. 
2. Hämta cellen där du vill infoga bilden.
3. Ange Cell.EmbeddedImage-egenskapen. 
4. Slutligen sparas arbetsboken i [utdata XLSX](ut.xlsx)-format. 

### **Exempel på kod för placering i cellen**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-place-image-in-cell.cs" >}}
{{< app/cells/assistant language="csharp" >}}

### **Hur man passar in en bild till cellens bredd och höjd med placering över cellerna**
Att lägga till bilder i ett kalkylblad är mycket enkelt. Det tar bara några rader kod:
Anropa enkelt [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) metoden i [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) samling (Inkapslad i [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) -objektet). Justera sedan bildens bredd och höjd baserat på cellernas storlek. Spara slutligen filen i [output XLSX](out_net.xlsx)-format. [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)-metoden tar följande parametrar:

- **Övre vänstra radindex**, indexet för den övre vänstra raden.
- **Övre vänstra kolumnindex**, indexet för den övre vänstra kolumnen.
- **Bildfilnamn**, namnet på bildfilen, komplett med sökväg.


### **Exempel på kod för placering över celler**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-place-image-over-cells-fit-cell-width-height.cs" >}}
{{< app/cells/assistant language="csharp" >}}

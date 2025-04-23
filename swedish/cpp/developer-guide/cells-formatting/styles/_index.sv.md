---
title: Hämta och sätt stil för celler med C++
linktitle: Stilar
type: docs
weight: 50
url: /sv/cpp/styling-and-data-formatting/
description: Upptäck hur man utför datamärkning och styling i Aspose.Cells for C++, inklusive textformatering, nummerformatering, datummärkning och andra stilalternativ. Vår guide hjälper dig att skapa professionella kalkylblad med attraktiv formatering.
keywords: Aspose.Cells for C++, datamärkning, styling, textformatering, nummerformatering, datummärkning, stilalternativ, kalkylblad, attraktiv formatering, professionell.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ infördes två nya metoder för cellformatering: `Cell.GetStyle` och `Cell.SetStyle`. Denna artikel granskar `Cell.GetStyle`/`SetStyle`-metoden för att hjälpa dig att bedöma vilken teknik som passar dig bäst.

{{% /alert %}}

## **Formatering av celler**
Det finns två sätt att formatera en cell, som illustreras nedan.

### **Användning av GetStyle()**
Med följande kodstycke initieras ett `Style`-objekt för varje cell vid formatering. Om många celler formateras används mycket minne eftersom `Style`-objektet är stort. Dessa `Style`-objekt frigörs inte förrän `Workbook.Save`-metoden anropas.

**C++**

```cpp
cell.GetStyle()->GetFont()->SetIsBold(true);
```

### **Användning av SetStyle()**
Det första tillvägagångssättet är enkelt och tydligt, så varför lade vi till det andra?

Vi lade till det andra tillvägagångssättet för att optimera minnesanvändningen. Efter att ha hämtat ett `Style`-objekt med `Cell.GetStyle`, ändra det och använd `Cell.SetStyle` för att tilldela det tillbaka till denna cell. Detta `Style`-objekt kommer inte att bevaras, och C++-körningen kommer att samla in det när det inte längre refereras.

När du anropar `Cell.SetStyle`-metoden sparas inte `Style`-objektet för varje cell. Istället jämförs detta `Style`-objekt med en intern `Style`-pool för att se om det kan återanvändas. Endast `Style`-objekt som skiljer sig från de befintliga sparas för varje `Workbook`. Detta innebär att det endast finns några hundra `Style`-objekt per Excel-fil istället för tusentals. För varje cell sparas endast en index till `Style`-poolen.

**C++**

```cpp
auto style = cell.GetStyle();
style->GetFont()->SetIsBold(true);
cell.SetStyle(style);
```

## **Avancerade ämnen**
- [Skapa Style-objekt med hjälp av CellsFactory-klassen](/cells/sv/cpp/create-style-object-using-cellsfactory-class/)
- [Modifiera en befintlig stil](/cells/sv/cpp/modify-an-existing-style/)
- [Återanvändning av Stilobjekt](/cells/sv/cpp/reusing-style-objects/)
- [Användning av inbyggda stilar](/cells/sv/cpp/using-built-in-styles/)

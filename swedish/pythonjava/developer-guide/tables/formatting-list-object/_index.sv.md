---
title: Formatering av Listobjekt
type: docs
weight: 30
url: /sv/python-java/formatting-list-object/
---

## **Formatering av Listobjekt**
En tabell är en serie rader och kolumner som innehåller relaterade data som hanteras oberoende av data i andra rader och kolumner. Som standard har varje kolumn i tabellen filtrering aktiverat i huvudraden så att du snabbt kan filtrera eller sortera din listobjektsdata. Du kan lägga till en totalrad (en specialrad i en lista som ger ett urval av aggregeringsfunktioner som är användbara för att arbeta med numeriska data) till listobjektet som ger en nedrullningsbar lista med aggregeringsfunktioner för varje totalradscell.

Aspose.Cells stödjer formatering av Listobjekt. För detta tillhandahåller API:et klasserna [ListObject](https://reference.aspose.com/cells/python/asposecells.api/ListObject) och [TableStyleType](https://reference.aspose.com/cells/python/asposecells.api/TableStyleType). Klassen [TableStyleType](https://reference.aspose.com/cells/python/asposecells.api/TableStyleType) innehåller konstanter som representerar de inbyggda tabellstilarna. Följande kodsnutt skapar ett nytt Listobjekt och anger dess tabellstiltyp till [TABLE_STYLE_MEDIUM_10](https://reference.aspose.com/cells/python/asposecells.api/tablestyletype#TABLE_STYLE_MEDIUM_10).



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-FormatListObject.py" >}}

---
title: Hantera områden
linktitle: Områden
type: docs
weight: 105
url: /sv/python-net/managing-ranges/
description: Den här artikeln visar hur man hanterar intervall med Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Python hantera intervall, Skapa intervall i Python, Python Sätt värde i cellerna i intervallet, Python Sätt stil på cellerna i intervallet, Python Hämta Aktuellt område från intervallet.
---

## **Introduktion**

I Excel kan du markera flera celler med musen, det markerade celluppsättningen kallas "Område".

Till exempel kan du klicka med vänster musknapp i cellen "A1" i Excel och sedan dra till cellen "C4". Det rektangulära området du valt kan också enkelt skapas som en objekt genom att använda Aspose.Cells för Python via .NET.

Så här skapar du området, anger värde, ställer in stil och utför fler operationer på "Området" objektet.

## **Hantera områden med hjälp av Aspose.Cells för Python Excel-bibliotek**

Aspose.Cells for Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-samling.

## **Hur man skapar område**

När du vill skapa ett rektangulärt område som sträcker sig över A1:C4 kan du använda följande kod:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Create.py" >}}

## **Hur man lägger värde i cellerna i området**

Säg att du har en rad celler som sträcker sig över A1:C4. Matrisen skapar 4 * 3 = 12 celler. De enskilda områdscellerna är ordnade sekventiellt.

Följande exempel visar hur man anger värden i cellerna i området.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-PutValue.py" >}}

## **Hur man inställer stil för cellerna i området**

Följande exempel visar hur man ställer in stil på cellerna i området.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-SetStyle.py" >}}

## **Hur man får helaRaden av området**

CurrentRegion är en egenskap som returnerar ett områdesobjekt som representerar det aktuella området. 

Det aktuella området är ett område som begränsas av en kombination av tomma rader och tomma kolumner. Endast läsbar.

I Excel kan du få aktuellt område genom att:
1. Välj ett område (område1) med muslådan.
2. Klicka på "Hem - Redigering - Sök och markera - Gå till speciellt - Aktuellt område", eller använd "Ctrl+Skift+*", du kommer att se att Excel automatiskt hjälper dig att välja ett område (område2), nu har du gjort det, område2 är det aktuella området för område1.

Med Aspose.Cells för Python via .NET kan du använda "Range.current_region" egenskapen för att utföra samma funktion.

Ladda ner följande testfil, öppna den i Excel, använd muslådan för att välja ett område "A1:D7", klicka sedan på "Ctrl+Skift+*", du kommer att se att område "A1:C3" är valt.

[current_region.xlsx](current_region.xlsx)

Nu kör följande exempel, se hur det fungerar i Aspose.Cells för Python via .NET:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CurrentRegion.py" >}}

## **Fortsatta ämnen**
- [Autofyllt område i Excel-fil](/cells/sv/python-net/autofill-ranges/)
- [Kopiera områden i Excel](/cells/sv/python-net/copy-ranges-of-excel/)
- [Kopiera områdesdata endast](/cells/sv/python-net/copy-range-data-only/)
- [Kopiera områdesdata med stil](/cells/sv/python-net/copy-range-data-with-style/)
- [Kopiera områdesstil endast](/cells/sv/python-net/copy-range-style-only/)
- [Skapa unionsspann](/cells/sv/python-net/create-union-range/)
- [Klipp och klistra område](/cells/sv/python-net/cut-and-paste-cells/)
- [Radera områden](/cells/sv/python-net/delete-ranges-from-excel/)
- [Få adresscellsantal offset hela kolumnen och hela raden för området](/cells/sv/python-net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Infoga områden](/cells/sv/python-net/insert-ranges-to-excel/)
- [Sammanfoga eller dela upp cellområde](/cells/sv/python-net/merge-or-unmerge-range-of-cells/)
- [Flytta cellområde i ett kalkylblad](/cells/sv/python-net/move-range-of-cells-in-a-worksheet/)
- [Skapa arbetsbok och arbetsbladsspecifika namngivna områden](/cells/sv/python-net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Sök och ersätt data i ett område](/cells/sv/python-net/search-and-replace-data-in-a-range/)


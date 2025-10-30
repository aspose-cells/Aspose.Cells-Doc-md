---
title: Hur man ställer in utskriftsområde med Python.NET
linktitle: Hur man ställer in utskriftsområde
type: docs
weight: 200
url: /sv/python-net/how-to-set-print-area/
description: Lär dig hur du ställer in och rensar utskriftsområden i Excel filer med Aspose.Cells för Python via .NET.
keywords: python ställer in utskriftsområde, rensar utskriftsintervall, python excel utskriftsinställningar, aspose.cells python utskriftsområde, python begränsa utskriftsintervall
---

## **Möjliga användningsscenario**

Att ange ett utskriftsområde i en dokument hjälper till att kontrollera utskriven innehåll. Viktiga skäl inkluderar:

1. Fokusera på specifika data: Skriva endast relevanta avsnitt
1. Förbättrad layout: Organisera innehåll snyggt över sidor
1. Spara resurser: Minska papper/bläckförbrukning
1. Professionell presentation: Säkerställ ett polerat utgångsresultat
1. Konsekvens: Bibehåll enhetliga utskrifter

## **Hur man sätter in utskriftsområde i Excel**

För att ställa in ett utskriftsområde programmatiskt:

1. Åtkomst till arbetsbladets sidinställningsegenskaper
1. Definiera utskriftsområde med cellintervallnotation
1. Spara den modifierade arbetsboken

```python
# Sample image reference remains unchanged
<img src="3.png" width=60% />
```

## **Hur man rensar utskriftsområde i Excel**

För att ta bort utskriftsområdesbegränsningar:

1. Åtkomst till sidinställningsegenskaper
1. Återställ utskriftsområde till tom sträng
1. Spara ändringar

```python
# Sample image reference remains unchanged
<img src="4.png" width=60% />
```

## **Vad händer efter att ha rensat utskriftsområdet**

Att rensa utskriftsområdet resulterar i:

1. Standardutskrift av hela bladet
1. Borttagning av tidigare begränsningar för området
1. Inkludering av alla formaterade celler

## **Så ställer du in utskriftsområdet med Aspose.Cells**

Ställ in utskriftsområdet via bladets sidkonfiguration:

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set print area to A1:D10
worksheet.page_setup.print_area = "A1:D10"

# Save modified workbook
workbook.save("output_set_print_area.xlsx")
```

```python
# Output image reference
<img src="1.png" width=60% />
```

## **Så rensar du utskriftsområdet med Aspose.Cells**

Ta bort befintlig definition av utskriftsområde:

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Clear print area
worksheet.page_setup.print_area = ""

# Save modified workbook
workbook.save("output_clear_print_area.xlsx")
```

```python
# Output image reference
<img src="2.png" width=60% />
```

```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Set the print area - specify the range you want to print
worksheet.page_setup.print_area = "A1:D10"

# Save the workbook
workbook.save("set_print_area.pdf")
```
```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Clear the print area
worksheet.page_setup.print_area = ""

# Save the workbook
workbook.save("clear_print_area.pdf")
```
{{< app/cells/assistant language="python-net" >}}

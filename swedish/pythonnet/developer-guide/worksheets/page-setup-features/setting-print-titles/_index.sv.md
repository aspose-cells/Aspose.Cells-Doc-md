---
title: Ställ in utskriftstitlar med Python.NET
linktitle: Ange utskriftstitlar
type: docs
weight: 200
url: /sv/python-net/how-to-set-print-titles/
description: Lär dig hur du konfigurerar upprepade rad /kolumnrubriker på utskrivna sidor med Aspose.Cells för Python via .NET.
keywords: Python upprepningsutskriftshrubbrik, Python ställ in utskriftstitlar, Python rensa utskriftstitlar, Excel sida inställning Python, Python.NET kalkylbladsutskrift
---

## **Möjliga användningsscenario**

Att ställa in utskriftstitlar i Excel säkerställer att specifika rader eller kolumner upprepas på varje utskriven sida, vilket är särskilt användbart för stora kalkylblad som sträcker sig över flera sidor. Här är några anledningar till varför du kan ställa in utskriftstitlar:

1. Förbättrad läsbarhet: Utskriftstitlar hjälper läsarna att förstå data genom att hålla rubriker synliga på alla sidor, vilket gör det lättare att tolka informationen på varje sida utan att behöva hänvisa tillbaka till första sidan.

1. Professionell presentation: Att konsekvent visa rubriker eller etiketter på varje sida skapar ett mer polerat och professionellt utseende på utskrivna dokument.

1. Förbättrad navigering: För dokument med omfattande data gör upprepning av rubriker på varje sida snabbare navigering och referens, vilket minskar behovet av att vända fram och tillbaka mellan sidor.

1. Minskade fel: När rubriker är närvarande på varje sida minimeras missförstånd eller datainmatningsfel, eftersom användare lätt kan se sammanhanget för data.

1. Konsekvens: Att säkerställa att viktig information, som kolumnrubriker eller radetiketter, alltid är synlig upprätthåller konsekvens och tydlighet genom hela dokumentet.

## **Hur man ställer in utskriftstitlar i Excel**

Följ dessa steg för att ställa in utskriftstitlar i Excel:

1. Öppna fliken "Sidlayout": Klicka på "Sidlayout"-fliken i menyfliksområdet högst upp i Excel-fönstret.
1. Få tillgång till Utskriftstitlar: I gruppen "Siduppställning" klickar du på "Utskriftstitlar".
1. Ställ in rader att upprepa: I dialogrutan "Siduppställning" går du till fliken "Blad". I avsnittet "Utskriftstitlar" anger du de rader som ska upprepas överst genom att klicka på rutan bredvid "Rader att upprepa längst upp" och välja rad(er) du vill upprepa.
1. Ställ in kolumner att upprepa (om behövs): På liknande sätt kan du ange de kolumner som ska upprepas längst till vänster genom att klicka på rutan bredvid "Kolumner att upprepa till vänster" och välja den eller de kolumner du vill upprepa.
<br>
<img src="3.png" width=60% />

1. Bekräfta och skriv ut: Klicka på "OK" för att tillämpa inställningarna. När du skriver ut kalkylbladet kommer de angivna raderna eller kolumnerna att visas på varje utskriven sida.

## **Hur man rensar utskriftstitlar i Excel**

För att rensa utskriftstitlar i Excel måste du ta bort de rader eller kolumner som är inställda att upprepas på varje utskriven sida. Så här gör du:

1. Öppna fliken "Sidlayout": Klicka på "Sidlayout"-fliken i menyfliksområdet högst upp i Excel-fönstret.
1. Få tillgång till Utskriftstitlar: I gruppen "Siduppställning" klickar du på "Utskriftstitlar".
1. Rensa utskriftstitlar: I dialogrutan "Siduppställning" går du till fliken "Blad". Radera texten i rutorna för "Rader att upprepa längst upp" och "Kolumner att upprepa till vänster" genom att ta bort innehållet i dem.
<br>
<img src="4.png" width=60% />

1. Bekräfta och stäng: Klicka på "OK" för att tillämpa ändringarna.

## **Hur man ställer in utskriftstitlar med Aspose.Cells**

För att ställa in utskriftstitlar i ett specificerat kalkylblad: Ladda först [filen exempel](input.xlsx), och redigera sedan egenskapen [**Worksheet.page_setup.print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows/) och [**Worksheet.page_setup.print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) för objektet [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/). Att sätta dessa egenskaper till ett intervallsträng kommer att konfigurera utskriftstitlar.

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set row 1 as repeating header
worksheet.page_setup.print_title_rows = "$1:$1"

# Save modified workbook
workbook.save("output.xlsx")
```

Utmatningsresultat:
<br>
<img src="1.png" width=60% />

## **Hur man rensar utskriftstitlar med Aspose.Cells**

För att rensa utskriftstitlar, anges utskriftstitlar till tomma strängar:

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Clear existing print titles
worksheet.page_setup.print_title_rows = ""
worksheet.page_setup.print_title_columns = ""

# Save modified workbook
workbook.save("output.xlsx")
```

Utmatningsresultat:
<br>
<img src="2.png" width=60% />

```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Set rows to repeat at the top (e.g., rows 1 and 2)
worksheet.page_setup.print_title_rows = "$1:$2"

# Set columns to repeat at the left (e.g., columns A and B)
worksheet.page_setup.print_title_columns = "$A:$B"

# Save the workbook
workbook.save("set_print_titles.pdf")
```
```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Clear the rows and columns set to repeat
worksheet.page_setup.print_title_rows = ""
worksheet.page_setup.print_title_columns = ""

# Save the workbook
workbook.save("clear_print_titles.pdf")
```
{{< app/cells/assistant language="python-net" >}}

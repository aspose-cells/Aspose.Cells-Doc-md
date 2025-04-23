---
title: Lås celler för att skydda dem med Python.NET
linktitle: Lås celler för att skydda dem
type: docs
weight: 130
url: /sv/python-net/how-to-lock-cells-to-protect-them/
description: Lär dig hur man låser specifika celler och skyddar arbetsblad i Excel filer med Aspose.Cells för Python via .NET.
keywords: Python låser celler, skyddar arbetsblad, cellskydd i Excel med Python, Aspose.Cells Python tutorial
---

## **Möjliga användningsscenario**
Att låsa celler för att skydda dem är en vanlig praxis i kalkylbladsapplikationer, som Microsoft Excel eller Google Sheets, av flera viktiga skäl:

1. Förhindra oavsiktliga ändringar: Låsning av celler kan förhindra att användare oavsiktligt ändrar viktig data eller formler.
2. Upprätthålla dataintegritet: Säkerställ att kritiska data förblir konsekventa och korrekta.
3. Kontrollerad tillgång: Hantera behörigheter för redigering i samarbetsmiljöer.
4. Skydda formler: Skydda viktiga beräkningar från ändringar.
5. Tillämpa affärsregler: Följa dataskyddskrav.
6. Vägleda användare: Ge tydliga redigeringsområden i komplexa kalkylblad.

## **Hur låser du celler för att skydda dem i Excel**
Så här låser du celler i Microsoft Excel:

1. Välj cellerna som ska låsas: Välj celler eller hoppa över för att låsa hela arket.
1. Öppna Format Cells-dialekten: Högerklicka > "Formatera celler" eller Ctrl+1.
<br>
<img src="1.png" width=60% />
1. Lås cellerna: Gå till "Skydd"-fliken > Markera "Låst" > Klicka på "OK."
1. Skydda arket: "Granska"-fliken > "Skydda blad" > Ange lösenord/tillstånd > Klicka på "OK."
<br>
<img src="2.png" width=60% />

## **Hur man låser celler för att skydda dem med Python**

Aspose.Cells för Python via .NET möjliggör programmatiskt cellskydd. Följ dessa steg:
1. Ladda [exempelfilen](sample.xlsx)
2. Lås upp alla celler (standardlåst tillstånd tillämpas inte förrän skyddet är aktiverat)
3. Lås specifika celler
4. Skydda arket för att tillämpa låsning

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]

# Unlock all cells first
style = ac.Style()
style.is_locked = False
style_flag = ac.StyleFlag()
style_flag.locked = True
worksheet.cells.apply_style(style, style_flag)

# Lock specific cells
worksheet.cells["A1"].get_style().is_locked = True
worksheet.cells["B2"].get_style().is_locked = True

# Enable worksheet protection
worksheet.protect(ac.ProtectionType.ALL)

# Save protected workbook
workbook.save("output.xlsx")
```

## **Utdataresultat**
Denna implementation låser angivna celler (A1 och B2) medan andra är redigerbara. Skydd av arbetsblad tillämpar dessa inställningar.

<br>
<img src="3.png" width=60% />

```python
from aspose.cells import Workbook, ProtectionType, StyleFlag

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Unlock all cells first
unlock_style = workbook.create_style()
unlock_style.is_locked = False

style_flag = StyleFlag()
style_flag.locked = True
sheet.cells.apply_style(unlock_style, style_flag)

# Lock specific cells (A1 and B2)
lock_style = workbook.create_style()
lock_style.is_locked = True

sheet.cells.get("A1").set_style(lock_style)
sheet.cells.get("B2").set_style(lock_style)

# Protect the worksheet to enforce locking
sheet.protect(ProtectionType.ALL)

# Save the modified workbook
workbook.save("output_locked.xlsx")
```

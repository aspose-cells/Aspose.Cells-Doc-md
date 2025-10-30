---
title: Tillämpa avancerad villkorlig formatering med Python.NET
linktitle: Tillämpa avancerad villkorlig formatering
type: docs
weight: 70
url: /sv/python-net/apply-advanced-conditional-formatting/
description: Lär dig hur du implementerar Excellens avancerade villkorliga formateringsfunktioner som datastaplar, färgskalor och ikonsatser med Aspose.Cells för Python via .NET.
keywords: Python Excel formatering, Villkorlig formatering Python, Datastaplar Python, Färgskalor Python, Ikonsatser Python, Aspose.Cells Python
---

{{% alert color="primary" %}} 

Microsoft Excel 2007 och senare versioner (2010/2013/2016) erbjuder avancerade funktioner för villkorsformatering inklusive cellskuggning, kantlinjer, färgade ikoner, pilar, flaggor och teckensnittformattering.

{{% /alert %}} 

## **Implementera avancerad villkorsformatering i Excelfiler**
Aspose.Cells för Python via .NET stöder alla avancerade funktioner för villkorsformatering inklusive:

- Lägg till skuggade datapålar för att grafiskt förbättra de underliggande siffrorna genom att infoga en enkel stapeldiagram i cellerna.
- Skugga automatiskt celler med färgskalor baserat på deras relation till värden i andra celler i området. Standardinställningarna skuggar det lägsta värdet i rött och går upp till det högsta värdet i grönt.
- Använd ikonsatser på ett liknande sätt som färgskalor, men istället för att skugga cellerna lägger den till små ikoner, såsom pilar och trafikljus i cellerna.

Aspose.Cells stöder fullt ut den villkorliga formateringen som tillhandahålls av Microsoft Excel 2007 och senare versioner i XLSX-format på celler vid körning. Detta exempel visar en övning för avancerade typer av villkorlig formatering inklusive Ikonsatser, Databar, Färgskalor, Tidsperioder, Topp/Botten och andra regler med olika uppsättningar attribut.

- [**Adding Color Scale Conditional Formattings**](/cells/sv/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/sv/python-net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/sv/python-net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/sv/python-net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/sv/python-net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/sv/python-net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/sv/python-net/how-to-add-top10-conditional-formatting/)



### **Beräkna Excels färgval för färgskaleformatering**
Denna kod visar hur man bestämmer vilken färg Excel väljer för villkorsformatering med färgskala:

```python
import os
from aspose.cells import Workbook
from aspose.pydrawing import Color

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-Python
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a workbook object and open the template file
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))
# Get the first worksheet
worksheet = workbook.worksheets[0]
# Get the A1 cell
a1 = worksheet.cells.get("A1")

# Get the conditional formatting resultant object
cfr1 = a1.get_conditional_formatting_result()
# Get the ColorScale resultant color object
c = cfr1.color_scale_result

# Read and print the color values
print(c.to_argb())
print(c.name)
```
{{< app/cells/assistant language="python-net" >}}

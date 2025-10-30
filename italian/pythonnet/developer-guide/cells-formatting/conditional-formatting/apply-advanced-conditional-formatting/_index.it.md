---
title: Applica la formattazione condizionale avanzata con Python.NET
linktitle: Applicare la formattazione condizionale avanzata
type: docs
weight: 70
url: /it/python-net/apply-advanced-conditional-formatting/
description: Impara come implementare le funzionalità avanzate di formattazione condizionale di Excel come barre dei dati, scale di colore e set di icone usando Aspose.Cells per Python via .NET.
keywords: Formattazione Excel in Python, Formattazione condizionale Python, Barre dei dati Python, Scale di colore Python, Set di icone Python, Aspose.Cells Python
---

{{% alert color="primary" %}} 

Microsoft Excel 2007 e versioni successive (2010/2013/2016) offrono funzionalità avanzate di formattazione condizionale, tra cui ombreggiatura delle celle, bordi, icone colorate, frecce, bandiere e formattazione dei caratteri.

{{% /alert %}} 

## **Implementare la formattazione condizionale avanzata nei file Excel**
Aspose.Cells per Python via .NET supporta tutte le funzionalità avanzate di formattazione condizionale inclusi:

- Aggiungere barre di dati sfumate per migliorare graficamente i numeri sottostanti incorporando un semplice grafico a barre nelle celle.
- Sfumare automaticamente le celle con scale di colori in base alla loro relazione con i valori in altre celle nel range. Le impostazioni predefinite sfumano il valore più basso in rosso fino al valore più alto in verde.
- Usare set di icone in modo simile alle scale di colori, ma anziché sfumare le celle aggiunge piccole icone, come frecce e semafori, alle celle.

Aspose.Cells supporta pienamente la formattazione condizionale fornita da Microsoft Excel 2007 e versioni successive in formato XLSX sulle celle in fase di esecuzione. Questo esempio dimostra un esercizio per tipi avanzati di formattazione condizionale, tra cui IconSets, DataBars, Color Scales, TimePeriods, Top/Bottom e altre regole con diversi insiemi di attributi.

- [**Adding Color Scale Conditional Formattings**](/cells/it/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/it/python-net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/it/python-net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/it/python-net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/it/python-net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/it/python-net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/it/python-net/how-to-add-top10-conditional-formatting/)



### **Calcola la selezione del colore di Excel per la formattazione con scala di colori**
Questo codice mostra come determinare il colore scelto da Excel per le regole di formattazione condizionale con scala di colori:

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

---
title: Come scalare un foglio di lavoro con Python.NET
linktitle: Come ridimensionare un foglio di lavoro
type: docs
weight: 130
url: /it/python-net/how-to-scale-a-worksheet/
description: Questo articolo spiega come scalare un foglio di lavoro usando Aspose.Cells for Python.NET.
keywords: Scala un foglio di lavoro con Python, Scala il foglio di lavoro con Python.NET, Adatta a pagina intera in Python, Percentuale di scalatura del foglio di lavoro in Python, Scalatura del foglio di lavoro Aspose.Cells Python.
---

## **Possibili Scenari di Utilizzo**
Ridimensionare un foglio di lavoro può essere utile per vari motivi, a seconda del contesto in cui si lavora. Ecco alcuni motivi comuni per ridimensionare un foglio di lavoro:
1. **Adatta a pagina**: Per assicurarsi che tutto il contenuto si adatti su una singola pagina o un numero specifico di pagine durante la stampa.
1. **Presentazione**: Per creare fogli di lavoro organizzati e dall'aspetto professionale da condividere.
1. **Leggibilità**: Per regolare le dimensioni del testo e degli elementi per una migliore accessibilità visiva.
1. **Gestione dello spazio**: Per ottimizzare il layout del foglio di lavoro e ridurre al minimo gli spazi bianchi non necessari.
1. **Visualizzazione dei dati**: Per dimensionare correttamente grafici e diagrammi all'interno dello spazio disponibile.
1. **Coerenza**: Per mantenere un aspetto uniforme tra più fogli di lavoro o documenti.

## **Come scalare un foglio di lavoro in Excel**
Scalare un foglio di lavoro in Excel aiuta ad adattare il contenuto alle pagine specificate durante la stampa. Segui questi passaggi:

1. Apri il tuo foglio di lavoro in Excel
1. Navigare su **Layout di pagina** > **Scala per adattarsi**
1. Regolare **Larghezza** e **Altezza** in base ai requisiti del numero di pagine
1. Impostare una percentuale di scalatura personalizzata se necessario
<br>
<img src="1.png" width=60% />

## **Come scalare un foglio di lavoro usando Python.NET**
Aspose.Cells per Python.NET offre capacità complete di scalatura dei fogli di lavoro. Usa questi metodi per scalare i fogli di lavoro programmaticamente:

### **Esempio di adattamento a pagina**
Regolare le impostazioni di stampa per adattare il contenuto alle pagine specificate:
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the worksheet to fit to 1 page wide and 1 page tall
page_setup.fit_to_pages_wide = 1
page_setup.fit_to_pages_tall = 1

# Save the modified workbook
workbook.save("output_fit_to_page.xlsx")
```
<br>
<img src="3.png" width=60% />

### **Esempio di scalatura in percentuale**
Applicare la percentuale di scalatura personalizzata ai contenuti del foglio di lavoro:
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the scaling to a specific percentage (e.g., 75%)
page_setup.zoom = 75

# Save the modified workbook
workbook.save("output_scaled_percentage.xlsx")
```
<br>
<img src="2.png" width=60% />

**Riferimenti principali API:**
- [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) classe
- [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) classe
- configurazione [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/)
{{< app/cells/assistant language="python-net" >}}

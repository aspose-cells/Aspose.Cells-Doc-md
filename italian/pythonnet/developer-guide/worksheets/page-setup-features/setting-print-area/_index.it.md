---
title: Come impostare l area di stampa con Python.NET
linktitle: Come impostare l area di stampa
type: docs
weight: 200
url: /it/python-net/how-to-set-print-area/
description: Impara come impostare e cancellare le aree di stampa nei file Excel usando Aspose.Cells per Python via .NET.
keywords: python imposta area di stampa, cancella intervallo di stampa, impostazioni di stampa Excel in Python, aspose.cells Python area di stampa, limita intervallo di stampa in Python
---

## **Possibili Scenari di Utilizzo**

Impostare un'area di stampa in un documento aiuta a controllare i contenuti stampati. Le ragioni principali includono:

1. Focalizzazione su dati specifici: stampa solo sezioni rilevanti
1. Layout migliorato: organizzare i contenuti in modo ordinato tra le pagine
1. Risparmio di risorse: ridurre consumo di carta/inchiostro
1. Presentazione professionale: garantire un risultato rifinito
1. Coerenza: mantenere output di stampa uniformi

## **Come impostare l'area di stampa in Excel**

Per impostare un'area di stampa programmaticamente:

1. Accedere alle proprietà di impostazione pagina del foglio di lavoro
1. Definire l'area di stampa usando la notazione dell'intervallo di celle
1. Salvare il workbook modificato

```python
# Sample image reference remains unchanged
<img src="3.png" width=60% />
```

## **Come eliminare l'area di stampa in Excel**

Per rimuovere i vincoli dell'area di stampa:

1. Accedere alle proprietà di impostazione pagina
1. Reimpostare l'area di stampa a stringa vuota
1. Salva le modifiche

```python
# Sample image reference remains unchanged
<img src="4.png" width=60% />
```

## **Cosa succede dopo aver eliminato l'area di stampa**

Risultato della cancellazione dell'area di stampa:

1. Stampa predefinita di tutto il foglio di lavoro
1. Rimozione dei vincoli di intervallo precedenti
1. Inclusione di tutte le celle formattate

## **Come impostare l'area di stampa utilizzando Aspose.Cells**

Imposta l'area di stampa tramite la configurazione della pagina del foglio di lavoro:

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

## **Come eliminare l'area di stampa usando Aspose.Cells**

Rimuovi la definizione dell'area di stampa esistente:

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

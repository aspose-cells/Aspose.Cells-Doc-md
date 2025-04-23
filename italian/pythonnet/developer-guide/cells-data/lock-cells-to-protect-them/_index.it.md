---
title: Bloccare le celle per proteggerle con Python.NET
linktitle: Bloccare le celle per proteggerle
type: docs
weight: 130
url: /it/python-net/how-to-lock-cells-to-protect-them/
description: Impara come bloccare celle specifiche e proteggere fogli di lavoro nei file Excel usando Aspose.Cells per Python via .NET.
keywords: Blocco delle celle con Python, proteggere i fogli di lavoro, protezione delle celle in Excel con Python, tutorial Aspose.Cells Python
---

## **Possibili Scenari di Utilizzo**
Bloccare le celle per proteggerle è una pratica comune nelle applicazioni di fogli di calcolo, come Microsoft Excel o Google Sheets, per diverse ragioni importanti:

1. Prevenire modifiche accidentali: bloccare le celle può impedire agli utenti di modificare accidentalmente dati o formule importanti.
2. Mantenere l'integrità dei dati: garantire che dati critici rimangano coerenti e accurati.
3. Accesso controllato: gestire i permessi di modifica in ambienti collaborativi.
4. Proteggere le formule: salvaguardare calcoli cruciali da modifiche.
5. Applicare regole aziendali: conformarsi ai requisiti di protezione dei dati.
6. Guidare gli utenti: fornire aree editabili chiare in fogli di calcolo complessi.

## **Come Bloccare le Celle per Proteggerle in Excel**
Ecco come puoi bloccare le celle in Microsoft Excel:

1. Seleziona le celle da bloccare: scegli le celle o salta per bloccare l'intero foglio.
1. Apri la finestra di dialogo Formato celle: clic destro > "Formato celle" o Ctrl+1.
<br>
<img src="1.png" width=60% />
1. Blocca le celle: vai alla scheda "Protezione" > Spunta "Bloccato" > Clicca su "OK."
1. Proteggi il foglio di lavoro: scheda "Revisione" > "Proteggi foglio" > Imposta password/permsessioni > Clicca su "OK."
<br>
<img src="2.png" width=60% />

## **Come bloccare le celle per proteggerle usando Python**

Aspose.Cells per Python via .NET consente la protezione delle celle tramite programmazione. Seguire questi passi:
1. Carica il [file di esempio](sample.xlsx)
2. Sblocca tutte le celle (lo stato di blocco predefinito non è applicato fino alla protezione)
3. Blocca le celle specifiche
4. Proteggi il foglio di lavoro per applicare il blocco

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

## **Risultato dell'Output**
Questa implementazione blocca le celle specificate (A1 e B2) mantenendo modificabili le altre. La protezione del foglio di lavoro applica queste impostazioni.

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

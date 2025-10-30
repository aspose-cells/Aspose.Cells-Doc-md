---
title: Modifica il Font su Caratteri Unicode Specifici durante il Salvataggio in PDF con Python.NET
linktitle: Modifica il Font su Caratteri Unicode Specifici
type: docs
weight: 260
url: /it/python-net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Scopri come modificare i font per caratteri Unicode specifici durante la conversione in PDF utilizzando Aspose.Cells per Python via .NET. Assicurati di una resa del testo precisa con sostituzione dei font a livello di carattere.
---

{{% alert color="primary" %}}

Alcuni caratteri Unicode non sono visualizzabili con i font specificati dall’utente. Uno di questi caratteri Unicode è **Sintagma Non-Lineare** (U+2011) con numero Unicode 8209. Questo carattere non può essere visualizzato con **Times New Roman** ma può essere mostrato con font come **Arial Unicode MS**.

Quando tali caratteri appaiono in testi formattati con un font specifico (ad esempio, Times New Roman), Aspose.Cells cambia automaticamente il font dell'intera parola/frase a uno compatibile (ad esempio, Arial Unicode MS). Per gli utenti che vogliono cambiare solo il font del carattere non visualizzabile, offriamo un controllo granulare tramite la proprietà **PdfSaveOptions.is_font_substitution_char_granularity**.

{{% /alert %}}

## **Esempio di Confronto**

Gli screenshot di seguito mostrano output con impostazioni differenti. Il primo PDF mostra la sostituzione del font completo del testo, mentre il secondo PDF modifica solo il font del carattere specifico.

|**Sostituzione Completa del Testo**|**Sostituzione a Livello di Carattere**|
| :- | :- |
|![Cambio Font Completo](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|![Cambio Font Selettivo](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

## **Passaggi di Implementazione**

Per abilitare la sostituzione del font a livello di carattere:

1. Crea un oggetto [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)
2. Accedi alle celle del foglio di lavoro usando la proprietà [**Worksheet.cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)
3. Imposta i valori delle celle contenenti caratteri Unicode speciali
4. Configura [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) con:
   - `is_font_substitution_char_granularity = True`
5. Salva il workbook in formato PDF

```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Create workbook object
workbook = Workbook()

# Access the first worksheet
worksheet = workbook.worksheets[0]

# Access cells
cell1 = worksheet.cells.get("A1")
cell2 = worksheet.cells.get("B1")

# Set the styles of both cells to Times New Roman
style = cell1.get_style()
style.font.name = "Times New Roman"
cell1.set_style(style)
cell2.set_style(style)

# Put the values inside the cell
cell1.put_value("Hello without Non-Breaking Hyphen")
cell2.put_value("Hello" + chr(8209) + " with Non-Breaking Hyphen")

# Autofit the columns
worksheet.auto_fit_columns()

# Save to Pdf without setting PdfSaveOptions.is_font_substitution_char_granularity
workbook.save(os.path.join(data_dir, "SampleOutput_out.pdf"))

# Save to Pdf after setting PdfSaveOptions.is_font_substitution_char_granularity to true
opts = PdfSaveOptions()
opts.is_font_substitution_char_granularity = True
workbook.save(os.path.join(data_dir, "SampleOutput2_out.pdf"), opts)
```

## **Configurazione Chiave**

Utilizza questi componenti API essenziali:

- Classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) per impostazioni di rendering PDF
- Proprietà **is_font_substitution_char_granularity** per sostituzione del font a livello di carattere
- Metodo [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/) per generazione output

{{% alert color="note" %}} 
**Nota differenza API**: In Python.NET, le proprietà boolean usano la nomenclatura snake_case (`is_font_substitution_char_granularity`) invece del PascalCase utilizzato in .NET.
{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}

---
title: Modifica il font sui caratteri Unicode specifici durante il salvataggio in PDF con Golang tramite C++
linktitle: Cambia il font sui caratteri Unicode
type: docs
weight: 260
url: /it/go-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Impara come cambiare il font di caratteri Unicode specifici durante il salvataggio in PDF usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

Alcuni caratteri Unicode non possono essere visualizzati dal font specificato dall'utente. Uno di questi caratteri Unicode è **Trattino Non-Rotoso** (U+2011) e il suo numero Unicode è 8209. Questo carattere non può essere visualizzato con **Times New Roman**, ma può essere visualizzato con altri font come **Arial Unicode MS**.

Quando un carattere di questo tipo compare all'interno di una parola o frase in un font specifico come Times New Roman, Aspose.Cells cambia il font dell'intera parola o frase in un font che può visualizzare questo carattere come Arial Unicode MS.

Tuttavia, questo comportamento è indesiderato per alcuni utenti, e desiderano che venga cambiato solo il font di quel carattere specifico invece di cambiare il font di tutta la parola o frase.

Per affrontare questo problema, Aspose.Cells fornisce la proprietà `PdfSaveOptions.IsFontSubstitutionCharGranularity`, che dovrebbe essere impostata su `true` per cambiare il font solo del carattere specifico che non può essere visualizzato, mantenendo invariato il font del resto della parola o frase.

{{% /alert %}}

## **Esempio**

Lo screenshot seguente confronta i due file PDF generati dal codice di esempio qui sotto.

Uno viene generato senza impostare la proprietà `PdfSaveOptions.IsFontSubstitutionCharGranularity`, e l'altro è stato generato dopo aver impostato la proprietà `PdfSaveOptions.IsFontSubstitutionCharGranularity` su `true`.

Come puoi vedere nel primo PDF, il carattere di tutta la frase è cambiato da Times New Roman a Arial Unicode MS a causa dell'Hypen Non Interrotto. Mentre nel secondo PDF, solo il font dell'Hypen Non Interrotto è cambiato.

|**Primo file PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**Secondo file PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheFontOnJustTheSpecificUnicodeCharactersWhileSavingToPdf.go" >}}

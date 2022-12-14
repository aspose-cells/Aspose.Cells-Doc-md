---
title: Cambia il carattere solo sui caratteri Unicode specifici durante il salvataggio in PDF
type: docs
weight: 260
url: /it/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}} 

 Alcuni caratteri Unicode non sono visualizzabili dal carattere specificato dall'utente. Uno di questi caratteri Unicode è**Trattino indivisibile** (U+2011) e il suo numero Unicode è 8209. Questo carattere non può essere visualizzato con**Times New Roman** , ma può essere visualizzato con altri tipi di carattere come**MS Arial Unicode**.

Quando un tale carattere si trova all'interno di una parola o frase che si trova in un carattere specifico come Times New Roman, allora Aspose.Cells cambia il carattere dell'intera parola o frase in un carattere che potrebbe visualizzare questo carattere come Arial Unicode in MS.

Tuttavia, questo è un comportamento indesiderato per alcuni utenti e desiderano che venga modificato solo il carattere di quel carattere specifico invece di modificare il carattere dell'intera parola o frase.

Per risolvere questo problema, Aspose.Cells fornisce la proprietà PdfSaveOptions.IsFontSubstitutionCharGranularity che dovrebbe essere impostata su true in modo che solo il carattere di un carattere specifico che non è visualizzabile venga modificato in carattere visualizzabile e il resto della parola o della frase rimanga nel carattere originale.

{{% /alert %}} 
## **Esempio**
Lo screenshot seguente confronta i due PDF di output generati dal codice di esempio riportato di seguito.

Uno viene generato senza impostare la proprietà PdfSaveOptions.IsFontSubstitutionCharGranularity e l'altro è stato generato dopo aver impostato la proprietà PdfSaveOptions.IsFontSubstitutionCharGranularity su true.

Come puoi vedere nel primo Pdf, il carattere dell'intera frase è cambiato da Times New Roman ad Arial Unicode MS a causa di Non-Breaking Hyphen. Mentre nel secondo Pdf è cambiato solo il font di Un-Breaking Hyphen.

|**Primo File Pdf**|
|:- |
|![cose da fare:immagine_alt_testo](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Secondo file Pdf**|
|:- |
|![cose da fare:immagine_alt_testo](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Codice di esempio**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}




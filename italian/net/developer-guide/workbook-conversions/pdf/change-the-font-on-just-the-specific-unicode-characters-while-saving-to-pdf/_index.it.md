---
title: Cambia il Font solo per i caratteri Unicode specifici durante il salvataggio in PDF
type: docs
weight: 260
url: /it/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}} 

Alcuni caratteri Unicode non sono visualizzabili con il font specificato dall'utente. Un tale carattere Unicode è il **Trattino Non Separabile** (U+2011) e il suo numero Unicode è 8209. Questo carattere non può essere visualizzato con **Times New Roman**, ma può essere visualizzato con altri font come **Arial Unicode MS**.

Quando un tale carattere compare all'interno di una parola o frase che si trova in un determinato font come Times New Roman, allora Aspose.Cells cambia il font di tutta la parola o frase al font che può visualizzare questo carattere come Arial Unicode MS.

Tuttavia, questo è un comportamento indesiderabile per alcuni utenti e vogliono solo che il font di quel personaggio specifico venga cambiato invece di cambiare il font dell'intera parola o frase.

Per risolvere questo problema, Aspose.Cells fornisce la proprietà PdfSaveOptions.IsFontSubstitutionCharGranularity che dovrebbe essere impostata su true in modo che venga cambiato solo il font di un carattere specifico che non è visualizzabile con un font visualizzabile e il resto della parola o frase dovrebbe rimanere nel font originale.

{{% /alert %}} 
## **Esempio**
Lo screenshot seguente confronta i due file PDF generati dal codice di esempio qui sotto.

Uno è generato senza impostare la proprietà PdfSaveOptions.IsFontSubstitutionCharGranularity e l'altro è generato dopo aver impostato la proprietà PdfSaveOptions.IsFontSubstitutionCharGranularity su true.

Come puoi vedere nel primo Pdf, il font dell'intera frase è cambiato da Times New Roman a Arial Unicode MS a causa del trattino non interrompibile. Mentre nel secondo Pdf, è cambiato solo il font del trattino non interrompibile.

|**Primo file Pdf**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Secondo file Pdf**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Codice di Esempio**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



{{< app/cells/assistant language="csharp" >}}

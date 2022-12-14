---
title: Cambia il carattere solo sui caratteri Unicode specifici durante il salvataggio in PDF
type: docs
weight: 150
url: /it/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}}

 Alcuni caratteri Unicode non sono visualizzabili dal carattere specificato dall'utente. Uno di questi caratteri Unicode è**Trattino indivisibile** (U+2011) e il suo numero Unicode è 8209. Questo carattere non può essere visualizzato con**Times New Roman** , ma può essere visualizzato con altri tipi di carattere come**MS Arial Unicode**.

Quando un tale carattere si trova all'interno di una parola o frase che si trova in un carattere specifico come Times New Roman, allora Aspose.Cells cambia il carattere dell'intera parola o frase in un carattere che potrebbe visualizzare questo carattere come Arial Unicode in MS.

Tuttavia, questo è un comportamento indesiderabile per alcuni utenti e desiderano solo che il carattere del carattere specifico debba essere cambiato invece di cambiare il carattere dell'intera parola o frase.

 Per far fronte a questo problema, Aspose.Cells fornisce[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) proprietà che deve essere impostata**VERO**in modo che venga modificato solo il carattere del carattere specifico che non è visualizzabile e il carattere per il resto della parola o della frase rimanga lo stesso.

{{% /alert %}}

## **Esempio**

 Lo screenshot seguente confronta i due PDF di output generati dal codice di esempio riportato di seguito. Uno è stato generato senza impostazione[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) property e l'altra è stata generata dopo aver impostato il file[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) proprietà a**VERO**. Come puoi vedere nel primo PDF, il carattere dell'intera frase è cambiato da Times New Roman ad Arial Unicode MS a causa di Non-Breaking Hyphen. Mentre nel secondo PDF, è cambiato solo il font di Un-Breaking Hyphen.

![cose da fare:immagine_alt_testo](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}

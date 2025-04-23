---
title: Cambia il Font solo per i caratteri Unicode specifici durante il salvataggio in PDF
type: docs
weight: 150
url: /it/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}}

Alcuni caratteri Unicode non possono essere visualizzati dal font specificato dall'utente. Uno di questi caratteri Unicode è **Trattino Non-Rotoso** (U+2011) e il suo numero Unicode è 8209. Questo carattere non può essere visualizzato con **Times New Roman**, ma può essere visualizzato con altri font come **Arial Unicode MS**.

Quando un tale carattere compare all'interno di una parola o di una frase che è in un font specifico come Times New Roman, Aspose.Cells cambia il font dell'intera parola o frase in un font che può visualizzare questo carattere come Arial Unicode to MS.

Tuttavia, questo comportamento è indesiderato per alcuni utenti e vogliono solo che il font del carattere specifico venga cambiato invece di cambiare il font dell'intera parola o frase.

Per affrontare questo problema, Aspose.Cells fornisce la proprietà [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) che dovrebbe essere impostata su **true** in modo che venga cambiato solo il font del carattere specifico che non è visualizzabile e il font per il resto della parola o della frase rimanga lo stesso.

{{% /alert %}}

## **Esempio**

La schermata seguente confronta i due PDF di output generati dal codice di esempio qui sotto. Uno è stato generato senza impostare la proprietà [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) e l'altro è stato generato dopo aver impostato la proprietà [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) su **true**. Come si può vedere nel primo PDF, il font dell'intera frase è cambiato da Times New Roman a Arial Unicode MS a causa del Trattino Non-Rotoso. Mentre nel secondo PDF, solo il font del Trattino Non-Rotoso è cambiato.

![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
{{< app/cells/assistant language="java" >}}

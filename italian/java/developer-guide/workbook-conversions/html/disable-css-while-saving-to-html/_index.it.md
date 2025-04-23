---
title: Disabilitare CSS durante il salvataggio in HTML
type: docs
weight: 320
url: /it/java/disable-css-while-saving-to-html/
---

## **Possibili Scenari di Utilizzo**

Quando salvi il tuo file Excel come HTML a pagina singola, di solito gli elementi CSS saranno incorporati nel file HTML e collocati nella sezione HEAD. Se allegi questo file come contenuto/corpo di un'email, gli elementi CSS verranno rimossi dalla maggior parte dei client di posta elettronica, risultando in un rendering non corretto. La versione 24.12 di Aspose.Cells introduce un'opzione che permette di disabilitare opzionalmente il CSS, consentendo di applicare gli stili direttamente negli elementi HTML stessi. Se vuoi impostare l'html come contenuto/corpo dell'email, utilizza la proprietà [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#DisableCss) e impostala a **true**.



## **Disabilita CSS durante il salvataggio in HTML**

Il codice di esempio seguente mostra l'uso della proprietà [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#DisableCss). 



## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-java-HTML-DisableCss-1.java" >}}
{{< app/cells/assistant language="java" >}}

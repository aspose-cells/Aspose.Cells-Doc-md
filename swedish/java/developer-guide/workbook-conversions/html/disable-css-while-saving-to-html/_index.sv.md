---
title: Inaktivera CSS vid sparning till HTML
type: docs
weight: 320
url: /sv/java/disable-css-while-saving-to-html/
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till en HTML-sida, är CSS-elementen normalt inbäddade i HTML-filen och finns i HEAD-sektionen. Om du bifogar denna fil som innehåll/kropp i ett e-postmeddelande, kommer CSS-elementen att tas bort av de flesta e-postklienter, vilket resulterar i felaktig rendering. Versionen 24.12 av Aspose.Cells introducerar ett alternativ som gör att du kan inaktivera CSS efter eget val, vilket tillåter att stilar tillämpas direkt inom HTML-elementen. Om du vill ställa in HTML som innehåll/kropp för e-postmeddelandet, använd [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#DisableCss)-egenskapen och ställ in den till **true**.



## **Inaktivera CSS vid sparning till HTML**

Följande kodexempel visar användningen av [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#DisableCss)-egenskapen. 



## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-java-HTML-DisableCss-1.java" >}}
{{< app/cells/assistant language="java" >}}

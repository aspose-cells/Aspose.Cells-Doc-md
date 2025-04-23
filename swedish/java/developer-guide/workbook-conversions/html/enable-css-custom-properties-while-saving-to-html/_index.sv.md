---
title: Aktivera CSS Anpassade Egenskaper under sparande till HTML
type: docs
weight: 320
url: /sv/java/enable-css-custom-properties-while-saving-to-html/
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML, för scenariot där det finns flera förekomster av en bas64-bild, behöver bilddata endast sparas en gång med den anpassade egenskapen för att förbättra prestandan för den resulterande HTML-filen. Använd [**HtmlSaveOptions.EnableCssCustomProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#EnableCssCustomProperties)-egenskapen och ställ in den till **true** vid sparning till HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Aktivera CSS Anpassade Egenskaper under sparande till HTML**

Följande kodexempel visar användningen av [**HtmlSaveOptions.EnableCssCustomProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#EnableCssCustompPoperties)-egenskapen. Skärmbilden visar effekten av denna egenskap när den inte är inställd på **true**. Ladda ner [mallen Excel-fil](50528260.xlsx) som används i denna kod och den [genererade HTML:n](50528261.zip) för referens.



## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-Java-HTML-·java" >}}
{{< app/cells/assistant language="java" >}}

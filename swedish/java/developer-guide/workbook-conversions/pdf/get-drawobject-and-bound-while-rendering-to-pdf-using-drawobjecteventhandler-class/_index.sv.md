---
title: Hämta DrawObject och Bound vid rendering till PDF med hjälp av DrawObjectEventHandler klassen
type: docs
weight: 60
url: /sv/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Möjliga användningsscenario**

Aspose.Cells tillhandahåller en abstrakt klass [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) som har en [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-) metod. Användaren kan implementera [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) och använda [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-) metoden för att hämta [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) och **Bound** vid rendering av Excel till PDF eller bild. Här är en kort beskrivning av parametrarna för [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-) metoden.

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) kommer att initieras och returneras vid rendering

- x: Vänster om [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y: Topp om [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- bredd: Bredd av [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- höjd: Höjd av [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

Om du renderar Excel-filen till PDF, kan du använda klassen [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) med [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). På samma sätt, om du renderar Excel-filen till bild, kan du använda klassen [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) med [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **Få DrawObject och Bound medan du renderar till Pdf med hjälp av DrawObjectEventHandler-klassen**

Se följande provkod. Det laddar den [prov Excel-filen](64716843.xlsx) och sparar den som [utdata-PDF](64716842.pdf). Vid rendering till PDF använder den egenskapen [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) och fångar [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) och **Bound** av befintliga celler och objekt, t.ex. bilder osv. Om drawObject-typen är Cell, skriver den ut dess Bound och StringValue. Och om drawObject-typen är Bild, skriver den ut dess Bound och formnamn. Se konsolresultatet från provkoden nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **Konsoloutput**

{{< highlight java >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

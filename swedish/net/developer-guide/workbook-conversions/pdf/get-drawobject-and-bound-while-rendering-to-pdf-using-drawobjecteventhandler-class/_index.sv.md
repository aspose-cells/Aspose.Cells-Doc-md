---
title: Hämta DrawObject och Bound vid rendering till PDF med hjälp av DrawObjectEventHandler klassen
type: docs
weight: 70
url: /sv/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Möjliga användningsscenario**

Aspose.Cells tillhandahåller en abstrakt klass [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) som har en [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)-metod. Användaren kan implementera [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) och använda [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)-metoden för att få [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) och Bound vid rendering av Excel till PDF eller bild. Här är en kort beskrivning av parametrarna till metoden [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) kommer att initialiseras och returneras vid rendering

- x: Vänster om [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y: Topp om [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- bredd: Bredd av [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- höjd: Höjd av [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

Om du renderar Excel-fil till PDF kan du använda klassen [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) med [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler). På samma sätt, om du renderar Excel-fil till bild, kan du använda klassen [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) med [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **Få DrawObject och Bound medan du renderar till Pdf med hjälp av DrawObjectEventHandler-klassen**

Vänligen se följande exempelkod. Den laddar [prov Excel-filen](64716821.xlsx) och sparar den som [utdata-PDF](64716822.pdf). Vid rendering till PDF använder den egenskapen [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) och fångar [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) och Bound av befintliga celler och objekt t.ex. bilder osv. Om [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)-typen är Cell skriver den ut dess Bound och StringValue. Och om [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)-typen är Bild skriver den ut dess Bound och Shape Name. Se konsol-utdata av exempelkoden nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Konsoloutput**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

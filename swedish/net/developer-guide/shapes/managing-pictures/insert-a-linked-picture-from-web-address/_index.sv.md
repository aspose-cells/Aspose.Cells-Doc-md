---
title: Infoga en länkad bild från webbadress
type: docs
weight: 450
url: /sv/net/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

Ibland behöver du infoga en bild från webben (http://) i ett kalkylblad. För att göra det, ange bildens URL och bilden kommer att laddas ner varje gång kalkylarket öppnas i Microsoft Excel. Bilden är inte fysiskt inbäddad i Excel-dokumentet, utan pekar på en webbresurs.

{{% /alert %}}

## **Använder Microsoft Excel**

I Microsoft Excel (till exempel 2007):

1.  Klicka på**Föra in** menyn och välj**Bild**.
1. Ange webbadressen för bilden i dialogrutan Infoga bild.

## **Använder Aspose.Cells för .NET**

 Aspose.Cells för .NET stöder att lägga till en länkad bild med hjälp av[**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture) . Metoden returnerar en[**Bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)objekt.

Följande exempel visar hur man lägger till länkad bild från webbadress till ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}

---
title: Infoga en länkad bild från webbadress
type: docs
weight: 450
url: /sv/python-net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

Ibland behöver du infoga en bild från webben (http://) i ett kalkylblad. För att göra detta, ange bildens URL och bilden kommer att hämtas varje gång kalkylarket öppnas i Microsoft Excel. Bilden är inte fysiskt inbäddad i Excel-dokumentet, utan pekar på en webbresurs.

{{% /alert %}}

## **Använda Microsoft Excel**

I Microsoft Excel (till exempel 2007):

1. Klicka på **Infoga** i menyn och välj **Bild**.
1. Ange webbadressen för bilden i dialogrutan Infoga bild.

## **Användning av Aspose.Cells för Python via .NET**

Aspose.Cells för Python via .NET stödjer att lägga till en länkad bild med hjälp av [**ShapeCollection.add_linked_picture(int upper_left_row, int upper_left_column, int height_pixels, int width_pixels, str source_full_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_linked_picture). Metoden returnerar ett [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)-objekt.

I följande exempel visas hur man lägger till en länkad bild från webbadress till ett kalkylblad.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertLinkedPicture-1.py" >}}

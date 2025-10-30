---
title: Infoga en länkad bild från webbadress med Golang via C++
linktitle: Infoga en länkad bild från webbadress
type: docs
weight: 450
url: /sv/go-cpp/insert-a-linked-picture-from-web-address/
description: Lär dig hur du infogar en länkad bild från en webbadress i ett arbetsblad med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Ibland behöver du infoga en bild från webben (http://) i ett kalkylblad. För att göra detta, ange bildens URL och bilden kommer att hämtas varje gång kalkylarket öppnas i Microsoft Excel. Bilden är inte fysiskt inbäddad i Excel-dokumentet, utan pekar på en webbresurs.

{{% /alert %}}

## **Använda Microsoft Excel**

I Microsoft Excel (till exempel 2007):

1. Klicka på **Infoga** i menyn och välj **Bild**.
1. Ange webbadressen för bilden i dialogrutan Infoga bild.

## **Använder Aspose.Cells for C++**

Aspose.Cells for C++ stöder att lägga till en länkad bild med hjälp av [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlinkedpicture/)-metoden. Metoden returnerar ett [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)-objekt.

Följande exempel visar hur man lägger till en länkad bild från en webbadress till ett arbetsblad.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertALinkedPictureFromWebAddress.go" >}}

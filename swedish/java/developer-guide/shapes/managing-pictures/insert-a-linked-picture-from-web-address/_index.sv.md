---
title: Infoga en länkad bild från webbadress
type: docs
weight: 50
url: /sv/java/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

Ibland behöver du infoga en bild från webben (http://) i ett kalkylblad. För att göra det, ange bildens URL och bilden kommer att laddas ner varje gång kalkylarket öppnas i Microsoft Excel. Bilden är inte fysiskt inbäddad i Excel-dokumentet, utan pekar på en webbresurs.

{{% /alert %}}

## **Infoga en länkad bild från webbadress**

### **Använder Microsoft Excel**

I Microsoft Excel (till exempel 2007):

1.  Klicka på**Föra in** menyn och välj**Bild**.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_1.png)

1.  Ange webbadressen för bilden i dialogrutan Infoga bild.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_2.png)

Bilden infogas.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_3.png)

### **Använder Aspose.Cells for Java**

 Aspose.Cells for Java stöder att lägga till en länkad bild med metoden[**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)).

 Metoden returnerar en[**Bild**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)objekt.

Följande exempel visar hur man lägger till länkad bild från webbadress till ett kalkylblad.

Efter att ha kört koden innehåller den genererade Excel-filen en länkad bild på det första kalkylbladet.

**Utdatafilen** 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}

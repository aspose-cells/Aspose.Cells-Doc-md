---
title: Hantera bilder
type: docs
weight: 10
url: /sv/java/managing-pictures/
---

Aspose.Cells tillåter utvecklare att lägga till bilder i kalkylbladet under körtiden. Dessutom kan placeringen av dessa bilder styras under körtiden, vilket diskuteras mer utförligt i de kommande avsnitten.

Den här artikeln förklarar hur man lägger till bilder och hur man infogar en bild som visar innehållet i vissa celler.

## **Lägga till bilder**

Att lägga till bilder i ett kalkylblad är väldigt enkelt. Det kräver bara några rader kod.

Ring enkelt [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String))-metoden för [**Pictures**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection)-samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-objektet). [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String))-metoden tar följande parametrar:

- **Övre vänstra radindex**, indexet för den övre vänstra raden.
- **Övre vänstra kolumnindex**, indexet för den övre vänstra kolumnen.
- **Bildfilnamn**, namnet på bildfilen, komplett med sökväg.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Positionering av bilder**

Bilder kan positioneras med hjälp av Aspose.Cells enligt följande:

- [Absolut positionering](/cells/sv/java/managing-pictures/#absolute-positioning).

### **Absolut positionering**

Utvecklare kan placera bilderna absolut genom att använda [**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX)- och [**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY)-metoderna för [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)-objektet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **Fortsatta ämnen**
- [Infoga en Länkbild från Webbadress](/cells/sv/java/insert-a-linked-picture-from-web-address/)
- [Infoga en bild baserad på cellreferens](/cells/sv/java/insert-a-picture-based-on-cell-reference/)
- [Infoga webb bild från en URL in i en Excel-kalkylblad](/cells/sv/java/insert-web-image-from-a-url-into-an-excel-worksheet/)

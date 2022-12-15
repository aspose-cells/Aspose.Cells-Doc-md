---
title: Hantera bilder
type: docs
weight: 10
url: /sv/java/managing-pictures/
---
{{% alert color="primary" %}}

Aspose.Cells tillåter utvecklare att lägga till bilder i kalkylblad under körning. Dessutom kan placeringen av dessa bilder styras under körning, vilket diskuteras mer i detalj i de kommande avsnitten.

Aspose.Cells for Java stöder endast bildformat: BMP, JPEG, PNG, GIF.

Index som används i exempel börjar från 0.

{{% /alert %}}

## **Lägga till bilder**

Det är väldigt enkelt att lägga till bilder i ett kalkylblad. Det tar bara några rader kod.

 Ring helt enkelt[**Lägg till**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String) ) metod för[**Bilder**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) samling (inkapslad i[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) objekt). De[**Lägg till**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) metod tar följande parametrar:

- **Övre vänstra radens index**, indexet för den övre vänstra raden.
- **Övre vänstra kolumnindex**, indexet för den övre vänstra kolumnen.
- **Bildfilens namn**, namnet på bildfilen, komplett med sökväg.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Placering av bilder**

Bilder kan placeras med Aspose.Cells enligt följande:

- [Absolut positionering](/cells/sv/java/managing-pictures/#absolute-positioning).

### **Absolut positionering**

 Utvecklare kan placera bilderna absolut genom att använda[**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) och[**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) metoder för[**Bild**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)objekt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **Förhandsämnen**
- [Infoga en länkad bild från webbadress](/cells/sv/java/insert-a-linked-picture-from-web-address/)
- [Infoga en bild baserat på Cell Referens](/cells/sv/java/insert-a-picture-based-on-cell-reference/)
- [Infoga webbbild från en URL i ett Excel-kalkylblad](/cells/sv/java/insert-web-image-from-a-url-into-an-excel-worksheet/)

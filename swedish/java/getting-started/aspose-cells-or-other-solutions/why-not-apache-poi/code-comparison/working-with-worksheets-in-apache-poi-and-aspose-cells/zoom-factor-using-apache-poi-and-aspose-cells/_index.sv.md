---
title: Zoomfaktor med Apache POI och Aspose.Cells
type: docs
weight: 70
url: /sv/java/zoom-factor-using-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Zoomfaktor**
Microsoft Excel tillhandahåller en funktion som låter användare ställa in ett kalkylblads zoom- eller skalningsfaktor. Den här funktionen hjälper användare att se kalkylbladets innehåll i mindre eller större vyer.

Aspose.Cells tillhandahåller en klass, arbetsbok, som representerar en Microsoft Excel-fil. Klassen Workbook innehåller en WorksheetCollection som ger åtkomst till varje kalkylblad i en Excel-fil.

Ett kalkylblad representeras av klassen Worksheet. Klassen Worksheet tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att ställa in ett kalkylblads zoomfaktor, använd arbetsbladsklassens setZoom-metod.

**Java**

{{< highlight "java" >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Zoomfaktor**
Apache POI tillhandahåller Sheet.setZoom()-metoden tillgänglig zoomfunktion.

**Java**

{{< highlight "java" >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)

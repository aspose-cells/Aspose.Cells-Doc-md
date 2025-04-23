---
title: Zoomfaktor med Apache POI och Aspose.Cells
type: docs
weight: 70
url: /sv/java/zoom-factor-using-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Zoomfaktor**
Microsoft Excel tillhandahåller en funktion som låter användare ställa in en kalkylblads zoom- eller skalfaktor. Denna funktion hjälper användare att se kalkylbladets innehåll i mindre eller större vyer.

Aspose.Cells tillhandahåller en klass, Workbook, som representerar en Microsoft Excel-fil. Workbook-klassen innehåller en WorksheetCollection som möjliggör åtkomst till varje kalkylblad i en Excel-fil.

Ett kalkylblad representeras av klassen Worksheet. Worksheet-klassen tillhandahåller ett brett utbud av egenskaper och metoder för hantering av kalkylblad. För att ställa in kalkylbladets zoomfaktor, använd Worksheet-klassens setZoom-metod.

**Java**

{{< highlight java >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Zoomfaktor**
Apache POI tillhandahåller Sheet.setZoom() metod för att tillhandahålla zoomfunktion.

**Java**

{{< highlight java >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)
{{< app/cells/assistant language="java" >}}

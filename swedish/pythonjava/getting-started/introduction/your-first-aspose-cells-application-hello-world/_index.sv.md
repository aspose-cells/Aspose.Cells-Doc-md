---
title: Din första Aspose.Cells applikation  Hej världen
type: docs
weight: 30
url: /sv/python-java/your-first-aspose-cells-application-hello-world/
---

{{% alert color="primary" %}}

Det här nybörjartemat visar hur utvecklare kan skapa en enkel första applikation (Hello World) med hjälp av Aspose.Cells enkla API. Applikationen skapar en Microsoft Excel-fil med orden Hello World i en angiven cell i en arbetsbok.

{{% /alert %}}

### **Skapa Hello World-applikationen**

För att skapa Hello World-applikationen med Aspose.Cells API:

1. Skapa en instans av [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)-klassen.
1. Tillämpa licensen:
   1. Om du har köpt en licens, använd licensen i din applikation för att få åtkomst till hela funktionaliteten hos Aspose.Cells
   1. Om du använder utvärderingsversionen av komponenten (om du använder Aspose.Cells utan licens), hoppa över detta steg.
1. Skapa en ny Microsoft Excel-fil eller öppna en befintlig fil där du vill lägga till/uppdatera någon text.
1. Få åtkomst till en valfri cell i en arbetsbok i den Microsoft Excel-filen.
1. Infoga orden **Hello World!** i en åtkomstcell.
1. Generera den modifierade Microsoft Excel-filen.

Exemplen nedan visar ovanstående steg.

#### **Skapa en arbetsbok**

I följande exempel skapas en ny arbetsbok från grunden, skriver orden "Hello World!" i cellen A1 på den första arbetsbladet och sparar filen.

**Den genererade kalkylbladet** 

![todo:image_alt_text](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFile.py" >}}

#### **Öppna en befintlig fil**

I följande exempel öppnas en befintlig Microsoft Excel-mallfil som kallas **bok1.xls**, skriver orden "Hello World!" i cellen A1 på den första arbetsbladet och sparar arbetsboken som en ny fil.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpeningExistingFile.py" >}}

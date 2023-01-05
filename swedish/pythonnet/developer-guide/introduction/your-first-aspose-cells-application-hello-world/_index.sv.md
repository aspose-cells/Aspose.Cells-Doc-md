---
title: Din första Aspose.Cells-ansökan - Hello World
type: docs
weight: 30
url: /sv/python-net/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

Det här nybörjarämnet visar hur utvecklare kan skapa en enkel första applikation (Hello World) med Aspose.Cells' enkel API. Applikationen skapar en Microsoft Excel-fil med orden Hello World i en specificerad cell i ett kalkylblad.

{{% /alert %}}

### **Skapar Hello World-applikationen**

Så här skapar du Hello World-applikationen med Aspose.Cells API:

1. Skapa en instans av klassen Workbook.
1. Använd licensen:
1. Om du har köpt en licens, använd sedan licensen i din applikation för att få tillgång till Aspose.Cells' full funktionalitet
 1. Om du använder utvärderingsversionen av komponenten (om du använder Aspose.Cells utan licens), hoppa över det här steget.
1. Skapa en ny Microsoft Excel-fil, eller öppna en befintlig fil där du vill lägga till/uppdatera lite text.
1. Få åtkomst till valfri cell i ett kalkylblad i Excel-filen Microsoft.
1.  Sätt in orden**Hello World!** in i en cell som nås.
1. Generera den modifierade Microsoft Excel-filen.

Exemplen nedan visar stegen ovan.

#### **Skapa en arbetsbok**

Följande exempel skapar en ny arbetsbok från början, skriver orden "Hello World!" i cell A1 på det första kalkylbladet och sparar filen.

**Det genererade kalkylarket** 

![todo:image_alt_text](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

#### **Öppna en befintlig fil**

 Följande exempel öppnar en befintlig Microsoft Excel-mallfil som heter**bok1.xls**, skriver orden "Hello World!" i cell A1 i det första kalkylbladet och sparar arbetsboken som en ny fil.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpeningExistingFile.py" >}}

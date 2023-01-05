---
title: Beräkna anpassade funktioner i GridWeb
type: docs
weight: 90
url: /sv/net/calculate-custom-functions-in-gridweb/
---
## **Möjliga användningsscenarier**
Aspose.Cells.GridWeb stöder beräkning av anpassade funktioner med egenskapen GridWeb.CustomCalculationEngine. Den här egenskapen tar instansen av GridAbstractCalculationEngine-gränssnittet. Vänligen implementera GridAbstractCalculationEngine-gränssnittet och beräkna dina anpassade funktioner med din egen logik.
## **Beräkna anpassade funktioner i GridWeb**
Följande exempelkod lägger till en anpassad funktion med namnet MYTESTFUNC() i cell B3. Sedan beräknar vi värdet på denna funktion genom att implementera GridAbstractCalculationEngine-gränssnittet. Vi beräknar MYTESTFUNC() på ett sådant sätt att den multiplicerar sin parameter med 2 och returnerar resultatet. Så om dess parameter är 9, kommer den att returnera 2*9 = 18.
### **Exempelkod**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}

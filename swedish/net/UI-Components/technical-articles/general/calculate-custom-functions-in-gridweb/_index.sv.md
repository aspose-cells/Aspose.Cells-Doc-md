---
title: Beräkna anpassade funktioner i GridWeb
type: docs
weight: 90
url: /sv/net/aspose-cells-gridweb/calculate-custom-functions-in-gridweb/
keywords: GridWeb,custom functions,custom,function
description: Den här artikeln introducerar funktioner för anpassade funktioner i GridWeb.
---


## **Möjliga användningsscenario**
Aspose.Cells.GridWeb stödjer beräkning av anpassade funktioner med egenskapen GridWeb.CustomCalculationEngine. Denna egenskap tar instansen av gränssnittet GridAbstractCalculationEngine. Implementera gränssnittet GridAbstractCalculationEngine och beräkna dina anpassade funktioner med din egen logik.
## **Beräkna anpassade funktioner i GridWeb**
Följande exempelkod lägger till en anpassad funktion med namnet MYTESTFUNC() i cell B3. Sedan beräknar vi värdet för denna funktion genom att implementera gränssnittet GridAbstractCalculationEngine. Vi beräknar MYTESTFUNC() på ett sådant sätt att den multiplicerar sitt parameter med 2 och returnerar resultatet. Så om dess parameter är 9, kommer den att returnera 2*9 = 18.
### **Exempelkod**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}

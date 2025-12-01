---
title: Calculate Custom Functions in GridWeb
type: docs
weight: 90
url: /net/aspose-cells-gridweb/calculate-custom-functions-in-gridweb/
keywords: GridWeb,custom functions,custom,function
description: This article introduce features of custom functions in GridWeb .
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


## **Possible Usage Scenarios**
Aspose.Cells.GridWeb supports the calculation of custom functions with the GridWeb.CustomCalculationEngine property. This property takes the instance of GridAbstractCalculationEngine interface. Please implement GridAbstractCalculationEngine interface and calculate your custom functions with your own logic.
## **Calculate Custom Functions in GridWeb**
The following sample code adds a custom function named MYTESTFUNC() in cell B3. Then we calculate the value of this function by implementing the GridAbstractCalculationEngine interface. We calculate MYTESTFUNC() in such a way that it multiplies its parameter with 2 and returns the result. So if its parameter is 9, it will return 2*9 = 18.
### **Sample Code**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}

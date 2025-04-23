---  
title: Sök data med hjälp av ursprungliga värden
type: docs  
weight: 380  
url: /sv/nodejs-cpp/search-data-using-original-values/  
description: Lär dig hur du söker data med ursprungsvärden via API et Aspose.Cells for Node.js via C++.  
keywords: Sök data med ursprungsvärden Node.js via C++, Hitta data med ursprungsvärden Node.js via C++, Sök data med ursprungsvärden Node.js via C++, Hitta data med ursprungsvärden Node.js via C++  
---  

{{% alert color="primary" %}}  

Ibland är värdet på datan dolt eftersom det är formaterat på något sätt. Till exempel, anta att cell D4 har formeln = Sum(A1:A2) och dess värde är 20, men det är formaterat som ---, då är värdet 20 dolt och kan inte hittas med hjälp av Microsoft Excels sökalternativ. Du kan dock hitta det med Aspose.Cells genom att använda [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype)  

{{% /alert %}}  

Följande exempelkod illustrerar ovanstående. Den hittar cell D4 som inte kan hittas med Microsoft Excels sökalternativ men Aspose.Cells kan hitta den med hjälp av [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype). Läs kommentarerna i koden för mer information.  

## Node.js-kod för att söka data med ursprungsvärden  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchDataUsingOriginalValues.js" >}}


## Konsolutdata som genereras av exempelkoden  

Här är konsoloutputen från ovanstående exempelkod.  

{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}  


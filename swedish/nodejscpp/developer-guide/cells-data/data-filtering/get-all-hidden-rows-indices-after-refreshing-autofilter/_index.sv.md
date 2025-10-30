---  
title: Få alla dolda radindex efter att autofiltreringen har uppdaterats 
type: docs  
weight: 320  
url: /sv/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Lär dig hur man hämtar alla dolda radindex efter att ha uppdaterat AutoFilter med API Aspose.Cells for Node.js via C++.  
keywords: Hämta alla dolda radindex efter att ha uppdaterat AutoFilter Node.js via C++, hämta alla dolda radindex efter att ha uppdaterat AutoFilter Node.js via C++, hämta alla dolda radindex efter att ha uppdaterat AutoFilter Node.js via C++  
---  

## **Möjliga användningsscenario**  

När du använder autofilter på arbetsbladsceller, blir vissa rader automatiskt dolda. Men det kan vara så att vissa rader redan är dolda manuellt av Excel-användaren och de döljs inte av autofilter. Det gör det svårt att veta vilka rader som är dolda av autofilter och vilka som är dolda manuellt av användaren. Aspose.Cells for Node.js via C++ hanterar detta problem med användning av `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-). Denna metod returnerar radindex för alla rader som är dolda av autofilter och inte manuellt av användaren.  

## **Hämta alla dolda radindex efter uppdatering av autofilter**  

Se följande exempel som laddar den [exempel-Excel filen](64716909.xlsx) som innehåller några rader dolda manuellt av användaren. Koden använder autofilter och uppdaterar det med hjälp av `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-) som returnerar radindex för alla dolda rader av autofilter. Den skriver sedan ut indexen för de dolda raderna på konsolen tillsammans med cellnamn och värden.  

## **Exempelkod**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.js" >}}


## **Konsoloutput**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}

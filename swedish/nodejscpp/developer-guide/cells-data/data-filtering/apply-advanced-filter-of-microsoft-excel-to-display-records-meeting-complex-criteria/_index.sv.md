---  
title: Tillämpa avancerad filter av Microsoft Excel för att visa poster som uppfyller komplexa kriterier
type: docs  
weight: 280  
url: /sv/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/  
description: Lär dig att tillämpa avancerad filter i Microsoft Excel för att visa poster som möter komplexa kriterier med hjälp av API et Aspose.Cells for Node.js via C++.  
keywords: Tillämpa avancerad filter Node.js via C++, ställ in avancerad filter Node.js via C++, lägg till avancerad filter Node.js via C++, skapa avancerad filter Node.js via C++, hur man lägger till avancerad filter till ett område Node.js via C++  
---  

## **Möjliga användningsscenario**  

Microsoft Excel tillåter att du tillämpar *Advanced Filter* på arbetsbladets data för att visa poster som möter komplexa kriterier. Du kan tillämpa avancerad filter med Microsoft Excel via dess *Data > Advanced* kommando som visas i denna skärmskärm.  

![todo:image_alt_text](1.png)  

Aspose.Cells for Node.js via C++ tillåter dig också att använda det avancerade filtret med metod [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-). Precis som Microsoft Excel, accepterar den följande parametrar.  

**isFilter**  

Anger om filtreringen av listan på plats.  

**listRange**  

Listan intervall.  

**criteriaRange**  

Kriterieintervallet.  

**copyTo**  

Intervallet där data kopieras till.  

**uniqueRecordOnly**  

Endast visa eller kopiera unika rader.  

## **Tillämpa Avancerat Filter i Microsoft Excel för att Visa Poster som Uppfyller Komplexa Kriterier**  

Följande kodexempel använder det avancerade filtret på [Exempelfilen Excel](48496692.xlsx) och genererar [Utdata Excel-fil](48496691.xlsx). Skärmbilden visar båda filerna för jämförelse. Som du kan se i skärmbilden, har data filtrerats i utdata Excel-filen enligt komplexa kriterier.  

![todo:image_alt_text](2.png)  

## **Exempelkod**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-AdvancedFilter.js" >}}



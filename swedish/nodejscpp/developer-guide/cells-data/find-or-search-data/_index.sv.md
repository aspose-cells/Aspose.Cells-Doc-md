---  
title: Hitta eller söka data
type: docs  
weight: 50  
url: /sv/nodejs-cpp/find-or-search-data/  
description: Lär dig hur du hittar eller söker celler i ett kalkblad som innehåller specificerad data via Aspose.Cells for Node.js via C++ API.  
keywords: Hitta data Node.js via C++, Sök data Node.js via C++, Hitta celler som innehåller en formel Node.js via C++, Sök celler som innehåller en formel Node.js via C++, Hitta data eller formler med FindOptions Node.js via C++, Sök data eller formler med FindOptions Node.js via C++, Hitta eller sök celler som innehåller ett specificerat strängt värde eller nummer Node.js via C++, Hitta eller sök celler som innehåller specificerad data  
---  

{{% alert color="primary" %}}  
Microsoft Excel tillåter användare att hitta celler i ett kalkblad som innehåller specificerad data.  
{{% /alert %}}  

## **Att hitta celler som innehåller specificerad data**  

### **Använda Microsoft Excel**  

Microsoft Excel tillåter användare att hitta celler i ett kalkblad som innehåller specificerad data. Om du väljer **Redigera** från **Sök**-menyn i Microsoft Excel, ser du en dialogruta där du kan ange sökvärdet.  

Här letar vi efter värdet "Apelsiner". Aspose.Cells tillåter också utvecklare att hitta celler i kalkylarket som innehåller specificerade värden.  

### **Användning av Aspose.Cells for Node.js via C++**  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) innehåller en [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som ger åtkomst till varje kalkblad i Excel-filen. Ett kalkblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) tillhandahåller en [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samling som representerar alla celler i kalkbladet. Samlingen [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) ger flera metoder för att hitta celler som innehåller användarspecifik data. Några av dessa metoder diskuteras nedan i mer detalj.  

{{% alert color="primary" %}}  
Alla Find-metoder returnerar referenser till celler som innehåller den specificerade datan att söka.  
{{% /alert %}}  

## **Att hitta celler som innehåller en formel**  

Utvecklare kan hitta en angiven formel i kalkbladet genom att anropa metoden [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) i [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-)-samlingen. Vanligtvis tar metoden [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) tre parametrar:  

- **Objekt:** Objektet att söka efter. Typen ska vara int, double, DateTime, string, bool.  
- **Föregående cell:** Föregående cell med samma objekt. Denna parameter kan sättas till null om sökningen börjar från början.  
- **FindOptions:** Inställningar för att hitta det erforderliga objektet.  

Nedan används exempel på kalkylarksdata för att öva på hittametoder.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainFormula.js" >}}


## **Hitta data eller formler med FindOptions**  

Det är möjligt att hitta specificerade värden med hjälp av [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen och [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-)-metoden med olika [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions). Vanligtvis accepterar [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-)-metoden följande parametrar:  

- **Sökvärde**, data eller värde som ska sökas efter.  
- **Föregående cell**, den sista cellen som innehöll samma värde. Denna parameter kan ställas in till null när du söker från början.  
- **Hitta alternativ**, hitta alternativ.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindDataUsingFindOptions.js" >}}


## **Hitta celler som innehåller specifierade strängvärden eller nummer**  

Det är möjligt att hitta angivna strängvärden genom att anropa samma [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-)-metod som finns i [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen med olika [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions).  

Ange egenskaperna [**FindOptions.setLookInType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookInType-lookintype-) och [**FindOptions.setLookAtType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookAtType-lookattype-). Följande kodexempel visar hur man använder dessa egenskaper för att hitta celler med olika antal strängar i början, mitten eller slutet av cellens text.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainSpecifyString.js" >}}



## **Fortsatta ämnen**  
- [Hitta celler med specifik stil](/cells/sv/nodejs-cpp/find-cells-with-specific-style/)  
- [Ta reda på om cellvärdet börjar med citattecken](/cells/sv/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Sök data med originalvärden](/cells/sv/nodejs-cpp/search-data-using-original-values/)  

{{< app/cells/assistant language="nodejs-cpp" >}}

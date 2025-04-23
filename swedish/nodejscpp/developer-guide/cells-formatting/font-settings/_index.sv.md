---  
title: Texinställningar med Node.js via C++  
linktitle: Fontinställningar  
description: Aspose.Cells är ett Node.js bibliotek för att arbeta med kalkylbladsfiler. Det stöder att ställa in cellers typsnitt, vilket gör det möjligt för användare att anpassa cellens teckenvy och egenskaper. Den här artikeln introducerar hur man använder Aspose.Cells biblioteket för att ställa in cellers typsnittsinställningar.  
keywords: Aspose.Cells, Celler, Typsnittsinställningar, Stilar, Egenskaper, Node.js via C++  
type: docs  
weight: 30  
url: /sv/nodejs-cpp/cells-font-settings/  
---  

{{% alert color="primary" %}}  
Utseendet och känslan av en text kan kontrolleras genom att ändra fontinställningarna. Fontinställningarna kan inkludera namn, stil, storlek, färg och andra effekter för teckensnitten. Precis som Microsoft Excel stöder även Aspose.Cells konfigurering av cellernas fontinställningar.  
{{% /alert %}}  

## **Konfigurera fontinställningar**  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som ger åtkomst till varje arbetsblad i en Excel-fil. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen ger en [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen.  

Aspose.Cells tillhandahåller [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassens [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) och [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) metoder som används för att hämta och ställa in en cells formateringsstil. [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-klassen ger egenskaper för att konfigurera typsnittsinställningar.  

### **Ange fontnamn**  

Utvecklare kan applicera vilken font som helst på texten inuti en cell genom att använda [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)-objektets [setName](https://reference.aspose.com/cells/nodejs-cpp/font/#setName-string-) metod.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontName.js" >}}


### **Ange fontstil till Fetstil**  

Utvecklare kan göra text fet genom att sätta [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)-objektets [**setIsBold**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsBold-boolean-)-metod till **true**.   

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetBoldStyle.js" >}}



### **Inställning av fontstorlek**  

Ange teckenstorleken med [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)-objektets [**setSize**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSize-number-)-metod.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontSize.js" >}}


### **Sätt Typsnittsfärg**  

Använd [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)-objektets [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-)-metod för att ställa in teckenfärgen. Välj vilken färg som helst från Color-uppräkningen (del av Node.js) och tilldela den till [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-)-metoden.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontColor.js" >}}


### **Inställning av font underlinjetyp**  

Använd [**setUnderline**](https://reference.aspose.com/cells/nodejs-cpp/font/#setUnderline-fontunderlinetype-)-metoden för [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)-objektet för att understryka text. Aspose.Cells erbjuder olika fördefinierade teckensnitts-understrykningstyper i [**FontUnderlineType**](https://reference.aspose.com/cells/nodejs-cpp/fontunderlinetype)-uppräkningen.  

|**Font Underline Types**|**Beskrivning**|  
| :- | :- |  
|Accounting|Enkel redovisningsunderstrykning|  
|Double|Dubbel understrykning|  
|DoubleAccounting|Dubbel redovisningsunderstrykning|  
|None|Ingen understrykning|  
|Single|Enkel understrykning|  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontUnderline.js" >}}


### **Inställning för överstruken effekt**  

Tillämpa linjering genom att ställa in [**setIsStrikeout**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsStrikeout-boolean-)-metoden för [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)-objektet till **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}


### **Inställning av understreckningseffekt**  

Tillämpa subscript genom att ställa in [**setIsSubscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSubscript-boolean-)-metoden för [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)-objektet till **true**.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}



### **Inställning av överstruken effekt på font**  

Utvecklare kan tillämpa exponenteffekten på teckensnittet genom att ställa in [**setIsSuperscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSuperscript-boolean-)-metoden för [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)-objektet till **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetSuperscript.js" >}}


## **Fortsatta ämnen**  
- [Applicera Superscript- och Subscript-effekter på typsnitt](/cells/sv/nodejs-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [Få en lista över typsnitt som används i en kalkylblad eller arbetsbok](/cells/sv/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)  



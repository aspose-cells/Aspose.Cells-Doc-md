---  
title: Nummerinställningar
linktitle: Nummerinställningar  
description: Aspose.Cells är ett Node.js bibliotek för att arbeta med kalkylbladsfiler som stöder många olika inställningar för cellnummer. Den här artikeln introducerar hur man använder Aspose.Cells biblioteket för att hantera cellernas nummerinställningar för att justera nummerformat i kalkylblad.  
keywords: Aspose.Cells, Node.js bibliotek, elektroniskt kalkylblad, cellnummerinställningar, formatering, hantering, Format av Nummer och Datum  
type: docs  
weight: 10  
url: /sv/nodejs-cpp/cells-number-settings/  
---  

## **Hur man ställer in visningsformat för nummer och datum**  

En mycket stark funktion i Microsoft Excel är att den tillåter användare att ställa in visningsformat för numeriska värden och datum. Vi vet att numeriska data kan användas för att representera olika värden inklusive decimal, valuta, procent, bråk eller bokföringsvärden, etc. Alla dessa numeriska värden visas i olika format beroende på vilken typ av information de representerar. På samma sätt finns det många format för hur ett datum eller en tid kan visas.  
Aspose.Cells stöder denna funktion och tillåter utvecklare att ställa in vilket visningsformat som helst för ett nummer eller ett datum.  

### **Hur man ställer in visningsformat i Microsoft Excel**  

För att ställa in visningsformat i Microsoft Excel:  

1. Högerklicka på vilken cell som helst.  
2. Välj **Formatera celler**. En dialogruta kommer att öppnas och används för att ställa in visningsformat för vilken som helst slags värde.  

På vänstra sidan av dialogrutan finns många kategorier av värden som **Allmän**, **Nummer**, **Valuta**, **Bokföring**, **Datum**, **Tid**, **Procent**, etc. Aspose.Cells stödjer alla dessa visningsformat.  

Aspose.Cells tillhandahåller en modul, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Excel-fil. Målmodulen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som ger tillgång till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av modulen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Modulen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) ger en [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-modulen.  

Aspose.Cells tillhandahåller [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getstyle--) och [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) metoder för [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-modulen. Dessa metoder används för att hämta och ställa in cellens formatering. Modulen [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) erbjuder några användbara egenskaper för att hantera visningsformat för nummer och datum.  

### **Hur man använder inbyggda nummerformat**  

Aspose.Cells erbjuder några inbyggda nummerformat för att konfigurera visningsformaten för nummer och datum. Dessa inbyggda nummerformat kan tillämpas genom att använda [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-)-metoden för [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektet. Alla inbyggda nummerformat tilldelas unika numeriska värden. Utvecklare kan tilldela vilket önskat numeriskt värde som helst till [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-)-metoden för [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektet för att tillämpa visningsformatet. Detta tillvägagångssätt är snabbt. Nedan listas de inbyggda nummerformaten som stöds av Aspose.Cells.  

|**Värde**|**Typ**|**Formatsträng**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


### **Hur man använder egna nummerformat**  

För att definiera din egen anpassade formateringssträng för att ställa in visningsformatet, använd [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektets [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-)-metod. Detta tillvägagångssätt är inte lika snabbt som att använda förinställda format, men det är mer flexibelt.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


{{% alert color="primary" %}}  

Om du använder [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-)-metoden för att ställa in nummerformatet, överskrids vilket tidigare format som än har satts med [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-)-metoden och vice versa.  

{{% /alert %}}  

## **Fortsatta ämnen**  
- [Kontrollera anpassat nummerformat vid inställning av Style.Custom-egenskap](/cells/sv/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [Lista över stödda nummerformat](/cells/sv/nodejs-cpp/list-of-supported-number-formats/)  
- [Rendera anpassat datumformatmönster g och ge mm dd](/cells/sv/nodejs-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Ange anpassade nummerdecimaler och gruppavgränsare för Arbetsbok](/cells/sv/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [Specificera DBNum anpassade mönsterformatering](/cells/sv/nodejs-cpp/specifying-dbnum-custom-pattern-formatting/)  
{{< app/cells/assistant language="nodejs-cpp" >}}

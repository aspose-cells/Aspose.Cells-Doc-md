---
title: Formatera smarta markörer
type: docs
weight: 20
url: /sv/java/formatting-smart-markers/
---
##  **Kopiera stilattribut**
Ibland, när du använder smarta markörer, vill du kopiera stilen på cellen som innehåller smarta markörtaggar. Du kan använda CopyStyle-attributet för smartmarkörens taggar för detta ändamål.
###  **Kopiera stilar från Cells med smarta markörer**
 Det här exemplet använder en enkel mall Microsoft Excel-fil med två markörer i A2- och B2-cellerna. Markören som klistras in i cell B2 använder CopyStyle-attributet, medan markören i cell A2 inte gör det. Använd enkel formatering (ställ till exempel teckensnittsfärgen till**röd** och ställ in cellfyllningsfärgen till *gul**).

 Detta exempel använder en[mallfil](template1.xlsx)med några markörer i cellerna. När koden körs kopierar Aspose.Cells formateringen till alla poster i kolumn B men behåller inte formateringen i kolumn A.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-UsingCopyStyleAttribute-1.java" >}}


##  **Lägga till anpassade etiketter**
###  **Introduktion**
När du arbetar med Smart Markers gruppdatafunktion behöver du ibland lägga till dina egna anpassade etiketter på sammanfattningsraden. Du vill också sammanfoga kolumnens namn med den etiketten, t.ex. "Subtotal av beställningar". Aspose.Cells ger dig Label- och LabelPosition-attribut, så att du kan placera dina anpassade etiketter i de smarta markörerna samtidigt som du sammanfogar med delsummaraderna i grupperingsdata.
###  **Lägga till anpassade etiketter för att sammanfoga med deltotalraderna i Smarta markörer**
 Detta exempel använder en[mallfil](template.xlsx) med några markörer i cellerna. När koden körs lägger Aspose.Cells till några anpassade etiketter till sammanfattningsraderna för den grupperade datan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-AddCustomLabels-1.java" >}}

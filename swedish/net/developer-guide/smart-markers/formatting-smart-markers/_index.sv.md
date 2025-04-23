---
title: Formatering Smart Markers
type: docs
weight: 20
url: /sv/net/formatting-smart-markers/
---

## **Kopiera stilmärkning**
Ibland, vid användning av smarta markeringar, vill du kopiera stilen från cellen som innehåller de smarta markeringarna. Du kan använda CopyStyle-attributet i de smarta markeringarna för detta ändamål.
### **Kopiera stilar från celler med Smart Markers**
Detta exempel använder en enkel Excel-fil med två markörer i cellerna A2 och B2. Markören som klistras in i cell B2 använder attributet CopyStyle, medan markören i cell A2 inte gör det. Utför enkel formatering (t.ex. ställ in fontfärgen till **röd** och ställ in fyllnadsfärgen till **gul**).

När koden körs kopierar Aspose.Cells formateringen till alla poster i kolumn B men behåller inte formateringen i kolumn A.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingCopyStyleAttribute-1.cs" >}}
## **Lägga till anpassade etiketter**
### **Introduktion**
När du arbetar med Smart Markers för grupperingsdata, behöver du ibland lägga till dina egna anpassade etiketter till summeringsraden. Du vill också sammanfoga kolumnens namn med den etiketten, t.ex. "Delsumma för beställningar". Aspose.Cells tillhandahåller dig attributen Label och LabelPosition, så att du kan placera dina anpassade etiketter i Smart Markers medan du sammanfogar med delsummor i grupperingsdatan.
### **Lägga till anpassade etiketter att sammanfoga med delsummor i Smart Markers**
I det här exemplet används en [datafil](96927971.xlsx) och en [mallfil](96927972.xlsx) med några markörer i cellerna. När koden körs lägger Aspose.Cells till några anpassade etiketter till sammanfattningsraderna för den grupperade datan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AddCustomLabels-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

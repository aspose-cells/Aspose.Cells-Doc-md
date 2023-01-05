---
title: Använder formelparametern i Smart Marker-fältet
type: docs
weight: 30
url: /sv/java/using-formula-parameter-in-smart-marker-field/
---
## **Möjliga användningsscenarier**
Ibland vill du bädda in formel i det smarta markörfältet. Den här artikeln beskriver hur man använder formelparametern för att bädda in formel i smart markörfält.
## **Använder formelparametern i Smart Marker-fältet**
 Följande exempelkod bäddar in formeln i den smarta markörvariabeln med namnet Test och dess datakällas namn är också Test, så det fullständiga fältet med formelparametern ser ut som**&=$Test(formel)** och efter exekvering av koden,[slutgiltig Excel-fil](47153156.xlsx) kommer att ha formler i celler från A1 till A5.
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-SmartMarkers-UsingFormulaParameterInSmartMarkerField.java" >}}

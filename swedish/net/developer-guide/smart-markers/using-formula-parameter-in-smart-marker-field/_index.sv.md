---
title: Använder formelparametern i Smart Marker-fältet
type: docs
weight: 40
url: /sv/net/using-formula-parameter-in-smart-marker-field/
---
## **Möjliga användningsscenarier**
Ibland vill du bädda in formel i det smarta markörfältet. Den här artikeln beskriver hur du använder*Formel*parameter för att bädda in formel i smartmarkörfältet.
## **Använder formelparametern i Smart Marker-fältet**
 Följande exempelkod bäddar in formeln i det smarta markörfältet med namnet TestFormula och dess datakällas namn är MyDataSource, så det kompletta fältet med formelparametern ser ut som &=MyDataSource.TestFormula(formula) och efter exekvering av koden,[slutgiltig Excel-fil](46465047.xlsx) kommer att ha formler i celler från A1 till A5.
## **Exempelkod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}

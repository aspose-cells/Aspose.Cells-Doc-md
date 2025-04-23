---
title: Använda Formelparameter i Smart Marker fält
type: docs
weight: 40
url: /sv/net/using-formula-parameter-in-smart-marker-field/
---


## **Möjliga användningsscenario**
Ibland vill du bädda in en formel i det smarta markörfältet. Den här artikeln beskriver hur du använder *Formel* parametern för att bädda in en formel i det smarta markörfältet.
## **Använda Formelparameter i Smart Marker-fält**
Följande kodexempel bäddar in formeln i det smarta markörfältet med namnet TestFormula och dess datakällnamn är MyDataSource, så det kompletta fältet med formelparametern ser ut som &=MyDataSource.TestFormula(formula) och efter att koden har körts kommer den [slutliga utmatningsfilen för Excel](46465047.xlsx) att innehålla formler i cellerna från A1 till A5.
## **Exempelkod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
{{< app/cells/assistant language="csharp" >}}

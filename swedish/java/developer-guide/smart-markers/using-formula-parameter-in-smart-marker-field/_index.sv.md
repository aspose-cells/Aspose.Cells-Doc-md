---
title: Använda Formelparameter i Smart Marker fält
type: docs
weight: 30
url: /sv/java/using-formula-parameter-in-smart-marker-field/
---

## **Möjliga användningsscenario**
Ibland vill du bädda in en formel i smart markerns fält. Denna artikel beskriver hur man använder Formelparameter för att bädda in en formel i smart markerns fält.
## **Använda Formelparameter i Smart Marker-fält**
Följande kodexempel bäddar in formeln i den smarta markerns variabel som heter Test och dess datakälla heter också Test, så det kompletta fältet med formelparameter ser ut som **&=$Test(formula)** och efter att koden har utförts kommer [slutresultatet av Excel-filen](47153156.xlsx) innehålla formler i cellerna från A1 till A5.
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-SmartMarkers-UsingFormulaParameterInSmartMarkerField.java" >}}
{{< app/cells/assistant language="java" >}}

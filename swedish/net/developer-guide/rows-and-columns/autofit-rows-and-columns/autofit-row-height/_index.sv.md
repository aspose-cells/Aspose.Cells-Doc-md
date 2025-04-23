---
title: Autofit radhöjden automatiskt när filen laddas
type: docs
weight: 120
url: /sv/net/autofit-row-height/
description: Lär dig hur du anpassar raderna vars höjd inte är anpassad manuellt.
keywords: Automatisk anpassning av radhöjd vid filinläsning, justera automatiskt radhöjden vid öppnande av Excel fil. 
---

## **Möjliga användningsscenario**
Radens höjd stämmer automatiskt överens med innehållets teckensnitt, men när radens höjd inte matchar innehållet i filen, kommer MS Excel automatiskt att justera radhöjden vid inläsning av filen, medan Aspose.Cells inte automatiskt kommer att justera den för att förbättra prestanda. Om du behöver använda Aspose.Cells-programmet för att automatiskt matcha radhöjder vid filinläsning kan du uppnå målet genom parametern [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

Se följande bilddata. Vi kan observera att cachradens höjd i rad 11 är 15, men Excel justerade automatiskt radhöjden när filen laddades.
<br>
<img src="1.png" width=70% />

## **Justera radhöjd med Aspose.Cells**
Om du direkt laddar filen och sparar den till PDF kommer datan inte att visas fullt ut i PDF eftersom dess cachradshöjd endast är 15.
<br>
<img src="2.png" width=70% />
<br>
Om du ställer in parametern [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) till true vid inläsning av filen, då kommer Aspose.Cells automatiskt att justera radhöjden. Den justerade radhöjden kan effektivt uppfylla textens visningskrav.
<br>
<img src="3.png" width=70% />

## **C# Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}
{{< app/cells/assistant language="csharp" >}}

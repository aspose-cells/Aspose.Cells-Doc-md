---
title: Autopassa radhöjd automatiskt när filen laddas
type: docs
weight: 120
url: /sv/net/autofit-row-height/
description: Lär dig hur du passar de rader vars höjd inte är anpassad.
keywords: AutoFit Row Height when loading file, automatically adjust the row height when opening excel file. 
---
##  **Möjliga användningsscenarier**
 Höjden på raden matchar automatiskt innehållets teckensnitt, men när höjden på den cachade raden inte matchar höjden på innehållet i filen kommer MS Excel automatiskt att justera radhöjden när filen laddas, medan Aspose.Cells inte justera den automatiskt för att förbättra prestandan. Om du behöver använda programmet Aspose.Cells för att automatiskt matcha radhöjder när du laddar filer, kan du uppnå målet genom parametern[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

Se följande bilddata. Vi kan observera att cache-radhöjden på rad 11 är 15, men Excel justerade automatiskt radhöjden när filen laddades.
<br>
<img src="1.png" width=70% />

##  **Justera radhöjden med Aspose.Cells**
Om du laddar filen direkt och sparar den till PDF, kommer data inte att visas helt i PDF eftersom dess cache-radhöjd bara är 15.
<br>
<img src="2.png" width=70% />
<br>
 Om du ställer in parametern[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) till sant när filen laddas, kommer Aspose.Cells automatiskt att justera radhöjden. Den justerade radhöjden kan effektivt uppfylla textvisningskraven.
<br>
<img src="3.png" width=70% />

##  **C# Provkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}
---
title: Autofit radhöjden automatiskt när filen laddas
type: docs
weight: 120
url: /sv/python-net/autofit-row-height/
description: Lär dig hur man passar rader vars höjd inte är anpassade via Aspose.Cells för Python via .NET API.
keywords: Python Excel Library, Python Autofit Row Height vid laddning av fil, Python justera automatiskt radhöjden vid öppnande av excelfilen. 
---

## **Möjliga användningsscenario**
Höjden på raden matchar automatiskt innehållets typsnitt, men när höjden på den cachade raden inte matchar innehållets höjd i filen, kommer MS Excel automatiskt att justera radhöjden när filen laddas, medan Aspose.Cells för Python via .NET inte automatiskt kommer att justera den för att förbättra prestanda. Om du behöver använda programmet Aspose.Cells för Python via .NET för att automatiskt matcha radhöjder vid filinläsning kan du uppnå målet genom parametern [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/).

Se följande bilddata. Vi kan observera att cachradens höjd i rad 11 är 15, men Excel justerade automatiskt radhöjden när filen laddades.
<br>
<img src="1.png" width=70% />

## **Justera radhöjden med hjälp av Aspose.Cells för Python Excel Library**
Om du direkt laddar filen och sparar den till PDF kommer datan inte att visas fullt ut i PDF eftersom dess cachradshöjd endast är 15.
<br>
<img src="2.png" width=70% />
<br>
Om du ställer in parametern [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) till true när du laddar filen, kommer Aspose.Cells för Python via .NET automatiskt att justera radhöjden. Den justerade radhöjden kan effektivt uppfylla textvisningskraven.
<br>
<img src="3.png" width=70% />

## **Python Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Rows-autofit-row-height.py" >}}

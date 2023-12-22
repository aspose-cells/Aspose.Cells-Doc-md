---
title: Konvertera JSON till CSV
type: docs
weight: 210
url: /sv/python-net/convert-json-to-csv/
description: Lär dig hur du konverterar json till csv-fil med Aspose.Cells for Python via .NET API.
keywords: Python Convert json to csv, Convert json to csv Pyton via NET, Export json to csv, Convert json to csv
---
##  **Konvertera JSON till CSV**

Aspose.Cells for Python via .NET stöder konvertering av både enkel och kapslad JSON till CSV. För detta tillhandahåller API**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)** och**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** klasser. De**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**klass ger alternativen för JSON layout som**[ignore_array_title](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/ignore_array_title/)**(ignorerar titeln om arrayen är en egenskap hos ett objekt) eller ** [array_as_table](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/array_as_table/)**(behandlar arrayen som en tabell). **[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**klass bearbetar JSON med hjälp av layoutalternativen som ställts in med**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**klass.

Följande kodexempel visar användningen av**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**och**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** klasser för att ladda[källfil JSON](104398869.json) och genererar[utgång CSV fil](104398870.csv).

###  **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.py" >}}

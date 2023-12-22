---
title: Byt namn på dubbletter av kolumner automatiskt när du exporterar kalkylbladsdata
type: docs
weight: 250
url: /sv/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Lär dig hur du byter namn på dubbletter av kolumner automatiskt när du exporterar kalkylbladsdata via Aspose.Cells for .NET API.
keywords: Rename duplicate columns while exporting worksheet data, Rename duplicate columns automatically while exporting  data to DataTable
---
##  **Möjliga användningsscenarier**

 Ibland står användaren inför ett problem med dubbletter av kolumner när data exporteras från kalkylbladet till datatabellen. DataTable kan inte ha dubblettkolumner så dubblettkolumner måste bytas om innan du kan exportera kalkylbladsdata till datatabellen. Aspose.Cells kan byta namn på dubblettkolumnerna automatiskt i enlighet med strategi som specificerats av dig med[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) fast egendom. Om du specificerar[**Byt namn på Strategi**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) .Siffra, kommer kolumner att döpas om som kolumn1, kolumn2, kolumn3, etc. och om du anger[**Byt namn på Strategi**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter, då kommer kolumner att döpas om som kolumnA, kolumnB, kolumnC osv.

##  **Byt namn på dubbletter av kolumner automatiskt när du exporterar kalkylbladsdata**

Följande exempelkod lägger till en del data i de tre första kolumnerna i kalkylbladet men alla kolumner har samma namn, dvs *People*. Sedan exporterar den data från kalkylblad till datatabell genom att specificera[**Byt namn på Strategi**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Brevstrategi. Den skriver sedan ut kolumnnamnen för datatabellen genererad av Aspose.Cells. Följande skärmdump visar datatabellen med exporterade data i visualizern. Som du kan se har duplicerade kolumner bytt namn till PeopleA, PeopleB etc.

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

##  **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

##  **Konsolutgång**

Här är konsolutgången för ovanstående exempelkod som referens.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}

---
title: Byt namn på dubbla kolumner automatiskt vid export av kalkylbladsdata
type: docs
weight: 250
url: /sv/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Lär dig hur man automatiskt byter namn på dubbla kolumner vid export av kalkylbladsdata genom API Aspose.Cells for .NET.
keywords: Byt namn på dubbla kolumner vid export av kalkylbladsdata, Byt namn på dubbla kolumner automatiskt vid export till DataTable
---

## **Möjliga användningsscenario**

Ibland stöter användare på problemet med dubbla kolumner vid export av data från kalkylblad till datatabell. DataTable kan inte ha dubbla kolumner, så dubbla kolumner måste döpas om innan du kan exportera kalkylbladsdata till datatabell. Aspose.Cells kan automatiskt döpa om dubbla kolumner enligt en av den specificerade strategin med egenskapen [**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy).Om du specificerar [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Digit kommer kolumnerna att döpas om som kolumn1, kolumn2, kolumn3, etc. och om du specificerar [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter, kommer kolumnerna att döpas om som kolumnA, kolumnB, kolumnC, etc.

## **Ändra namn automatiskt på dubbletter av kolumner vid export av kalkylbladsdata**

Följande provkod lägger till lite data i de tre första kolumnerna i kalkylbladet men alla kolumner har samma namn, dvs. *Folk*. Sedan exporterar den datan från kalkylbladet till datatabell genom att ange [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter strategin. Sedan skriver den ut kolumnnamnen i den datatabell som genererats av Aspose.Cells. Följande skärmbild visar datatabellen med exporterad data i visualiseraren. Som du kan se har dubbla kolumner bytt namn till FolkA, FolkB osv.

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **Konsoloutput**

Här är konsolens utmatning av ovanstående provkod som referens.

{{< highlight java >}}

People

PeopleA

PeopleB

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

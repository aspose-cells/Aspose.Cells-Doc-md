---
title: Aspose.Cells för .NET 19.10 Release Notes
type: docs
weight: 30
url: /sv/net/aspose-cells-for-net-19-10-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 19.10](https://www.nuget.org/packages/Aspose.Cells/19.10.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46926|PageSavingCallback när du sparar till TIFF|Ny funktion|
|CELLSNET-46927|IMailMergeDataSource-motsvarighet för Cells|Ny funktion|
|CELLSNET-46903|Ändra stil på ContentTypeProperties|Förbättring|
|CELLSNET-46954|Höj undantag som liknar Excel istället för hängande program|Prestanda|
|CELLSNET-46896|Trattdiagram försvinner|Insekt|
|CELLSNET-46934|Fördröjning och minnesanvändning vid konvertering till PDF-filformat|Insekt|
|CELLSNET-43416|Sorteringen av pivotfältet ändras efter att kalkylarket har renderats till PDF|Insekt|
|CELLSNET-44686|Pivotsortering tillämpas inte vid extrahering av diagram|Insekt|
|CELLSNET-46793|Ett problem med pivottabeller|Insekt|
|CELLSNET-46882|Problem när du grupperar pivottabellen efter datum och sparar som PDF|Insekt|
|CELLSNET-46935|Radbryt text som inte återges i HTML|Insekt|
|CELLSNET-46940|Tabellkanter är inte korrekt renderade i HTML|Insekt|
|CELLSNET-46939|Stöd för TEXTJOIN()-funktionen|Insekt|
|CELLSNET-46237|Cell Format fastnar inte|Insekt|
|CELLSNET-46245|Klipp ut/klistra in kopierar inte namnet på Cell till den nya platsen i GridDesktop|Insekt|
|CELLSNET-46910|Valideringar av listdata (rullgardinsmenyer) fungerar inte med Aspose.Cells.GridWeb-matris|Insekt|
|CELLSNET-46943|ImportXML-funktion Tabelldata hämtas från fel post|Insekt|
|CELLSNET-46899|Utseendet på trattdiagrammet ändras (titelteckensnitt, nummerformat, diagrambredd)|Insekt|
|CELLSNET-46900|Kartdiagrammets färgschema ändras|Insekt|
|CELLSNET-46902|Alternativet Radera rad manuellt är inaktiverat i tabellen efter att Excel-filen har fyllts i med ImportData|Insekt|
|CELLSNET-46916|Insert Range orsakar filkorruption|Insekt|
|CELLSNET-46919|Skadad fil vid byte till XLSB-filformat från XLSX|Insekt|
|CELLSNET-46925|Problem vid extrahering av OLE-objekt från XLSX|Insekt|
|CELLSNET-46928|Conholdate Total licensemission|Insekt|
|CELLSNET-46929|Kartaxeletikettens (titel) orientering ändrades vid kopiering av arbetsblad|Insekt|
|CELLSNET-46933|Att öppna och spara en XLS-fil tar bort alla dokument och anpassade egenskaper|Insekt|
|CELLSNET-46945|Extend Range.RemoveDuplicates|Insekt|
|CELLSNET-46948|Range.Copy prestanda för stor volym|Insekt|
|CELLSNET-46949|OLE-objekt blir bilder vid kopiering av arbetsblad|Insekt|
|CELLSNET-46941|Spara som HTML ger ett undantag när cellen har en filreferens|Undantag|
|CELLSNET-46952|Undantag vid anrop av Workbook.RemoveUnusedStyles()|Undantag|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Lägger till metoden Cells.RemoveDuplicates().**
Tar bort dubbletter av data från intervallet.
#### **Lägger till egenskapen OleObject.FullObjectBin**
Hämtar den fullständiga inbäddade ole-objektets binära data i mallfilen.
#### **Lägger till egenskapen ContentTypeProperty.IsNillable**
Anger om egenskapen kan vara null.
#### **Lägg till metoden WorkbookDesigner.SetDataSource(String,ICellsDataTable).**
Ställer in datakällan för smart markördesigner.
#### **Lägger till egenskapen ImageOrPrintOptions.PageSavingCallback**
Kontroller/indikerar framsteg för sidsparprocessen.
#### **Lägger till egenskapen ImageOrPrintOptions.IsFontSubstitutionCharGranularity**
Anger om teckensnittet endast ersätts när cellteckensnittet inte är kompatibelt med det.

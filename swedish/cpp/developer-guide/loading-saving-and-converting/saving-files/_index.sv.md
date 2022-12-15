---
title: Sparar filer
type: docs
weight: 20
url: /sv/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells gör det möjligt att skapa och spara filer och att manipulera befintliga filer. Den här artikeln förklarar de olika sätten på vilka filer kan sparas.

{{% /alert %}} 
## **Olika sätt att spara filer**
 Aspose.Cells tillhandahåller[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) som representerar en Microsoft Excel-fil och tillhandahåller metoder som är nödvändiga för att arbeta med Excel-filer. De[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) klass ger[Spara](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) metod som används för att spara Excel-filer. De[Spara](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) Metoden har många överbelastningar som används för att spara filer på olika sätt. Filformatet som filen sparas i bestäms av[SaveFormat](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)uppräkning.
## **Sparar fil på någon plats**
 För att spara filer till en lagringsplats, ange filnamnet (komplett med lagringssökväg) och önskat filformat (från[SaveFormat](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)uppräkning) när du anropar[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) objekt[Spara](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)metod.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation.cpp" >}}


## **Sparar fil för att streama**
 För att spara filer till en ström, skapa ett MemoryStream- eller FileStream-objekt och spara filen till det strömobjektet genom att anropa[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) objekt[Spara](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) metod. Ange önskat filformat med hjälp av[SaveFormat](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) uppräkning när du ringer till[Spara](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)metod.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream.cpp" >}}

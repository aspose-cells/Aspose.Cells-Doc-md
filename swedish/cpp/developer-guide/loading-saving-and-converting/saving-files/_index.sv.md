---
title: Sparar filer
type: docs
weight: 20
url: /sv/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells gör det möjligt att skapa och spara filer och att manipulera befintliga filer. Den här artikeln förklarar de olika sätten på vilka filer kan sparas.

{{% /alert %}} 
##  **Olika sätt att spara filer**
 Aspose.Cells tillhandahåller[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil och tillhandahåller metoder som är nödvändiga för att arbeta med Excel-filer. De[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klass ger[Spara](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metod som används för att spara Excel-filer. De[Spara](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Metoden har många överbelastningar som används för att spara filer på olika sätt. Filformatet som filen sparas i bestäms av[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)uppräkning.
##  **Sparar fil på någon plats**
För att spara filer till en lagringsplats, ange filnamnet (komplett med lagringssökväg) och önskat filformat (från[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) uppräkning) när du anropar[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) föremål[Spara](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)metod.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


##  **Sparar fil för att streama**
 För att spara filer till en ström, skapa ett MemoryStream- eller FileStream-objekt och spara filen till det strömobjektet genom att anropa[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) föremål[Spara](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metod. Ange önskat filformat med hjälp av[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) uppräkning när du ringer till[Spara](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)metod.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}

---
title: Spara filer
type: docs
weight: 20
url: /sv/cpp/saving-files/
---

{{% alert color="primary" %}} 

Aspose.Cells gör det möjligt att skapa och spara filer samt manipulera befintliga filer. Den här artikeln förklarar olika sätt där filer kan sparas.

{{% /alert %}} 
## **Olika sätt att spara filer**
Aspose.Cells tillhandahåller [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil och tillhandahåller de metoder som behövs för att arbeta med Excel-filer. Klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) tillhandahåller metoden [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) som används för att spara Excel-filer. Metoden [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) har många överbelastningar som används för att spara filer på olika sätt. Filformatet som filen sparas till bestäms av uppräkningen [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/).
## **Spara fil till en plats**
För att spara filer till en lagringsplats, ange filnamnet (kompletterat med lagringsvägen) och önskat filformat (från uppräkningen [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)) när du anropar [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objektets [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metod.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


## **Spara fil till ström**
För att spara filer till en ström, skapa ett MemoryStream- eller FileStream objekt och spara filen i det strömobjektet genom att anropa [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objektets [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metod. Ange det önskade filformatet med uppräkningen [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) vid anrop av [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metoden.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}

## **Spara fil till PDF**
För att spara önskat innehåll till en PDF-fil med hjälp av biblioteket Aspose.Cells for C++, skapa en ny [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objekt eller konstruera ett [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objekt genom att läsa in en befintlig Excel-fil och sedan [spara](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) filen som PDF genom att anropa Save-metoden för [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objektet. När du anropar Save-metoden, använd uppräkningen [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) för att ange det önskade filformatet.


{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToPdf-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}

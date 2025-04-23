---  
title: Verifica se il Codice VBA è Firmato con C++  
linktitle: Verifica se il Codice VBA è Firmato  
type: docs  
weight: 100  
url: /it/cpp/check-if-vba-code-is-signed/  
description: Impara come verificare se il codice VBA nei file Excel è firmato usando Aspose.Cells con C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells consente all’utente di verificare se il progetto VBA è firmato o meno. Usa la proprietà [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/) per controllare se il progetto VBA è firmato o meno.  

{{% /alert %}}  

Il seguente esempio di codice spiega come verificare se il codice VBA è firmato o meno usando la proprietà [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/). Puoi usare uno qualsiasi dei tuoi file Excel per testare questo codice. Per scopi di prova, puoi usare [questo file Excel usato nel codice](5115032.xlsm).  

## **Verifica se il Codice VBA è Firmato in C++**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleVBAProjectSigned.xlsm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Check if the VBA code project is signed
    std::wcout << U"Is VBA Code Project Signed: " << workbook.GetVbaProject().IsSigned() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  

## Output della console  

Di seguito è riportato l'output della console del codice precedente utilizzando il [file Excel di esempio](5115032.xlsm) fornito dal link.  

{{< highlight java >}}  

Is VBA Code Project Signed: True  

{{< /highlight >}}  

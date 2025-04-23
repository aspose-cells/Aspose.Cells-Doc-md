---  
title: Crittografa e decifra file ODS con C++  
linktitle: Crittografa e decritta i file ODS  
type: docs  
weight: 10  
url: /it/cpp/encrypt-and-decrypt-ods-files/  
description: Proteggi con password e cripta file ODS usando Aspose.Cells for C++, che è una libreria C++ pura.  
---  

{{% alert color="primary" %}}  
OpenOffice.org è una suite di ufficio completa che supporta la protezione con password e la crittografia dei file. Tuttavia, un file ODS criptato può essere aperto da OpenOffice solo fornendo la password. Excel non può aprire il file ODS criptato e potrebbe mostrare un messaggio di avviso. Le opzioni di crittografia non sono applicabili ai file ODS a differenza di altri tipi di file.  
Aspose.Cells consente di criptare e decriptare i file ODS. I file ODS decriptati possono essere aperti sia in Excel che in OpenOffice.  
{{% /alert %}}  

## **Crittografa con OpenOffice Calc**  
1. Seleziona **Salva come** e clicca sulla casella **Salva con password**.  
1. Fai clic sul pulsante **Salva**.  
1. Digita la password desiderata nei campi **Inserisci password per aprire** e **Conferma password** nella finestra Imposta password che si apre.  
1. Fare clic sul pulsante **OK** per salvare il file.  

## **Cripta file ODS con Aspose.Cells for C++**  
Per cifrare un file ODS, caricare il file e impostare il valore [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) alla password effettiva prima di salvarlo. Il file ODS cifrato risultante può essere aperto solo con OpenOffice.  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C++

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an ODS file
    Workbook workbook(sourceDir + u"sampleODSFile.ods");

    // Password protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the ODS file
    workbook.Save(outputDir + u"outputEncryptedODSFile.ods");

    std::cout << "ODS file password protected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  

## **Decripta file ODS con Aspose.Cells for C++**  

Per decriptare un file ODS, caricare il file fornendo una password nella proprietà [**LoadOptions.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getpassword/). Una volta caricato il file, impostare la stringa [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) su null.  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the source directory
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an encrypted ODS file
    LoadOptions loadOptions(LoadFormat::Ods);

    // Set original password
    loadOptions.SetPassword(u"1234");

    // Load the encrypted ODS file with the appropriate load options
    Workbook workbook(sourceDir + u"sampleEncryptedODSFile.ods", loadOptions);

    // Set the password to null
    workbook.GetSettings().SetPassword(nullptr);

    // Save the decrypted ODS file
    workbook.Save(outputDir + u"outputDecryptedODSFile.ods");

    std::cout << "Decrypted ODS file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  

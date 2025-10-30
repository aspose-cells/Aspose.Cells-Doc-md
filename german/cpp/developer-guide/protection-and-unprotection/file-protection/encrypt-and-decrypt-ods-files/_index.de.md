---  
title: Verschlüsseln und Entschlüsseln von ODS Dateien mit C++  
linktitle: ODS Dateien verschlüsseln und entschlüsseln  
type: docs  
weight: 10  
url: /de/cpp/encrypt-and-decrypt-ods-files/  
description: Schutzpasswörter und Verschlüsselung von ODS Dateien mit Aspose.Cells for C++, einer reinen C++ Bibliothek.  
---  

{{% alert color="primary" %}}  
OpenOffice.org ist eine voll ausgestattete Office-Suite, die das Passwortschutz und die Verschlüsselung von Dateien unterstützt. Eine verschlüsselte ODS-Datei kann jedoch nur nach Eingabe des Passworts mit OpenOffice geöffnet werden. Excel kann die verschlüsselte ODS-Datei nicht öffnen und eventuell eine Warnmeldung anzeigen. Die Verschlüsselungsoptionen sind für ODS-Dateien im Gegensatz zu anderen Dateitypen nicht anwendbar.  
Aspose.Cells ermöglicht die Verschlüsselung und Entschlüsselung von ODS-Dateien. Entschlüsselte ODS-Dateien können in Excel und OpenOffice geöffnet werden.  
{{% /alert %}}  

## **Mit OpenOffice Calc verschlüsseln**  
1. Wählen Sie **Speichern unter** und aktivieren Sie das Kästchen **Mit Passwort speichern**.  
1. Klicken Sie auf die **Speichern**-Schaltfläche.  
1. Geben Sie Ihr gewünschtes Passwort in die Felder **Kennwort eingeben zum Öffnen** und **Kennwort bestätigen** im Fenster **Passwort festlegen** ein, das geöffnet wird.  
1. Klicken Sie auf die Schaltfläche **OK**, um die Datei zu speichern.  

## **Verschlüsseln Sie die ODS-Datei mit Aspose.Cells for C++**  
Für die Verschlüsselung einer ODS-Datei laden Sie die Datei und setzen Sie den Wert [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) auf das tatsächliche Passwort, bevor Sie sie speichern. Die verschlüsselte Ausgabedatei im ODS-Format kann nur in OpenOffice geöffnet werden.  

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

## **Entschlüsseln Sie die ODS-Datei mit Aspose.Cells for C++**  

Beim Entschlüsseln einer ODS-Datei laden Sie die Datei, indem Sie im [**LoadOptions.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getpassword/)-Eigenschaft ein Passwort angeben. Sobald die Datei geladen ist, setzen Sie den [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/)-String auf null.  

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
{{< app/cells/assistant language="cpp" >}}

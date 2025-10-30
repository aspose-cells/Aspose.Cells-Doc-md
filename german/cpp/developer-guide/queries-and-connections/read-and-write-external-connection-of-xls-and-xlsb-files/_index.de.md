---
title: Lesen und Schreiben externer Verbindungen in XLS und XLSB Dateien mit C++
linktitle: Externe Verbindung von XLS und XLSB Dateien lesen und schreiben
type: docs
weight: 80
url: /de/cpp/read-and-write-external-connection-of-xls-and-xlsb-files/
description: Lernen, wie man externe Datenbankverbindungen in XLS/XLSB Dateien mit Aspose.Cells for C++ liest und ändert.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells for C++ unterstützt das Lesen und Schreiben externer Verbindungen für XLSX-Dateien und erweitert diese Fähigkeit nun auf XLSB- und XLS-Formate. Die gleiche Code-Struktur funktioniert für alle unterstützten Dateitypen.

## **Externe Verbindung von XLS/XLSB-Dateien lesen und schreiben**

Der folgende Beispielcode lädt eine Beispiel-XLSB-Datei (funktioniert auch mit XLS) und ändert ihre erste externe Verbindung (typischerweise eine Microsoft Access-Datenbankverbindung). Der Code zeigt, wie man:

1. Die Tabellenkalkulationsdatei lädt
2. Zugriff auf externe Verbindungen
3. VerbindungsEigenschaften ändert
4. Die geänderte Datei speichert

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **Beispielcode**

Dieser Code funktioniert sowohl für XLSB- als auch für XLS-Dateien, indem die Eingabe-/Ausgabedateierweiterungen angepasst werden.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // File paths
    U16String inputFilePath = srcDir + u"sampleExternalConnection_XLSB.xlsb";
    U16String outputFilePath = outDir + u"outputExternalConnection_XLSB.xlsb";

    // Load source workbook
    Workbook workbook(inputFilePath);

    // Get first external connection
    ExternalConnectionCollection connections = workbook.GetDataConnections();
    DBConnection dbCon = connections.Get(0);

    // Print connection details
    std::cout << "Connection Name: " << dbCon.GetName().ToUtf8() << std::endl;
    std::cout << "Command: " << dbCon.GetCommand().ToUtf8() << std::endl;
    std::cout << "Connection Info: " << dbCon.GetConnectionString().ToUtf8() << std::endl;

    // Modify connection name
    dbCon.SetName(u"NewCust");

    // Save modified workbook
    workbook.Save(outputFilePath);

    std::cout << "External connection updated successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

**C++-Äquivalent:**

```cpp
#include <iostream>
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::ExternalConnections;

int main() {
    Aspose::Cells::Startup();
    // Load source workbook
    Workbook workbook(u"source.xlsb");
    // Access first external connection
    DBConnection conn(workbook.GetDataConnections().Get(0));

    // Output original connection details
    std::cout << "Connection Name: " << conn.GetName().ToUtf8() << std::endl;
    std::cout << "Command: " << conn.GetCommand().ToUtf8() << std::endl;
    std::cout << "Connection Info: " << conn.GetConnectionInfo().ToUtf8() << std::endl;

    // Modify connection name
    conn.SetName(u"Cust_Modified");

    // Save updated workbook
    workbook.Save(u"output.xlsb");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Konsolenausgabe**

{{< highlight cpp >}}
Connection Name: Cust
Command: Customer
Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}

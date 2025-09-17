##Get or Set the Class Identifier of the Embedded OLE Object with C++
Learn how to get or set the class identifier of embedded OLE objects using Aspose.Cells with C++.
## **Possible Usage Scenarios**
Aspose.Cells provides the [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getclassidentifier/) property which you can use to get or set the class identifier of embedded OLE object. OLE Object Class Identifiers are actually GUIDs, i.e., Globally Unique Identifiers. GUID is always 16-bytes long, therefore Class Identifiers are also 16-bytes long. They are often found inside the Windows Registry and provide information to the host application about how to open embedded OLE objects containing various embedded resources inside the client application.
## **Get or Set the Class Identifier of the Embedded OLE Object**
The following screenshot shows the OLE Object Class Identifier, i.e., GUID, which has been read from the [sample excel file](5115190.xls) containing the embedded PowerPoint OLE object.
![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **Sample Code**
Please see the following sample code executed with the [sample excel file](5115190.xls) and its console output which prints the Class Identifier of the OLE Object, i.e., GUID. The printed GUID is exactly the same as shown inside the screenshot.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include <guiddef.h>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
int main()
{
Aspose::Cells::Startup();
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
Workbook wb(srcDir + u"sample.xls");
Worksheet ws = wb.GetWorksheets().Get(0);
OleObject oleObj = ws.GetOleObjects().Get(0);
Vector<uint8_t> classIdentifier = oleObj.GetClassIdentifier();
GUID guid;
memcpy(&guid, classIdentifier.GetData(), sizeof(GUID));
char guidStr[39];
snprintf(guidStr, sizeof(guidStr), "{%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X}",
guid.Data1, guid.Data2, guid.Data3,
guid.Data4[0], guid.Data4[1], guid.Data4[2], guid.Data4[3],
guid.Data4[4], guid.Data4[5], guid.Data4[6], guid.Data4[7]);
std::cout << guidStr << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Console Output**
This is the console output of the above sample code when executed with the [sample excel file](5115190.xls).
DC020317-E6E2-4A62-B9FA-B3EFE16626F4

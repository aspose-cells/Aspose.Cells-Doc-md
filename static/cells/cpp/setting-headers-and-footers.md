##Setting Headers and Footers with C++
This article explains how to programmatically insert an image in the header and footer of Excel worksheets by setting the header and footer with script commands using the C++ API or Library.
Headers and footers are the lines of text displayed below the top margin or above the bottom margin respectively. It's possible to add headers and footers to the worksheets also. Headers and footers can be used to display useful information like page number, author name, topic name, or date and time. Headers and footers are managed using the page setup settings.
## **Setting Headers and Footers**
Aspose.Cells allows you to add headers and footers to worksheets at runtime but we recommend setting headers and footers manually in a pre-designed file for printing. You can use Microsoft Excel as a GUI tool to set headers and footers to save effort and development time. Aspose.Cells can import the file and save the settings.
To add headers and footers at runtime, Aspose.Cells provides special API calls and script commands to format headers and footers.
### **Script Commands**
Script commands are special commands that allow you to set header and footer formatting.
|**Script Commands**|**Description**|
| :- | :- |
|&P|The current page number|
|&G|A picture|
|&N|The total number of pages|
|&D|The current date|
|&T|The current time|
|&A|The worksheet name|
|&F|The file name without its path|
|&&Text|Shows &Text. For example: &&WO will be displayed as &WO|
|&"\<FontName>"|Represents a font name. For example: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Represents font name with style. For example: &"Arial,Bold"|
|&\<FontSize>|Represents font size. For example: “&14abc”. But, if this command is followed by a plain number to be printed in the header, this should be separated with a space character from the font size. For example: “&14 123”.|
### **Set Headers and Footers**
The [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) class provides two methods, [**SetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheader/) and [**SetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooter/), used to add a header and footer to a worksheet. These methods take only two parameters:
- **Section** – the section where the header or footer should be placed. There are three sections: left, center and right, represented by 0, 1 and 2 respectively.
- **Script** – the script to be used for the header or footer. This script contains script commands to format headers or footers.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Create a new workbook
Workbook excel;
// Get the first worksheet's PageSetup
PageSetup pageSetup = excel.GetWorksheets().Get(0).GetPageSetup();
// Set worksheet name at the left section of the header
pageSetup.SetHeader(0, u"&A");
// Set current date and time at the central section of the header with custom font
pageSetup.SetHeader(1, u"&\"Times New Roman,Bold\"&D-&T");
// Set current file name at the right section of the header with custom font
pageSetup.SetHeader(2, u"&\"Times New Roman,Bold\"&12&F");
// Set a string at the left section of the footer with custom font for part of the string
pageSetup.SetFooter(0, u"Hello World! &\"Courier New\"&14 123");
// Set the current page number at the central section of the footer
pageSetup.SetFooter(1, u"&P");
// Set page count at the right section of the footer
pageSetup.SetFooter(2, u"&N");
// Save the workbook
excel.Save(u"SetHeadersAndFooters_out.xls");
Aspose::Cells::Cleanup();
return 0;
}
```
### **Insert an Image into a Header or Footer**
The [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) class has two additional methods, [**SetHeaderPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheaderpicture/) and [**SetFooterPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooterpicture/), used to add pictures into the header and footer. These methods take the parameters:
- **Section** – the header or footer section where the picture will be placed. There are three sections, left, center and right, represented by the values 0, 1 and 2 respectively.
- **Byte array** – the graphical data (the binary data should be written into the buffer of a byte array).
After executing the code below and opening the file, check the header of the worksheet by:
1. On the **File** menu, select **Page Setup**. A dialog will be displayed.
1. Select the **Header/Footer** tab.
```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace std;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
// Creating a Workbook object
Workbook workbook;
// Creating a string variable to store the url of the logo/picture
U16String logo_url = srcDir + u"aspose-logo.jpg";
// Declaring a FileStream object
ifstream inFile;
// Declaring a byte array
vector<uint8_t> binaryData;
// Opening the logo/picture in the stream
inFile.open(logo_url.ToUtf8(), ios::binary);
if (inFile.is_open())
{
// Get the size of the file
inFile.seekg(0, ios::end);
size_t fileSize = inFile.tellg();
inFile.seekg(0, ios::beg);
// Resize the byte array to the size of the file
binaryData.resize(fileSize);
// Read the file into the byte array
inFile.read(reinterpret_cast<char*>(binaryData.data()), fileSize);
// Creating a PageSetup object to get the page settings of the first worksheet of the workbook
PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();
// Convert std::vector to Aspose::Cells::Vector
Aspose::Cells::Vector<uint8_t> asposeBinaryData(binaryData.data(), static_cast<int32_t>(binaryData.size()));
// Setting the logo/picture in the central section of the page header
pageSetup.SetHeaderPicture(1, asposeBinaryData);
// Setting the script for the logo/picture
pageSetup.SetHeader(1, u"&G");
// Setting the Sheet's name in the right section of the page header with the script
pageSetup.SetHeader(2, u"&A");
// Saving the workbook
workbook.Save(outDir + u"InsertImageInHeaderFooter_out.xls");
// Closing the FileStream object
inFile.close();
}
else
{
cerr << "Failed to open the image file." << endl;
}
Aspose::Cells::Cleanup();
return 0;
}
```

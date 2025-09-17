##Insert Background Image to Excel with C++
"How to insert background image to Excel using Aspose.Cells for C++."
You can make a worksheet more appealing by adding a picture as a worksheet background. This feature can be quite effective if you have a special corporate graphic that adds a hint of the background without obscuring the data on the sheet. You can set background picture for a sheet using Aspose.Cells API.
## **Setting Sheet Background in Microsoft Excel**
To set a sheet's background image in Microsoft Excel (for example, Microsoft Excel 2019):
1. From the **Page Layout** menu, find the **Page Setup** option, and then click the **Background** option.
1. Select a picture to set the sheet's background picture.
**Setting a sheet background**
![todo:image_alt_text](insert-background-to-excel.jpg)
## **Setting Sheet Background with Aspose.Cells**
The code below sets a background image using an image from a stream.
```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
Vector<uint8_t> GetDataFromFile(const U16String& file)
{
std::string f = file.ToUtf8();
// open a file
std::ifstream fileStream(f, std::ios::binary);
if (!fileStream.is_open()) {
std::cerr << "Failed to open the file." << std::endl;
return 1;
}
// Get file size
fileStream.seekg(0, std::ios::end);
std::streampos fileSize = fileStream.tellg();
fileStream.seekg(0, std::ios::beg);
// Read file contents into uint8_t array
uint8_t* buffer = new uint8_t[fileSize];
fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
fileStream.close();
Vector<uint8_t>data(buffer, fileSize);
delete[] buffer;
return data;
}
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Create a new Workbook
Workbook workbook;
// Get the first worksheet
Worksheet sheet = workbook.GetWorksheets().Get(0);
Vector<uint8_t> buffer = GetDataFromFile(U16String(u"background.jpg"));
// Set the background image for the worksheet
sheet.SetBackgroundImage(buffer);
// Save the Excel file
workbook.Save(u"outputBackImageSheet.xlsx");
// Save the HTML file
workbook.Save(u"outputBackImageSheet.html", SaveFormat::Html);
std::cout << "Files saved successfully." << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
## Related Articles
- [Working with Background in ODS Files](https://docs.aspose.com/cells/cpp/working-with-background-in-ods-files/)

##Load a Web Image from a URL into an Excel Worksheet with C++
Learn how to convert an image from URL to Excel embedded image using C++ and Aspose.Cells for C++ API.
## Load an Image from a URL into an Excel Worksheet
Aspose.Cells for C++ API provides a straightforward method to load images from URLs into Excel Worksheets. This article explains how to download image data into a memory stream and insert it into the worksheet using Aspose.Cells. The image becomes embedded in the Excel file and doesn't require external downloads when opened.
## Sample Code
```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source and output directories
U16String srcDir(u"../Data/01_SourceDirectory/");
U16String outDir(u"../Data/02_OutputDirectory/");
try
{
// Create a new workbook
Workbook wb;
// Get the first worksheet
WorksheetCollection worksheets = wb.GetWorksheets();
Worksheet sheet = worksheets.Get(0);
// Get the pictures collection
PictureCollection pictures = sheet.GetPictures();
// Insert the picture from local file to B2 cell (row 1, column 1)
// Note: Image file should be pre-downloaded to source directory
U16String imagePath = srcDir + u"aspose-logo.jpg";
pictures.Add(1, 1, imagePath);
// Save the Excel file
wb.Save(outDir + u"webimagebook.out.xlsx");
std::cout << "Image added successfully." << std::endl;
}
catch (const std::exception& ex)
{
std::cerr << "Error: " << ex.what() << std::endl;
return 1;
}
Aspose::Cells::Cleanup();
return 0;
}
```
For scenarios requiring always-updated images from a URL, use the method described in [Insert a Linked Picture from Web Address](https://docs.aspose.com/cells/cpp/insert-a-linked-picture-from-web-address/). This approach loads the image from the URL each time the worksheet is opened.

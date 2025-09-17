##Detect File Format of Encrypted Office Open XML - OOXML Files with C++
Learn how to detect the file format of encrypted Office Open XML (OOXML) files using Aspose.Cells for C++.
**Office Open XML** (also known as **OOXML** or **Microsoft Open XML** (MOX)) is an XML-based file format developed by Microsoft for representing office documents like spreadsheets, charts, presentations, and word processing documents.
Aspose.Cells provides a way to detect the file format of encrypted **Microsoft Open XML** files. To identify the file type, use the [FileFormatUtil.DetectFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) method as shown below in the code example.
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
int main()
{
Aspose::Cells::Startup();
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
U16String filename = srcDir + u"encryptedBook1.out.tmp";
Vector<uint8_t> fileStream = GetDataFromFile(filename);
FileFormatInfo fileFormatInfo = FileFormatUtil::DetectFileFormat(fileStream, u"1234");
std::cout << "File Format: " << static_cast<int>(fileFormatInfo.GetFileFormatType()) << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```

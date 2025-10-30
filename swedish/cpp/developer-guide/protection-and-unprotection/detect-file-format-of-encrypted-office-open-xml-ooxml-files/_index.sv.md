---
title: Upptäck filformat för krypterade Office Open XML  OOXML filer med C++
linktitle: Upptäck filformat för krypterade OOXML filer
type: docs
weight: 340
url: /sv/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Lär dig hur du upptäcker filformat för krypterade Office Open XML (OOXML) filer med Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

**Office Open XML** (även känt som **OOXML** eller **Microsoft Open XML** (MOX)) är ett XML-baserat filformat utvecklat av Microsoft för att representera kontorsdokument som kalkylblad, diagram, presentationer och ordbehandlingsdokument.

{{% /alert %}} 

Aspose.Cells ger en metod för att upptäcka filformat för krypterade **Microsoft Open XML** filer. För att identifiera filtypen, använd metoden [FileFormatUtil.DetectFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) som visas nedan i kodexemplet.

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
{{< app/cells/assistant language="cpp" >}}

---
title: Şifreli Office Open XML  OOXML Dosyalarının Formatını Tespit Edin (C++)
linktitle: Şifreli OOXML Dosya Formatını Tespit Etmek
type: docs
weight: 340
url: /tr/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Aspose.Cells for C++ kullanarak şifreli Office Open XML (OOXML) dosyalarının dosya formatını nasıl tespit edeceğinizi öğrenin.
---

{{% alert color="primary" %}} 

**Office Open XML** (ayrıca **OOXML** veya **Microsoft Open XML** (MOX) olarak da bilinir) Microsoft tarafından ofis belgelerini temsil etmek için geliştirilmiş bir XML tabanlı dosya biçimidir. Aspose.Cells, şifreli **Microsoft Open XML** dosyalarının dosya biçimini algılamak için [FileFormatUtil.DetectFileFormat](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) yöntemini kullanma olanağı sağlar.

{{% /alert %}} 

Aspose.Cells, şifreli **Microsoft Open XML** dosya formatını tespit etmek için bir yol sağlar. Dosya türünü belirlemek için aşağıdaki kod örneğinde gösterildiği gibi [FileFormatUtil.DetectFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) yöntemini kullanın.

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

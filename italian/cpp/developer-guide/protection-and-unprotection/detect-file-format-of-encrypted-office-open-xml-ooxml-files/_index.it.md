---
title: Rileva il formato del file di Office Open XML criptato  OOXML Files con C++
linktitle: Rileva il formato del file di OOXML criptato
type: docs
weight: 340
url: /it/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Scopri come rilevare il formato del file di Office Open XML (OOXML) criptato usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

**Office Open XML** (noto anche come **OOXML** o **Microsoft Open XML** (MOX)) è un formato file basato su XML sviluppato da Microsoft per rappresentare documenti di ufficio come fogli di calcolo, grafici, presentazioni e documenti di elaborazione testi.

{{% /alert %}} 

Aspose.Cells fornisce un metodo per rilevare il formato del file di**Microsoft Open XML** criptato. Per identificare il tipo di file, usa il metodo [FileFormatUtil.DetectFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) come mostrato nell'esempio di codice.

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

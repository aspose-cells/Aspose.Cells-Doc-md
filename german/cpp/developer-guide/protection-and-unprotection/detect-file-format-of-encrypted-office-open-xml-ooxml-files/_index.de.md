---
title: Dateiformat verschlüsselter Office Open XML  OOXML Dateien erkennen mit C++
linktitle: Verschlüsseltes OOXML Dateiformat erkennen
type: docs
weight: 340
url: /de/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Erfahren Sie, wie Sie das Dateiformat verschlüsselter Office Open XML (OOXML) Dateien mit Aspose.Cells for C++ erkennen können.
---

{{% alert color="primary" %}} 

**Office Open XML** (auch bekannt als **OOXML** oder **Microsoft Open XML** (MOX)) ist ein auf XML basierendes Dateiformat, das von Microsoft zur Darstellung von Bürodokumenten wie Tabellenkalkulationen, Diagrammen, Präsentationen und Textverarbeitungsdokumenten entwickelt wurde.

{{% /alert %}} 

Aspose.Cells bietet eine Möglichkeit, das Dateiformat verschlüsselter **Microsoft Open XML**-Dateien zu erkennen. Um den Dateityp zu identifizieren, verwenden Sie die Methode [FileFormatUtil.DetectFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) wie im untenstehenden Codebeispiel gezeigt.

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

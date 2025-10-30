---
title: Detectar formato de archivo de archivos cifrados Office Open XML  OOXML con C++
linktitle: Detectar formato de archivo de archivos OOXML cifrados
type: docs
weight: 340
url: /es/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Aprende cómo detectar el formato de archivo de archivos Office Open XML (OOXML) cifrados usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

**Office Open XML** (también conocido como **OOXML** o **Microsoft Open XML** (MOX)) es un formato de archivo basado en XML desarrollado por Microsoft para representar documentos de oficina como hojas de cálculo, gráficos, presentaciones y documentos de procesamiento de palabras.

{{% /alert %}} 

Aspose.Cells proporciona una forma de detectar el formato de archivo de archivos **Microsoft Open XML** cifrados. Para identificar el tipo de archivo, usa el método [FileFormatUtil.DetectFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) como se muestra en el ejemplo de código.

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

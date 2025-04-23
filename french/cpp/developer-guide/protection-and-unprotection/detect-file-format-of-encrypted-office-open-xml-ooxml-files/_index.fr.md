---
title: Détecter le format de fichier des fichiers OOXML cryptés avec C++
linktitle: Détecter le format de fichier des fichiers OOXML cryptés
type: docs
weight: 340
url: /fr/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Apprenez comment détecter le format de fichier des fichiers Office Open XML (OOXML) cryptés en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

**Office Open XML** (également connu sous le nom **OOXML** ou **Microsoft Open XML** (MOX)) est un format de fichier basé sur XML développé par Microsoft pour représenter des documents de bureau tels que des feuilles de calcul, des graphiques, des présentations et des documents de traitement de texte.

{{% /alert %}} 

Aspose.Cells fournit une méthode pour détecter le format de fichier des fichiers Microsoft Open XML cryptés. Pour identifier le type de fichier, utilisez la méthode [FileFormatUtil.DetectFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) comme illustré dans l'exemple de code ci-dessous.

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

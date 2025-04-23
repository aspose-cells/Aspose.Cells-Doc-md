---
title: Обнаружение формата файла зашифрованных Office Open XML—OOXML файлов с C++
linktitle: Обнаружение формата зашифрованных OOXML файлов
type: docs
weight: 340
url: /ru/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Узнайте, как обнаружить формат файла зашифрованных Office Open XML (OOXML) файлов с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

**Office Open XML** (также известный как **OOXML** или **Microsoft Open XML** (MOX)) - это основанный на XML формат файлов, разработанный Microsoft для представления документов офиса, таких как таблицы, диаграммы, презентации и текстовые документы.

{{% /alert %}} 

Aspose.Cells предоставляет способ определения формата файла зашифрованных **Microsoft Open XML** файлов. Для определения типа файла используйте метод [FileFormatUtil.DetectFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/), приведенный в примере ниже.

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

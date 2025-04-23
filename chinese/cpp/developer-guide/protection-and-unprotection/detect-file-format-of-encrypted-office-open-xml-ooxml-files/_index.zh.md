---
title: 使用 C++ 检测加密的 Office Open XML（OOXML）文件的文件格式
linktitle: 检测加密的 OOXML 文件的文件格式
type: docs
weight: 340
url: /zh/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: 学习如何使用 Aspose.Cells for C++检测加密的 Office Open XML (OOXML) 文件的文件格式。
---

{{% alert color="primary" %}} 

**Office Open XML**（也称为**OOXML**或**Microsoft Open XML**（MOX））是由Microsoft开发的用于表示办公文档的基于XML的文件格式，如电子表格、图表、演示文稿和文字处理文档。

{{% /alert %}} 

 Aspose.Cells 提供检测加密 **Microsoft Open XML** 文件格式的方法。要识别文件类型，请使用 [FileFormatUtil.DetectFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) 方法，如下示例中的代码所示。

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

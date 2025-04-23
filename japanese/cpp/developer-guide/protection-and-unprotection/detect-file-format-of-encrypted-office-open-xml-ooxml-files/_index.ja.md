---
title: 暗号化されたOffice Open XML（OOXML）ファイルのフォーマット検出（C++）
linktitle: 暗号化されたOOXMLファイルのフォーマットを検出します。
type: docs
weight: 340
url: /ja/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Aspose.Cells for C++を使用して暗号化されたOffice Open XML（OOXML）ファイルのファイル形式を検出する方法を学びます。
---

{{% alert color="primary" %}} 

**Office Open XML** （または**OOXML**、**Microsoft Open XML**（MOX）としても知られる）は、Microsoftによって開発されたXMLベースのファイル形式で、スプレッドシート、チャート、プレゼンテーション、ワード処理などのオフィスドキュメントを表現するために使用されます。

{{% /alert %}} 

Aspose.Cellsは、暗号化された**Microsoft Open XML**ファイルのファイル形式を検出する方法を提供します。ファイルタイプを識別するには、以下のコード例に示すように[FileFormatUtil.DetectFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/)メソッドを使用します。

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

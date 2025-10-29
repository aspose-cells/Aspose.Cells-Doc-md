---
title: الكشف عن تنسيق ملف ملفات Office المشفرة  ملفات OOXML باستخدام C++
linktitle: الكشف عن تنسيق ملف الملفات ذات صيغة OOXML المشفرة
type: docs
weight: 340
url: /ar/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: تعلم كيفية اكتشاف تنسيق ملفات Office Open XML المشفرة باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

**ملفات Office Open XML** (المعروفة أيضًا بـ **OOXML** أو **Microsoft Open XML (MOX)**) هي تنسيق ملفات مستند XML المعتمد من Microsoft لتمثيل المستندات الإدارية مثل جداول البيانات والرسوم البيانية والعروض التقديمية ومستندات معالجة النصوص.

{{% /alert %}} 

يوفر Aspose.Cells طريقة لكشف تنسيق ملفات **مايكروسوفت أوفيس أوتوماتيك** المشفرة. لتحديد نوع الملف، استخدم طريقة [FileFormatUtil.DetectFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) كما هو موضح في المثال التالي في الكود.

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

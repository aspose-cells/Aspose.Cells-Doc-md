---
title: 用C++向Excel插入背景图片
linktitle: 将背景图像插入Excel
type: docs
weight: 90
url: /zh/cpp/insert-background-image-to-excel/
description: “如何用Aspose.Cells for C++向Excel插入背景图片。”
---

{{% alert color="primary" %}} 

通过添加图片作为工作表背景，你可以使工作表更具吸引力。如果你有一个特殊的公司图形，它可以在不遮挡工作表数据的情况下为背景增添一丝色彩。你可以使用Aspose.Cells API设置工作表的背景图片。

{{% /alert %}} 

## **在Microsoft Excel中设置工作表背景**

在Microsoft Excel（例如Microsoft Excel 2019）中设置工作表的背景图片：

1. 从**页面布局**菜单中找到**页面设置**选项，然后点击**背景**选项。
1. 选择一张图片来设置工作表的背景图片。

   **设置工作表背景**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **使用Aspose.Cells设置工作表背景**

下面的代码使用从流中读取的图像设置了一个背景图像。

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

using namespace Aspose::Cells;

int main()
{
	Aspose::Cells::Startup();

	// Create a new Workbook
	Workbook workbook;

	// Get the first worksheet
	Worksheet sheet = workbook.GetWorksheets().Get(0);

	Vector<uint8_t> buffer = GetDataFromFile(U16String(u"background.jpg"));

	// Set the background image for the worksheet
	sheet.SetBackgroundImage(buffer);

	// Save the Excel file
	workbook.Save(u"outputBackImageSheet.xlsx");

	// Save the HTML file
	workbook.Save(u"outputBackImageSheet.html", SaveFormat::Html);

	std::cout << "Files saved successfully." << std::endl;

	Aspose::Cells::Cleanup();
	return 0;
}
```

## 相关文章

- [在ODS文件中处理背景](/cells/zh/cpp/working-with-background-in-ods-files/)

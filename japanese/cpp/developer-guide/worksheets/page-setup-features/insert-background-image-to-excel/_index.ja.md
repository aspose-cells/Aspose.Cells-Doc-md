---
title: C++でExcelに背景画像を挿入
linktitle: Excelに背景画像を挿入する
type: docs
weight: 90
url: /ja/cpp/insert-background-image-to-excel/
description: 「Aspose.Cells for C++を使用してExcelに背景画像を挿入する方法」。
---

{{% alert color="primary" %}} 

特別な要素がシート上のデータを遮らずに背景のヒントを追加する特別な企業図形がある場合、これはワークシートをより魅力的にすることができます。Aspose.Cells APIを使用して、シートの背景画像を追加することができます。

{{% /alert %}} 

## **Microsoft Excelでのシートの背景の設定方法（例：Microsoft Excel 2019）：**

1. **ページレイアウト**メニューから**ページの設定**オプションを見つけ、**背景**オプションをクリックします。

1. **ページレイアウト**メニューから**ページ設定**オプションを見つけ、**背景**オプションをクリックします。
1. シートの背景画像を設定するために画像を選択します。

   シートの背景を設定する

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Aspose.Cellsを使用してシートの背景を設定する**

以下のコードは、ストリームから画像を使用して背景画像を設定します。

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

## 関連記事

- [ODSファイルで背景を操作する](/cells/ja/cpp/working-with-background-in-ods-files/)
{{< app/cells/assistant language="cpp" >}}

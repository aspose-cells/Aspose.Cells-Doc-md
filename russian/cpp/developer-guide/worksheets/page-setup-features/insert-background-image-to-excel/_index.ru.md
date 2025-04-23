---
title: Добавить фоновое изображение в Excel с помощью C++
linktitle: Вставить фоновое изображение в Excel
type: docs
weight: 90
url: /ru/cpp/insert-background-image-to-excel/
description: "Как вставить фоновое изображение в Excel с использованием Aspose.Cells for C++."
---

{{% alert color="primary" %}} 

Вы можете сделать лист более привлекательным, добавив изображение в качестве фонового изображения рабочего листа. Эта функция может быть довольно эффективной, если у вас есть специальная корпоративная графика, которая добавляет намек на фон, не заслоняя данные на листе. Вы можете установить фоновое изображение для листа с помощью API Aspose.Cells.

{{% /alert %}} 

## **Установка фонового изображения на листе в Microsoft Excel**

Чтобы установить фоновое изображение листа в Microsoft Excel (например, Microsoft Excel 2019):

1. Из меню **Макет страницы** найдите опцию **Настройка страницы**, затем щелкните опцию **Фон**.
1. Выберите изображение для установки фонового изображения листа.

   **Установка фона листа**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Установка фонового изображения с помощью Aspose.Cells**

Приведенный ниже код устанавливает фоновое изображение с использованием изображения из потока.

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

## Связанные статьи

- [Работа с фоном в файлах ODS](/cells/ru/cpp/working-with-background-in-ods-files/)

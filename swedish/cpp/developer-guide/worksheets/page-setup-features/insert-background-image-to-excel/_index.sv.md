---
title: Infoga bakgrundsbild i Excel med C++
linktitle: Infoga bakgrundsbild i Excel
type: docs
weight: 90
url: /sv/cpp/insert-background-image-to-excel/
description: "Hur man infogar bakgrundsbild till Excel med Aspose.Cells for C++."
---

{{% alert color="primary" %}} 

Du kan göra ett kalkylblad mer lockande genom att lägga till en bild som bakgrund. Denna funktion kan vara ganska effektiv om du har en speciell företagsgrafik som lägger till en antydan till bakgrunden utan att dölja data på bladet. Du kan ange bakgrundsbild för ett blad med Aspose.Cells API.

{{% /alert %}} 

## **Ange bakgrund på kalkylblad i Microsoft Excel**

För att ange ett kalkylblads bakgrundsbild i Microsoft Excel (t.ex. Microsoft Excel 2019):

1. Från menyn **Sidlayout**, hitta alternativet **Sidlayout** och klicka sedan på alternativet **Bakgrund**.
1. Välj en bild för att sätta kalkylbladets bakgrundsbild.

   **Ange en ark-bakgrund**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Ange bakgrundsbild med Aspose.Cells**

Koden nedan ställer in en bakgrundsbild med en bild från en ström.

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

## Relaterade artiklar

- [Arbeta med bakgrund i ODS-filer](/cells/sv/cpp/working-with-background-in-ods-files/)

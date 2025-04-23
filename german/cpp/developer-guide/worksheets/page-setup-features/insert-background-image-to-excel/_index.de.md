---
title: Hintergrundbild in Excel mit C++ einfügen
linktitle: Hintergrundbild in Excel einfügen
type: docs
weight: 90
url: /de/cpp/insert-background-image-to-excel/
description: „Wie man mit Aspose.Cells for C++ ein Hintergrundbild in Excel einfügt.“
---

{{% alert color="primary" %}} 

Sie können ein Arbeitsblatt attraktiver gestalten, indem Sie ein Bild als Hintergrundbild hinzufügen. Diese Funktion kann sehr effektiv sein, wenn Sie eine spezielle Unternehmensgrafik haben, die einen Hauch des Hintergrunds hinzufügt, ohne die Daten auf dem Blatt zu verdecken. Sie können mithilfe der Aspose.Cells-API ein Hintergrundbild für ein Blatt festlegen.

{{% /alert %}} 

## **Blatthintergrund in Microsoft Excel festlegen**

Um ein Hintergrundbild für ein Blatt in Microsoft Excel festzulegen (z. B. Microsoft Excel 2019):

1. Wählen Sie im Menü **Seitenlayout** die Option **Seiteneinrichtung** und anschließend die Option **Hintergrund**.
1. Wählen Sie ein Bild aus, um das Hintergrundbild des Blatts festzulegen.

   **Festlegen eines Blatthintergrunds**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Blatthintergrund mit Aspose.Cells festlegen**

Der unten stehende Code legt ein Hintergrundbild mithilfe eines Bildes aus einem Stream fest.

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

## Verwandte Artikel

- [Arbeiten mit Hintergründen in ODS-Dateien](/cells/de/cpp/working-with-background-in-ods-files/)

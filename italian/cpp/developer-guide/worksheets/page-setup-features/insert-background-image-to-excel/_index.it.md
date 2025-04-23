---
title: Inserire immagine di sfondo in Excel con C++
linktitle: Inserire un immagine di sfondo in Excel
type: docs
weight: 90
url: /it/cpp/insert-background-image-to-excel/
description: "Come inserire un immagine di sfondo in Excel usando Aspose.Cells for C++."
---

{{% alert color="primary" %}} 

Puoi rendere un foglio di lavoro più accattivante aggiungendo un'immagine come sfondo del foglio. Questa funzionalità può essere molto efficace se hai una grafica aziendale speciale che aggiunge un tocco di sfondo senza oscurare i dati nel foglio. Puoi impostare l'immagine di sfondo per un foglio utilizzando l'API Aspose.Cells.

{{% /alert %}} 

## **Impostare lo sfondo del foglio in Microsoft Excel**

Impostare un'immagine di sfondo di un foglio in Microsoft Excel (ad esempio, Microsoft Excel 2019):

1. Dal menu **Layout di pagina**, individuare l'opzione **Imposta pagina** e fare clic sull'opzione **Sfondo**.
1. Seleziona un'immagine da impostare come sfondo del foglio.

   **Impostazione di uno sfondo del foglio**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Impostare lo sfondo del foglio con Aspose.Cells**

Il codice di seguito imposta un'immagine di sfondo utilizzando un'immagine da un flusso.

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

## Articoli correlati

- [Lavorare con lo sfondo nei file ODS](/cells/it/cpp/working-with-background-in-ods-files/)

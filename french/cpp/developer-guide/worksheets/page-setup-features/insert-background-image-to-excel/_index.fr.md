---
title: Insérer une image d arrière plan dans Excel avec C++
linktitle: Insérer une image d arrière plan dans Excel
type: docs
weight: 90
url: /fr/cpp/insert-background-image-to-excel/
description: "Comment insérer une image d arrière plan dans Excel en utilisant Aspose.Cells for C++."
---

{{% alert color="primary" %}} 

Vous pouvez rendre une feuille de calcul plus attrayante en ajoutant une image en arrière-plan. Cette fonctionnalité peut être très efficace si vous avez une illustration graphique d'entreprise spéciale qui ajoute une touche de fond sans obscurcir les données sur la feuille. Vous pouvez configurer une image d'arrière-plan pour une feuille à l'aide de l'API Aspose.Cells.

{{% /alert %}} 

## **Configuration de l'arrière-plan de la feuille dans Microsoft Excel**

Pour définir une image d'arrière-plan de la feuille dans Microsoft Excel (par exemple, Microsoft Excel 2019) :

1. Dans le menu **Mise en page**, recherchez l'option **Configuration de la page**, puis cliquez sur l'option **Arrière-plan**.
1. Sélectionnez une image pour définir l'arrière-plan de la feuille.

   **Configuration d'un arrière-plan de feuille**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Configuration de l'arrière-plan de la feuille avec Aspose.Cells**

Le code ci-dessous définit une image d'arrière-plan à l'aide d'une image provenant d'un flux.

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

## Articles Connexes

- [Travailler avec l'arrière-plan dans les fichiers ODS](/cells/fr/cpp/working-with-background-in-ods-files/)

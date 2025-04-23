---
title: Insertar imagen de fondo en Excel con C++
linktitle: Insertar imagen de fondo en Excel
type: docs
weight: 90
url: /es/cpp/insert-background-image-to-excel/
description: "Cómo insertar imagen de fondo en Excel usando Aspose.Cells for C++."
---

{{% alert color="primary" %}} 

Puede hacer que una hoja de cálculo sea más atractiva agregando una imagen como fondo de la hoja. Esta función puede ser muy efectiva si tiene un gráfico corporativo especial que agrega un toque del fondo sin ocultar los datos en la hoja. Puede establecer una imagen de fondo para una hoja utilizando la API de Aspose.Cells.

{{% /alert %}} 

## **Establecer fondo de hoja en Microsoft Excel**

Para establecer una imagen de fondo de hoja en Microsoft Excel (por ejemplo, Microsoft Excel 2019):

1. Desde el menú **Diseño de página**, encontrar la opción **Configurar página**, y luego hacer clic en la opción **Fondo**.
1. Seleccionar una imagen para establecer la imagen de fondo de la hoja.

   **Establecer un fondo de hoja**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Establecer fondo de hoja con Aspose.Cells**

El código a continuación establece una imagen de fondo utilizando una imagen de un flujo.

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

## Artículos relacionados

- [Trabajar con fondo en archivos ODS](/cells/es/cpp/working-with-background-in-ods-files/)

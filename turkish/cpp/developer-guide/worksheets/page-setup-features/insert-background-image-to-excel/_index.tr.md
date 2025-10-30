---
title: Excel e Arka Plan Resmi Ekleme (C++ ile)
linktitle: Excel e Arka Plan Görüntüsü Ekleme
type: docs
weight: 90
url: /tr/cpp/insert-background-image-to-excel/
description: "Aspose.Cells for C++ kullanarak Excel e arka plan resmi nasıl eklenir."
---

{{% alert color="primary" %}} 

Bir çalışma sayfasına resim ekleyerek çalışma sayfasını daha çekici hale getirebilirsiniz. Bu özellik, çalışma sayfasındaki verileri engellemeden arka plana hafif bir ipucu ekleyen özel bir kurumsal grafik veya resminiz varsa oldukça etkili olabilir. Aspose.Cells API'sini kullanarak bir sayfa için arka plan resmi ayarlayabilirsiniz.

{{% /alert %}} 

## **Microsoft Excel'de Sayfa Arka Planını Ayarlama**

Microsoft Excel'de bir sayfanın arka plan görüntüsünü ayarlamak için (örneğin, Microsoft Excel 2019 için):

1. **Sayfa Düzeni** menüsünden **Sayfa Ayarı** seçeneğini bulun ve ardından **Arka Plan** seçeneğine tıklayın.
1. Tablonun arka plan resmini ayarlamak için bir resim seçin.

   **Tablo arka planı ayarlama**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Aspose.Cells ile Sayfa Arka Planı Ayarlama**

Aşağıdaki kod, bir akıştaki bir resim kullanarak arka plan resmini ayarlar.

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

## İlgili Makaleler

- [ODS Dosyalarında Arkaplanla Çalışma](/cells/tr/cpp/working-with-background-in-ods-files/)
{{< app/cells/assistant language="cpp" >}}

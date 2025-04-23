---
title: إضافة صورة خلفية إلى Excel باستخدام C++
linktitle: إدراج صورة خلفية إلى إكسل
type: docs
weight: 90
url: /ar/cpp/insert-background-image-to-excel/
description: كيف تدخل صورة خلفية إلى Excel باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

يمكنك تحسين جاذبية ورقة العمل عن طريق إضافة صورة كخلفية. يمكن أن يكون هذا الميزة فعالًا إذا كان لديك صورة توضيحية خاصة للشركة تضيف لمسة من الخلفية دون حجب البيانات على الورقة. يمكنك تعيين صورة خلفية لورقة باستخدام واجهة برمجة التطبيقات Aspose.Cells.

{{% /alert %}} 

## **تعيين خلفية الورقة في Microsoft Excel**

لتعيين صورة خلفية لورقة في Microsoft Excel (على سبيل المثال، Microsoft Excel 2019):

1. من القائمة **تخطيط الصفحة**، ابحث عن خيار **إعداد الصفحة**، ثم انقر فوق خيار **الخلفية**.
1. حدد صورة لتعيين صورة خلفية للورقة.

   **تعيين خلفية لورقة**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **تعيين خلفية الورقة باستخدام Aspose.Cells**

يقوم الكود أدناه بتعيين صورة خلفية باستخدام صورة من مصدر بيانات.

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

## مقالات ذات صلة

- [العمل مع الخلفية في ملفات ODS](/cells/ar/cpp/working-with-background-in-ods-files/)

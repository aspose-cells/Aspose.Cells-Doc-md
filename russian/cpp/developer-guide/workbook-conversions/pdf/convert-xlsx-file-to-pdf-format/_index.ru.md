---
title: Конвертация файла XLSX в PDF на C++
linktitle: Преобразовать файл XLSX в формат PDF
type: docs
weight: 30
url: /ru/cpp/convert-xlsx-file-to-pdf-format/
description: Узнайте, как преобразовать файлы Excel в PDF с высокой точностью и аккуратностью, используя Aspose.Cells for C++.
---

{{% alert color="primary" %}}

PDF (Portable Document Format) представляет документы независимо от используемого программного обеспечения, аппаратных средств и операционной системы. PDF-файл может содержать любой набор текста, графики и изображений в независимом от устройства и разрешения виде. PDF-файлы часто сжимаются, что уменьшает их размер по сравнению с исходным файлом.

Иногда нужно конвертировать файл Microsoft Excel в PDF. Для этого требуется быстрое, безопасное, точное и надежное решение, которое позволяет распространять PDF-документы по всему миру. Существует множество инструментов для конвертации, которые могут выполнить эту задачу. Однако необходимо убедиться, что макет исходного документа Excel сохраняется в выходном PDF-файле. Изображения, графики, фигуры, форматирование данных, шрифты, атрибуты, цвета, настройки страницы, ориентация текста, границы, графики и т.д. должны отображаться точно и аккуратно. [Aspose.Cells](https://products.aspose.com/cells/cpp/) обеспечивает высокое качество конвертации.

Этот документ предназначен для всестороннего понимания того, как можно преобразовать документ Microsoft Excel (с изображениями, графиками, форматированием и т.д.) в PDF. В нем показано, как создать простое консольное приложение на C++, которое конвертирует файл Excel в PDF с помощью API Aspose.Cells. Конвертация выполняется с высокой точностью и аккуратностью.

{{% /alert %}}

## **Преобразование Excel в PDF**

Этот пример использует файл Excel (SampleInput.xlsx) в качестве шаблона. Рабочая книга содержит листы с графиками и изображениями. Каждый лист содержит разные типы форматирования с использованием шрифтов, атрибутов, цветов, эффектов затенения и границ. На первом листе есть столбчатая диаграмма, а на последнем — изображение.

### **Файл шаблона Excel**

Файл шаблона содержит три листа, включая графики и изображения в разделе Media. Первый лист содержит графики, а последний — изображение, как показано на скриншотах.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Первый лист **(Прогноз продаж)**|Второй лист **(Отчет о продажах)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Третий лист **(Ввод данных)**|Последний лист **(Изображение)**|

### **Процесс конвертации**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    try
    {
        // Get the template excel file path
        U16String designerFile = srcDir + u"SampleInput.xlsx";

        // Specify the pdf file path
        U16String pdfFile = outDir + u"Output.out.pdf";

        // Open the template excel file
        Workbook wb(designerFile);

        // Save the pdf file
        wb.Save(pdfFile, SaveFormat::Pdf);

        std::cout << "PDF file saved successfully!" << std::endl;
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Если в таблице есть формулы, лучше всего вызвать метод [Workbook.CalculateFormula](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) непосредственно перед преобразованием книги в PDF. Это гарантирует перерасчет значений, зависящих от формул, и правильное отображение их в PDF.

{{% /alert %}}

### **Результат**

После выполнения вышеуказанного кода создается PDF-файл в папке Files в вашем каталоге приложения.
Следующие скриншоты показывают страницы PDF. Обратите внимание, что в выходном PDF-файле также сохранены заголовки и нижние колонтитулы.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Первый лист **(Прогноз продаж)**|Второй лист **(Отчет о продажах)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Третий лист **(Ввод данных)**|Последний лист **(Изображение)**|
{{< app/cells/assistant language="cpp" >}}

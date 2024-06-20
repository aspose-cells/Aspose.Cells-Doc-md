---
title: Преобразование книги Excel в PDF
type: docs
weight: 80
url: /ru/cpp/convert-excel-workbook-to-pdf/
---

## **Преобразование книги Excel в PDF**
Файлы PDF широко используются для обмена документами между организациями, государственными секторами и физическими лицами. Это стандартный формат документа, и разработчиков программного обеспечения часто просят найти способ преобразовать файлы Microsoft Excel в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и поддерживает высокую визуальную точность при преобразовании.

{{% alert color="primary" %}} 

Aspose.Cells напрямую записывает информацию о версии API и номере версии в выходных документах. Например, при рендеринге документа в PDF, Aspose.Cells for C++ заполняет поле **Приложение** значением 'Aspose.Cells' и поле **PDF-производитель** значением 'Aspose.Cells v18.5.0'.

Обратите внимание, что вы не можете указать Aspose.Cells for C++ изменить или удалить эту информацию из выходных документов.

{{% /alert %}} 
### **Прямое преобразование**
Aspose.Cells поддерживает конвертацию из электронных таблиц в формат PDF независимо от другого программного обеспечения. Просто сохраните файл Excel в формат PDF, используя метод [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) класса [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Метод [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) предоставляет член перечисления [SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/), который преобразует исходные файлы Excel в формат PDF.

Следуйте нижеприведенным шагам, чтобы непосредственно преобразовать электронные таблицы Excel в формат PDF:

1. Создайте объект класса [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) вызовом его пустого конструктора.
1. Вы можете открыть/загрузить существующий файл шаблона, или пропустить этот шаг, если создаете книгу из нуля.
1. Выполните любую работу (ввод данных, применение форматирования, задание формул, вставка изображений или других объектов рисования и т. д.) на электронной таблице, используя API Aspose.Cells.
1. Когда код электронной таблицы завершен, вызовите метод [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) класса [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), чтобы сохранить электронную таблицу.

Формат файла должен быть PDF, поэтому выберите соответствующий PDF (заранее определенное значение) из перечисления SaveFormat для создания окончательного документа в формате PDF.

Пожалуйста, ознакомьтесь с примером кода, его [образцом файла Excel](67338368.xlsx) и [выходным PDF](67338369.pdf) для вашего справочного руководства.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
### **Расширенное преобразование**
Вы также можете использовать класс [PdfSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) для установки различных атрибутов конвертации. Установка различных свойств класса **PdfSaveOptions** дает вам контроль над настройками печати, шрифтов, защиты и сжатия для выходного PDF. Самое важное свойство - [SetCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/), позволяющее сохранять файлы Excel в формате PDF/A совместимых PDF-файлов.
#### **Сохранение книги в формате PDF/A**
В следующем фрагменте кода демонстрируется использование класса **PdfSaveOptions** для сохранения файлов Excel в формате PDF/A совместимого PDF.

Пожалуйста, ознакомьтесь с примером кода и его [выходным PDF](67338370.pdf) для вашего справочного руководства.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
#### **Установить время создания PDF**
С классом **IPdfSaveOptions** вы можете получить или установить время создания PDF.

Пожалуйста, ознакомьтесь с примером кода и его [выходным PDF](67338371.pdf) для вашего справочного руководства.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}

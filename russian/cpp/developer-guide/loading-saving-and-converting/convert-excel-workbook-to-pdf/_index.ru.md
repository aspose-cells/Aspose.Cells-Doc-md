---
title: Преобразовать книгу Excel в PDF
type: docs
weight: 80
url: /ru/cpp/convert-excel-workbook-to-pdf/
---
##  **Преобразование книги Excel в PDF**
Файлы PDF широко используются для обмена документами между организациями, государственными секторами и частными лицами. Это стандартный формат документов, и разработчиков программного обеспечения часто просят найти способ конвертировать файлы Excel Microsoft в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и обеспечивает высокую визуальную точность преобразования.

{{% alert color="primary" %}} 

 Aspose.Cells напрямую записывает информацию о API и номере версии в выходные документы. Например, при рендеринге документа на номер PDF, Aspose.Cells for C++ заполняет**Приложение** поле со значением «Aspose.Cells» и**PDF Производитель** поле со значением, например, «Aspose.Cells v18.5.0».

Обратите внимание, что вы не можете дать указание Aspose.Cells for C++ изменить или удалить эту информацию из выходных документов.

{{% /alert %}} 
###  **Прямое преобразование**
Aspose.Cells поддерживает преобразование электронных таблиц в PDF независимо от другого программного обеспечения. Просто сохраните файл Excel по адресу PDF, используя[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)сорт'[Сохранять](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)метод.[Сохранять](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)метод обеспечивает[SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)член перечисления, преобразующий собственные файлы Excel в формат PDF.

Выполните следующие шаги, чтобы напрямую преобразовать таблицы Excel в формат PDF:

1.  Создать экземпляр объекта[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)класс, вызвав его пустой конструктор.
1. Вы можете открыть/загрузить существующий файл шаблона или пропустить этот шаг, если создаете книгу с нуля.
1. Выполняйте любую работу (ввод данных, применение форматирования, установку формул, вставку изображений или других объектов рисования и т. д.) в электронной таблице с помощью API-интерфейсов Aspose.Cells'.
1.  Когда код электронной таблицы будет готов, вызовите[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)сорт'[Сохранять](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)метод сохранения таблицы.

Формат файла должен быть PDF, поэтому выберите соответствующий PDF (предварительно определенное значение) из перечисления SaveFormat, чтобы сгенерировать окончательный документ PDF.

 См. следующий пример кода, его[образец файла Excel](67338368.xlsx) и[вывод PDF](67338369.pdf) для вашей справки.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
###  **Расширенное преобразование**
Вы также можете использовать[PDFSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)class для установки различных атрибутов для преобразования. Установка различных свойств**PDFSaveOptions** Класс дает вам контроль над настройками печати, шрифта, безопасности и сжатия для вывода PDF. Наиболее важным свойством является[УстановитьСоответствие](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/)что позволяет сохранять файлы Excel в файлы PDF, соответствующие стандарту PDF/A.
####  **Сохранение книги в файлах, соответствующих PDF/A**
Следующий фрагмент кода демонстрирует, как использовать**PDFSaveOptions**класс для сохранения файлов Excel в формате PDF, совместимом с PDF/A.

 Пожалуйста, ознакомьтесь со следующим примером кода и его[вывод PDF](67338370.pdf) для вашей справки.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
####  **Установите время создания PDF.**
С**IPdfSaveOptions** class, вы можете получить или установить время создания PDF.

 Пожалуйста, ознакомьтесь со следующим примером кода и его[вывод PDF](67338371.pdf) для вашей справки.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}

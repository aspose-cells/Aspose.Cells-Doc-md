---
title: Конвертировать книгу Excel в PDF
type: docs
weight: 80
url: /ru/cpp/convert-excel-workbook-to-pdf/
---
## **Преобразование книги Excel в PDF**
Файлы PDF широко используются для обмена документами между организациями, государственными секторами и отдельными лицами. Это стандартный формат документов, и разработчиков программного обеспечения часто просят найти способ конвертировать Microsoft файлы Excel в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и обеспечивает высокую визуальную точность преобразования.

{{% alert color="primary" %}} 

 Aspose.Cells напрямую записывает информацию о API и номере версии в выходные документы. Например, при преобразовании документа в PDF Aspose.Cells вместо C++ заполняет**Заявление** поле со значением «Aspose.Cells» и**PDF-продюсер**поле со значением, например 'Aspose.Cells v18.5.0'.

Обратите внимание, что вы не можете поручить Aspose.Cells для C++ изменить или удалить эту информацию из выходных документов.

{{% /alert %}} 
### **Прямое преобразование**
Aspose.Cells поддерживает преобразование электронных таблиц в PDF независимо от другого программного обеспечения. Просто сохраните файл Excel в PDF, используя[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)учебный класс'[Сохранять](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)метод.[Сохранять](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)метод обеспечивает[СохранитьФормат_Pdf](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)член перечисления, который преобразует собственные файлы Excel в формат PDF.

Выполните следующие шаги, чтобы напрямую преобразовать электронные таблицы Excel в формат PDF:

1.  Создать экземпляр объекта[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)class, вызвав его пустой конструктор.
1. Вы можете открыть/загрузить существующий файл шаблона или пропустить этот шаг, если создаете книгу с нуля.
1. Выполняйте любую работу (ввод данных, применение форматирования, установка формул, вставка рисунков или других объектов рисования и т. д.) в электронной таблице с помощью API-интерфейсов Aspose.Cells'.
1. Когда код электронной таблицы будет готов, вызовите[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)учебный класс'[Сохранять](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)метод сохранения таблицы.

Формат файла должен быть PDF, поэтому выберите соответствующий PDF (заранее определенное значение) из перечисления SaveFormat, чтобы создать окончательный PDF-документ.

 См. следующий пример кода, его[образец файла Excel](67338368.xlsx) а также[вывод PDF](67338369.pdf) для вашей справки.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion.cpp" >}}
### **Расширенное преобразование**
Вы также можете выбрать использование[IPdfSaveOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options)класс для установки различных атрибутов для преобразования. Установка различных свойств**IPdfSaveOptions** class дает вам контроль над настройками печати, шрифта, безопасности и сжатия для выходного PDF. Наиболее важным свойством является[СетСоответствие](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options#a2158ff23d7c071f8224b1cd063233c07)который позволяет сохранять файлы Excel в PDF-файлы, совместимые с PDF/A.
#### **Сохранение рабочей книги в файлах PDF/A Complied**
В следующем фрагменте кода показано, как использовать**IPdfSaveOptions**класс для сохранения файлов Excel в формате PDF, совместимом с PDF/A

 См. следующий пример кода и его[вывод PDF](67338370.pdf) для вашей справки.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles.cpp" >}}
#### **Установите время создания PDF**
С**IPdfSaveOptions** class вы можете получить или установить время создания PDF.

 См. следующий пример кода и его[вывод PDF](67338371.pdf) для вашей справки.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime.cpp" >}}

---
title: Управление таблицами
type: docs
weight: 20
url: /ru/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

Разработчики могут легко создавать листы в файлах Excel Microsoft и управлять ими программно с помощью гибкого API Aspose.Cells. В этом разделе описаны подходы к добавлению и удалению листов в файлах Excel Microsoft.

{{% /alert %}} 

 Aspose.Cells предоставляет класс[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) который представляет файл Excel.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)коллекция, которая обеспечивает доступ к каждому листу в файле Excel.

Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт.[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Класс предоставляет широкий спектр методов для управления рабочими листами.
##  **Добавление листов в новый файл Excel**
Чтобы создать новый файл Excel программным способом:

1.  Создайте объект[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)сорт.
1.  Позвоните в[Добавлять](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) метод[Рабочий ЛистКоллекция](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) коллекция. Пустой лист автоматически добавляется в файл Excel. На него можно ссылаться, передав индекс нового рабочего листа в метод[Рабочий ЛистКоллекция](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)коллекция.
1. Получите ссылку на рабочий лист.
1. Выполните работу по рабочим листам.
1. Сохраните новый файл Excel с новыми листами, вызвав метод[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) сорт[Сохранять](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)метод.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
##  **Доступ к листам с помощью индекса листов**
В следующем примере кода показано, как получить доступ к любому листу или получить его, указав его индекс.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
##  **Удаление листов с помощью индекса листов**
 Удаление листов по имени хорошо работает, если имя листа известно. Если вы не знаете имя листа, используйте перегруженную версию[Удалитьат](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat)метод, который принимает индекс листа вместо имени листа.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}

---
title: Управление рабочими листами
type: docs
weight: 20
url: /ru/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

Разработчики могут легко создавать рабочие листы в файлах Excel Microsoft и управлять ими программно, используя Aspose.Cells гибкий API. В этом разделе описываются подходы к добавлению и удалению рабочих листов в файлах Excel Microsoft.

{{% /alert %}} 

 Aspose.Cells предоставляет класс[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) который представляет файл Excel.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс.[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)Класс предоставляет широкий спектр методов для управления рабочими листами.
## **Добавление рабочих листов в новый файл Excel**
Чтобы создать новый файл Excel программно:

1.  Создайте объект из[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)учебный класс.
1.  Позвоните[Добавлять](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa2bb166f57a4d8eba8e25ce1f99d0c55) метод[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) коллекция. Пустой рабочий лист автоматически добавляется в файл Excel. На него можно сослаться, передав индекс листа нового рабочего листа в[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)коллекция.
1. Получите ссылку на рабочий лист.
1. Выполнить работу с рабочими листами.
1.  Сохраните новый файл Excel с новыми рабочими листами, вызвав[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) учебный класс[Сохранять](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)метод.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile.cpp" >}}
## **Доступ к рабочим листам с помощью индекса листов**
В следующем примере кода показано, как получить доступ к любому рабочему листу, указав его индекс.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex.cpp" >}}
## **Удаление рабочих листов с помощью индекса листов**
 Удаление рабочих листов по имени хорошо работает, когда известно имя рабочего листа. Если вы не знаете имя рабочего листа, используйте перегруженную версию[RemoveAt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#addabcc7d7d76874694018fb3ba37b72c)метод, который принимает индекс листа рабочего листа вместо его имени листа.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex.cpp" >}}

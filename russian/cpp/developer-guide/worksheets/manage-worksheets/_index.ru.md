---
title: Управление рабочими листами
type: docs
weight: 20
url: /ru/cpp/manage-worksheets/
---

{{% alert color="primary" %}} 

Разработчики могут легко создавать и управлять рабочими листами в файлах Microsoft Excel программно с помощью гибкого API Aspose.Cells. В этой теме описаны подходы к добавлению и удалению рабочих листов в файлах Microsoft Excel.

{{% /alert %}} 

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), позволяющую получить доступ к каждому рабочему листу в файле Excel.

Рабочий лист представляется классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет широкий спектр методов для управления рабочими листами.
## **Добавление рабочих листов в новый файл Excel**
Для создания нового файла Excel программно:

1. Создайте объект класса [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).
2. Вызовите метод [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) коллекции [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/). Пустой рабочий лист будет добавлен в файл Excel автоматически. Можно ссылаться на него, передавая индекс листа нового рабочего листа в коллекцию [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).
3. Получите ссылку на рабочий лист.
1. Выполнение работы с рабочими листами.
1. Сохраните новый файл Excel с новыми рабочими листами, вызвав метод [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) класса [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
## **Доступ к рабочим листам с использованием индекса листа.**
Приведенный ниже образец кода показывает, как получить любой рабочий лист, указав его индекс.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
## **Удаление рабочих листов с использованием индекса листа.**
Удаление листов по имени хорошо работает, когда известно имя листа. Если вы не знаете имя листа, используйте перегруженную версию метода [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat), который принимает индекс листа вместо его имени.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}

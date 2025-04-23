---
title: Управление рабочими листами
type: docs
weight: 20
url: /ru/go-cpp/manage-worksheets/
---

{{% alert color="primary" %}}

Разработчики могут легко создавать и управлять рабочими листами в файлах Microsoft Excel программно с помощью гибкого API Aspose.Cells. В этой теме описаны подходы к добавлению и удалению рабочих листов в файлах Microsoft Excel.

{{% /alert %}}

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет файл Excel. Класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/), которая позволяет получать доступ к каждому листу в Excel файле.

Лист представлен классом [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) предоставляет широкий набор методов для управления листами.

## **Добавление рабочих листов в новый файл Excel**

Для создания нового файла Excel программно:

1. Создайте объект класса [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/).
1. Вызовите метод [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_string/) коллекции [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/). В файл Excel автоматически добавляется пустой лист. Его можно получить, передав индекс нового листа в коллекцию [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/).
3. Получите ссылку на рабочий лист.
1. Выполнение работы с рабочими листами.
1. Сохраните новый файл Excel с новыми листами, вызвав метод [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) класса [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingWorksheetsToNewExcelFile.go" >}}

## **Доступ к рабочим листам с использованием индекса листа.**

Приведенный ниже образец кода показывает, как получить любой рабочий лист, указав его индекс.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessingWorksheetsUsingSheetIndex.go" >}}

## **Удаление рабочих листов с использованием индекса листа.**

Удаление листов по имени хорошо работает, если имя листа известно. Если вы не знаете имя листа, используйте перегруженную версию метода [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat), который принимает индекс листа вместо имени.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingWorksheetsUsingSheetIndex.go" >}}

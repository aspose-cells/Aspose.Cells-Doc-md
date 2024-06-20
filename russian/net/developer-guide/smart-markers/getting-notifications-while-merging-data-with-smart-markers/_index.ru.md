---
title: Получение уведомлений при объединении данных с помощью интеллектуальных маркеров Smart Markers
type: docs
weight: 20
url: /ru/net/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

API Aspose.Cells предоставляет класс [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) для [работы с интеллектуальными маркерами](https://docs.aspose.com/cells/net/smart-markers/), где форматирование и формулы размещаются в [дизайнерских электронных таблицах](/cells/ru/net/what-is-a-designer-spreadsheet/) и затем обрабатываются с помощью класса [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) для заполнения данных в соответствии с указанными интеллектуальными маркерами. Иногда может потребоваться получать уведомления о ссылке ячейки или конкретном интеллектуальном маркере, который обрабатывается. Это можно сделать с помощью свойства [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) и интерфейса [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback), представленного в выпуске Aspose.Cells for .NET 8.6.2.

{{% /alert %}} 

Ниже приведен фрагмент кода, демонстрирующий использование интерфейса [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) для определения нового класса, обрабатывающего вызов для метода [WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



Остальная часть процесса включает загрузку дизайнерской электронной таблицы, содержащей интеллектуальные маркеры, с использованием [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) и ее обработку путем установки источника данных. Для простоты примера мы использовали предопределенную дизайнерскую электронную таблицу, содержащую только два интеллектуальных маркера, как показано на снимке экрана ниже, где источник данных создается динамически для объединения данных в соответствии с указанными интеллектуальными маркерами.

|![todo:image_alt_text](getting-notifications-while-merging-data-with-smart-markers_1.png)|
| :- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}

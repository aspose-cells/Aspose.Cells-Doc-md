---
title: Получение уведомлений при объединении данных со смарт-маркерами
type: docs
weight: 20
url: /ru/net/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 Aspose.Cells API предоставляют[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) класс для[работа со смарт маркерами](https://docs.aspose.com/cells/net/smart-markers/) где форматирование и формулы помещаются в[дизайнерские таблицы](/cells/ru/net/what-is-a-designer-spreadsheet/) а затем обрабатываются с помощью[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) класс для заполнения данных в соответствии с указанными смарт-маркерами. Иногда может потребоваться получать уведомления о ссылке на ячейку или конкретном обрабатываемом смарт-маркере. Это может быть достигнуто с помощью[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) имущество и[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) интерфейс выставлен с выпуском Aspose.Cells for .NET 8.6.2.

{{% /alert %}} 

 Следующий фрагмент кода демонстрирует использование[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) интерфейс для определения нового класса, который обрабатывает обратный вызов для[WorkbookDesigner.Процесс](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)метод.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



 Остальная часть процесса включает в себя загрузку электронной таблицы дизайнера, содержащей смарт-маркеры с[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)и обработайте его, установив источник данных. Чтобы упростить пример, мы использовали предопределенную электронную таблицу конструктора, содержащую только два интеллектуальных маркера, как показано на снимке ниже, где источник данных создается динамически для объединения данных в соответствии с указанными интеллектуальными маркерами.

|![дело:изображение_альтернативный_текст](getting-notifications-while-merging-data-with-smart-markers_1.png)|
|:- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}

---
title: Получение уведомлений при объединении данных со смарт-маркерами
type: docs
weight: 460
url: /ru/java/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 Aspose.Cells API предоставляют[WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) класс для[работа со смарт маркерами](/cells/ru/java/smart-markers/) где форматирование и формулы помещаются в[дизайнерские таблицы](/cells/ru/java/what-is-a-designer-spreadsheet/) а затем обрабатываются с помощью[WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) класс для заполнения данных в соответствии с указанными смарт-маркерами. Иногда может потребоваться получать уведомления о ссылке на ячейку или конкретном обрабатываемом смарт-маркере. Это может быть достигнуто с помощью[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) имущество и[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)интерфейс выставлен с выпуском Aspose.Cells for Java 8.6.2.

{{% /alert %}} 
## **Получайте уведомления при объединении данных со смарт-маркерами**
 Следующий фрагмент кода демонстрирует использование[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)интерфейс для определения нового класса, который обрабатывает обратный вызов для[WorkbookDesigner.процесс](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) метод.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


Чтобы сделать пример простым и точным, в следующем фрагменте создается пустая электронная таблица дизайнера, вставляется смарт-маркер и обрабатывается с помощью динамически созданного источника данных.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}

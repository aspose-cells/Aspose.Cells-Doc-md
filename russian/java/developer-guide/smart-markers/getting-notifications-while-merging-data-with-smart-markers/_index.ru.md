---
title: Получение уведомлений при объединении данных с помощью интеллектуальных маркеров Smart Markers
type: docs
weight: 460
url: /ru/java/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

API Aspose.Cells предоставляет класс WorkbookDesigner для работы с умными маркерами, где форматирование и формулы размещаются в дизайнерских электронных таблицах, а затем обрабатываются с использованием класса WorkbookDesigner для заполнения данных в соответствии с указанными умными маркерами. Иногда может потребоваться получать уведомления о ссылке ячейки или конкретном умном маркере, который обрабатывается. Это можно сделать, используя свойство WorkbookDesigner.CallBack и интерфейс ISmartMarkerCallBack, который доступен с выпуском Aspose.Cells for Java 8.6.2.

{{% /alert %}} 
## **Получение уведомлений во время объединения данных с умными маркерами**
Следующий фрагмент кода демонстрирует использование интерфейса ISmartMarkerCallBack для определения нового класса, который обрабатывает обратный вызов для метода WorkbookDesigner.process.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


Чтобы сделать пример более простым и лаконичным, следующий фрагмент кода создает пустую дизайнерскую электронную таблицу, вставляет умные маркеры и обрабатывает ее с динамически созданным источником данных.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}

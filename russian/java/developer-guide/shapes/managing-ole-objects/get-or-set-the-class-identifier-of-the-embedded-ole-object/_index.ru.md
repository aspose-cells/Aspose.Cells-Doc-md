---
title: Получение или установка идентификатора класса встроенного объекта OLE
type: docs
weight: 920
url: /ru/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Возможные сценарии использования**
Aspose.Cells предоставляет свойство [OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier), которое вы можете использовать для получения или установки идентификатора класса встроенного объекта OLE. Идентификаторы классов объектов OLE на самом деле являются GUID, то есть глобально уникальные идентификаторы. GUID всегда имеет длину 16 байт, поэтому идентификаторы классов также имеют длину 16 байт. Они часто находятся в реестре Windows и предоставляют информацию о приложении-хосте о том, как открыть встроенный объект OLE, содержащий различные встроенные ресурсы в клиентском приложении.
## **Получение или установка идентификатора класса встроенного объекта OLE**
На следующем скриншоте показан идентификатор класса встроенного объекта OLE, т.е. GUID, который был считан из [образца файла Excel](5473378.xls) с встроенным объектом PowerPoint.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **Образец кода**
Пожалуйста, ознакомьтесь с следующим образцом кода, выполненным с [образцом файла Excel](5473378.xls) и его консольным выводом, который печатает *Идентификатор класса* встроенного объекта OLE, т.е. GUID. Распечатанный GUID полностью совпадает с показанным на скриншоте.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **Вывод в консоль**
Это вывод консоли приведенного выше образца кода при выполнении с [образцом excel-файла](5473378.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

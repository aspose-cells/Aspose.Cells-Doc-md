---
title: Получение или установка идентификатора класса встроенного объекта OLE
type: docs
weight: 200
url: /ru/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Возможные сценарии использования**
Aspose.Cells предоставляет свойство [OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier), которое вы можете использовать для получения или установки идентификатора класса встроенного объекта OLE. Идентификаторы класса объектов OLE фактически являются GUID, т.е. глобально уникальными идентификаторами. GUID всегда имеет длину 16 байт, поэтому идентификаторы классов также имеют длину 16 байт. Они часто находятся в реестре Windows и предоставляют информацию приложению-хозяину о том, как открыть встроенный объект OLE, содержащий различные встроенные ресурсы в клиентском приложении.
## **Получение или установка идентификатора класса встроенного объекта OLE**
На следующем скриншоте показан идентификатор класса встроенного объекта OLE, т.е. GUID, который был прочитан из [образца файла Excel](5115190.xls) с встроенным объектом OLE PowerPoint.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **Образец кода**
Пожалуйста, ознакомьтесь с примером работы кода, выполненного с [образцовым файлом Excel](5115190.xls) и консольным выводом, который печатает идентификатор класса объекта Ole, т.е. GUID. Напечатанный GUID точно такой же, как показан на скриншоте.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **Вывод в консоль**
Это консольный вывод вышеуказанного образца кода при выполнении с [образцовым файлом Excel](5115190.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

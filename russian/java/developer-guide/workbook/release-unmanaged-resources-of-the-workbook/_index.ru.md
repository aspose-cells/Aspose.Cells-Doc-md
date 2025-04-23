---
title: Освобождение неуправляемых ресурсов книги
type: docs
weight: 290
url: /ru/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells предоставляет метод [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) для освобождения неуправляемых ресурсов объекта [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Паттерн dispose используется только для объектов, которые имеют доступ к неуправляемым ресурсам, таким как дескрипторы файлов и каналов, дескрипторы реестра, дескрипторы ожидания или указатели на блоки неуправляемой памяти. Это связано с тем, что сборщик мусора очень эффективен в возврате неиспользуемых управляемых объектов, но он не может возвращать неуправляемые объекты.

{{% /alert %}} 
## **Освобождение неуправляемых ресурсов книги**
Следующий пример кода показывает, как использовать метод [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
{{< app/cells/assistant language="java" >}}

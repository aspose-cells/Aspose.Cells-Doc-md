---
title: Освобождение неуправляемых ресурсов книги
type: docs
weight: 290
url: /ru/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells предоставляет метод [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) для освобождения неуправляемых ресурсов объекта [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Шаблон dispose используется только для объектов, обращающихся к неуправляемым ресурсам, таким как файловые и канальные дескрипторы, дескрипторы реестра, дескрипторы ожидания или указатели на блоки неуправляемой памяти. Это потому, что сборщик мусора очень эффективен при восстановлении неиспользуемых управляемых объектов, но не способен восстанавливать неуправляемые объекты.

{{% /alert %}} 
## **Освобождение неуправляемых ресурсов книги**
Приведенный ниже образец кода показывает, как использовать метод [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\))

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}

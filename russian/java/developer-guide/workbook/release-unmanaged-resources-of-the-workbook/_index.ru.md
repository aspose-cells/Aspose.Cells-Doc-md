---
title: Освобождение неуправляемых ресурсов книги
type: docs
weight: 290
url: /ru/java/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}} 

 Aspose.Cells предоставляет[Рабочая книга.распоряжаться()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\) ) способ освобождения неуправляемых ресурсов[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)объект. Шаблон удаления используется только для объектов, которые обращаются к неуправляемым ресурсам, таким как дескрипторы файлов и каналов, дескрипторы реестра, дескрипторы ожидания или указатели на блоки неуправляемой памяти. Это связано с тем, что сборщик мусора очень эффективно освобождает неиспользуемые управляемые объекты, но не может освобождать неуправляемые объекты.

{{% /alert %}} 
## **Освобождение неуправляемых ресурсов книги**
В следующем примере кода показано, как использовать[Рабочая книга.распоряжаться()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) метод.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}

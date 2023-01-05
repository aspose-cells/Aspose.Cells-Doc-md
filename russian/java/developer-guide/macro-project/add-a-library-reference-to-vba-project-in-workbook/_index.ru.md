---
title: Добавить ссылку на библиотеку в проект VBA в книге
type: docs
weight: 10
url: /ru/java/add-a-library-reference-to-vba-project-in-workbook/
---
{{% alert color="primary" %}}

 В Microsoft Excel вы можете добавить ссылку на библиотеку в проект VBA, щелкнув значок**Инструменты > Ссылки...** вручную. Откроется следующее диалоговое окно, которое поможет вам выбрать из существующих ссылок или просмотреть вашу библиотеку самостоятельно.

![дело:изображение_альтернативный_текст](add-a-library-reference-to-vba-project-in-workbook_1.png)

 Но иногда вам нужно добавить или зарегистрировать ссылку на библиотеку в проекте VBA через код. Вы можете сделать это, используя Aspose.Cells[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) метод.

{{% /alert %}}

## **Добавить ссылку на библиотеку в проект VBA в книге**

 Следующий пример кода добавляет или регистрирует две ссылки на библиотеку в проекте VBA книги, используя[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) метод.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}

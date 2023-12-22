---
title: Добавьте ссылку на библиотеку в проект VBA в книгу.
type: docs
weight: 10
url: /ru/java/add-a-library-reference-to-vba-project-in-workbook/
description: Узнайте, как добавить ссылку на библиотеку в проект VBA в книгу по номеру Aspose.Cells for Java API.
keywords: How to Add a library reference to VBA project in workbook in Java, Insert a library reference to VBA project in workbook using Java, Java Set library reference to VBA project in workbook. 
---
{{% alert color="primary" %}}

 В Excel Microsoft вы можете добавить ссылку на библиотеку в проект VBA, щелкнув значок**Инструменты > Ссылки...** вручную. Откроется следующее диалоговое окно, которое поможет вам выбрать из существующих ссылок или просмотреть свою библиотеку самостоятельно.

![задача: image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

Но иногда вам необходимо добавить или зарегистрировать ссылку на библиотеку в проект VBA с помощью кода. Вы можете сделать это по номеру Aspose.Cells.[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) метод.

{{% /alert %}}

##  **Как добавить ссылку на библиотеку в проект VBA в книге**

 Следующий пример кода добавляет или регистрирует две ссылки на библиотеки в проект VBA книги, используя[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) метод.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}

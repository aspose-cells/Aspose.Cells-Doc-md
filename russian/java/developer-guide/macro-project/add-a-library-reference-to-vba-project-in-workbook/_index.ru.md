---
title: Добавить ссылку на библиотеку в проект VBA в книге
type: docs
weight: 10
url: /ru/java/add-a-library-reference-to-vba-project-in-workbook/
description: Узнайте, как добавить ссылку на библиотеку в проект VBA в книге через API Aspose.Cells for Java.
keywords: Как добавить ссылку на библиотеку в проект VBA в книге в Java, вставить ссылку на библиотеку в проект VBA в книге с использованием Java, Java установить ссылку на библиотеку в проект VBA в книге. 
---

{{% alert color="primary" %}}

В Microsoft Excel вы можете добавить ссылку на библиотеку в проект VBA, щелкнув **Сервис > Ссылки...** вручную. Это откроет следующее диалоговое окно, которое поможет вам выбрать из существующих ссылок или просмотреть библиотеку самостоятельно.

![todo:image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

Но иногда нужно добавить или зарегистрировать ссылку библиотеки в проект VBA через код. Вы можете сделать это, используя метод Aspose.Cells [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)).

{{% /alert %}}

## **Как добавить ссылку на библиотеку в проект VBA в книге**

В следующем примере кода добавляются или регистрируются две ссылки на библиотеку в проекте VBA книги с использованием метода [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}

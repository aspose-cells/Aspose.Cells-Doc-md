﻿---
title: Ваша первая заявка Aspose.Cells - Hello World
type: docs
weight: 30
url: /ru/java/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

В этом разделе для начинающих показано, как разработчики могут создать простое первое приложение (Hello World), используя Aspose.Cells' simple API. Приложение создает файл Excel Microsoft со словами Hello World в указанной ячейке рабочего листа.

{{% /alert %}}

### **Создание приложения Hello World**

Чтобы создать приложение Hello World, используя Aspose.Cells API:

1.  Создайте экземпляр**[Рабочая тетрадь] (https://reference.aspose.com/cells/java/com.aspose.cells/workbook)**учебный класс.
1. Применить лицензию:
1. Если вы приобрели лицензию, то используйте лицензию в своем приложении, чтобы получить доступ к полному функционалу Aspose.Cells.
 1. Если вы используете ознакомительную версию компонента (если вы используете Aspose.Cells без лицензии), пропустите этот шаг.
1. Создайте новый файл Excel Microsoft или откройте существующий файл, в который вы хотите добавить/обновить некоторый текст.
1. Получите доступ к любой ячейке рабочего листа в файле Excel Microsoft.
1.  Вставьте слова**Hello World!** в ячейку, к которой осуществляется доступ.
1. Создайте измененный файл Excel Microsoft.

Приведенные ниже примеры демонстрируют описанные выше шаги.

#### **Создание книги**

В следующем примере создается новая книга с нуля, в нее записываются слова «Hello World!». в ячейку A1 на первом листе и сохраняет файл.

**Сгенерированная электронная таблица** 

![дело:изображение_альтернативный_текст](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CreatingWorkbook-1.java" >}}

#### **Открытие существующего файла**

 В следующем примере открывается существующий файл шаблона Excel Microsoft с именем**book1.xls**, пишет слова "Hello World!" в ячейке A1 на первом листе и сохраняет книгу как новый файл.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-OpeningExistingFile-1.java" >}}
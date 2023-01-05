---
title: Проверьте пароль для изменения, используя Aspose.Cells
type: docs
weight: 190
url: /ru/java/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 Вы можете назначить**Пароль для открытия** и**Пароль для изменения** при создании книг в Microsoft Excel. Посмотрите этот снимок экрана, на котором показан интерфейс Microsoft, который Excel предоставляет для указания этих паролей.

![дело:изображение_альтернативный_текст](check-password-to-modify-using-aspose-cells_1.png)

 Иногда вам нужно проверить, совпадает ли данный пароль с**Пароль для изменения** программно. Aspose.Cells предоставляет[**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword(java.lang.String)), который вы можете использовать, чтобы проверить, является ли данный пароль для изменения правильным или нет.

{{% /alert %}}

## Java код для проверки Пароль для изменения с помощью Aspose.Cells

 Следующие примеры кодов загружают[исходный файл Excel](5473057.xlsx) файл. У него есть пароль для открытия как*1234* и пароль для изменения как*5678* . Сначала код проверяет,*567* правильный пароль для изменения, и он возвращает**ЛОЖЬ** а затем он проверяет, если*5678* это пароль для изменения, и он возвращает**истинный**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Вывод консоли, сгенерированный кодом Java

 Вот консольный вывод приведенного выше примера кода после загрузки[исходный файл Excel](5473057.xlsx) файл.

{{< highlight "java" >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}

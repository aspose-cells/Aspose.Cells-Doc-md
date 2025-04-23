---
title: Проверка пароля для изменения с использованием Aspose.Cells
type: docs
weight: 190
url: /ru/java/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Вы можете назначить **Пароль для открытия** и **Пароль для изменения** при создании рабочих книг в Microsoft Excel. Пожалуйста, обратитесь к этому скриншоту, где показан интерфейс Microsoft Excel для указания этих паролей.

![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)

Иногда вам нужно проверить, соответствует ли указанный пароль **Паролю для изменения** программно. Aspose.Cells предоставляет метод [**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword-java.lang.String-), который можно использовать для проверки корректности указанного пароля для изменения.

{{% /alert %}}

## Java код для проверки пароля для изменения с помощью Aspose.Cells

Следующие образцы кода загружают файл [исходный Excel](5473057.xlsx). В нем установлен пароль для открытия *1234* и пароль для изменения *5678*. Код сначала проверяет, является ли *567* правильным паролем для изменения, и возвращает **false**, затем он проверяет, является ли *5678* паролем для изменения, и возвращает **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Выход консоли, созданный Java-кодом

Вот выход консоли из приведенного выше образца кода после загрузки [исходного Excel](5473057.xlsx) файла.

{{< highlight java >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

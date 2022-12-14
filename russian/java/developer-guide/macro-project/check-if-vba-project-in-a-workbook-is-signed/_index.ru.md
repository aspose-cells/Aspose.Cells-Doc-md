---
title: Проверьте, подписан ли проект VBA в рабочей книге
type: docs
weight: 40
url: /ru/java/check-if-vba-project-in-a-workbook-is-signed/
---
{{% alert color="primary" %}}

 Вы можете проверить, подписан ли ваш проект VBA или нет, используя Microsoft Excel через**Инструменты > Цифровые подписи...** команда меню. Точно так же вы можете проверить это программно, используя Aspose.Cells.[**Рабочая книга.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) метод.

{{% /alert %}}

## **Проверьте, подписан ли проект VBA в рабочей книге**

 Следующий код загружает книгу и проверяет, подписан ли ее проект VBA с помощью[**Рабочая книга.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)имущество. Имущество вернется**истинный** если проект подписан иначе он вернется**ЛОЖЬ**.

## Образец кода

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}

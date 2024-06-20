---
title: Проверка подписан ли проект VBA в книге Excel
type: docs
weight: 40
url: /ru/java/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Вы можете проверить, подписан ли ваш проект VBA, используя Microsoft Excel через команду меню **Инструменты > Цифровые подписи...**. Аналогично, вы можете проверить это программно, используя метод [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) Aspose.Cells.

{{% /alert %}}

## **Проверить, подписан ли проект VBA в книге Excel**

Следующий код загружает книгу и проверяет, подписан ли ее проект VBA, используя свойство [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned). Свойство вернет **true**, если проект подписан, в противном случае оно вернет **false**.

## Образец кода

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}

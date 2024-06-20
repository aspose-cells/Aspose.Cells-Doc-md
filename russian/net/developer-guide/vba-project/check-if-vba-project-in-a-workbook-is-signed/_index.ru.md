---
title: Проверка подписан ли проект VBA в книге Excel
type: docs
weight: 70
url: /ru/net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Вы можете проверить подписан ли ваш проект VBA или нет, используя Microsoft Excel через меню **Инструменты > Цифровые подписи...**. Аналогичным образом, вы можете проверить это программным способом с помощью свойства [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned) библиотеки Aspose.Cells.

{{% /alert %}}

## **Проверка наличия подписанного проекта VBA в книге Excel в C#**

Следующий код загружает книгу и проверяет, подписан ли ее проект VBA, используя свойство [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned). Свойство вернет **true**, если проект подписан, в противном случае оно вернет **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaProjectSigned-1.cs" >}}

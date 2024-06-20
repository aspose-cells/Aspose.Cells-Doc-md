---
title: Создание Именованных Диапазонов с Глобальной Областью и Областью Листа
type: docs
weight: 10
url: /ru/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям определить именованные диапазоны с двумя различными областями: книга (также известная как глобальная область) и лист.

- Именованные диапазоны с глобальной областью могут быть доступны с любого листа внутри этой книги, просто используя его имя.
- Именованные диапазоны с областью листа доступны с помощью ссылки на конкретный лист, на котором он был создан.

Aspose.Cells предоставляет ту же функциональность, что и Microsoft Excel для добавления именованных диапазонов с областью книги и листа. При создании именованного диапазона с областью листа следует использовать ссылку на лист в именованном диапазоне, чтобы указать его как именованный диапазон с областью листа.

{{% /alert %}}

Ниже приведены примеры кода, показывающие, как создавать именованные диапазоны с областью книги и листа, используя класс [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range).

## **Добавление Именованного Диапазона с Областью Книги**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **Добавление Именованного Диапазона с Областью Листа**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}

---
title: Создание рабочей книги (глобальной) и именованных диапазонов рабочего листа
type: docs
weight: 10
url: /ru/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---
{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям определять именованные диапазоны с двумя разными областями: рабочая книга (также известная как глобальная область) и рабочий лист.

- Доступ к именованным диапазонам с областью действия рабочей книги можно получить с любого рабочего листа в этой рабочей книге, просто используя его имя.
- Доступ к именованным диапазонам рабочего листа осуществляется со ссылкой на конкретный рабочий лист, на котором он был создан.

Aspose.Cells обеспечивает ту же функциональность, что и Microsoft Excel, для добавления именованных диапазонов рабочей книги и рабочего листа. При создании именованного диапазона рабочего листа следует использовать ссылку рабочего листа в именованном диапазоне, чтобы указать его как именованный диапазон рабочего листа.

{{% /alert %}}

 В следующих примерах кода показано, как создавать диапазоны имен рабочей книги и рабочего листа с помощью[**Спектр**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) учебный класс.

## **Добавление именованного диапазона с областью рабочей книги**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **Добавление именованного диапазона с областью рабочего листа**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}

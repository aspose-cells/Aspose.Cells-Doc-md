---
title: Создание именованных диапазонов рабочей книги и листа
linktitle: Именованный диапазон
type: docs
weight: 40
url: /ru/net/create-workbook-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}} 

Microsoft Excel позволяет пользователям определить именованные диапазоны с двумя различными областями: книга (также известная как глобальная область) и лист.

- Именованные диапазоны с глобальной областью могут быть доступны с любого листа внутри этой книги, просто используя его имя.
- Именованные диапазоны с областью листа доступны с помощью ссылки на конкретный лист, на котором он был создан.

Aspose.Cells предоставляет ту же функциональность, что и Microsoft Excel для добавления именованных диапазонов с областью книги и листа. При создании именованного диапазона с областью листа следует использовать ссылку на лист в именованном диапазоне, чтобы указать его как именованный диапазон с областью листа.

{{% /alert %}} 
## **Добавление именованного диапазона с областью видимости рабочей книги**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.cs" >}}
## **Добавление Именованного Диапазона с Областью Листа**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-WorksheetNamedRange-1.cs" >}}

## **Продвинутые темы**
- [Создание доступа и копирование именованных диапазонов](/cells/ru/net/create-access-and-copy-named-ranges/)
- [Форматирование и изменение именованных диапазонов](/cells/ru/net/format-and-modify-named-ranges/)
- [Получить диапазон с внешними ссылками](/cells/ru/net/get-range-with-external-links/)
- [Реализация не последовательных диапазонов](/cells/ru/net/implementing-non-sequential-ranges/)
{{< app/cells/assistant language="csharp" >}}

﻿---
title: Добавить PDF Закладки
type: docs
weight: 10
url: /ru/net/add-pdf-bookmarks/
---
{{% alert color="primary" %}}

В этой статье содержится информация о том, как вставить закладки PDF при преобразовании электронной таблицы в PDF.

Aspose.Cells позволяет добавлять закладки на лету. PDF закладки могут значительно улучшить навигацию по длинным документам. При добавлении ссылок закладок в документ PDF вы можете точно контролировать желаемое представление, вы не ограничены ссылкой на страницу. Вы можете настроить точное представление, расположив целевую страницу, а затем создав закладку.

{{% /alert %}}

См. следующий пример кода, чтобы узнать, как добавить закладки PDF. Код создает простую книгу, указывает закладки PDF с целевым расположением и создает файл PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddPDFBookmarks-1.cs" >}}

{{% alert color="primary" %}}

Если в вашей электронной таблице есть формулы, лучше всего вызвать[**Workbook.CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) непосредственно перед рендерингом электронной таблицы в формат PDF. Это обеспечит правильное обновление и отображение зависимых от формулы значений в PDF.

{{% /alert %}}

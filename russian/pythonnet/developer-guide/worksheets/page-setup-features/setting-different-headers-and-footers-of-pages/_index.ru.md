---
title: Установка разных заголовков и нижних колонтитулов для разных страниц
type: docs
weight: 35
url: /ru/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: В этой статье приведен образец кода, показывающий, как программно устанавливать различные заголовки и нижние колонтитулы настроек страницы листа Excel с использованием API Aspose.Cells для Python. Вы можете установить заголовки и нижние колонтитулы для первой страницы, нечетных страниц и четных страниц.
keywords: Библиотека Python Excel, установка заголовка нижнего колонтитула Excel в Python, установка заголовка и нижнего колонтитула Excel для нечетных страниц на Python, установка заголовка и нижнего колонтитула Excel для четных страниц с использованием Python.
---

{{% alert color="primary" %}}

MS Excel поддерживает установку различных заголовков и нижних колонтитулов для первой страницы, нечетных страниц и четных страниц с версии Excel 2007.
Aspose.Cells для Python via .NET поддерживает ту же функцию.

{{% /alert %}}

## **Как установить разные заголовки и колонтитулы в MS Excel**

**![Установка различных заголовков и нижних колонтитулов](difpage.png)**

1. Нажмите **Разметка страницы > Печать заголовков > Заголовок/нижний колонтитул**.
1. Установите **Разные нечетные и четные страницы** или **Разные для первой страницы**.
1. Введите разные заголовки и нижние колонтитулы.

## **Как установить различные заголовки и нижние колонтитулы с помощью библиотеки Excel Aspose.Cells для Python**

Aspose.Cells для Python via .NET ведет себя так же, как Excel.
1. Устанавливает флаги [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) и [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. Введите разные заголовки и нижние колонтитулы.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}

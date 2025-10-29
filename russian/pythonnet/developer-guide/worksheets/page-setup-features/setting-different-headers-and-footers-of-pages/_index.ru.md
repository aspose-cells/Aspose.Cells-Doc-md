---
title: Установка разных заголовков и нижних колонтитулов для разных страниц
type: docs
weight: 35
url: /ru/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Этот пример кода показывает, как программно задавать различные заголовки и колонтитулы настроек страницы листа Excel с помощью API Aspose.Cells for Python. Можно установить заголовки и колонтитулы для первой страницы, нечетных страниц и четных страниц.
keywords: Библиотека Python Excel, установка заголовков и колонтитулов для первой страницы Excel, установка заголовков и колонтитулов для нечетных страниц в Python, установка заголовков и колонтитулов для четных страниц в Python.
---

{{% alert color="primary" %}}

MS Excel поддерживает установку различных заголовков и нижних колонтитулов для первой страницы, нечетных страниц и четных страниц с версии Excel 2007.
Aspose.Cells for Python via .NET поддерживает ту же функцию.

{{% /alert %}}

## **Как установить разные заголовки и колонтитулы в MS Excel**

**![Установка различных заголовков и нижних колонтитулов](difpage.png)**

1. Нажмите **Разметка страницы > Печать заголовков > Заголовок/нижний колонтитул**.
1. Установите **Разные нечетные и четные страницы** или **Разные для первой страницы**.
1. Введите разные заголовки и нижние колонтитулы.

## **Как установить разные заголовки и колонтитулы с помощью библиотеки Aspose.Cells for Python Excel**

Aspose.Cells for Python via .NET ведет себя так же, как Excel.
1. Устанавливает флаги [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) и [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. Введите разные заголовки и нижние колонтитулы.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
{{< app/cells/assistant language="python-net" >}}

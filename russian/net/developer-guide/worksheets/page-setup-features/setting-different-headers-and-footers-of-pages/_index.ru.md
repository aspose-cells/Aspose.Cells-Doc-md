---
title: Настройка разных верхних и нижних колонтитулов для разных страниц
type: docs
weight: 35
url: /ru/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: В этой статье представлен пример кода, который показывает, как программно установить различные верхние и нижние колонтитулы параметров страницы листа Excel с помощью библиотеки C# и .NET API. Вы можете установить верхние и нижние колонтитулы для первой страницы, нечетных страниц и четных страниц.
keywords: set excel header footer first page c#, set excel header footer odd pages c#, set excel header footer even pages c#
---
{{% alert color="primary" %}}

MS Excel поддерживает настройку разных верхних и нижних колонтитулов для первой страницы, нечетных и четных страниц, начиная с Excel 2007.
Aspose.Cells поддерживает ту же функцию.

{{% /alert %}}

##  **Настройка разных верхних и нижних колонтитулов в MS Excel**

**![Настройка разных верхних и нижних колонтитулов](difpage.png)**

1. Нажмите *Макет страницы > Печатать заголовки > Верхний/нижний колонтитул**.
1.  Проверять**Разные нечетные и четные страницы** или *Другая еловая страница**.
1. Введите разные верхние и нижние колонтитулы.

##  **Настройка разных верхних и нижних колонтитулов с помощью Aspose.Cells**

Aspose.Cells ведет себя так же, как Excel.
1.  Устанавливает флаги[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) и[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Введите разные верхние и нижние колонтитулы.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}

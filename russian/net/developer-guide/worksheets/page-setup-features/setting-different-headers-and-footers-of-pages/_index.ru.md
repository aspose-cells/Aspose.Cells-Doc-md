---
title: Настройка разных верхних и нижних колонтитулов для разных страниц
type: docs
weight: 35
url: /ru/net/setting-different-headers-and-footers-for-pages-to-Excel/
---
{{% alert color="primary" %}}

MS Excel поддерживает настройку разных верхних и нижних колонтитулов для первой страницы, нечетных и четных страниц, начиная с Excel 2007.
Aspose.Cells поддерживает ту же функцию.

{{% /alert %}}

## **Настройка разных верхних и нижних колонтитулов в MS Excel**

**![Настройка разных верхних и нижних колонтитулов](difpage.png)**

1.  Нажмите**Макет страницы > Печать заголовков > Верхний/нижний колонтитул**.
1.  Проверять**Разные нечетные и четные страницы** или же**Разная еловая страница**.
1. Введите разные верхние и нижние колонтитулы.

## **Настройка разных верхних и нижних колонтитулов с помощью Aspose.Cells**

Aspose.Cells ведет себя так же, как Excel.
1.  Устанавливает флаги[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) а также[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Введите разные верхние и нижние колонтитулы.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}

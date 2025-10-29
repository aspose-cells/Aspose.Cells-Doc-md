---
title: Получить лист с диаграммой с Golang через C++
linktitle: Получить рабочий лист диаграммы
description: Узнайте, как получать связанный с графиком лист Excel с помощью Aspose.Cells for C++. Наш гид покажет, как получить доступ к листу и выполнять операции над ним для манипуляции базовыми данными графика.
keywords: Aspose.Cells for C++, графики Excel, листы, управление данными, базовые данные, операции.
type: docs
weight: 1000
url: /ru/go-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Иногда нужно получить доступ к листу через ссылку графика. Aspose.Cells предоставляет метод [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/), который возвращает ссылку на лист, содержащий график.

{{% /alert %}}

Пример показывает, как использовать метод [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/). Сначала он выводит имя листа, затем получает первый график на листе и снова выводит название листа с помощью метода [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWorksheetOfTheChart.go" >}}
Ниже приведен вывод консоли, который получается в результате примера. Как видно, он дважды выводит одно и то же имя листа.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}

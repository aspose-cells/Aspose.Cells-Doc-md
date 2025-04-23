---
title: Чтение значений ячеек в нескольких потоках одновременно
linktitle: Несколько потоков
type: docs
weight: 1800
url: /ru/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Узнайте, как читать значения ячеек одновременно из нескольких потоков через API Aspose.Cells for Node.js via C++.
keywords: Чтение значений ячеек в нескольких потоках одновременно в Node.js при помощи C++, Aspose.Cells C++ Многопоточность, чтение данных в нескольких потоках
---

{{% alert color="primary" %}}

Необходимость чтения значений ячеек в нескольких потоках одновременно - это распространенная потребность. В этой статье объясняется, как использовать Aspose.Cells для этой цели.

{{% /alert %}}

Для чтения значений ячеек в нескольких потоках одновременно установите [**Cells.setMultiThreadReading(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setMultiThreadReading-boolean-) в **true**. Иначе вы можете получить неправильные значения ячеек.

Следующий код:

1. Создает рабочую книгу.
1. Добавляет лист.
1. Заполняет лист строковыми значениями.
1. Затем создает два потока, которые одновременно читают значения из случайных ячеек.
   Если прочитанные значения правильные, ничего не происходит. Если прочитанные значения неправильные, то отображается сообщение.

Если вы закомментируете эту строку:

{{< highlight javascript >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

тогда отображается следующее сообщение:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

В противном случае программа работает без отображения любого сообщения, что означает, что все значения, считываемые из ячеек, являются правильными.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-multiple-threads.js" >}}

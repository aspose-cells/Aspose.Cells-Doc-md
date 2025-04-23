---
title: Чтение значений ячеек в нескольких потоках одновременно
linktitle: Несколько потоков
type: docs
weight: 1800
url: /ru/net/reading-cell-values-in-multiple-threads-simultaneously/
description: Узнайте, как читать значения ячеек в нескольких потоках одновременно через API Aspose.Cells for .NET.
keywords: Чтение значений ячеек в нескольких потоках одновременно, Aspose.Cells C# Несколько потоков, Чтение данных в нескольких потоках
---

{{% alert color="primary" %}}

Необходимость чтения значений ячеек в нескольких потоках одновременно - это распространенная потребность. В этой статье объясняется, как использовать Aspose.Cells для этой цели.

{{% /alert %}}

Для чтения значений ячеек в более чем одном потоке одновременно установите [**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) в **true**. В противном случае вы можете получить неправильные значения ячеек.

Следующий код:

1. Создает рабочую книгу.
1. Добавляет лист.
1. Заполняет лист строковыми значениями.
1. Затем создает два потока, которые одновременно читают значения из случайных ячеек.
   Если прочитанные значения правильные, ничего не происходит. Если прочитанные значения неправильные, то отображается сообщение.

Если вы закомментируете эту строку:

{{< highlight java >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

тогда отображается следующее сообщение:

{{< highlight java >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

В противном случае программа работает без отображения любого сообщения, что означает, что все значения, считываемые из ячеек, являются правильными.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

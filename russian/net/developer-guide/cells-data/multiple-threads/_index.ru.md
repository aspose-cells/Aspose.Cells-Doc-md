---
title: Чтение значений Cell в нескольких потоках одновременно
linktitle: Несколько потоков
type: docs
weight: 1800
url: /ru/net/reading-cell-values-in-multiple-threads-simultaneously/
description: Узнайте, как читать значения Cell в нескольких потоках одновременно с помощью Aspose.Cells for .NET API.
keywords: Read Cell Values in Multiple Threads Simultaneously, Aspose.Cells C# Multiple Threads, Read data in Multiple Threads
---
{{% alert color="primary" %}}

Необходимость одновременного чтения значений ячеек в нескольких потоках является распространенным требованием. В этой статье объясняется, как использовать для этой цели Aspose.Cells.

{{% /alert %}}

 Чтобы читать значения ячеек в нескольких потоках одновременно, установите[**Рабочий лист.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading)на *истину**. Если вы этого не сделаете, вы можете получить неправильные значения ячеек.

Следующий код:

1. Создает рабочую книгу.
1. Добавляет рабочий лист.
1. Заполняет рабочий лист строковыми значениями.
1. Затем он создает два потока, которые одновременно считывают значения из случайных ячеек.
 Если считанные значения верны, ничего не происходит. Если считанные значения неверны, отображается сообщение.

Если вы прокомментируете эту строку:

{{< highlight "java" >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

то появится следующее сообщение:

{{< highlight "java" >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

В противном случае программа запускается без какого-либо сообщения, что означает, что все значения, считанные из ячеек, верны.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}

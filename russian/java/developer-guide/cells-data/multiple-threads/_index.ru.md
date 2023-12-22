---
title: Чтение значений Cell в нескольких потоках одновременно
linktitle: Несколько потоков
type: docs
weight: 1100
url: /ru/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Узнайте, как читать значения Cell в нескольких потоках одновременно с помощью API Aspose.Cells for Java.
keywords: Java Read Cell Values in Multiple Threads Simultaneously, Multiple Threads for Aspose.Cells for Java APIs.
---
{{% alert color="primary" %}}

Необходимость одновременного чтения значений ячеек в нескольких потоках является распространенным требованием. В этой статье объясняется, как использовать для этой цели Aspose.Cells.

{{% /alert %}}

##  **Как читать значения Cell в нескольких потоках одновременно с Aspose.Cells for Java**

 Чтобы читать значения ячеек в нескольких потоках одновременно, установите[**Рабочий лист.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading)на *истину**. Если вы этого не сделаете, вы можете получить неправильные значения ячеек. Обратите внимание: некоторые функции, такие как форматирование значений ячеек, не поддерживаются для многопоточности. Таким образом, MultiThreadReading позволяет вам получить доступ только к исходным данным ячейки. В многопоточной среде, если вы попытаетесь получить форматированное значение ячейки, например, с помощью Cell.getStringValue() для числовых значений, вы можете получить неожиданный результат или исключение.

Следующий код:

1. Создает рабочую книгу.
1. Добавляет рабочий лист.
1. Заполняет рабочий лист строковыми значениями.
1. Затем он создает два потока, которые одновременно считывают значения из случайных ячеек.
 Если считанные значения верны, ничего не происходит. Если считанные значения неверны, отображается сообщение.

Если вы прокомментируете эту строку:

{{< highlight "java" >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

то появится следующее сообщение:

{{< highlight "java" >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

В противном случае программа запускается без какого-либо сообщения, что означает, что все значения, считанные из ячеек, верны.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}

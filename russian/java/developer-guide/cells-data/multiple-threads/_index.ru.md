---
title: Чтение значений ячеек в нескольких потоках одновременно
linktitle: Несколько потоков
type: docs
weight: 1100
url: /ru/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Узнайте, как читать значения ячеек в нескольких потоках одновременно с помощью API Aspose.Cells for Java.
keywords: Чтение значений ячеек в нескольких потоках одновременно в Java, Несколько потоков для API Aspose.Cells for Java.
---

{{% alert color="primary" %}}

Необходимость чтения значений ячеек в нескольких потоках одновременно - это распространенная потребность. В этой статье объясняется, как использовать Aspose.Cells для этой цели.

{{% /alert %}}

## **Как читать значения ячеек в нескольких потоках одновременно с Aspose.Cells for Java**

Для чтения значений ячеек в более чем одном потоке одновременно установите [**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) в **true**. В противном случае вы можете получить неверные значения ячеек. Обратите внимание, некоторые функции, такие как форматирование значений ячеек, не поддерживаются для многопоточности. Поэтому MultiThreadReading позволяет получить доступ только к исходным данным ячейки. В среде многопоточности, если вы попытаетесь получить отформатированное значение ячейки, например, с помощью Cell.getStringValue() для числовых значений, вы можете получить непредвиденный результат или исключение.

Следующий код:

1. Создает рабочую книгу.
1. Добавляет лист.
1. Заполняет лист строковыми значениями.
1. Затем создает два потока, которые одновременно читают значения из случайных ячеек.
   Если прочитанные значения правильные, ничего не происходит. Если прочитанные значения неправильные, то отображается сообщение.

Если вы закомментируете эту строку:

{{< highlight java >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

тогда отображается следующее сообщение:

{{< highlight java >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

В противном случае программа работает без отображения любого сообщения, что означает, что все значения, считываемые из ячеек, являются правильными.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
{{< app/cells/assistant language="java" >}}

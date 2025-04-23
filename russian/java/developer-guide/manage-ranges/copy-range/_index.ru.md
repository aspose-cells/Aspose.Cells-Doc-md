---
title: Копирование диапазонов Excel
linktitle: Копирование диапазонов
type: docs
weight: 30
url: /ru/java/copy-ranges-of-Excel/
---

## **Введение**

В Excel вы можете выбрать диапазон, скопировать его, а затем вставить его с определенными параметрами на ту же рабочую книгу, другие листы или другие файлы.

## **Копирование диапазонов с использованием Aspose.Cells**

Aspose.Cells предоставляет некоторые перегрузки методов [Range.Copy](https://reference.aspose.com/cells/java/com.aspose.cells/range) для копирования диапазона.
## **Копировать диапазон**

Создание двух диапазонов: исходного диапазона, целевого диапазона, а затем копирование исходного диапазона в целевой диапазон с помощью метода Range.Copy.

См. следующий код:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range.java" >}}

## **Вставка диапазона с параметрами**

Aspose.Cells поддерживает вставку диапазона с определенным типом.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Paste-Range.java" >}}

## **Только копирование данных диапазона.**
Также вы можете скопировать данные с помощью метода Range.CopyData, как показано в следующем коде:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range-Data.java" >}}


{{< app/cells/assistant language="java" >}}

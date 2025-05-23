---
title: Преобразование между именем ячейки и индексом строки/столбца
linktitle: Преобразование имени ячейки и индекса
type: docs
weight: 10
url: /ru/net/names-and-indices/
description: Узнайте, как получить конвертацию между именем ячейки и индексом строки/столбца через API Aspose.Cells for .NET.
keywords: Получить имя ячейки из индексов строки и столбца, Получить индексы строки и столбца из имени ячейки, Создать безопасные имена листов, Добавить безопасные имена листов
---

## **Получить имя ячейки по индексам строки и столбца**
Возможно определить имя ячейки по индексам строки и столбца. В этой статье объясняется как это сделать.
Aspose.Cells предоставляет метод CellsHelper.CellIndexToName, который позволяет разработчикам получить имя ячейки, если они предоставляют индекс строки и столбца.

{{% alert color="primary" %}} 

Microsoft Excel начинает нумерацию индексов строк и столбцов с 1. В отличие от Microsoft Excel, Aspose.Cells начинает нумерацию индексов строк и столбцов с 0.

{{% /alert %}} 

Приведенный ниже образец кода иллюстрирует, как использовать CellsHelper.CellIndexToName, чтобы получить имя ячейки при известном индексе строки и столбца. Код генерирует следующий вывод.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **Получить индексы строки и столбца из имени ячейки**
Возможно определить индекс строки и столбца ячейки по ее имени. В этой статье объясняется как это сделать.
Aspose.Cells предоставляет метод CellsHelper.CellNameToIndex, который позволяет разработчикам получить индекс строки и столбца по имени ячейки.

{{% alert color="primary" %}} 

Microsoft Excel начинает нумерацию индексов строк и столбцов с 1. В отличие от Microsoft Excel, Aspose.Cells начинает нумерацию индексов строк и столбцов с 0.

{{% /alert %}} 

Приведенный ниже образец кода иллюстрирует, как использовать CellsHelper.CellNameToIndex для получения индекса строки и столбца по имени ячейки. Код генерирует следующий вывод.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **Создать безопасные имена листов**
Иногда требуется назначить имя листа во время выполнения. В этом сценарии могут присутствовать имена листов, содержащие дополнительные символы, такие как <>+(?”. Необходимо заменить любой такой символ, который не допускается как имя листа, предопределенным символом, предоставленным пользователем. Аналогично длина имени может увеличиться более чем до 31 символа, что требует усечения. Apache POI предоставляет определенные возможности создания безопасных имен, поэтому аналогичная возможность предоставляется Aspose.Cells для решения всех этих проблем. Приведенный ниже образец кода демонстрирует эту возможность:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Вывод:

это первое имя, которое создано

` `< > + (adj.Private _"Частный"
{{< app/cells/assistant language="csharp" >}}

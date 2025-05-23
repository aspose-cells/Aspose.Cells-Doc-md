---
title: Автоподгонка строк для объединенных ячеек
type: docs
weight: 120
url: /ru/net/autofit-rows-for-merged-cells/
---

{{% alert color="primary" %}}

Microsoft Excel предоставляет функцию, которая позволяет автоматически подгонять высоту ячейки в соответствии с ее содержимым. Функция называется автоматическим регулированием строк. В Microsoft Excel не устанавливается автоматическое регулирование на объединенных ячейках по умолчанию. Иногда функция становится жизненно важной для пользователя, который действительно нуждается в реализации автоподгонки строк и на объединенных ячейках тоже.

{{% /alert %}}

## **Как использовать AutoFitMergedCellsType для автоподгонки строк**
Aspose.Cells поддерживает эту функцию через API [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/). С помощью этого API возможно автоматически подогнать строки в листе, включая объединенные ячейки. Вот список всех возможных типов автоматической подгонки объединенных ячеек:

- Нет
- Первая строка
- Последняя строка
- Каждая строка

## **Автонастройка строк для объединенных ячеек**

Пожалуйста, посмотрите следующий код, он создает объект книги и добавляет несколько рабочих листов. Используйте различные методы для автонастройки строк в каждом рабочем листе. Снимок экрана показывает результат после выполнения примерного кода.

<br>
<img src="result.png" width=80% />

## **Пример кода на C#**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

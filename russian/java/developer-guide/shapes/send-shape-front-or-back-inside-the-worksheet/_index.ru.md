---
title: Отправить фигуру спереди или сзади внутри рабочего листа
type: docs
weight: 600
url: /ru/java/send-shape-front-or-back-inside-the-worksheet/
---
## **Возможные сценарии использования**

Когда в одном и том же месте присутствует несколько фигур, то, как они будут видны, определяется их положением в z-порядке. Aspose.Cells предоставляет[**Форма.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) метод, который изменяет положение формы по оси z. Если вы хотите отправить форму на задний план, вы будете использовать отрицательное число, например -1, -2, -3 и т. д., а если вы хотите отправить форму на передний план, вы будете использовать положительное число, например 1, 2, 3, и т.д.

## **Отправить фигуру спереди или сзади внутри рабочего листа**

В следующем примере кода объясняется использование[**Форма.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) метод. Пожалуйста, смотрите[образец файла Excel](50528362.xlsx)используется внутри кода и[выходной файл Excel](50528361.xlsx)порожденный им. На снимке экрана показано влияние кода на образец файла Excel при выполнении.

![дело:изображение_альтернативный_текст](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}

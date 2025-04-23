---
title: Настройка общих формул
type: docs
weight: 10
url: /ru/java/setting-shared-formula/
---

{{% alert color="primary" %}} 

Предположим, у вас есть лист с данными в формате, который выглядит как приведенный ниже образец листа.

**Входной файл с одним столбцом или данными** 

![todo:image_alt_text](setting-shared-formula_1.png)

Вы хотите добавить функцию в B2, которая будет вычислять налог с продаж для первой строки данных. Налог составляет **9%**. Формула, вычисляющая налог с продаж, такова: **"=A2*0.09"**. В этой статье объясняется, как применить эту формулу с помощью Aspose.Cells.

{{% /alert %}} 

Aspose.Cells позволяет указать формулу с использованием свойства [Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula), конкретно методов [Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) и [Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula).

Есть два варианта добавления формул в другие ячейки (B3, B4, B5 и так далее) в столбце.

Либо сделать то же самое, что и для первой ячейки, эффективно установив формулу для каждой ячейки, обновляя ссылку на ячейку соответственно (`A3*0.09`, `A4*0.09`, `A5*0.09` и так далее). Для этого необходимо обновлять ссылки на ячейки для каждой строки. Это также требует разбора Aspose.Cells каждой формулы индивидуально, что может быть времязатратно для больших электронных таблиц и сложных формул. Также это добавляет дополнительные строки кода, хотя циклы могут уменьшить их.

Другой подход — использовать **общую формулу**. С помощью общей формулы формулы автоматически обновляются для ссылок на ячейки в каждой строке, чтобы правильно рассчитывался налог. Метод [Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula-java.lang.String-int-int-) более эффективен, чем первый.

Следующий пример демонстрирует, как его использовать. Ниже показан снимок экрана выходного файла.

**Файл вывода: применение общей формулы** 

![todo:image_alt_text](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
{{< app/cells/assistant language="java" >}}

---
title: Вычисление массивной формулы таблиц данных
type: docs
weight: 550
url: /ru/java/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}} 

Вы можете создать таблицу данных в Microsoft Excel с помощью Данные > Анализ по сценариям > Таблица данных.... Aspose.Cells теперь позволяет вычислить массивную формулу таблицы данных. Пожалуйста, используйте [Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) как обычно для вычисления любого типа формул.

{{% /alert %}} 
## **Расчет массивной формулы таблиц данных**
В следующем образце кода мы использовали этот [исходный файл Excel](5472579.xlsx), который также показан на следующем изображении.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

Если вы измените значение ячейки B1 на 100, значения таблицы данных, заполненные желтым цветом, станут 120. В образцовом коде генерируется [файл PDF](5472577.pdf), который показывает 120 в качестве значений в таблице данных, как показано на этом изображении.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Вот образец кода, используемый для генерации [файла PDF](5472577.pdf) из [исходного файла Excel](5472579.xlsx). Пожалуйста, прочитайте комментарии для получения дополнительной информации.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}

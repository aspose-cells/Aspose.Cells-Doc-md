---
title: Применение расширенного условного форматирования
description: Как использовать библиотеку Aspose.Cells в C#, чтобы применить расширенное условное форматирование. Подстройкой этих критериев вы получаете больше контроля над тем, как выглядят и отображаются ячейки.
keywords: Aspose.Cells, Расширенное условное форматирование, C#, Условное, Форматирование
type: docs
weight: 70
url: /ru/net/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}} 

Microsoft Excel 2007 и более поздние версии (2010/2013/2016) предоставляют некоторые расширенные функции для условного форматирования. Например, он позволяет применять заливку ячеек, границы, цветные значки, стрелки, флажки и форматирование шрифтов и т.д., что стало довольно сложным.

{{% /alert %}} 
## **Применить расширенное условное форматирование к файлам Microsoft Excel**
Условное форматирование может:

- Добавлять заштрихованные полосы данных для графического улучшения базовых чисел, вставляя простую столбчатую диаграмму в ячейки.
- Автоматически заливать ячейки цветовыми шкалами на основе их отношения к значениям в других ячейках в диапазоне. По умолчанию наименьшее значение закрашивается красным, постепенно переходя к наибольшему значению зеленым.
- Используйте наборы значков аналогично цветовым шкалам, но вместо заливки ячеек добавляйте маленькие значки, такие как стрелки и светофоры, в ячейки.

Aspose.Cells полностью поддерживает условное форматирование, предоставляемое Microsoft Excel 2007 и более поздние версии в формате XLSX в реальном времени. В этом примере демонстрируется упражнение для продвинутых типов условного форматирования, включая IconSets, DataBars, Color Scales, TimePeriods, Top/Bottom и другие правила с различными наборами свойств.

- [**Adding Color Scale Conditional Formattings**](/cells/ru/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/ru/net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/ru/net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/ru/net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/ru/net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/ru/net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/ru/net/how-to-add-top10-conditional-formatting/)


### **Вычисление цвета, выбранного Microsoft Excel для условного форматирования ColorScale**
Aspose.Cells позволяет вычислить выбранный Microsoft Excel цвет при использовании условного форматирования ColorScale в файле шаблона. Приведенный ниже образец кода поможет вам научиться вычислять выбранный Microsoft Excel цвет.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ComputeColorChoosenByMSExcel-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

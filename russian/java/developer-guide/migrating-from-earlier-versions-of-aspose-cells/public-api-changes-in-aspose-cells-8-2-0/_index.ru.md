---
title: Общедоступный API Изменения в Aspose.Cells 8.2.0
type: docs
weight: 80
url: /ru/java/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.1.2 до 8.2.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлено свойство MultiThreadReading для класса Cells.**
В версии Aspose.Cells for Java 8.2.0 свойство MultiThreadReading было добавлено в класс Cells, чтобы обеспечить более надежный механизм для одновременного чтения значений ячеек несколькими потоками. Установка для свойства логического типа значения true в многопоточном приложении гарантирует, что каждый поток получит правильное значение ячеек.

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Одновременное чтение значений Cells в многопоточной среде](/cells/ru/java/reading-cell-values-in-multiple-threads-simultaneously/) Чтобы получить больше информации.

{{% /alert %}}
## **Добавлены перегрузки для методов autoFitRows и autoFitColumns.**
 Новые перегрузки для autoFitRows и autoFitColumns были добавлены в класс Worksheet, что позволяет разработчикам автоматически подбирать строки и столбцы на основе их соответствующих диапазонов при передаче экземпляра класса AutoFitterOptions.

Сигнатуры вышеуказанных методов следующие:

1. autoFitRows (параметры int startRow, int endRow, AutoFitterOptions)
1. autoFitColumns (int firstColumn, int lastColumn, параметры AutoFitterOptions)

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Автоподбор строк и столбцов](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}

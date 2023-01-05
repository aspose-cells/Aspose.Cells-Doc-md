---
title: Общедоступный API Изменения в Aspose.Cells 8.2.0
type: docs
weight: 70
url: /ru/net/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.1.2 до 8.2.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлено свойство MultiThreadReading для класса Cells.**
В версии Aspose.Cells for .NET 8.2.0 свойство MultiThreadReading было добавлено в класс Cells, чтобы обеспечить более надежный механизм для одновременного чтения значений ячеек несколькими потоками. Установка для свойства логического типа значения true в многопоточном приложении гарантирует, что каждый поток получит правильное значение ячеек.

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Одновременное чтение значений Cells в многопоточной среде](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) для дополнительной информации.

{{% /alert %}}
## **Добавлены перегрузки для методов AutoFitRows и AutoFitColumns.**
 Новые перегрузки для AutoFitRows и AutoFitColumns были добавлены в класс Worksheet, что позволяет разработчикам автоматически подбирать строки и столбцы на основе их соответствующих диапазонов при передаче экземпляра класса AutoFitterOptions.

Сигнатуры вышеуказанных методов следующие:

1. AutoFitRows (параметры int startRow, int endRow, AutoFitterOptions)
1. AutoFitColumns (int firstColumn, int lastColumn, параметры AutoFitterOptions)

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Автоподбор строк и столбцов](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns).

{{% /alert %}}

---
title: Изменения в публичном API Aspose.Cells 8.2.0
type: docs
weight: 70
url: /ru/net/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.1.2 до 8.2.0, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные открытые методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлено свойство MultiThreadReading для класса Cells**
С Aspose.Cells for .NET 8.2.0 свойство MultiThreadReading было добавлено в класс Cells для обеспечения более надежного механизма считывания значений ячеек с несколькими потоками одновременно. Установка значения типа Boolean в true в многопоточном приложении гарантирует, что каждый поток получит правильное значение ячеек.

{{% alert color="primary" %}} 

Пожалуйста, проверьте подробную статью на [Одновременное считывание значений ячеек в многопоточной среде](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) для получения дополнительной информации.

{{% /alert %}}
## **Добавлены перегрузки для методов AutoFitRows и AutoFitColumns**
В классе Worksheet были добавлены новые перегрузки для методов AutoFitRows и AutoFitColumns, позволяющие разработчикам автоматически подгонять высоту строк и ширину столбцов на основе соответствующих диапазонов с передачей экземпляра класса AutoFitterOptions. 

Сигнатуры вышеперечисленных методов следующие:

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь с подробной статьей по [Автоматическая подгонка строк и столбцов](http://aspose.com/docs/display/cellsnet/AutoFit+ Rows+and+Columns).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

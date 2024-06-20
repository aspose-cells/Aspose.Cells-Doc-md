---
title: Изменения в публичном API Aspose.Cells 8.2.0
type: docs
weight: 80
url: /ru/java/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.1.2 до 8.2.0, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные открытые методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлено свойство MultiThreadReading для класса Cells**
В Aspose.Cells for Java 8.2.0 свойство MultiThreadReading было добавлено в класс Cells для предоставления более надежного механизма чтения значений ячеек с несколькими потоками одновременно. Установка свойства типа Boolean в true в многопоточном приложении гарантирует, что каждый поток получит правильное значение ячейки.

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь со подробной статьей о [Одновременное чтение значений ячеек в многопоточной среде](/cells/ru/java/reading-cell-values-in-multiple-threads-simultaneously/) для получения дополнительной информации.

{{% /alert %}}
## **Добавлены перегрузки методов autoFitRows & autoFitColumns**
Классу Worksheet были добавлены новые перегрузки для методов autoFitRows & autoFitColumns, позволяющие разработчикам автоматически подгонять строки и столбцы на основе соответствующих диапазонов при передаче экземпляра класса AutoFitterOptions. 

Сигнатуры вышеперечисленных методов следующие:

1. autoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. autoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

Пожалуйста, проверьте подробную статью о [Автонастройке строк и столбцов](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}

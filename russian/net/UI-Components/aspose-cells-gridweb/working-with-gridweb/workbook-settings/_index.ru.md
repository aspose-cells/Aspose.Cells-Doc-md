---
title: Настройки для рабочей книги
type: docs
weight: 250
url: /ru/net/aspose-cells-gridweb/aspose-cells-gridweb/workbook-settings/
description: Эта статья описывает настройки рабочей книги в GridWeb.
keywords: GridWeb, настройки
---


Существуют некоторые настройки, которые мы можем указать с помощью настроек GridWorkbookSettings:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/GridWorkbookSettings)

|**Название** |**Описание** |
| :- | :- |
|MaxIteration | Получить или установить максимальное количество итераций для разрешения циклической ссылки, значение по умолчанию - 100.
|Iteration | Получить или установить, используется ли итерация для разрешения циклических ссылок.
|ForceFullCalculate | Получить или установить, полностью ли производится расчет при каждом вызове вычисления.
|CreateCalcChain | Получить или установить, создается ли цепочка вычисляемых формул. По умолчанию false.
|ReCalculateOnOpen | Получает или устанавливает, следует ли пересчитывать все формулы при открытии файла. |
|PrecisionAsDisplayed | True, если вычисления в этой книге будут выполняться с использованием только точности чисел, так как они отображаются |
|Date1904 | Получает или устанавливает значение, которое представляет, использует ли книга систему 1904 года. |
|CheckCustomNumberFormat | Получает или устанавливает, проверять ли настраиваемый числовой формат при установке Style.Custom. |
|Author | Получает и задает автора файла. |



Например, следующий код устанавливает ReCalculateOnOpen в false, чтобы остановить вычисление при открытии файла :

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 следующий код задает автора для файла :

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}



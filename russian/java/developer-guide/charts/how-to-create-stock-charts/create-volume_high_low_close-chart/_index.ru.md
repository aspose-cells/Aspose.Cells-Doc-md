---
title: Создать график акций Volume-High-Low-Close (VHLC)
type: docs
weight: 183
url: /ru/java/create-volume-high-low-close-stock-chart/
description: Как создать диаграмму акций Volume-High-Low-Close (VHLC), как добавить диаграмму акций Volume-High-Low-Close (VHLC), как создать диаграмму акций Volume-High-Low-Close (VHLC) .
keywords: Add Volume-High-Low-Close(VHLC) Stock Chart, Create Volume-High-Low-Close(VHLC) Stock Chart, Generate Volume-High-Low-Close(VHLC) Stock Chart.
---
##  **Возможные сценарии использования**
Третий график акций, который мы рассмотрим, — это график объема High Low Close. Опять же важно повторить, что данные должны быть в правильном порядке. Если вам нужно изменить порядок таблицы данных, вам следует сделать это до настройки диаграммы.
Эта диаграмма включает столбец объема сразу после первого столбца (категории), а диаграммы включают гистограмму на главной оси, показывающую этот объем, а цены перемещаются на второстепенную ось.

![задача: image_alt_text](data.png)
##  **График акций «Объем-максимум-минимум-закрытие» (VHLC)**

![задача: image_alt_text](sample.png)
##  **Образец кода**
 Следующий пример кода загружает[образец файла Excel](Volume-High-Low-Close.xlsx) и генерирует[выходной файл Excel](out.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-create-volume-high-low-close-stock-chart.java" >}}

---
title: Реализация пользовательского размера бумаги для рендеринга листа
type: docs
weight: 70
url: /ru/python-net/implement-custom-paper-size-of-worksheet-for-rendering/
description: В данной статье объясняется, как использовать образец кода Aspose.Cells для Python via .NET для установки настраиваемого размера бумаги желаемых листов при рендеринге файла Excel в формат PDF программно.
keywords: Библиотека Python Excel, установка настраиваемого размера бумаги при рендеринге Excel в PDF, Реализация настраиваемого размера бумаги страницы для рендеринга в Python.
---

## **Возможные сценарии использования**

В MS Excel нет прямой опции для создания настраиваемых размеров бумаги, однако вы можете устанавливать настраиваемый размер бумаги для желаемых листов при рендеринге файла Excel в формат PDF. Данный документ объясняет, как установить настраиваемый размер бумаги для листа с использованием API Aspose.Cells для Python via .NET.

## **Настройка пользовательского размера бумаги для отображения на листе**

Aspose.Cells для Python via .NET позволяет реализовать желаемый размер бумаги листа. Вы можете использовать метод [**custom_paper_size**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/custom_paper_size/#float-float) класса [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) для указания настраиваемого размера страницы. В следующем образце кода показано, как указать настраиваемый размер бумаги для первого листа в книге. См. также [выходной файл PDF](45056028.pdf), сгенерированный с помощью следующего кода для справки.

## **Снимок экрана**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.py" >}}

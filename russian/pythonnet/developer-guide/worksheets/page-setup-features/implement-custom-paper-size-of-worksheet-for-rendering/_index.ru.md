---
title: Реализация пользовательского размера бумаги для рендеринга листа
type: docs
weight: 70
url: /ru/python-net/implement-custom-paper-size-of-worksheet-for-rendering/
description: В этой статье объясняется, как использовать пример кода Aspose.Cells для Python via .NET для установки пользовательского размера бумаги выбранных листов при рендеринге файла Excel в PDF программно.
keywords: Библиотека Excel на Python, установка пользовательского размера бумаги при преобразовании Excel в PDF, настройка пользовательского размера бумаги листа при рендеринге в Python.
---

## **Возможные сценарии использования**

В MS Excel нет прямой возможности создавать пользовательские размеры бумаги, однако вы можете установить пользовательский размер бумаги для нужных листов при сохранении файла Excel в формат PDF. Этот документ объясняет, как задать пользовательский размер бумаги листа с помощью API Aspose.Cells for Python via .NET.

## **Настройка пользовательского размера бумаги для отображения на листе**

Aspose.Cells for Python via .NET позволяет реализовать желаемый размер бумаги листа. Вы можете использовать метод [**custom_paper_size**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/custom_paper_size/#float-float) класса [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) для указания пользовательского размера страницы. Ниже представлен пример кода, который показывает, как задать пользовательский размер бумаги для первого листа в книге. Также смотрите сгенерированный PDF [выходной файл](45056028.pdf) для справки.

## **Снимок экрана**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.py" >}}

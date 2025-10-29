---
title: Ресемплирование добавленных изображений  конвертация Excel в PDF с Golang через C++
linktitle: Добавление перерасчета изображений  конвертация Excel в PDF
type: docs
weight: 150
url: /ru/go-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Узнайте, как ресемплировать добавленные изображения для уменьшения размера PDF с помощью Aspose.Cells и Golang через C++.
---

{{% alert color="primary" %}}

При работе с большими файлами Microsoft Excel с большим количеством изображений вам может потребоваться сжимать добавленные изображения, чтобы уменьшить размер выходного PDF файла и улучшить общую производительность конвертации. Aspose.Cells поддерживает перерасчет добавленных изображений для уменьшения размера выходного PDF файла и улучшения производительности в некоторой степени.

{{% /alert %}}

Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, описывающим, как выполнить задачу с использованием API Aspose.Cells. В примере происходит преобразование файла Microsoft Excel в файл PDF с одновременным сжатием изображений в файле.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ResamplingAddedImagesExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

Использование опции [**SetImageResample**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/setimageresample/) позволяет минимизировать размер выходного PDF, но это может немного повлиять на качество изображения.

{{% /alert %}} 

{{% alert color="primary" %}}

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}


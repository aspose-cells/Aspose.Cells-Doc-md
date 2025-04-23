---
title: Указание значащих разрядов для хранения в файле Excel
type: docs
weight: 30
url: /ru/net/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **Возможные сценарии использования**

По умолчанию Aspose.Cells хранит 17 значащих разрядов для значений double внутри файла Excel, в отличие от MS-Excel, который хранит только 15 значащих разрядов. Вы можете изменить стандартное поведение Aspose.Cells с 17 значащими разрядами на 15 значащих разрядов, используя свойство [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits).

## **Указание значащих разрядов для хранения в файле Excel**

Нижеприведенный образец кода принуждает Aspose.Cells использовать 15 значимых разрядов при сохранении значений double в файл Excel. Пожалуйста, проверьте [выходной файл Excel](22774105.xlsx). Измените его расширение на .zip, разархивируйте его, и вы увидите, что внутри файла Excel хранится только 15 значащих разрядов. Ниже приведены скриншоты, поясняющие эффект свойства [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits) на выходной файл Excel.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
{{< app/cells/assistant language="csharp" >}}

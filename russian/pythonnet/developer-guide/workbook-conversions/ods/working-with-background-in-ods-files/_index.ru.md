---
title: Работа с фоном в файлах ODS
type: docs
weight: 150
url: /ru/python-net/working-with-background-in-ods-files/
description: Как работать с фоном в файлах ODS с использованием Aspose.Cells для Python via .NET API.
keywords: Python работать с фоном в файлах ODS, читать информацию о фоне из файла ODS, добавить цветной фон к файлу ODS с помощью Python via NET, добавить графический фон к файлу ODS с помощью Python via NET.
---

## **Фон в файлах ODS**

Фон можно добавлять к листам в файлах ODS. Фон может быть цветным или графическим. Фон не виден при открытии файла, но если файл распечатать в формате PDF, фон будет виден в полученном PDF. Фон также виден в диалоге предварительного просмотра печати.

Aspose.Cells для Python via .NET предоставляет возможность читать информацию о фоне и добавлять фон в файлах ODS.

## **Чтение информации о фоне из файла ODS**

Aspose.Cells для Python via .NET предоставляет класс [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) для управления фоном в файлах ODS. Нижеприведенный пример кода демонстрирует использование класса [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground), загружая файл ODS из [исходного файла ODS](90112030.ods) и читая информацию о фоне. Обратитесь к выводу консоли, сгенерированному кодом, для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ReadODSBackground-1.py" >}}

### **Вывод в консоль**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Добавить цветной фон в файл ODS**

Aspose.Cells для Python via .NET предоставляет класс [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) для управления фоном в файлах ODS. Нижеприведенный пример кода демонстрирует использование свойства [**OdsPageBackground.color**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/color/) для добавления цветного фона к файлу ODS. Обратитесь к [выходному файлу ODS](90112031.ods), сгенерированному кодом, для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSColoredBackground-1.py" >}}

## **Добавить графический фон в файл ODS**

Aspose.Cells для Python via .NET предоставляет класс [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) для управления фоном в файлах ODS. Нижеприведенный пример кода демонстрирует использование свойства [**OdsPageBackground.graphic_data**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/graphic_data/) для добавления графического фона к файлу ODS. Обратитесь к [выходному файлу ODS](90112030.ods) для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSGraphicBackground-1.py" >}}
{{< app/cells/assistant language="python-net" >}}

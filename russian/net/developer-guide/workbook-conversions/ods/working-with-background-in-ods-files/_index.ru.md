---
title: Работа с фоном в файлах ODS
type: docs
weight: 150
url: /ru/net/working-with-background-in-ods-files/
---

## **Фон в файлах ODS**

Фон можно добавлять к листам в файлах ODS. Фон может быть цветным или графическим. Фон не виден при открытии файла, но если файл распечатать в формате PDF, фон будет виден в полученном PDF. Фон также виден в диалоге предварительного просмотра печати.

Aspose.Cells предоставляет возможность читать информацию о фоне и добавлять фон в файлах ODS.

## **Чтение информации о фоне из файла ODS**

Aspose.Cells предоставляет класс [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) для управления фоном в файлах ODS. Приведенный ниже образец кода демонстрирует использование класса [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) путем загрузки [исходного файла ODS](90112030.ods) и чтения информации о фоне. Пожалуйста, обратитесь к выводу консоли, сгенерированному кодом для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadODSBackground-1.cs" >}}

### **Вывод в консоль**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Добавить цветной фон в файл ODS**

Aspose.Cells предоставляет класс [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) для управления фоном в файлах ODS. Приведенный ниже образец кода демонстрирует использование свойства [**OdsPageBackground.Color**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/color) для добавления цветного фона в файл ODS. Пожалуйста, обратитесь к [выходному файлу ODS](90112031.ods), сгенерированному кодом для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSColoredBackground-1.cs" >}}

## **Добавить графический фон в файл ODS**

Aspose.Cells предоставляет класс [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) для управления фоном в файлах ODS. Приведенный ниже образец кода демонстрирует использование свойства [**OdsPageBackground.GraphicData**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/graphicdata) для добавления графического фона в файл ODS. Пожалуйста, обратитесь к [выходному файлу ODS](90112030.ods), сгенерированному кодом для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSGraphicBackground-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

---
title: Работа с фоном в файлах ODS
type: docs
weight: 170
url: /ru/java/working-with-background-in-ods-files/
---

## **Фон в файлах ODS**

Фон может быть добавлен на листы в файлах ODS. Фон может быть цветным или графическим. Фон не виден при открытии файла, но если файл распечатывается в формате PDF, фон виден в созданном PDF. Фон также виден в диалоговом окне предварительного просмотра перед печатью.

Aspose.Cells предоставляет возможность читать фоновую информацию и добавлять фон в файлы ODS.

## **Чтение информации о фоне из файла OSD**

Aspose.Cells предоставляет класс [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) для управления фоном в файлах ODS. В следующем примере кода демонстрируется использование класса [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground), загрузка файла [source ODS] (GraphicBackground.ods) и чтение информации о фоне. Пожалуйста, обратитесь к выходным данным консоли, сгенерированным кодом, для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **Вывод в консоль**

{{< highlight java >}}

Background Type: GRAPHIC

Backgorund Position: CENTER_CENTER

{{< /highlight >}}

## **Добавить цветной фон в файл ODS**

Aspose.Cells предоставляет класс [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) для управления фоном в файлах ODS. В следующем примере кода демонстрируется использование свойства [**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color) для добавления цветного фона в файл ODS. Пожалуйста, обратитесь к файлу [output ODS] (ColoredBackground.ods), сгенерированному кодом, для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **Добавить графический фон в файл ODS**

Aspose.Cells предоставляет класс [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) для управления фоном в файлах ODS. В следующем примере кода демонстрируется использование свойства [**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData) для добавления графического фона в файл ODS. Пожалуйста, обратитесь к файлу [output ODS] (GraphicBackground.ods), сгенерированному кодом, для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}

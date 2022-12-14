---
title: Работа с фоном в файлах ODS
type: docs
weight: 170
url: /ru/java/working-with-background-in-ods-files/
---
## **Фон в файлах ODS**

Фон можно добавить к листам в файлах ODS. Фон может быть цветным или графическим. Фон не виден, когда файл открыт, но если файл распечатан в формате PDF, фон виден в сгенерированном PDF-файле. Фон также виден в диалоговом окне предварительного просмотра печати.

Aspose.Cells предоставляет возможность считывать фоновую информацию и добавлять фон в файлы ODS.

## **Чтение справочной информации из файла OSD**

Aspose.Cells обеспечивает[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)класс для управления фоном в файлах ODS. В следующем примере кода показано использование[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)класс, загрузив[источник ОРВ](GraphicBackground.ods)файл и чтение справочной информации. Для справки см. вывод консоли, сгенерированный кодом.

### **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **Консольный вывод**

Тип фона: ГРАФИЧЕСКИЙ

Фоновая позиция: CENTER_CENTER

## **Добавить цветной фон в файл ODS**

Aspose.Cells обеспечивает[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)класс для управления фоном в файлах ODS. В следующем примере кода показано использование[**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color)для добавления цветного фона в файл ODS. Пожалуйста, смотрите[вывод ОРВ](ColoredBackground.ods)файл, сгенерированный кодом для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **Добавить графический фон в файл ODS**

Aspose.Cells обеспечивает[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)класс для управления фоном в файлах ODS. В следующем примере кода показано использование[**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData)для добавления графического фона в файл ODS. Пожалуйста, смотрите[вывод ОРВ](GraphicBackground.ods)файл, сгенерированный кодом для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}

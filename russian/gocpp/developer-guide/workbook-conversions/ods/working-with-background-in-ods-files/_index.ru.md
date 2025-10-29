---
title: Работа с фоном в файлах ODS с помощью Golang через C++
linktitle: Работа с фоном в файлах ODS
type: docs
weight: 150
url: /ru/go-cpp/working-with-background-in-ods-files/
description: Узнайте, как управлять цветными и графическими фонами в файлах ODS с помощью Aspose.Cells и Golang через C++.
---

## **Фон в файлах ODS**

Фон можно добавлять к листам в файлах ODS. Фон может быть цветным или графическим. Фон не виден при открытии файла, но если файл распечатать в формате PDF, фон будет виден в полученном PDF. Фон также виден в диалоге предварительного просмотра печати.

Aspose.Cells предоставляет возможность читать информацию о фоне и добавлять фон в файлах ODS.

## **Чтение информации о фоне из файла ODS**

Aspose.Cells предоставляет класс [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) для управления фоном в файлах ODS. Следующий пример демонстрирует использование класса [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/), загружая исходный файл [ODS](90112030.ods) и считывая информацию о фоне. Посмотрите вывод консоли, сгенерированный этим кодом, для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles.go" >}}
### **Вывод в консоль**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Добавить цветной фон в файл ODS**

Aspose.Cells предоставляет класс [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) для управления фоном в файлах ODS. Следующий пример демонстрирует использование свойства [**OdsPageBackground.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/) для добавления цветового фона в файл ODS. Посмотрите сгенерированный этим кодом [выходной файл ODS](90112031.ods) для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-1.go" >}}
## **Добавить графический фон в файл ODS**

Aspose.Cells предоставляет класс [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) для управления фоном в файлах ODS. Следующий пример демонстрирует использование свойства [**OdsPageBackground.GetGraphicData()**](https://reference.aspose.com/cells/go-cpp/odspagebackground/getgraphicdata/) для добавления графического фона в файл ODS. Посмотрите сгенерированный этим кодом [выходной файл ODS](90112030.ods) для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-2.go" >}}

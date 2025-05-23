---
title: Отображение временной шкалы
type: docs
weight: 40
url: /ru/java/rendering-timeline/
description: Управление временными шкалами файлов Excel с помощью Aspose.Cells для Java.
keywords: Преобразование временной шкалы без использования Office 2013, Office 2016, Office 2019 и Office 365
---

## **Возможные сценарии использования**
Aspose.Cells поддерживает визуализацию временной шкалы без использования office 2013, office 2016, office 2019 и office 365. Если вы конвертируете свой лист в изображение или сохраняете свою книгу в форматах PDF или HTML, то вы увидите, что временные шкалы визуализированы правильно.

## **Визуализация временной шкалы**
В следующем образце кода загружается [образец Excel-файла](input.xlsx), содержащий существующую временную шкалу. Получите объект формы по имени временной шкалы, а затем визуализируйте его в виде изображения через метод Shape.ToImage(). Полученное изображение - это [выходное изображение](out.png), которое показывает визуализированную временную шкалу. Как видите, временная шкала была правильно визуализирована и выглядит так же, как в образцовом Excel-файле.

![todo:image_alt_text](out.png)
### **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-RenderingTimeline.java" >}}

{{< app/cells/assistant language="java" >}}

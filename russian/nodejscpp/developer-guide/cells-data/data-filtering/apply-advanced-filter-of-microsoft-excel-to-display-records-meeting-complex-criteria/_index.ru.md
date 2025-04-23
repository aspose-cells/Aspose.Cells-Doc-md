---  
title: Применить Расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным критериям
type: docs  
weight: 280  
url: /ru/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/  
description: Узнайте, как применять расширенный фильтр в Microsoft Excel для отображения записей, соответствующих сложным критериям, используя API Aspose.Cells for Node.js via C++.  
keywords: Применить расширенный фильтр Node.js через C++, установить расширенный фильтр Node.js через C++, добавить расширенный фильтр Node.js через C++, создать расширенный фильтр Node.js через C++, как добавить расширенный фильтр к диапазону Node.js через C++  
---  

## **Возможные сценарии использования**  

Microsoft Excel позволяет применять *Расширенный фильтр* к данным листа для отображения записей, соответствующих сложным критериям. Вы можете применить расширенный фильтр через команду *Данные > Расширенный*, как показано на скриншоте.  

![todo:image_alt_text](1.png)  

API Aspose.Cells for Node.js via C++ также позволяет применять расширенный фильтр с помощью метода [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-). Как и в Microsoft Excel, он принимает следующие параметры.  

**isFilter**  

Указывает, фильтровать ли список на месте.  

**listRange**  

Диапазон списка.  

**criteriaRange**  

Диапазон критериев.  

**copyTo**  

Диапазон, куда копируются данные.  

**uniqueRecordOnly**  

Отображение или копирование только уникальных строк.  

## **Применение расширенного фильтра Microsoft Excel для отображения записей, удовлетворяющих сложным критериям**  

Следующий пример кода применяет расширенный фильтр к [пробному Excel-файлу](48496692.xlsx) и создает [выходной Excel-файл](48496691.xlsx). Скриншот показывает оба файла для сравнения. Внутри скриншота видно, что данные были отфильтрованы внутри выходного файла согласно сложным условиям.  

![todo:image_alt_text](2.png)  

## **Образец кода**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-AdvancedFilter.js" >}}



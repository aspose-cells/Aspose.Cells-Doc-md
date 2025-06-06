---  
title: Повторное использование объектов стиля
linktitle: Повторное использование объектов стиля  
description: В Aspose.Cells for Node.js via C++, создание и использование повторно используемых объектов стиля позволяет упростить управление стилями и повысить эффективность кода. Наше руководство поможет вам использовать преимущества повторно используемых объектов стиля и внедрять их в ваше приложение.  
keywords: Aspose.Cells for Node.js via C++, Повторное использование объектов стилей, Управление стилями, Эффективность кода, Повторно используемые стили, Разработка приложений, API справочник, Пример кода, Скачать, Поддержка.  
type: docs  
weight: 3000  
url: /ru/nodejs-cpp/reusing-style-objects/  
---  

{{% alert color="primary" %}}  
Повторное использование объектов стиля может сэкономить память и ускорить работу программы.  
{{% /alert %}}  

Чтобы применить форматирование к большому диапазону ячеек на листе:

1. Создайте объект стиля.
1. Укажите атрибуты.
1. Примените стиль к ячейкам в диапазоне.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-ReusingStyleObjects.js" >}}


{{% alert color="primary" %}}  
Поскольку подход [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) / [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) использует намного меньше памяти и является более эффективным, устаревшее свойство Cell.style, которое занимало много лишней памяти, было удалено с выпуском Aspose.Cells 7.1.0.  
{{% /alert %}}  


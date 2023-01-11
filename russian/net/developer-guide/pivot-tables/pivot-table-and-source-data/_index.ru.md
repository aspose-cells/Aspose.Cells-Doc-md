﻿---
title: Сводная таблица и исходные данные
type: docs
weight: 30
url: /ru/net/pivot-table-and-source-data/
---
## **Исходные данные сводной таблицы**

Бывают случаи, когда вы хотите создать Microsoft отчеты Excel со сводными таблицами, которые берут данные из разных источников данных (например, из базы данных), неизвестных во время разработки. В этой статье представлен подход к динамическому изменению источника данных сводной таблицы.

### **Изменение исходных данных сводной таблицы**

1. Создание нового шаблона конструктора.
1. Создайте новый файл шаблона дизайнера, как показано на скриншоте ниже.
 1. Затем определите именованный диапазон,**Источник данных**, который относится к этому диапазону ячеек.

      **Создание шаблона конструктора и определение именованного диапазона, DataSource** 

![дело:изображение_альтернативный_текст](pivot-table-and-source-data_1.png)
   
1. Создание сводной таблицы на основе этого именованного диапазона.
 1. В Excel Microsoft выберите**Данные** , тогда**сводная таблица** и**Отчет сводной диаграммы**.
 1. Создайте сводную таблицу на основе именованного диапазона, созданного на первом шаге.

      **Создание сводной таблицы на основе именованного диапазона DataSource** 

![дело:изображение_альтернативный_текст](pivot-table-and-source-data_2.png)

   
 1. Перетащите соответствующее поле в строку и столбец сводной таблицы, затем создайте результирующую сводную таблицу, как показано на снимке экрана ниже.

   **Создание сводной таблицы на основе соответствующего поля** 

![дело:изображение_альтернативный_текст](pivot-table-and-source-data_3.png)

   
1.  Щелкните правой кнопкой мыши сводную таблицу и выберите**Параметры таблицы**.
 1. Проверить**Обновлять при открытии** в**Параметры данных** настройки.

      **Настройка параметров сводной таблицы** 

![дело:изображение_альтернативный_текст](pivot-table-and-source-data_4.png)


Теперь вы можете сохранить этот файл как файл шаблона дизайнера.

1. Заполнение новыми данными и изменение исходных данных сводной таблицы.
1. После создания шаблона конструктора используйте следующий код, чтобы изменить исходные данные сводной таблицы.

Выполнение приведенного ниже примера кода изменяет исходные данные сводной таблицы.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ChangeSourceData-1.cs" >}}
